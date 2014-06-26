from ctypes import CDLL, cast, byref, c_void_p, c_int, c_int64, c_char_p, POINTER, pointer, Structure

__all__ = [
    "set_serial", "get_serial", "OrcmCluster", "Node", "NodeList", "PartitionList", "Partition", "JobList", "Job",
]

bridge = CDLL("liborcm.so")
libc = CDLL("libc.so.6")

status_t = c_int

def free_value (cdata):
    value = cdata.value
    libc.free(cdata)
    return value

def check_status (status, **kwargs):
    if status == 0:
        return status
    
    exceptions = kwargs.get("exceptions")
    if exceptions is None:
        exceptions = (
            PartitionNotFound, JobNotFound, BasePartitionNotFound,
            SwitchNotFound, JobAlreadyDefined, ConnectionError,
            InternalError, InvalidInput, IncompatibleState,
            InconsistentData
        )
    default = kwargs.get("default")
    if default is None:
        default = BridgeException
    
    for exception in exceptions:
        if status == exception.status:
            raise exception()
    raise BridgeException("encountered unexpected status: %i" % status)

rm_element_t = c_void_p
rm_component_id_t = c_char_p
rm_sequence_id_t = c_int64

bridge.rm_get_data.argtypes = [rm_element_t, c_int, c_void_p]
bridge.rm_get_data.restype = check_status

bridge.rm_set_data.argtypes = [rm_element_t, c_int, c_void_p]
bridge.rm_set_data.restype = check_status


class BridgeException (Exception):
    
    """An exception caused by the c bridge library."""

class PartitionNotFound (BridgeException):
    
    status = -1


class JobNotFound (BridgeException):
    
    status = -2


class BasePartitionNotFound (BridgeException):
    
    status = -3


class SwitchNotFound (BridgeException):
    
    status = -4


class JobAlreadyDefined (BridgeException):
    
    status = -5


class ConnectionError (BridgeException):
    
    status = -10


class InternalError (BridgeException):
    
    status = -11


class InvalidInput (BridgeException):
    
    status = -12


class IncompatibleState (BridgeException):
    
    status = -13


class InconsistentData (BridgeException):
    
    status = -14


class Resource (object):
    _free = False
    
    def __init__ (self, element_pointer, **kwargs):
        self._as_parameter_ = element_pointer
        self._free = kwargs.get("free")
    
    def _get_data (self, field, ctype):
        data = ctype()
        bridge.rm_get_data(self, field, byref(data))
        return data

    def _set_data (self, field, data):
        bridge.rm_set_data(self, field, byref(data))


class ElementGenerator (object):
    
    def __init__ (self, container, cls, numfield, firstfield, nextfield):
        self._container = container
        self._cls = cls
        self._numfield = numfield
        self._firstfield = firstfield
        self._nextfield = nextfield
            
    def __len__ (self):
        return self._container._get_data(self._numfield, c_int).value

    def __iter__ (self):
        for x in xrange(len(self)):
            if x == 0:
                yield self._cls(self._container._get_data(self._firstfield, self._cls._ctype))
            else:
                yield self._cls(self._container._get_data(self._nextfield, self._cls._ctype))

    def __getitem__ (self, index):
        return list(self)[index]

rm_serial_t = rm_component_id_t
bridge.rm_set_serial.argtypes = [rm_serial_t]
bridge.rm_set_serial.restype = check_status

def set_serial (serial):
    bridge.rm_set_serial(rm_serial_t(serial))

bridge.rm_get_serial.argtypes = []
bridge.rm_get_serial.restype = check_status

def get_serial ():
    serial = rm_serial_t()
    bridge.rm_get_serial(byref(serial))
    return serial.value


class rm_orcm_t (Structure):
    _fields_ = []


bridge.rm_get_orcm.argtypes = [POINTER(POINTER(rm_orcm_t))]
bridge.rm_get_orcm.restype = check_status

bridge.rm_free_orcm.argtypes = [POINTER(rm_orcm_t)]
bridge.rm_free_orcm.restype = check_status


