import os
import numpy as np
import scipy.misc.pilutil as smp

class NesRom:
    
    _headerLength = 16
    
    _prgLength = 0
    _chrLength = 0

    isThisFormat = True
    numPRGBanks = 0
    numCHRBanks = 0
    mirroringValue = 0
    mapper = 0
    extendedMapper = 0
    numROMBanks = 0
    isNTSC = True

    fileName = ""

    

    def __init__(self, fileName):
        self.fileName = fileName

    def readRom(self):
        """Reads in the rom and sets object state depending on header info"""

        # The first 16 bytes in the file is header info:
        #  Field 1: 4 bytes: NES^Z
        #  Field 2: 1 byte: Number of 16KB pages of program code
        #  Field 3: 1 byte: Number of 8KB pages of characters (sprites)
        #  Field 4: 1 byte: First hex digit: mirroring value. Second hex digit: mapper
        #  Field 5: 1 byte: First hex digit only: extended mapper (I think)
        #  Field 6: 1 byte: Number of 8KB rom banks. If 0 then it's really 1.
        #  Field 7: 1 byte: First bit: 1 for a PAL cartridge else NTSC. Other bits: zero
        #  The rest of the fields: TODO
        fieldLengths = [4, 1, 1, 1, 1, 1, 1, 6]
        headerField1Expected = "NES\x1a"

        prgPageLength = 16384
        chrPageLength = 8192

        rom = open(self.fileName, "rb")

        try:
            field1 = rom.read(fieldLengths[0])
        
            if field1 == headerField1Expected:
                self.isThisFormat = True
            
                self.numPRGBanks = ord(rom.read(fieldLengths[1]))
                self._prgLength = self.numPRGBanks * prgPageLength
            
                self.numCHRBanks = ord(rom.read(fieldLengths[2]))
                self._chrLength = self.numCHRBanks * chrPageLength
            
                field4 = str(ord(rom.read(fieldLengths[3])))
                self.mirroring = field4[0]
                self.mapper = field4[1]

                extendedMapper = str(ord(rom.read(fieldLengths[4])))

                field6 = ord(rom.read(fieldLengths[5]))
                self.numROMBanks = 1 if field6 == 0 else field6

                self.isNTSC = ord(rom.read(fieldLengths[6])) == 0
                
                field8 = rom.read(fieldLengths[7])
                
                counter = 0
                while counter<fieldLengths[7]:
                    print ord(field8[counter])
                    counter += 1

            else:
                self.isThisFormat = False
        finally:
            rom.close()



    def getSprites(self):
        rom = open(self.fileName, "rb")

        black = [0,0,0]
        red = [255,0,0]
        green = [0,255,0]
        blue = [0,0,255]

        spriteHeight = 8
        spriteWidth = 8
        
        chrStart = self._prgLength + self._headerLength
        rom.seek(chrStart)

        while rom.tell() < (self._headerLength + self._prgLength + self._chrLength):
            sprite = rom.read(16)
                       
            data = np.zeros((spriteWidth,spriteHeight,3), dtype=np.uint8 )

            rowCounter = 0
            while rowCounter < 16:
                
                channelA = bin(ord(sprite[rowCounter]))[2:].zfill(8)
                channelB = bin(ord(sprite[rowCounter+1]))[2:].zfill(8)

                colCounter = 7

                while colCounter >= 0:
                    colourNum = int(channelB[colCounter])*2 + int(channelA[colCounter])
                    
                    colourOut = black

                    if colourNum == 1:
                        colourOut = red
                    if colourNum == 2:
                        colourOut = blue
                    if colourNum == 3:
                        colourOut = green
                    
                    data[colCounter,rowCounter/2] = colourOut
                    img = smp.toimage(data)
                    img.save("output/image%d.bmp" % rom.tell())
    
                    colCounter -= 1
                    
                rowCounter += 2

                



