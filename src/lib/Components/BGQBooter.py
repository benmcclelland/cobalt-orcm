import threading
import Queue
import logging
import threading
import Cobalt.TriremeStateMachine
import Cobalt.QueueThread
from Cobalt.Components.bgq_base_system import Block
from Cobalt.QueueThread import ValidationError
from Cobalt.Data import IncrID

import mock_pybgsched as pybgsched


#FIXME: also make this handle cleanup
#TODO: Add message handling
#TODO: Hook for booting status and suspending ongoing boots

import sys
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.StreamHandler(sys.stdout))

_boot_id_gen = IncrID()

class DupicateStateError(Exception):
    pass

class BaseState(object):

    _short_string = 'base'
    _destination_states = frozenset([])

    def __init__(self, context=None):
        self.context = context

    def __str__(self):
        return self._short_string

    def __repr__(self):
        return "<State '%s'>" % self._short_string

    def __hash__(self):
        return hash(self._short_string)

    def __eq__(self, other):
        return str(self) == str(other)

    @property
    def destination_states(self):
        return self._destination_states

    def exit(self):
        '''Actions to execute on exiting a state

        '''
        pass

    def progress(self):
        raise NotImplementedError('Progress has not been overridden.')

    def get_valid_transition_dict(self):
        transition_dict = {}
        for state in self._destination_states:
            transition_dict[state] = str(state)
        return transition_dict

    def validate_transition(self, new_state):
        '''Take terminal actions for new state

        '''
        if not isinstance(new_state, BaseState):
            raise TypeError, "%s is not a BaseState object"
        if new_state not in self._destination_states:
            return False
        return True


def _initiate_boot(context):
    '''Initiate the boot. If problems are encountered, then return a BootFailed state, otherwise, return a BootInitiating state.

    '''
    try:
        pybgsched.Block.initiateBoot(context.subblock_parent)
    except RuntimeError:
        #fail the boot
        context.status_string.append("%s/%s: Unable to boot block %s due to RuntimeError. Aborting job startup." % (context.user,
            context.job_id, context.subblock_parent))
        return BootFailed(context)
    else:
        context.status_string.append("%s/%s: Initiating boot at location %s." % (context.user,
            context.job_id, context.subblock_parent))
        #log boot success
        return BootInitiating(context)

def get_compute_block(block, extended_info=False):
    '''We do this a lot, this is just to make the information call more readable.

    block -- a string containing the block name
    extended_info -- Default: False.  If set to true, pulls extended info for the
        block like hardware information.

    '''
    block_location_filter = pybgsched.BlockFilter()
    block_location_filter.setName(block)
    if extended_info:
        block_location_filter.setExtendedInfo(True)
    return pybgsched.getBlocks(block_location_filter)[0]

class BootPending(BaseState):
    '''A boot has been requested.  This state handles boot initiation.
    Errors contacting the control system at this point are considered fatal for the boot.
    Depending on when this occurs, it may also be fatal to the requesting job.

    '''
    _short_string = 'pending'

    def __init__(self, context):
        super(BootPending, self).__init__(context)
        self._destination_states = frozenset([BootPending, BootInitiating, BootComplete, BootFailed])

    def progress(self):
        #Make sure we have the lock for this resource, set user and start booting.
        if self.context.under_resource_reservation():
            #we can continue the boot, we're not out of time.
            try:
                compute_block = get_compute_block(self.context.subblock_parent)
                pybgsched.Block.addUser(self.context.subblock_parent, self.context.user)
            except RuntimeError:
                #control system connection has blown.  This boot may as well be dead.
                self.context.status_string.append("%s/%s: Unable to retrieve control system data for block %s. Aborting job." % \
                        (self.context.user, self.context.job_id, self.context.subblock_parent))
                return BootFailed(self.context)
            if self.context.block.block_type == 'pseudoblock':
                #we have to boot a subblock job. If already booted, this is complete.
                if compute_block.getStatus() in [pybgsched.Block.Allocated, pybgsched.Block.Booting]:
                    #Boot in progress: move to initiating
                    return BootInitiating(self.context)
                elif compute_block.getStatus() == pybgsched.Block.Initialized:
                    if compute_block.getAction() == pybgsched.Action._None:
                        compute_block.addUser(self.context.subblock_parent, self.context.user)
                        self.context.status_string.append("%s/%s: Block %s for location %s already booted." \
                                "  Boot Complete from pending." % (self.context.user, self.context.job_id,
                                    self.context.subblock_parent, self.context.block_id))
                        return BootComplete(self.context)
                    else: #we're going to have to wait for this block to free and reboot the block.
                        _logger.info("%s/%s: trying to start on freeing block %s. waiting until free.", self.context.user, 
                                self.context.job_id, self.context.subblock_parent)
                        return self
            return _initiate_boot(self.context)
        else:
            self.context.status_string.append("%s/%s: the internal reservation on %s expired; job has been terminated" % \
                    (self.context.user, self.context.job_id, self.context.subblock_parent))
            return BootFailed(self.context)
        raise RuntimeError, "Unable to return a valid state"