class OrcmCluster (Resource):
    
    """The ORCM Cluster object represents the system.
    
    This object can be used to retrieve information and status for other
    components in the system.
    
    example:
    >>> set_serial("ORCM") # informs the bridge of which machine to reference
    >>> orcm = OrcmCluster.by_serial() # get the machine
    
    """
    
    _ctype = POINTER(rm_orcm_t)
    
    @classmethod
    def by_serial (cls):
        """Retrieve a BlueGene object based on the global serial id."""
        element_pointer = cls._ctype()
        bridge.rm_get_orcm(byref(element_pointer))
        return cls(element_pointer, free=True)
    
    def __init__ (self, element_pointer, **kwargs):
        """Create a BlueGene object based on existing memory.
        
        arguments:
        element_pointer -- memory address for machine in bridge
        """
        Resource.__init__(self, element_pointer, **kwargs)
        self.base_partitions = list(ElementGenerator(self, BasePartition, RM_BPNum, RM_FirstBP, RM_NextBP))
        self.switches = list(ElementGenerator(self, Switch, RM_SwitchNum, RM_FirstSwitch, RM_NextSwitch))
        self.wires = list(ElementGenerator(self, Wire, RM_WireNum, RM_FirstWire, RM_NextWire))
    
    def __del__ (self):
        if self._free:
            bridge.rm_free_orcm(self)
    
    def _get_base_partition_size (self):
        size = self._get_data(RM_BPsize, rm_size3D_t)
        return to_size_tuple(size)
    
    base_partition_size = property(_get_base_partition_size,
        doc="The size of a base partition (in c-nodes) in each dimension.")
    
    def _get_machine_size (self):
        size = self._get_data(RM_Msize, rm_size3D_t)
        return to_size_tuple(size)
    
    machine_size = property(_get_machine_size,
        doc="The size of the machine in base partition units.")


class rm_partition_t (Structure):
    _fields_ = []

pm_partition_id_t = c_char_p
rm_partition_state_t = c_int
rm_partition_state_values = ("RM_PARTITION_FREE", "RM_PARTITION_CONFIGURING", "RM_PARTITION_READY", "RM_PARTITION_BUSY", "RM_PARTITION_DEALLOCATING", "RM_PARTITION_ERROR", "RM_PARTITION_NAV")
                                 "RM_PARTITION_DEALLOCATING", "RM_PARTITION_ERROR", "RM_PARTITION_NAV")
rm_partition_mode_t = c_int
rm_partition_mode_values = ("RM_PARTITION_COPROCESSOR_MODE", "RM_PARTITION_VIRTUAL_NODE_MODE")

bridge.rm_get_partition.argtypes = [pm_partition_id_t, POINTER(POINTER(rm_partition_t))]
bridge.rm_get_partition.restype = check_status

bridge.rm_free_partition.argtypes = [POINTER(rm_partition_t)]
bridge.rm_free_partition.restype = check_status

bridge.pm_destroy_partition.argtypes = [pm_partition_id_t]
bridge.pm_destroy_partition.restype = check_status

RM_PartitionID = 39
RM_PartitionState = 40
RM_PartitionConnection = 41
RM_PartitionUserName = 42
RM_PartitionBPNum = 43
RM_PartitionFirstBP = 44
RM_PartitionNextBP = 45
RM_PartitionSwitchNum = 46
RM_PartitionFirstSwitch = 47
RM_PartitionNextSwitch = 48
RM_PartitionMloaderImg = 49
RM_PartitionBlrtsImg = 50
RM_PartitionLinuxImg = 51
RM_PartitionRamdiskImg = 52
RM_PartitionOptions = 53
RM_PartitionMode = 54
RM_PartitionDescription = 55
RM_PartitionSmall = 56
RM_PartitionNodeCardNum = 57
RM_PartitionFirstNodeCard = 58
RM_PartitionNextNodeCard = 59
RM_PartitionPsetsPerBP = 60
RM_PartitionUsersNum = 61
RM_PartitionFirstUser = 62
RM_PartitionNextUser = 63

