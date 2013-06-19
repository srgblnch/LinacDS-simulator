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

'''This code has been made to simulate the behaviour of the Siemens S7 plcs
   placed by Thales for the Linac control at ALBA.
'''

import socket
import select
import threading
import signal
import time,sys
#memory maps
import plc1,plc2,plc3,plck

plcs = []
plcports = [2011,2012,2013,2014,2015]

def getMemoryMap(plc_number):
    if plc_number == 1:
        return plc1.memoryMap
    elif plc_number == 2:
        return plc2.memoryMap
    elif plc_number == 3:
        return plc3.memoryMap
    elif plc_number in [4,5]:
        return plck.memoryMap
    return None

class PLC:
    #----TODO: implement the memory map to simulate the PLCs of the linac
    def __init__(self,port,memoryMap):
        self.__hostName = socket.gethostname()
        #self.__host = ''#means available for all interfaces
        #self.__host = '127.0.0.1'#means only loopback interface
        self.__host = '0.0.0.0'
        self.__port = port
        self.__memoryMap = memoryMap
        self.__socket = None
        self.__thread = None
        self.__joinerEvent = threading.Event()#to communicate between threads
        self.__joinerEvent.clear()
        print("(%d) PLC object build."%(self.__port))
    def listen(self):
        if hasattr(self,'__thread') and self.__thread and self.__thread.isAlive():
            return
        self.__thread = threading.Thread(target=self.listener)
        self.__thread.setDaemon(True)
        self.__thread.start()
        print("(%d) PLC thread created."%(self.__port))
    def listener(self):
        self.buildSocket()
        connection = self.listenAndAccept()
        while not self.joinEventIsSet():
            try:
                ready = select.select( [connection.fileno()], E,E, 0)
                if ready[0]:
                    recv = connection.recv(256)
                    if len(recv) != 0:
                        print("(%d) received '%s'"%(self.__port,recv))
                connection.send(self.__memoryMap.tostring())
                #print("(%d) send the memory map"%(self.__port))
                time.sleep(0.5)#FIXME: heartbeat emit
            except Exception,e:
                print("(%d) Exiting the loop due to Exception: %s"%(self.__port,e))
                try: connection.close()
                except: pass
                self.buildSocket()
                connection = self.listenAndAccept()
        connection.close()
    def buildSocket(self):
        #create the tcp socket
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.__socket.setblocking(0)
        #bind socket and port
        self.__socket.bind((self.__host,self.__port))
    def listenAndAccept(self):
        backlog = 1#only wait for one connection.
        #listen for connections
        self.__socket.listen(backlog)
        print("(%d) PLC listener prepared."%(self.__port))
        connection,address = self.__socket.accept()
        print("(%d) PLC connection accepted (descriptor %d)."%(self.__port,connection.fileno()))
        return connection
    def joinEventIsSet(self):
        return self.__joinerEvent.isSet()
    def setJoinEvent(self):
        self.__joinerEvent.set()
        print("(%d) join event set"%(self.__port))

def signal_handler(signum, frame=None):
    print("SIGINT received")
    global plcs
    for plc in plcs:
        plc.setJoinEvent()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    try:
        for port in plcports:
            plc = PLC(port,getMemoryMap(port-2010))
            plcs.append(plc)
            plc.listen()
        joined = 0
        while not joined==len(plcports):
            joined = 0
            for plc in plcs:
                if plc.joinEventIsSet(): joined+=1
            time.sleep(10)
        sys.exit(-1)
    except KeyboardInterrupt:
        print("Keyboard interruption")
    