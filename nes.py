import os
import struct
import sys

from rom import Rom
from chip import NesCpu

class Nes:

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

        print self._rom.RomData[self._cpu.pc]
        
        
        
nes = Nes()
nes.PowerOn()
