import logging

import Cobalt.Components.bgqsystem 
from Cobalt.Components.bgqsystem import BGSystem
#from test_base import TestComponent

class TestBGQSystem(object):
    
    def setup (self):
        #TestComponent.setup(self)
        self.bgqsystem = BGSystem()


    def test_parse_subblock_config_empty(self):

        ret = self.bgqsystem.parse_subblock_config('Empty')
        assert {} == ret, "Failed: String 'Empty' did not return empty dict."

    def test_parse_subblock_config_none(self):
        ret = self.bgqsystem.parse_subblock_config(None)
        assert {} == ret, "Failed: Passing in None did not return empty dict."

    
    def test_parse_subblock_config_empty_str(self):
        ret = self.bgqsystem.parse_subblock_config('')
        assert {} == ret, "Failed: Passing in empty string did not return empty dict."

    def test_parse_subblock_cofng_str(self):

        ok_dict ={'TEST-00000-11331-128':32,
                  'TEST1-22000-33331-128':64,
                  'TEST2-00040-11331-128':1}
        ret = self.bgqsystem.parse_subblock_config(
                'TEST-00000-11331-128:32,TEST1-22000-33331-128:64,TEST2-00040-11331-128:1')
        assert ok_dict == ret, "Failed: Incorrect parsing of test string."

    def test_node_map_gen(self):

        correct_node_map = {0:[0,0,0,0,0],1:[0,0,1,0,0],
                           2:[0,1,1,0,0],3:[0,1,0,0,0],
                           4:[0,1,0,0,1],5:[0,1,1,0,1],
                           6:[0,0,1,0,1],7:[0,0,0,0,1],
                           8:[0,1,0,1,1],9:[0,1,1,1,1],
                           10:[0,0,1,1,1],11:[0,0,0,1,1],
                           12:[0,0,0,1,0],13:[0,0,1,1,0],
                           14:[0,1,1,1,0],15:[0,1,0,1,0],
                           16:[1,0,1,1,0],17:[1,0,0,1,0],
                           18:[1,1,0,1,0],19:[1,1,1,1,0],
                           20:[1,1,1,1,1],21:[1,1,0,1,1],
                           22:[1,0,0,1,1],23:[1,0,1,1,1],
                           24:[1,1,1,0,1],25:[1,1,0,0,1],
                           26:[1,0,0,0,1],27:[1,0,1,0,1],
                           28:[1,0,1,0,0],29:[1,0,0,0,0],
                           30:[1,1,0,0,0],31:[1,1,1,0,0]}
        generated_node_map = Cobalt.Components.bgq_base_system.generate_base_node_map()

        for i in range(0,32):
            assert correct_node_map[i] == generated_node_map[i], "Node map failure: expected %s for position %s, got %s"% (correct_node_map[i], i, generated_node_map[i])

    def test_nodeboard_masks(self):
        
        #make sure that the proper dimension reversals happen.

        assert Cobalt.Components.bgq_base_system.NODECARD_A_DIM_MASK == 4
        assert Cobalt.Components.bgq_base_system.NODECARD_B_DIM_MASK == 8
        assert Cobalt.Components.bgq_base_system.NODECARD_C_DIM_MASK == 1
        assert Cobalt.Components.bgq_base_system.NODECARD_D_DIM_MASK == 2
        assert Cobalt.Components.bgq_base_system.NODECARD_E_DIM_MASK == 8


        for i in range(0,16):
            check = 0
            check += i & Cobalt.Components.bgq_base_system.NODECARD_A_DIM_MASK
            check += i & Cobalt.Components.bgq_base_system.NODECARD_B_DIM_MASK
            check += i & Cobalt.Components.bgq_base_system.NODECARD_C_DIM_MASK
            check += i & Cobalt.Components.bgq_base_system.NODECARD_D_DIM_MASK
            assert i == check, "Mask for %d did not match expected value" % i


        reverse_dims = ([0,0,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,1,1,0],
                        [1,0,0,0,0],[1,0,1,0,0],[1,0,0,1,0],[1,0,1,1,0], 
                        [0,1,0,0,1],[0,1,1,0,1],[0,1,0,1,1],[0,1,1,1,1],
                        [1,1,0,0,1],[1,1,1,0,1],[1,1,0,1,1],[1,1,1,1,1]) 

        for i in range(0,16):
            rev_A = bool(i & Cobalt.Components.bgq_base_system.NODECARD_A_DIM_MASK)
            rev_B = bool(i & Cobalt.Components.bgq_base_system.NODECARD_B_DIM_MASK)
            rev_C = bool(i & Cobalt.Components.bgq_base_system.NODECARD_C_DIM_MASK)
            rev_D = bool(i & Cobalt.Components.bgq_base_system.NODECARD_D_DIM_MASK)
            rev_E = bool(i & Cobalt.Components.bgq_base_system.NODECARD_E_DIM_MASK)
            
            assert int(rev_A) == reverse_dims[i][0], "Mismatch in reversed A dimension: board %d, value" % i
            assert int(rev_B) == reverse_dims[i][1], "Mismatch in reversed B dimension: board %d, value" % i
            assert int(rev_C) == reverse_dims[i][2], "Mismatch in reversed C dimension: board %d, value" % i
            assert int(rev_D) == reverse_dims[i][3], "Mismatch in reversed D dimension: board %d, value" % i
            assert int(rev_E) == reverse_dims[i][4], "Mismatch in reversed E dimension: board %d, value" % i

    def test_extents_from_size(self):

        correct_extents = {1:[1,1,1,1,1],
                           2:[1,1,1,1,2],
                           4:[1,1,1,2,2],
                           8:[1,1,2,2,2],
                           16:[1,2,2,2,2],
                           32:[2,2,2,2,2],
                           64:[2,2,4,2,2],
                           128:[2,2,4,4,2]}

        for size,extents in correct_extents.iteritems():
            ret_extents = Cobalt.Components.bgq_base_system.get_extents_from_size(size)
           
            for i in range(0,5):
                assert ret_extents[i] == extents[i], "Mismatch in extents for size %d"% size