class BootInitiating(BaseState):
    '''Check to determine if our boot is still continuing or has completed.
    Problems contacting the control system at this point are considered fatal to the ongoing boot.

    '''
    _short_string = 'initiating'

    def __init__(self, context):
        super(BootInitiating, self).__init__(context)
        self._destination_states = frozenset([BootInitiating, BootComplete, BootFailed, BootRebooting])

    def progress(self):
        '''check up on groups that are waiting to start up.

        '''
        # Make sure we still have the reservation, otherise allow cleanup to clear the block
        if not self.context.under_resource_reservation():
            self.context.status_string.append("%s/%s: the internal reservation on %s expired; job has been terminated" % \
                    (self.context.user, self.context.job_id, self.context.subblock_parent))
            return BootFailed(self.context)

        boot_block = get_compute_block(self.context.subblock_parent)
        if boot_block.getStatus() == pybgsched.Block.Initialized:
            if boot_block.getAction() == pybgsched.Action.Free:
                _logger.warning("%s/%s: Block for pending boot on %s freeing. Attempting reboot.", self.context.user, self.context.job_id,
                    self.context.subblock_parent)
                return BootRebooting(self.context)
            else:
                self.context.status_string.append("%s/%s: Block %s for location %s successfully booted (Initiating). " % \
                    (self.context.user, self.context.job_id, self.context.subblock_parent, self.context.block.name))
                return BootComplete(self.context)
        elif boot_block.getStatus() in [pybgsched.Block.Free, pybgsched.Block.Terminating]:
            #may have had an inopportune free, go ahead and make this and try and reboot.
            _logger.warning("%s/%s: Block for pending boot on %s freeing. Attempting reboot.", self.context.user, self.context.job_id,
                    self.context.subblock_parent)
            return BootRebooting(self.context)
        #allocated and booting states on the block means we stay in this state
        return self

class BootComplete(BaseState):

    _short_string = 'complete'

    def __init__(self, context):
        super(BootComplete, self).__init__(context)
        self._destination_states = frozenset([BootComplete])

    def progress(self):
        '''Boot has completed, wait until the boot is acknowledged and reaped.

        '''
        return self

class BootFailed(BaseState):
    _short_string = 'failed'

    def __init__(self, context):
        super(BootFailed, self).__init__(context)
        self._destination_states = frozenset([BootFailed])

    def progress(self):
        '''Boot has failed.  Messages have been logged.  Wait for reaping.

        '''
        return self

