#! /usr/bin/python

import sys
import nes
from helpers import NesMappers as m

if len(sys.argv) < 2:
    print "Usage: python start.py <rom filename>"
    sys.exit(0)

a = nes.NesRom(sys.argv[1])

a.readRom()

print "Rom has %d program data banks" % a.numPRGBanks
print "Rom has %d character banks" % a.numCHRBanks
print "Rom uses mirroring value %s" % a.mirroringValue
print "Rom uses mapper %s (%s)." % (a.mapper, m.NesMappers.mapperToString(a.mapper))
print "Rom uses extended mapper %s" % a.extendedMapper
print "Rom has %d 8KB memory bank(s)" % a.numROMBanks
print "It is %r that this rom is NTSC" % a.isNTSC

if a.isThisFormat:
    print "Layout of the header looks fine."
else:
    print "Something is wrong with the header."

print "\n"
print "Title data (if any): %s" % a.titleData

print "\nReleasing rom\n"
a.release()



