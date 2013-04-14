#! /usr/bin/python

import sys
import nes

if len(sys.argv)<2:
    print "Usage: python start.py <rom filename>"
    sys.exit(0)

a = nes.NesRom(sys.argv[1])
a.readRom()

print "Rom has %d program data banks" % a.numPRGBanks
print "Rom has %d character banks" % a.numCHRBanks
print "Rom uses mirroring value %s" % a.mirroring
print "Rom uses mapper %s" % a.mapper
print "Rom uses extended mapper %s" % a.extendedMapper
print "Rom has %d 8KB memory bank(s)" % a.numROMBanks
print "It is %r that this rom is NTSC" % a.isNTSC

if a.isThisFormat:
    print "Layout of the header looks fine."
else:
    print "Something is wrong with the header."