class Partition (Resource):
    
    _ctype = POINTER(rm_partition_t)
    
    @classmethod
    def by_id (cls, id):
        element_pointer = cls._ctype()
        bridge.rm_get_partition(pm_partition_id_t(id), byref(element_pointer))
        return cls(element_pointer, free=True)
    
    def __init__ (self, element_pointer, **kwargs):
        Resource.__init__(self, element_pointer, **kwargs)
        self.base_partitions = list(ElementGenerator(self, BasePartition, RM_PartitionBPNum, RM_PartitionFirstBP, RM_PartitionNextBP))
        
        self._nodes = list(ElementGenerator(self, Node, RM_PartitionNodeNum, RM_PartitionFirstNode, RM_PartitionNextNode))
    
    def _get_nodes (self):
        return self._nodes
    
    nodes = property(_get_nodes)
    
    def _get_partition_nodes (self):
        for partition in self.partitions:
            for node in NodeList.by_partition(partition):
                yield node
    
    def _get_id (self):
        id = self._get_data(RM_PartitionID, pm_partition_id_t)
        return free_value(id)
    
    id = property(_get_id)
    
    def _get_state (self):
        state = self._get_data(RM_PartitionState, rm_partition_state_t)
        return rm_partition_state_values[state.value]
    
    state = property(_get_state)
    
    def _get_job_id (self):
        job_id = self._get_data(RM_PartitionJobID, c_int)
        return job_id.value
    
    def _get_user_name (self):
        name = self._get_data(RM_PartitionUserName, c_char_p)
        return free_value(name)
    
    user_name = property(_get_user_name)
    
    def _get_compute_node_kernel_image (self):
        image = self._get_data(RM_PartitionCnloadImg, c_char_p)
        return free_value(image)

    compute_node_kernel_image = property(_get_compute_node_kernel_image)
    
    def _get_description (self):
        description = self._get_data(RM_PartitionDescription, c_char_p)
        return free_value(description)
    
    description = property(_get_description)
    
    def _get_options (self):
        options = self._get_data(RM_PartitionOptions, c_char_p)
        return options.value
    
    options = property(_get_options)
   
    def _get_partition_size(self):
        size = self._get_data(RM_PartitionSize, c_int)
        return size.value

    partition_size = property(_get_partition_size)

    def _get_mode (self):
        mode = self._get_data(RM_PartitionMode, rm_partition_mode_t)
        return rm_partition_mode_values[mode.value]

class rm_node_t (Structure):
    _fields_ = []

rm_node_id_t = rm_component_id_t
rm_node_state_t = c_int
rm_node_state_values = ("RM_NODE_UP", "RM_NODE_DOWN", "RM_NODE_MISSING", "RM_NODE_ERROR", "RM_NODE_NAV")

RM_NodeID = 18
RM_NodeState = 20
RM_NodePartID = 22
RM_NodePartState = 23

bridge.rm_free_node.argtypes = [POINTER(rm_nodecard_t)]
bridge.rm_free_node.restype = check_status

class Node (Resource):
    
    _ctype = POINTER(rm_node_t)
    
    def __del__ (self):
        if self._free:
            bridge.rm_free_node(self)
    
    def _get_id (self):
        id = self._get_data(RM_NodeID, rm_node_id_t)
        return free_value(id)
    
    id = property(_get_id)
    
    def _get_state (self):
        state = self._get_data(RM_NodeState, rm_node_state_t)
        return rm_node_state_values[state.value]
    
    state = property(_get_state)
    
    def _get_partition_id (self):
        partition_id = self._get_data(RM_NodePartID, pm_partition_id_t)
        return free_value(partition_id)
    
    partition_id = property(_get_partition_id)
    
    def _get_partition_state (self):
        state = self._get_data(RM_NodePartState, rm_partition_state_t)
        return rm_partition_state_values[state.value]
    
    partition_state = property(_get_partition_state)


class rm_node_list_t (Structure):
    _fields_ = []

bridge.rm_get_nodes.argtypes = [rm_bp_id_t, POINTER(POINTER(rm_nodecard_list_t))]
bridge.rm_get_nodes.restype = check_status
bridge.rm_free_node_list.argtypes = [POINTER(rm_nodecard_list_t)]
bridge.rm_free_node_list.restype = check_status

class NodeList (Resource, list):
    
    _ctype = POINTER(rm_node_list_t)
    
    @classmethod
    def by_base_partition (cls, base_partition):
        try:
            base_partition_id = base_partition.id # accepts a BasePartition...
        except AttributeError:
            base_partition_id = base_partition # or a bpid
        element_pointer = cls._ctype()
        bridge.rm_get_nodecards(c_char_p(base_partition_id), byref(element_pointer))
        return cls(element_pointer, free=True)
    
    def __init__ (self, element_pointer, **kwargs):
        Resource.__init__(self, element_pointer, **kwargs)
        self.extend(ElementGenerator(self, Node, RM_NodeListSize, RM_NodeListFirst, RM_NodeListNext))
    
    def __del__ (self):
        if self._free:
            bridge.rm_free_node_list(self)
    
    def __repr__ (self):
        return "<%s %i>" % (self.__class__.__name__, len(self))


