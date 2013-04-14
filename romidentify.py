#! /usr/bin/python

import nes

a = nes.NesRom("NinWrldC.nes")
a.readRom()

print "Rom has %d program data banks" % a.numPRGBanks
print "Rom has %d character banks" % a.numCHRBanks
print "Rom uses mirroring value %d" % a.mirroring
print "Rom uses mapper %d" % a.mapper

#a.getSprites()

