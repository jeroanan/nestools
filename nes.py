from PIL import Image, ImageDraw
from Tkinter import Tk, Canvas, PhotoImage
import os
import numpy as np
import scipy.misc.pilutil as smp

class NesRom:
    
    _headerLength = 16
    
    _headerField1Start = 0
    _headerField1Bytes = 4
    _headerField1Expected = "NES\x1a"
    
    _headerField2Start = 4
    _headerField2Bytes = 1

    _headerField3Start = 5
    _headerField3Bytes = 1

    isThisFormat = 0
    numPRGBanks = 0
    numCHRBanks = 0

    _prgLength = 0
    _chrLength = 0

    fileName = ""

    def __init__(self, fileName):
        self.fileName = fileName

    def readRom(self):
        rom = open(self.fileName, "rb")

        try:
            rom.seek(0)        
            field1 = rom.read(self._headerField1Bytes)
        
            if field1 == self._headerField1Expected:
                self.isThisFormat = 1
            
                rom.seek(self._headerField2Start)
                field2 = rom.read(self._headerField2Bytes)
            
                self.numPRGBanks = ord(field2)
                self._prgLength = self.numPRGBanks * 16384
            
                rom.seek(self._headerField3Start)
                field3 = rom.read(self._headerField3Bytes)
                self.numCHRBanks = ord(field3)
                self._chrLength = self.numCHRBanks * 8192
            
            else:
                self.isThisFormat = 0
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
        
        chrStart = self._prgLength + 16
        rom.seek(chrStart)

        while rom.tell() < (16 + self._prgLength + self._chrLength):
            sprite = rom.read(16)
            
            rowCounter = 0
            
            data = np.zeros((spriteWidth,spriteHeight,3), dtype=np.uint8 )

            while rowCounter < 16:
                
                channelA = bin(ord(sprite[rowCounter]))[2:].zfill(8)
                channelB = bin(ord(sprite[rowCounter+1]))[2:].zfill(8)

                colCounter = 0

                while colCounter <= 7:
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
    
                    colCounter += 1
                    
                rowCounter += 2

                



