import os
import struct

import rom.Rom

class Nes:

    _rom = ""

    def PowerOn(self):
        """System boot"""
        if len(sys.argv) < 2:
            print "Usage: python start.py <rom filename>"
            sys.exit(0)

        self._rom = Rom.Rom(sys.argv[1])

        a.ReadRom()
    