class BootRebooting(BaseState):
    _short_string = 'rebooting'

    def __init__(self, context):
        super(BootRebooting, self).__init__(context)
        _destination_states = frozenset([BootPending, BootInitiating, BootComplete, BootFailed])

    def progress(self):
        '''Block found in state that requires reboot.  Increment reboot counter, and check if we have already failed.

        '''
        #Do we still have the resource?
        if not self.context.under_resource_reservation():
            self.context.status_string.append("%s/%s: the internal reservation on %s expired; job has been terminated" % \
                    (self.context.user, self.context.job_id, self.context.subblock_parent))
            return BootFailed(self.context)
        #Check to see if we have any reboots left, if so, wait until free(?) Then go to pending.
        #If we find that our block is in a booting state already, then go along with the reboot in progress.
        if self.context.max_reboot_attempts != None and self.context.reboot_attempts >= self.context.max_reboot_attempts:
            self.context.status_string.append("%s/%s: Boot terminated on %s: too many reboot attempts." % (self.context.user,
                self.context.job_id, self.context.subblock_parent))
            return BootFailed(self.context)
        try:
            reboot_block = get_compute_block(self.context.subblock_parent)
        except Exception as e:
            _logger.critical("%s/%s: Unable to contact control system for block information.", self.context.user,
                    self.context.job_id, exc_info=True)
            return self
        if reboot_block.getStatus() == pybgsched.Block.Free:
            self.context.status_string.append("%s/%s: Block %s free, retrying boot." % (self.context.user,
                self.context.job_id, self.context.subblock_parent))
            self.context.reboot_attempts += 1
            return BootPending(self.context)
        elif reboot_block.getStatus() in [pybgsched.Block.Allocated, pybgsched.Block.Booting]:
            #block has already started a reboot.  This can happen esaily with subblocks.
            self.context.status_string.append("%s/%s: Block %s now booting. Waiting for boot completion." % (self.context.user,
                self.context.job_id, self.context.subblock_parent))
            self.context.reboot_attempts += 1
            return BootInitiating(self.context)
        elif reboot_block.getStatus() == pybgsched.Block.Initialized and reboot_block.getAction() != pybgsched.Action.Free:
            #The block is apparently in a normal booted state, also shows up in subblock jobs.
            self.context.status_string.append("%s/%s: Block %s found booted.  Boot complete." % (self.context.user,
                self.context.job_id, self.context.subblock_parent))
            self.context.reboot_attempts += 1
            return BootComplete(self.context)
        return self


class BootContext(object):

    '''Context for ongonig boot.  This should include any resources specific to that individual boot.
    A pointer to one of these objects is passed to the boot state for processing.

    '''
    def __init__(self, block, job_id, user, block_lock, subblock_parent=None):

        self.block = block
        self.block_id = self.block.name
        self.job_id = job_id
        self.user = user
        self.block_lock = block_lock
        if subblock_parent == None:
            self.subblock_parent = self.block.name
        else:
            self.subblock_parent = subblock_parent
        self.max_reboot_attempts = 0 #FIXME: make sure this is set
        self.reboot_attempts = 0
        self.status_string = []

    def under_resource_reservation(self):
        '''Return whether or not the block is under a resource reservation.  Handle locking as well for this check.

        '''
        self.block_lock.acquire()
        under_res = self.block.under_resource_reservation(self.job_id)
        self.block_lock.release()
        return under_res

class BGQBoot(object):
    '''Ongoing boot data object

    '''

    global _boot_id_gen

    _state_list = [BootPending, BootInitiating, BootComplete, BootFailed, BootRebooting,]
    _state_instances = []

    def __init__(self, block, job_id, user, block_lock, subblock_parent=None, boot_id=None):
        if boot_id != None:
            self.boot_id == boot_id
        else:
            self.boot_id = _boot_id_gen.next()
        self.context = BootContext(block, job_id, user, block_lock, subblock_parent)
        self.__statemachine = Cobalt.TriremeStateMachine.StateMachineProcessor()
        self.initialize_state_machine()

    def initialize_state_machine(self):

        for state in self._state_list:
            state_instance = state(self.context)
            self._state_instances.append(state_instance)
            self.__statemachine.add_transition(str(state_instance), state_instance.progress, state_instance.get_valid_transition_dict())
        self.__statemachine.set_initialstate('pending')
        self.__statemachine.set_exceptionstate('failed')
        self.__statemachine.initialize()
        self.__statemachine.start()

    #get/setstate not allowed.  Should not be used with this class due to the lock and block data reacquistion.  Must be
    #reconstructed at restart --PMR

    def __getstate__(self):
        raise RuntimeError, "Serialization for Block not allowed, must be reconstructed."

    def __setstate__(self, state):
        raise RuntimeError, "Deerialization for Block not allowed, must be reconstructed."

    @property
    def state(self):
        return self.__statemachine.get_state()

    @property
    def block_id(self):
        return self.context.block_id

    @property
    def failure_string(self):
        return self.context.failure_string

    def get_details(self):
        return {'boot_id': self.boot_id, 'block_name': self.context.block.name, 'job_id': self.context.job_id,
                'user': self.context.user, 'state': self.__statemachine.get_state(),}

    def __str__(self):
        return str(self.get_details())

    def __eq__(self, other):
        return self.boot_id == other.boot_id

    def __hash__(self):
        return hash(self.boot_id)

    def progress(self):
        self.__statemachine.process()


