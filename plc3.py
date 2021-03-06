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

'''Simulation of the PLC3 for the Linac control at ALBA.
'''

from numpy import array,uint8
import PyTango

READSIZE = 292
WRITESIZE = 131

memoryMap = array([0x00]*(READSIZE),dtype=uint8)

#---- Read from li/ct/plc3 the 20130626
#     first level keys:
#      - type: type of stored data
#      - read_{addr,bit,value}: memory position when memory is send to read
#      - write_{addr,bit,value}: memory position from the received memory to write
#     second level keys:
#      - updatable: this attribute has some noise
#      - std: how big is the noise of this attribute
#      - step: on each refresh loop the change to do.
#      - reference: (TODO) key whose name is readback
#      - formula: (TODO) in case is more a reference than a readback
attributes = \
{#----AS1
 'AS1_ONC':          {'read_addr': 290,
                      'read_bit': 0,
                      'read_value': True,
                      'type': PyTango.DevBoolean,
                      'write_addr': 129,
                      'write_bit': 0,
                      'write_value': True},
 'AS1H_I':           {'read_addr': 92,
                      'read_value': 0.2309,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'AS1H_I_setpoint',
                      'switch':'AS1_ONC'},
 'AS1H_I_setpoint':  {'read_addr':253,
                      'read_value': 0.2309,
                      'type': ('f', 4),
                      'write_addr': 92,
                      'write_value': 0.2299},
 'AS1H_ST':          {'read_addr': 151,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'AS1V_I':           {'read_addr': 96,
                      'read_value': 0.2199,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'AS1V_I_setpoint',
                      'switch':'AS1_ONC'},
 'AS1V_I_setpoint':  {'read_addr':257,
                      'read_value': 0.2199,
                      'type': ('f', 4),
                      'write_addr': 96,
                      'write_value': 0.2199},
 'AS1V_ST':          {'read_addr': 152,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 #----AS2
 'AS2_ONC':          {'read_addr': 290,
                      'read_bit': 2,
                      'read_value': True,
                      'type': PyTango.DevBoolean,
                      'write_addr': 129,
                      'write_bit': 2,
                      'write_value': True},
 'AS2H_I':          {'read_addr': 108,
                      'read_value': 0.2309,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'AS2H_I_setpoint',
                      'switch':'AS2_ONC'},
 'AS2H_I_setpoint':  {'read_addr':269,
                      'read_value': 0.2309,
                      'type': ('f', 4),
                      'write_addr': 108,
                      'write_value': 0.2299},
 'AS2H_ST':          {'read_addr': 155,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'AS2V_I':           {'read_addr': 112,
                      'read_value': 0.2199,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'AS2V_I_setpoint',
                      'switch':'AS2_ONC'},
 'AS2V_I_setpoint':  {'read_addr':273,
                      'read_value': 0.2199,
                      'type': ('f', 4),
                      'write_addr': 112,
                      'write_value': 0.2199},
 'AS2V_ST':          {'read_addr': 156,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 #----BC1
 'BC1_ONC':          {'read_addr': 289,
                      'read_bit': 5,
                      'read_value': True,
                      'type': PyTango.DevBoolean,
                      'write_addr': 128,
                      'write_bit': 5,
                      'write_value': True},
 'BC1F_I':           {'read_addr': 16,
                      'read_value': 149.3634,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'BC1F_I_setpoint',
                      'switch':'BC1_ONC'},
 'BC1F_I_setpoint':  {'read_addr': 177,
                      'read_value': 149.3634,
                      'type': ('f', 4),
                      'write_addr': 16,
                      'write_value': 150.0},
 'BC1F_ST':          {'read_addr': 132,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'BC1H_I':           {'read_addr': 68,
                      'read_value': -0.9652,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      #'write_addr': 68,
                      #'write_value': -0.9699,
                      'reference':'BC1H_I_setpoint',
                      'switch':'BC1_ONC'},
 'BC1H_I_setpoint':  {'read_addr': 229,
                      'read_value': -0.9652,
                      'type': ('f', 4),
                      'write_addr': 68,
                      'write_value': -0.9699},
 'BC1H_ST':          {'read_addr': 145,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'BC1V_I':           {'read_addr': 72,
                      'read_value': -0.3663,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'BC1V_I_setpoint',
                      'switch':'BC1_ONC'},
 'BC1V_I_setpoint':  {'read_addr': 233,
                      'read_value': -0.3663,
                      'type': ('f', 4),
                      'write_addr': 72,
                      'write_value': -0.3700},
 'BC1V_ST':          {'read_addr': 146,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 #----BC2
 'BC2_ONC':          {'read_addr': 289,
                      'read_bit': 6,
                      'read_value': True,
                      'type': PyTango.DevBoolean,
                      'write_addr': 128,
                      'write_bit': 6,
                      'write_value': True},
 'BC2F_I':           {'read_addr': 20,
                      'read_value': 134.1435,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'BC2F_I_setpoint',
                      'switch':'BC2_ONC'},
 'BC2F_I_setpoint':  {'read_addr': 181,
                      'read_value': 134.1435,
                      'type': ('f', 4),
                      'write_addr': 20,
                      'write_value': 135.0},
 'BC2F_ST':          {'read_addr': 133,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'BC2H_I':           {'read_addr': 76,
                      'read_value': 0.0503,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'BC2H_I_setpoint',
                      'switch':'BC2_ONC'},
 'BC2H_I_setpoint':  {'read_addr': 237,
                      'read_value': 0.0503,
                      'type': ('f', 4),
                      'write_addr': 76,
                      'write_value': 0.0500},
 'BC2H_ST':          {'read_addr': 147,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'BC2V_I':           {'read_addr': 80,
                      'read_value': 0.0196,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'BC2V_I_setpoint',
                      'switch':'BC2_ONC'},
 'BC2V_I_setpoint':  {'read_addr': 241,
                      'read_value': 0.0196,
                      'type': ('f', 4),
                      'write_addr': 80,
                      'write_value': 0.0199},
 'BC2V_ST':          {'read_addr': 148,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 #----GL
 'GL_ONC':           {'read_addr': 289,
                      'read_bit': 7,
                      'read_value': True,
                      'type': PyTango.DevBoolean,
                      'write_addr': 128,
                      'write_bit': 7,
                      'write_value': True},
 'GLF_I':            {'read_addr': 24,
                      'read_value': 0.1128,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'GLF_I_setpoint',
                      'switch':'GL_ONC'},
 'GLF_I_setpoint':   {'read_addr': 185,
                      'read_value': 0.1128,
                      'type': ('f', 4),
                      'write_addr': 24,
                      'write_value': 0.0},
 'GLF_ST':           {'read_addr': 134,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'GLH_I':            {'read_addr': 84,
                      'read_value': 0.0694,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'GLH_I_setpoint',
                      'switch':'GL_ONC'},
 'GLH_I_setpoint':   {'read_addr': 245,
                      'read_value': 0.0694,
                      'type': ('f', 4),
                      'write_addr': 84,
                      'write_value': 0.0699},
 'GLH_ST':           {'read_addr': 149,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'GLV_I':            {'read_addr': 88,
                      'read_value': 0.1990,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'GLV_I_setpoint',
                      'switch':'GL_ONC'},
 'GLV_I_setpoint':   {'read_addr': 249,
                      'read_value': 0.1991,
                      'type': ('f', 4),
                      'write_addr': 88,
                      'write_value': 0.2000},
 'GLV_ST':           {'read_addr': 150,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 #----Heartbeat and Locking
 'HeartBeat':        {'read_addr': 160,
                      'read_bit': 0,
                      'read_value': False,
                      'type': PyTango.DevBoolean},
 'Lock_ST':          {'read_addr': 159,
                      'read_value': 0,
                      'type': ('B',1)},
 'Locking':          {'read_addr': 291,
                      'read_bit': 0,
                      'read_value': False,
                      'type': PyTango.DevBoolean,
                      'write_addr': 130,
                      'write_bit': 0,
                      'write_value': False},
 'MA_Interlock_RC':  {'read_addr': 289,
                      'read_bit': 0,
                      'read_value': False,
                      'type': PyTango.DevBoolean,
                      'write_addr': 128,
                      'write_bit': 0,
                      'write_value': False},
 #----QT
 'QT_ONC':           {'read_addr': 290,
                      'read_bit': 1,
                      'read_value': True,
                      'type': PyTango.DevBoolean,
                      'write_addr': 129,
                      'write_bit': 1,
                      'write_value': True},
 'QT1F_I':           {'read_addr': 28,
                      'read_value': 2.8055,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'QT1F_I_setpoint',
                      'switch':'QT_ONC'},
 'QT1F_I_setpoint':  {'read_addr': 189,
                      'read_value': 2.8055,
                      'type': ('f', 4),
                      'write_addr': 28,
                      'write_value': 2.8300},
 'QT1F_ST':          {'read_addr': 135,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'QT1H_I':           {'read_addr':100,
                      'read_value': -0.0277,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'QT1H_I_setpoint',
                      'switch':'QT_ONC'},
 'QT1H_I_setpoint':  {'read_addr': 261,
                      'read_value': -0.0277,
                      'type': ('f', 4),
                      'write_addr': 100,
                      'write_value': 0.0},
 'QT1H_ST':          {'read_addr': 153,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'QT1V_I':           {'read_addr': 104,
                      'read_value': -0.0370,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'QT1V_I_sepoint',
                      'switch':'QT_ONC'},
 'QT1V_I_sepoint':   {'read_addr': 265,
                      'read_value': -0.0370,
                      'type': ('f', 4),
                      'write_addr': 104,
                      'write_value': 0.0},
 'QT1V_ST':          {'read_addr': 154,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'QT2F_I':           {'read_addr': 32,
                      'read_value': 3.1990,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'QT2F_I_setpoint',
                      'switch':'QT_ONC'},
 'QT2F_I_setpoint':  {'read_addr': 193,
                      'read_value': 3.1991,
                      'type': ('f', 4),
                      'write_addr': 32,
                      'write_value': 3.1950},
 'QT2F_ST':          {'read_addr': 136,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 #----SL1
 'SL1_ONC':          {'read_addr': 289,
                      'read_bit': 1,
                      'read_value': True,
                      'type': PyTango.DevBoolean,
                      'write_addr': 128,
                      'write_bit': 1,
                      'write_value': True},
 'SL1F_I':           {'read_addr': 0,
                      'read_value': 0.2502,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'SL1F_I_setpoint',
                      'switch':'SL1_ONC'},
 'SL1F_I_setpoint':  {'read_addr': 161,
                      'read_value': 0.2502,
                      'type': ('f', 4),
                      'write_addr': 0,
                      'write_value': 0.2499},
 'SL1F_ST':          {'read_addr': 128,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'SL1H_I':           {'read_addr': 36,
                      'read_value': 0.0,
                      'type': ('f', 4),
                      'updatable':True,
                      'std':0.01,
                      'reference':'SL1H_I_setpoint',
                      'switch':'SL1_ONC'},
 'SL1H_I_setpoint':  {'read_addr': 197,
                      'read_value': 0.0,
                      'type': ('f', 4),
                      'write_addr': 36,
                      'write_value': 0.0},
 'SL1H_ST':          {'read_addr': 137,
                      'read_value': 5,
                      'type': ('B', 1),
                      'updatable':False,'range':[1,5]},
 'SL1V_I':            {'read_addr': 40,
                       'read_value': 0.4467,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL1V_I_setpoint',
                       'switch':'SL1_ONC'},
 'SL1V_I_setpoint':   {'read_addr': 201,
                       'read_value': 0.4467,
                       'type': ('f', 4),
                       'write_addr': 40,
                       'write_value': 0.4499},
 'SL1V_ST':           {'read_addr': 138,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 #----SL2
 'SL2_ONC':           {'read_addr': 289,
                       'read_bit': 2,
                       'read_value': True,
                       'type': PyTango.DevBoolean,
                       'write_addr': 128,
                       'write_bit': 2,
                       'write_value': True},
 'SL2F_I':            {'read_addr': 4,
                       'read_value': 0.2809,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL2F_I_setpoint',
                       'switch':'SL2_ONC'},
 'SL2F_I_setpoint':   {'read_addr': 165,
                       'read_value': 0.2809,
                       'type': ('f', 4),
                       'write_addr': 4,
                       'write_value': 0.2800},
 'SL2F_ST':           {'read_addr': 129,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 'SL2H_I':            {'read_addr': 44,
                       'read_value': -0.0891,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL2H_I_setpoint',
                       'switch':'SL2_ONC'},
 'SL2H_I_setpoint':   {'read_addr': 205,
                       'read_value': -0.0891,
                       'type': ('f', 4),
                       'write_addr': 44,
                       'write_value': -0.0900},
 'SL2H_ST':           {'read_addr': 139,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 'SL2V_I':            {'read_addr': 48,
                       'read_value': -0.6169,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL2V_I_setpoint',
                       'switch':'SL2_ONC'},
 'SL2V_I_setpoint':   {'read_addr': 209,
                       'read_value': -0.6169,
                       'type': ('f', 4),
                       'write_addr': 48,
                       'write_value': -0.6199},
 'SL2V_ST':           {'read_addr': 140,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 #----SL3
 'SL3_ONC':           {'read_addr': 289,
                       'read_bit': 3,
                       'read_value': True,
                       'type': PyTango.DevBoolean,
                       'write_addr': 128,
                       'write_bit': 3,
                       'write_value': True},
 'SL3F_I':            {'read_addr': 8,
                       'read_value': 0.4493,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL3F_I_setpoint',
                       'switch':'SL3_ONC'},
 'SL3F_I_setpoint':   {'read_addr': 169,
                       'read_value': 0.4493,
                       'type': ('f', 4),
                       'write_addr': 8,
                       'write_value': 0.4499},
 'SL3F_ST':           {'read_addr': 130,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 'SL3H_I':            {'read_addr': 52,
                       'read_value': 0.6689,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL3H_I_setpoint',
                       'switch':'SL3_ONC'},
 'SL3H_I_setpoint':   {'read_addr': 213,
                       'read_value': 0.6689,
                       'type': ('f', 4),
                       'write_addr': 52,
                       'write_value': 0.6700},
 'SL3H_ST':           {'read_addr': 141,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 'SL3V_I':            {'read_addr': 56,
                       'read_value': 0.6070,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL3V_I_setpoint',
                       'switch':'SL3_ONC'},
 'SL3V_I_setpoint':   {'read_addr': 217,
                       'read_value': 0.6070,
                       'type': ('f', 4),
                       'write_addr': 56,
                       'write_value': 0.6100},
 'SL3V_ST':           {'read_addr': 142,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 #----SL4
 'SL4_ONC':           {'read_addr': 289,
                       'read_bit': 4,
                       'read_value': True,
                       'type': PyTango.DevBoolean,
                       'write_addr': 128,
                       'write_bit': 4,
                       'write_value': True},
 'SL4F_I':            {'read_addr': 12,
                       'read_value': 0.4305,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL4F_I_setpoint',
                       'switch':'SL4_ONC'},
 'SL4F_I_setpoint':   {'read_addr': 173,
                       'read_value': 0.4305,
                       'type': ('f', 4),
                       'write_addr': 12,
                       'write_value': 0.4300},
 'SL4F_ST':           {'read_addr': 131,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 'SL4H_I':            {'read_addr': 60,
                       'read_value': -0.1093,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL4H_I_setpoint',
                       'switch':'SL4_ONC'},
 'SL4H_I_setpoint':   {'read_addr': 221,
                       'read_value': -0.1093,
                       'type': ('f', 4),
                       'write_addr': 60,
                       'write_value': -0.1099},
 'SL4H_ST':           {'read_addr': 143,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
 'SL4V_I':            {'read_addr': 64,
                       'read_value': -0.2488,
                       'type': ('f', 4),
                       'updatable':True,
                       'std':0.01,
                       'reference':'SL4V_I_setpoint',
                       'switch':'SL4_ONC'},
 'SL4V_I_setpoint':   {'read_addr': 225,
                       'read_value': -0.2488,
                       'type': ('f', 4),
                       'write_addr': 64,
                       'write_value': -0.2500},
 'SL4V_ST':           {'read_addr': 144,
                       'read_value': 5,
                       'type': ('B', 1),
                       'updatable':False,'range':[1,5]},
}
