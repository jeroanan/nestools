import os
import struct
import sys

from rom import Rom
from chip import NesCpu

class Nes(object):
"""Class to represent the NES console"""
    _rom = ""
    _cpu = ""

    def PowerOn(self):
        """System boot"""
        if len(sys.argv) < 2:
            print "Usage: python nes.py <rom filename>"
            sys.exit(0)

        self._rom = Rom.Rom(sys.argv[1])
        
        self._cpu = NesCpu.NesCpu()
        self._cpu.pc = 0x8000
        self.cpu.mem = [0xff] * (0x800)

        print self._rom.RomData[self._cpu.pc]
        
        
        
nes = Nes()
nes.PowerOn()