class BGQBooter(Cobalt.QueueThread.QueueThread):
    '''Track boots and reboots.

    '''

    def __init__(self, all_blocks, block_lock, *args, **kwargs):
        '''register handlers for this set of messages
        The start method must be called separately.
        This thread runs itself detached by default.
        Input:
            block_lock -- reference to the thread lock for block data
            all_blocks -- a reference to the blocks list.  This should be all available blocks, not just managed blocks
        '''
        #must be reinstantiated so that it gets the right lock instance, threading locks are not serializable.
        super(BGQBooter, self).__init__(*args, **kwargs)
        self.pending_boots = set()
        self.all_blocks = all_blocks
        self.block_lock = block_lock
        self.boot_data_lock = threading.Lock()
        self.daemon = True
        #register actions to take during the run loop:
        self.booting_suspended = False
        self.register_run_action('progress_boot', self.progress_boot)
        self.register_handler('initiate_boot', self.handle_initiate_boot)

    def __getstate__(self):
        #provided as a convenience for later reconstruction
        return {'version': 1, 'next_boot_id': __boot_id_gen.idnum,
                'pending_boots': [boot.get_details() for boot in list(self.pending_boots)],
                'booting_suspended':self.booting_suspended}

    def __setstate__(self, spec):
        raise NotImplementedError, "Setstate is forbidden for this object."

    def restore_boot_id(self, restore_val):
        '''restore the boot id to a saved value.
        '''
        global _boot_id_gen
        _boot_id_gen.idnum = restore_val - 1
        return

    def suspend_booting(self):
        '''Halt boot progress, needed if force-cleaning a block and certain control system actions'''
        self.booting_suspended = True

    def resume_bootng(self):
        '''Allow booting to progress again'''
        self.booting_suspended = False

    def stat(self, block_ids=None):
        '''Return pending boot statuses.

        block_ids (default None): a list of blocks id's to return pending boot statuses, if None, apply to all blocks

        '''
        self.boot_data_lock.acquire()
        if block_ids == None:
            boot_set = list(self.pending_boots)
        else:
            boot_set = set([pending_boot for pending_boot in list(self.pending_boots) if pending_boot.block_id in block_ids])
        self.boot_data_lock.release()
        return list(boot_set)

    def reap(self, block_id):
        '''clear out completed, failed, or otherwise terminated boots

        '''
        boots_to_clear = []
        for boot in self.pending_boots():
            if boot.block_id == block_id and boot.state in ['complete', 'failed']:
                boots_to_clear.append(boot)

        for boot in boots_to_clear:
            self.pending_boots.remove(boot)
        return

    def initiate_boot(self, block_id, job_id, user, subblock_parent=None):
        '''Asynchrynously initiate a boot.  This will return immediately, the boot should be in the pending state.

        '''
        self.send(InitiateBootMsg(block_id, job_id, user, subblock_parent))
        return

    def progress_boot(self):
        '''callback to be registered with the run method.
        This gets executed after all messages have been parsed.

        '''
        if not self.booting_suspended:
            self.boot_data_lock.acquire()
            for boot in self.pending_boots:
                boot.progress()
            self.boot_data_lock.release()
        return

    def handle_initiate_boot(self, msg):
        '''callback for handling an initate boot message and constructing the boot object

        '''
        new_boot = BGQBoot(self.all_blocks[msg.block_id], msg.job_id, msg.user, self.block_lock)
        try:
            if msg.msg_type == 'initiate_boot':
                self.pending_boots.add(new_boot)
                return True
        except AttributeError:
            #We apparently cannot handle this message as it lacks a message type
            return False
        return False

