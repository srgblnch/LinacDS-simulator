#!/usr/bin/python
# -*- coding: utf-8 -*-

# LinacSimulator.py
# This file is part of tango-ds (http://sourceforge.net/projects/tango-ds/)
#
# tango-ds is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# tango-ds is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with tango-ds.  If not, see <http://www.gnu.org/licenses/>.

'''Simulation of the PLC2 for the Linac control at ALBA.
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-

# LinacSimulator.py
# This file is part of tango-ds (http://sourceforge.net/projects/tango-ds/)
#
# tango-ds is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# tango-ds is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with tango-ds.  If not, see <http://www.gnu.org/licenses/>.

'''Simulation of the PLC1 for the Linac control at ALBA.
'''

from numpy import array,uint8
import PyTango

READSIZE = 121
WRITESIZE = 21

memoryMap = array([0x00]*(READSIZE),dtype=uint8)

#---- Read from li/ct/plc2 the 20130626
#     first level keys:
#      - type: type of stored data
#      - read_{addr,bit,value}: memory position when memory is send to read
#      - write_{addr,bit,value}: memory position from the received memory to write
#     second level keys:
#      - updatable: this attribute has some noise
#      - std: how big is the noise of this attribute
#      - reference: (TODO) key whose name is readback
#      - formula: (TODO) in case is more a reference than a readback
attributes = \
{'AC_IS': {'read_addr': 99,
           'read_bit': 1,
           'read_value': True,
           'type': PyTango.DevBoolean,
           'updatable':True,'probability':0.1},
 'CL1_ONC': {'read_addr': 117,
             'read_bit': 2,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'write_addr': 17,
             'write_bit': 2,
             'write_value': True},
 'CL1_PWD': {'read_addr': 68,
             'read_value': 19.59284782409668,
             'type': ('f', 4),
             'updatable':True,
             'std':1.01,},
 'CL1_ST': {'read_addr': 96,
            'read_value': 6,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'CL1_T': {'read_addr': 56,
           'read_value': 32.475811004638672,
           'type': ('f', 4),
           'updatable':True,
           'std':1.01,
           'write_addr': 0,
           'write_value': 32.500022888183594},
 'CL2_ONC': {'read_addr': 117,
             'read_bit': 3,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'write_addr': 17,
             'write_bit': 3,
             'write_value': True},
 'CL2_PWD': {'read_addr': 72,
             'read_value': 39.969795227050781,
             'type': ('f', 4),
             'updatable':True,
             'std':1.01,},
 'CL2_ST': {'read_addr': 97,
            'read_value': 4,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'CL2_T': {'read_addr': 60,
           'read_value': 30.513551712036133,
           'type': ('f', 4),
           'updatable':True,
           'std':1.01,
           'write_addr': 4,
           'write_value': 30.500024795532227},
 'CL3_ONC': {'read_addr': 117,
             'read_bit': 4,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'write_addr': 17,
             'write_bit': 4,
             'write_value': True},
 'CL3_PWD': {'read_addr': 76,
             'read_value': 32.003673553466797,
             'type': ('f', 4)},
 'CL3_ST': {'read_addr': 98,
            'read_value': 4,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'CL3_T': {'read_addr': 64,
           'read_value': 30.457548141479492,
           'type': ('f', 4),
           'updatable':True,
           'std':1.01,
           'write_addr': 8,
           'write_value': 30.500024795532227},
 'HVG1_IS': {'read_addr': 85,
             'read_bit': 2,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'updatable':True,'probability':0.1},
 'HVG1_P': {'read_addr': 36,
            'read_value': 9.4962517849239703e-09,
            'type': ('f', 4),
            'updatable':True,
            'std':1e-9,},
 'HVG2_IS': {'read_addr': 85,
             'read_bit': 3,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'updatable':True,'probability':0.1},
 'HVG2_P': {'read_addr': 40,
            'read_value': 2.7392012214022543e-08,
            'type': ('f', 4),
            'updatable':True,
            'std':1e-09,},
 'HVG3_IS': {'read_addr': 85,
             'read_bit': 4,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'updatable':True,'probability':0.1},
 'HVG3_P': {'read_addr': 44,
            'read_value': 7.9858120116682585e-09,
            'type': ('f', 4),
            'updatable':True,
            'std':1e-9},
 'HVG4_IS': {'read_addr': 85,
             'read_bit': 5,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'updatable':True,'probability':0.1},
 'HVG4_P': {'read_addr': 48,
            'read_value': 7.421486980518921e-09,
            'type': ('f', 4),
            'updatable':True,
            'std':1e-9},
 'HVG5_IS': {'read_addr': 85,
             'read_bit': 6,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'updatable':True,'probability':0.1},
 'HVG5_P': {'read_addr': 52,
            'read_value': 2.4070379023299893e-09,
            'type': ('f', 4),
            'updatable':True,
            'std':1e-9},
 'HeartBeat': {'read_addr': 99,
               'read_bit': 0,
               'read_value': False,
               'type': PyTango.DevBoolean},
 'IP1_IS': {'read_addr': 86,
            'read_bit': 0,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP1_P': {'read_addr': 0,
           'read_value': 4.4451846648030369e-09,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP1_ST': {'read_addr': 84,
            'read_bit': 0,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP2_IS': {'read_addr': 86,
            'read_bit': 1,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP2_P': {'read_addr': 4,
           'read_value': 4.6279962084838644e-09,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP2_ST': {'read_addr': 84,
            'read_bit': 1,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP3_IS': {'read_addr': 86,
            'read_bit': 2,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP3_P': {'read_addr': 8,
           'read_value': 1.7733842172518166e-09,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP3_ST': {'read_addr': 84,
            'read_bit': 2,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP4_IS': {'read_addr': 86,
            'read_bit': 3,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP4_P': {'read_addr': 12,
           'read_value': 1.0758641755259646e-09,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP4_ST': {'read_addr': 84,
            'read_bit': 3,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP5_IS': {'read_addr': 86,
            'read_bit': 4,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP5_P': {'read_addr': 16,
           'read_value': 1.3520482511353293e-08,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP5_ST': {'read_addr': 84,
            'read_bit': 4,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP6_IS': {'read_addr': 86,
            'read_bit': 5,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP6_P': {'read_addr': 20,
           'read_value': 5.894064791789333e-09,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP6_ST': {'read_addr': 84,
            'read_bit': 5,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP7_IS': {'read_addr': 86,
            'read_bit': 6,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP7_P': {'read_addr': 24,
           'read_value': 6.6515992713789274e-09,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP7_ST': {'read_addr': 84,
            'read_bit': 6,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP8_IS': {'read_addr': 86,
            'read_bit': 7,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP8_P': {'read_addr': 28,
           'read_value': 2.0668922129374323e-09,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP8_ST': {'read_addr': 84,
            'read_bit': 7,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP9_IS': {'read_addr': 86,
            'read_bit': 8,
            'read_value': False,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'IP9_P': {'read_addr': 32,
           'read_value': 2.3138175819781281e-09,
           'type': ('f', 4),
           'updatable':True,
           'std':1e-9},
 'IP9_ST': {'read_addr': 85,
            'read_bit': 0,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'updatable':True,'probability':0.1},
 'Lock_ST': {'read_addr': 95,
             'read_value': 0,
             'type': ('B',1)},
 'Locking': {'read_addr': 120,
             'read_bit': 0,
             'read_value': False,
             'type': PyTango.DevBoolean,
             'write_addr': 20,
             'write_bit': 0,
             'write_value': False},
 'Util_Interlock_RC': {'read_addr': 117,
                       'read_bit': 0,
                       'read_value': False,
                       'type': PyTango.DevBoolean,
                       'write_addr': 17,
                       'write_bit': 0,
                       'write_value': False},
 'VCV_ONC': {'read_addr': 116,
             'read_bit': 0,
             'read_value': True,
             'type': PyTango.DevBoolean,
             'write_addr': 16,
             'write_bit': 0,
             'write_value': True},
 'VCV_ST': {'read_addr': 87,
            'read_value': 2,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'VC_Interlock_RC': {'read_addr': 117,
                     'read_bit': 1,
                     'read_value': False,
                     'type': PyTango.DevBoolean,
                     'write_addr': 17,
                     'write_bit': 1,
                     'write_value': False},
 'VC_OK': {'read_addr': 85,
           'read_bit': 1,
           'read_value': True,
           'type': PyTango.DevBoolean,
           'updatable':True,'probability':0.1},
 'VV1_OC': {'read_addr': 116,
            'read_bit': 1,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'write_addr': 16,
            'write_bit': 1,
            'write_value': True},
 'VV1_ST': {'read_addr': 88,
            'read_value': 2,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'VV2_OC': {'read_addr': 116,
            'read_bit': 2,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'write_addr': 16,
            'write_bit': 2,
            'write_value': True},
 'VV2_ST': {'read_addr': 89,
            'read_value': 2,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'VV3_OC': {'read_addr': 116,
            'read_bit': 3,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'write_addr': 16,
            'write_bit': 3,
            'write_value': True},
 'VV3_ST': {'read_addr': 90,
            'read_value': 2,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'VV4_OC': {'read_addr': 116,
            'read_bit': 4,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'write_addr': 16,
            'write_bit': 4,
            'write_value': True},
 'VV4_ST': {'read_addr': 91,
            'read_value': 2,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'VV5_OC': {'read_addr': 116,
            'read_bit': 5,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'write_addr': 16,
            'write_bit': 5,
            'write_value': True},
 'VV5_ST': {'read_addr': 92,
            'read_value': 2,
            'type': ('B', 1),
            'updatable':True,'range':5},
 'VV6_OC': {'read_addr': 116,
            'read_bit': 6,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'write_addr': 16,
            'write_bit': 6,
            'write_value': True},
 'VV6_ST': {'read_addr': 93,
            'read_value': 2,
            'type': ('B', 1),
            #'updatable':True,'range':5
            },
 'VV7_OC': {'read_addr': 116,
            'read_bit': 7,
            'read_value': True,
            'type': PyTango.DevBoolean,
            'write_addr': 16,
            'write_bit': 7,
            'write_value': True},
 'VV7_ST': {'read_addr': 94,
            'read_value': 2,
            'type': ('B', 1),
            #'updatable':True,'range':5
            }
}
