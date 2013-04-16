import os
import numpy as np
import scipy.misc.pilutil as smp
import struct

class NesRom:
    
    #constants
    HEADER_LENGTH = 16    
    PRG_PAGE_LENGTH = 16384
    CHR_PAGE_LENGTH = 8192
    TITLE_DATA_LENGTH = 128

    __prgLength = 0
    __chrLength = 0

    isThisFormat = True
    numPRGBanks = 0
    numCHRBanks = 0
    mirroringValue = 0
    mapper = 0
    extendedMapper = 0
    numROMBanks = 0
    isNTSC = True
    titleData = ""

    fileName = ""

    def __init__(self, fileName):
        self.fileName = fileName
        self.__getFileContent()

    def __getFileContent(self):
        """Read file data into a var for later use."""
        rom = open(self.fileName, "rb")

        try:            
            self.__fileData = rom.read()
        finally:
            rom.close()

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
        #  Field 8: 6 bytes: All zeroes.
        fieldOffsets = [0, 4, 5, 6, 7, 8, 9, 10]
        headerField1Expected = ord("N"), ord("E"), ord("S"), ord("\x1a")       
                
        if struct.unpack("BBBB", self.__fileData[fieldOffsets[0]:fieldOffsets[1]]) == headerField1Expected:        
            self.isThisFormat = True
            
            self.numPRGBanks = ord(self.__fileData[fieldOffsets[1]:fieldOffsets[2]])
            self.__prgLength = self.numPRGBanks * self.PRG_PAGE_LENGTH
                
            self.numCHRBanks = ord(self.__fileData[fieldOffsets[2]:fieldOffsets[3]])
            self.__chrLength = self.numCHRBanks * self.CHR_PAGE_LENGTH
            
            field4 = str(ord(self.__fileData[fieldOffsets[3]:fieldOffsets[4]]))
            self.mirroring = field4[0]
            self.mapper = field4[1]
            
            extendedMapper = str(ord(self.__fileData[fieldOffsets[4]:fieldOffsets[5]]))
            
            field6 = ord(self.__fileData[fieldOffsets[5]:fieldOffsets[6]])
            self.numROMBanks = 1 if field6 == 0 else field6
            
            self.isNTSC = ord(self.__fileData[fieldOffsets[6]:fieldOffsets[7]]) == 0
            
            field8 = self.__fileData[fieldOffsets[7]:fieldOffsets[7]+6]
            
            counter = 0
            while counter < 6:
                if ord(field8[counter]) != 0:
                    self.isThisFormat = False
                counter += 1

            # Check for title data
            otherStuff = self.HEADER_LENGTH + self.__prgLength + self.__chrLength
            
            if len(self.__fileData)-otherStuff == self.TITLE_DATA_LENGTH:
                titleData = self.__fileData[otherStuff:]
                
                counter = 0
                while ord(titleData[counter]) != 0:
                    self.titleData += titleData[counter]
                    counter += 1
        else:
            self.isThisFormat = False


    def getSprites(self):
        """This really isn't so good. Will come back to it later."""
        rom = open(self.fileName, "rb")

        black = [0,0,0]
        red = [255,0,0]
        green = [0,255,0]
        blue = [0,0,255]

        spriteHeight = 8
        spriteWidth = 8
        
        chrStart = self.__prgLength + self.HEADER_LENGTH
        rom.seek(chrStart)

        while rom.tell() < (self.HEADER_LENGTH + self.__prgLength + self.__chrLength):
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

                