#Boot messages, possibly break out into separate file
class InitiateBootMsg(object):

    def __init__(self, block_id, job_id, user, subblock_parent=None):
        self.msg_type = 'initiate_boot'
        self.block_id = block_id
        self.job_id = job_id
        self.user = user
        self.subblock_parent = subblock_parent

    def __str__(self):
        return "<InitiateBootMsg: msg_type=%s, block_id=%s, job_id=%s, user=%s, subblock_parent=%s>" % (self.msg_type, self.block_id, self.job_id, self.user, self.subblock_parent)



#break this into a unit test file

from nose import *
from nose.tools import timed, TimeExpired
from TestCobalt.Utilities.Time import timeout
import time

class test_BGQBoot(object):

    class TestBlock(object):

        def __init__(self, name, reserved=True, block_type='normal'):
            self.name = name
            self.reserved = reserved
            self.block_type = 'normal'

        def under_resource_reservation(self, job_id):
            return self.reserved

    def setup(self):
        pybgsched.Block('TB-1', 512)
        self.block_lock = threading.Lock()

    def teardown(self):
        pybgsched.block_dict = {}

    def test_initialization(self):
        boot = BGQBoot(pybgsched.block_dict['TB-1'], 1, 'testuser', self.block_lock)
        assert str(boot) == "{'block_name': 'TB-1', 'user': 'testuser', 'state': 'pending', 'job_id': 1, 'boot_id': 1}", "Malformed boot: %s" % boot


class test_BGQBooter(object):

    class TestBlock(object):

        def __init__(self, name, reserved=True, block_type='normal'):
            self.name = name
            self.reserved = reserved
            self.block_type = 'normal'

        def under_resource_reservation(self, job_id):
            return self.reserved

    def setup(self):
        pybgsched.Block('TB-1', 512)
        pybgsched.Block('TB-2', 512)
        pybgsched.Block('TB-3', 512)
        self.test_blocks = {}
        self.test_blocks['TB-1'] = test_BGQBooter.TestBlock('TB-1')
        self.test_blocks['TB-2'] = test_BGQBooter.TestBlock('TB-2')
        self.test_blocks['TB-3'] = test_BGQBooter.TestBlock('TB-3')
        self.block_lock = threading.Lock()

        self.booter = BGQBooter(self.test_blocks, self.block_lock)
        self.booter.restore_boot_id(1)

    def teardown(self):
        if self.booter.is_alive():
            self.booter.close()
        pybgsched.block_dict = {}

    @timeout(3)
    def test_message_creation(self):
        self.booter.start()
        self.booter.initiate_boot('TB-1', 1, 'testuser')
        assert self.booter.all_blocks['TB-1'].under_resource_reservation(1)
        time.sleep(2)
        assert self.booter.pending_boots, 'boot not added: %s' % self.booter.pending_boots