JOB_IDLE_FLAG = 0x1
JOB_STARTING_FLAG = 0x2
JOB_RUNNING_FLAG = 0x4
JOB_TERMINATED_FLAG = 0x8
JOB_ERROR_FLAG = 0x10
JOB_DYING_FLAG = 0x20
JOB_DEBUG_FLAG = 0x40
JOB_LOAD_FLAG = 0x80
JOB_LOADED_FLAG = 0x100
JOB_BEGIN_FLAG = 0x200
JOB_ATTACH_FLAG = 0x400
JOB_KILLED_FLAG = 0x800
JOB_ALL_FLAG = 0xFFF

class rm_job_list_t (Structure):
    _fields_ = []

rm_job_state_flag_t = c_int
bridge.rm_get_jobs.argtypes = [rm_job_state_flag_t, POINTER(POINTER(rm_job_list_t))]
bridge.rm_get_jobs.restype = check_status
bridge.rm_free_job_list.argtypes = [POINTER(rm_job_list_t)]
bridge.rm_free_job_list.restype = check_status

class JobList (Resource, list):
    
    _ctype = POINTER(rm_job_list_t)
    
    @classmethod
    def by_flag (cls, flag=JOB_ALL_FLAG):
        element_pointer = cls._ctype()
        bridge.rm_get_jobs(c_int(flag), byref(element_pointer))
        return cls(element_pointer, free=True)
    
    @classmethod
    def by_filter (cls, job_filter):
        element_pointer = cls._ctype()
        bridge.rm_get_filtered_jobs(job_filter, byref(element_pointer))
        return cls(element_pointer, free=True)
    
    def __init__ (self, element_pointer, **kwargs):
        Resource.__init__(self, element_pointer, **kwargs)
        self.extend(ElementGenerator(self, Job, RM_JobListSize, RM_JobListFirstJob, RM_JobListNextJob))
    
    def __del__ (self):
        if self._free:
            bridge.rm_free_job_list(self)


class rm_job_t (Structure):
    _fields_ = []

rm_job_id_t = c_char_p
db_job_id_t = c_int
rm_job_state_t = c_int
rm_job_state_values = ("RM_JOB_IDLE", "RM_JOB_STARTING", "RM_JOB_RUNNING", "RM_JOB_TERMINATED", "RM_JOB_KILLED", "RM_JOB_ERROR", "RM_JOB_DYING", "RM_JOB_DEBUG", "RM_JOB_LOAD", "RM_JOB_LOADED", "RM_JOB_BEGIN", "RM_JOB_ATTACH", "RM_JOB_NAV")
rm_job_mode_t = c_int
rm_job_mode_values = ("RM_COPROCESSOR_MODE", "RM_VIRTUAL_NODE_MODE")
rm_job_strace_t = c_int
rm_job_stdin_info_t = c_int
rm_job_stdout_info_t = c_int
rm_job_stderr_info_t = c_int
rm_job_runtime_t = c_int
rm_job_computenodes_used_t = c_int
rm_job_exitstatus_t = c_int
rm_signal_t = c_int
rm_job_user_uid_t = c_int
rm_job_user_gid_t = c_int
rm_job_location_t = c_char_p
pm_pool_id_t = c_char_p

RM_JobState = 64
RM_JobExecutable = 65
RM_JobID = 66
RM_JobPartitionID = 67
RM_JobUserName = 68
RM_JobDBJobID = 69
RM_JobOutFile = 70
RM_JobInFile = 71
RM_JobErrFile = 72
RM_JobOutDir = 73
RM_JobErrText = 74
RM_JobArgs = 75
RM_JobEnvs = 76
RM_JobInHist = 77
RM_JobExitStatus = 78
RM_JobMode = 79
# Revision 2
RM_JobStrace = 89
RM_JobStdinInfo = 90
RM_JobStdoutInfo = 91
RM_JobStderrInfo = 92
# Revision 3
RM_JobStartTime = 94
RM_JobEndTime = 95
RM_JobRunTime = 96
RM_JobComputeNodesUsed = 97

RM_JOB_IDLE = 0
RM_JOB_STARTING = 1
RM_JOB_RUNNING = 2
RM_JOB_TERMINATED = 3
RM_JOB_KILLED = 4
RM_JOB_ERROR = 5
RM_JOB_DYING = 6
RM_JOB_DEBUG = 7
RM_JOB_LOAD = 8
RM_JOB_LOADED = 9
RM_JOB_BEGIN = 10
RM_JOB_ATTACH = 11


bridge.jm_signal_job.argtypes = [db_job_id_t, rm_signal_t]
bridge.jm_signal_job.restype = check_status

bridge.jm_cancel_job.argtypes = [db_job_id_t]
bridge.jm_cancel_job.restype = check_status