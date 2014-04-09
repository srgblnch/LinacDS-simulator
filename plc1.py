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

READSIZE = 165
WRITESIZE = 81

memoryMap = array([0x00]*(READSIZE),dtype=uint8)

#---- Read from li/ct/plc1 the 20130626 and modified
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
{'GUN_Filament_V': {'type': ('f', 4),   'read_addr':  0,    'read_value':  0.0,
                    'updatable':True,'std':0.1},
 'GUN_Filament_I': {'type': ('f', 4),   'read_addr':  4,    'read_value': 0.0,
                    'updatable':True,'std':0.1},
 'GUN_Kathode_V':  {'type': ('f', 4),   'read_addr':  8,    'read_value': 0.0,
                    'updatable':True,'std':0.1},
 'GUN_Kathode_T':  {'type': ('f', 4),   'read_addr': 12,    'read_value': 25.0,
                    'updatable':True,'std':0.1,},
#free floats 16,20,24,28
 'GUN_HV_V':       {'type': ('f', 4),   'read_addr': 32,    'read_value': 0.0,
                    'updatable':True,'std':0.1,},
 'GUN_HV_I':       {'type': ('f', 4),   'read_addr': 36,    'read_value': 0.0,
                    'updatable':True,'std':0.1,},
 'PHS1_Phase':     {'type': ('f', 4),   'read_addr': 40,    'read_value': 152.87,
                    'updatable':True,'std':0.1,},
#free float 44
 'SF6_P1':         {'type': ('f', 4),   'read_addr': 48,    'read_value': 2.96,
                    'updatable':True,'std':0.1,},
 'SF6_P2':         {'type': ('f', 4),   'read_addr': 52,    'read_value': 2.80,
                    'updatable':True,'std':0.1,},
 'PHS2_Phase':     {'type': ('f', 4),   'read_addr': 56,    'read_value': 92.52,
                    'updatable':True,'std':0.1,},
 'ATT2_P':         {'type': ('f', 4),   'read_addr': 60,    'read_value':  -3.92,
                    'updatable':True,'std':0.1},
#free float 64
 'TB_ST':          {'type': PyTango.DevBoolean,
                    'read_addr': 68,'read_bit': 0,'read_value': False,
                    'updatable':True,'probability':0.1},
 'A0_ST':          {'type': PyTango.DevBoolean,
                    'read_addr': 68,'read_bit': 4,'read_value': True,
                    'updatable':True,'probability':0.1},
 'RFS_ST':         {'type': PyTango.DevBoolean,
                    'read_addr': 68,'read_bit': 5,'read_value': True,
                    'updatable':True,'probability':0.1},
#free byte 69
 'EG_ENB':         {'type': PyTango.DevBoolean,
                    'read_addr': 70,'read_bit': 0,'read_value': True,
                    'updatable':True,'probability':0.1},
 'KA_ENB':         {'type': PyTango.DevBoolean,
                    'read_addr': 70,'read_bit': 1,'read_value': True,
                    'updatable':True,'probability':0.1},
 'TL_VOK':         {'type': PyTango.DevBoolean,
                    'read_addr': 70,'read_bit': 2,'read_value': True,
                    'updatable':True,'probability':0.1},
 'IU_RDY':         {'type': PyTango.DevBoolean,
                    'read_addr': 70,'read_bit': 5,'read_value': True,
                    'updatable':True,'probability':0.1},
 'W1_UF':          {'type': PyTango.DevBoolean,
                    'read_addr': 70,'read_bit': 6,'read_value': True,
                    'updatable':True,'probability':0.1},
 'W2_UF':          {'type': PyTango.DevBoolean,
                    'read_addr': 70,'read_bit': 7,'read_value': True,
                    'updatable':True,'probability':0.1},
 'W3_UF':          {'type': PyTango.DevBoolean,
                    'read_addr': 71,'read_bit': 0,'read_value': True,
                    'updatable':True,'probability':0.1},
 'RL1_UF':         {'type': PyTango.DevBoolean,
                    'read_addr': 71,'read_bit': 1,'read_value': True,
                    'updatable':True,'probability':0.1},
 'RL2_UF':         {'type': PyTango.DevBoolean,
                    'read_addr': 71,'read_bit': 2,'read_value': True,
                    'updatable':True,'probability':0.1},
 'RL3_UF':         {'type': PyTango.DevBoolean,
                    'read_addr': 71,'read_bit': 3,'read_value': True,
                    'updatable':True,'probability':0.1},
 'UT_IS':          {'type': PyTango.DevBoolean,
                    'read_addr': 71,'read_bit': 4,'read_value': True,
                    'updatable':True,'probability':0.1},
 'MG_IS':          {'type': PyTango.DevBoolean,
                    'read_addr': 71,'read_bit': 5,'read_value': True,
                    'updatable':True,'probability':0.1},
 'GM_DI':          {'type': PyTango.DevBoolean,
                    'read_addr': 71,'read_bit': 6,'read_value': True,
                    'updatable':True,'probability':0.1},
 'LI_VOK':         {'type': PyTango.DevBoolean,
                    'read_addr': 71,'read_bit': 7,'read_value': True,
                    'updatable':True,'probability':0.1},
 'HeartBeat':      {'type': PyTango.DevBoolean,
                    'read_addr': 72,'read_bit': 0,'read_value': False},
 'PLC1_PR':        {'type': PyTango.DevBoolean,
                    'read_addr': 72,'read_bit': 2,'read_value': True,
                    'updatable':True,'probability':0.1},
 'PLC!_Ps':        {'type': PyTango.DevBoolean,
                    'read_addr': 72,'read_bit': 4,'read_value': True,
                    'updatable':True,'probability':0.1},
 'SF6_P1_ST':      {'type': PyTango.DevBoolean,
                    'read_addr': 73,'read_bit': 0,'read_value': True,
                    'updatable':True,'probability':0.1,},
 'SF6_P2_ST':      {'type': PyTango.DevBoolean,
                    'read_addr': 73,'read_bit': 1,'read_value': True,
                    'updatable':True,'probability':0.1},
 'KA1_OK':         {'type': PyTango.DevBoolean,
                    'read_addr': 73,'read_bit': 2,'read_value': True,
                    'updatable':True,'probability':0.1},
 'KA2_OK':         {'type': PyTango.DevBoolean,
                    'read_addr': 73,'read_bit': 3,'read_value': True,
                    'updatable':True,'probability':0.1},
 'LI_OK':          {'type': PyTango.DevBoolean,
                    'read_addr': 73,'read_bit': 4,'read_value': True,
                    'updatable':True,'probability':0.1},
 'RF_OK':          {'type': PyTango.DevBoolean,
                    'read_addr': 73,'read_bit': 5,'read_value': True,
                    'updatable':True,'probability':0.1},
 'Gun_HV_ST':      {'type': ('B', 1),   'read_addr': 74,'read_value': 4,
                    'updatable':True,'range':5},
 'Gun_ST':         {'type': ('B', 1),   'read_addr': 75,'read_value': 8,
                    'updatable':True,'range':8},
 'SCM1_ST':        {'type': ('B', 1),   'read_addr': 76,'read_value': 2,
                    'updatable':True,'range':4},
 'SCM2_ST':        {'type': ('B', 1),   'read_addr': 77,'read_value': 2,
                    'updatable':True,'range':4},
 'SCM3_ST':        {'type': ('B', 1),   'read_addr': 78,'read_value': 2,
                    'updatable':True,'range':4},
 'PHS1_ST':        {'type': ('B', 1),   'read_addr': 79,'read_value': 2,
                    'updatable':True,'range':5},
 'PHS2_ST':        {'type': ('B', 1),   'read_addr': 80,'read_value': 2,
                    'updatable':True,'range':5},
 'ATT2_ST':        {'type': ('B', 1),   'read_addr': 81,'read_value': 2,
                    'updatable':True,'range':5},
 'Lock_ST':        {'type': ('B', 1),   'read_addr': 82,'read_value': 0},
#unknown 83
 'GUN_Filament_V_setpoint': {'type': ('f', 4),
                             'read_addr':  84,   'read_value':  0.0,
                             'write_addr':  0,   'write_value': 0.0},
 'GUN_cathode_V_setpoint': {'type': ('f', 4),
                            'read_addr':  88,   'read_value':  0.0,
                            'write_addr':  4,   'write_value': 0.0},
 'GUN_HV_V_setpoint': {'type': ('f', 4),'read_addr': 100,   'read_value':  0.0,
                                        'write_addr': 16,   'write_value': 0.0},
 'TB_GPA':         {'type': ('f', 4),   'read_addr': 104,   'read_value':  0.0,
                                        'write_addr': 20,   'write_value': 0.0},
 'PHS1_Phase_setpoint':{'type': ('f', 4),'read_addr': 108,   'read_value':  0.0,
                                        'write_addr': 24,   'write_value': 0.0},
 'A0_OP':          {'type': ('f', 4),   'read_addr': 112,   'read_value':  475.0,
                                        'write_addr': 28,   'write_value': 475.0},
 'TPS0_Phase':     {'type': ('f', 4),   'read_addr': 116,   'read_value': 192.0,
                                        'write_addr': 32,   'write_value': 192.0},
 'TPS1_Phase':     {'type': ('f', 4),   'read_addr': 120,   'read_value': 112.0,
                                        'write_addr': 36,   'write_value': 112.0},
 'TPS2_Phase':     {'type': ('f', 4),   'read_addr': 124,   'read_value': 151.0,
                                        'write_addr': 40,   'write_value': 151.0},
 'TPSX_Phase':     {'type': ('f', 4),   'read_addr': 128,   'read_value': 145.0,
                                        'write_addr': 44,   'write_value': 145.0},
#free 132,136 floats
 'PHS2_Phase_setpoint':{'type': ('f', 4),'read_addr':140,   'read_value':  0.0,
                                        'write_addr': 56,   'write_value': 0.0},
 'ATTP_P_setpoint':{'type': ('f', 4),   'read_addr': 144,   'read_value': 0.0,
                                        'write_addr': 60,   'write_value': 0.0},
 'TB_KA1_Delay':   {'type': ('h', 2),   'read_addr': 148,   'read_value': 49,
                                        'write_addr': 64,   'write_value': 49},
 'TB_KA2_Delay':   {'type': ('h', 2),   'read_addr': 150,   'read_value': 2720,
                                        'write_addr': 66,   'write_value': 2720},
 'TB_RF2_Delay':   {'type': ('h', 2),   'read_addr': 152,   'read_value': 1920,
                                        'write_addr': 68,   'write_value': 1920},
 'TB_Gun_Delay':   {'type': ('h', 2),   'read_addr': 154,   'read_value': 3168,
                                        'write_addr': 70,   'write_value': 3168},
 'TB_GPI':         {'type': ('h', 2),   'read_addr': 156,   'read_value': 64,
                                        'write_addr': 72,   'write_value': 64},
 'TB_GPN':         {'type': ('h', 2),   'read_addr': 158,   'read_value': 8,
                                        'write_addr': 74,   'write_value': 8},
 'TB_GPM':         {'type': ('h', 2),   'read_addr': 160,   'read_value': 2,
                                        'write_addr': 76,   'write_value': 2},
 'TB_MBM':         {'type': PyTango.DevBoolean,
                    'read_addr': 162,'read_bit': 0,'read_value': True,
                    'write_addr': 78,'write_bit': 0,'write_value': True},
 'GUN_HV_ONC':     {'type': PyTango.DevBoolean,
                    'read_addr': 162,'read_bit': 2,'read_value': False,
                    'write_addr': 78,'write_bit': 2,'write_value': False},
 'Interlock_RC':   {'type': PyTango.DevBoolean,
                    'read_addr': 162,'read_bit': 3,'read_value': False,
                    'write_addr': 78,'write_bit': 3,'write_value': False},
 'GUN_LV_ONC':     {'type': PyTango.DevBoolean,
                    'read_addr': 162,'read_bit': 5,'read_value': False,
                    'write_addr': 78,'write_bit': 5,'write_value': False},
 'SCM1_DC':        {'type': PyTango.DevBoolean,
                    'read_addr': 163,'read_bit': 0,'read_value': False,
                    'write_addr': 79,'write_bit': 0,'write_value': False},
 'SCM2_DC':        {'type': PyTango.DevBoolean,
                    'read_addr': 163,'read_bit': 1,'read_value': False,
                    'write_addr': 79,'write_bit': 1,'write_value': False},
 'SCM3_DC':        {'type': PyTango.DevBoolean,
                    'read_addr': 163,'read_bit': 2,'read_value': False,
                    'write_addr': 79,'write_bit': 2,'write_value': False},
 'SCM1_LC':        {'type': PyTango.DevBoolean,
                    'read_addr': 163,'read_bit': 3,'read_value': False,
                    'write_addr': 79,'write_bit': 3,'write_value': False},
 'SCM2_LC':        {'type': PyTango.DevBoolean,
                    'read_addr': 163,'read_bit': 4,'read_value': False,
                    'write_addr': 79,'write_bit': 4,'write_value': False},
 'SCM3_LC':        {'type': PyTango.DevBoolean,
                    'read_addr': 163,'read_bit': 5,'read_value': False,
                    'write_addr': 79,'write_bit': 5,'write_value': False},
 'Locking':        {'type': PyTango.DevBoolean,
                    'read_addr': 164,'read_bit': 0,'read_value': False,
                    'write_addr': 80,'write_bit': 0,'write_value': False},
}