class test_BootPending(object):


    class TestBlock(object):

        def __init__(self, name, reserved=True, block_type='normal'):
            self.name = name
            self.reserved = reserved
            self.block_type = 'normal'

        def under_resource_reservation(self, job_id):
            return self.reserved

    def setup(self):
        pybgsched.Block('TB-1', 512)
        self.block_lock = threading.Lock()

    def teardown(self):
        pybgsched.block_dict = {}

    def test_not_reserved(self):
        block = self.TestBlock('TB-1', reserved=False)
        context = BootContext(block, 1, 'testuser', self.block_lock)
        next_state = BootPending(context).progress()
        assert 'failed' == str(next_state), "Returned state was %s" % next_state

    def test_reserved_non_subblock(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        next_state = BootPending(context).progress()
        assert 'initiating' == str(next_state), "Returned state was %s" % next_state

    def test_control_system_failure(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        pybgsched.Block.set_error('control system failure')
        next_state = BootPending(context).progress()
        assert 'failed' == str(next_state), "Returned state was %s" % next_state

    def test_initial_subblock(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        block.block_type = 'pseudoblock'
        next_state = BootPending(context).progress()
        assert 'initiating' == str(next_state), "Returned state was %s" % next_state

    def test_subblock_pending_action(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        block.block_type = 'pseudoblock'
        pybgsched.block_dict['TB-1'].set_action(pybgsched.Action.Free)
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Initialized)
        next_state = BootPending(context).progress()
        assert 'pending' == str(next_state), "Returned state was %s" % next_state

    def test_subblock_already_initialized(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        block.block_type = 'pseudoblock'
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Initialized)
        next_state = BootPending(context).progress()
        assert 'complete' == str(next_state), "Returned state was %s" % next_state

class test_BootInitiating(object):

    class TestBlock(object):

        def __init__(self, name, reserved=True, block_type='normal'):
            self.name = name
            self.reserved = reserved
            self.block_type = 'normal'

        def under_resource_reservation(self, job_id):
            return self.reserved

    def setup(self):
        pybgsched.Block('TB-1', 512)
        self.block_lock = threading.Lock()

    def teardown(self):
        pybgsched.block_dict = {}

    def test_not_reserved(self):
        block = self.TestBlock('TB-1', reserved=False)
        context = BootContext(block, 1, 'testuser', self.block_lock)
        next_state = BootInitiating(context).progress()
        assert 'failed' == str(next_state), "Returned state was %s" % next_state

    def test_continuing_initialization(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Booting)
        next_state = BootInitiating(context).progress()
        assert 'initiating' == str(next_state), "Returned state was %s" % next_state
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Allocated)
        next_state = BootInitiating(context).progress()
        assert 'initiating' == str(next_state), "Returned state was %s" % next_state

    def test_action_set(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        pybgsched.block_dict['TB-1'].set_action(pybgsched.Action.Free)
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Initialized)
        next_state = BootInitiating(context).progress()
        assert 'rebooting' == str(next_state), "Returned state was %s" % next_state

    def test_go_to_reboot(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Terminating)
        next_state = BootInitiating(context).progress()
        assert 'rebooting' == str(next_state), "Returned state was %s" % next_state
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Free)
        next_state = BootInitiating(context).progress()
        assert 'rebooting' == str(next_state), "Returned state was %s" % next_state

    def test_boot_completion(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Initialized)
        next_state = BootInitiating(context).progress()
        assert 'complete' == str(next_state), "Returned state was %s" % next_state


class test_BootRebooting(object):

    class TestBlock(object):

        def __init__(self, name, reserved=True, block_type='normal'):
            self.name = name
            self.reserved = reserved
            self.block_type = 'normal'

        def under_resource_reservation(self, job_id):
            return self.reserved

    def setup(self):
        pybgsched.Block('TB-1', 512)
        self.block_lock = threading.Lock()

    def teardown(self):
        pybgsched.block_dict = {}

    def test_reboot_free(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        context.max_reboot_attempts = 3
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Free)
        next_state = BootRebooting(context).progress()
        assert 'pending' == str(next_state), "Returned state was %s" % next_state

    def test_reboot_initialized(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        context.max_reboot_attempts = 3
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Initialized)
        next_state = BootRebooting(context).progress()
        assert 'complete' == str(next_state), "Returned state was %s" % next_state

    def test_reboot_initialized_free_pending(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        context.max_reboot_attempts = 3
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Initialized)
        pybgsched.block_dict['TB-1'].set_action(pybgsched.Action.Free)
        next_state = BootRebooting(context).progress()
        assert 'rebooting' == str(next_state), "Returned state was %s" % next_state

    def test_reboot_booting(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        context.max_reboot_attempts = 3
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Booting)
        next_state = BootRebooting(context).progress()
        assert 'initiating' == str(next_state), "Returned state was %s" % next_state

    def test_reboot_allocating(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        context.max_reboot_attempts = 3
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Allocated)
        next_state = BootRebooting(context).progress()
        assert 'initiating' == str(next_state), "Returned state was %s" % next_state

    def test_reboot_terminating(self):
        block = self.TestBlock('TB-1')
        context = BootContext(block, 1, 'testuser', self.block_lock)
        context.max_reboot_attempts = 3
        pybgsched.block_dict['TB-1'].set_status(pybgsched.Block.Terminating)
        next_state = BootRebooting(context).progress()
        assert 'rebooting' == str(next_state), "Returned state was %s" % next_state


