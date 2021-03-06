import os
import struct
from array import array

class Rom:
   
    #constants
    HEADER_LENGTH = 16    
    PRG_PAGE_LENGTH = 16384
    CHR_PAGE_LENGTH = 8192
    TITLE_DATA_LENGTH = 128

    RomData = array('B')

    _prgLength = 0
    _chrLength = 0
    _fileName = ""
    _fileData = ""
    _isThisFormat = True
    _numPRGBanks = 0
    _numCHRBanks = 0
    _mirroringValue = 0
    _mapper = 0
    _extendedMapper = 0
    _numROMBanks = 0
    _isNTSC = True
    _titleData = ""    

    def __init__(self, fileName):
        """Initialise the object. This will cause the given rom 
        to be read into memory."""        
        try:
            self._fileName = fileName
            rom = open(fileName, "rb")
            self._fileData = rom.read()            
            self.readRom()
            del self._fileData 
            self.LoadRomIntoMemory(rom)
        finally:
            rom.close()

    @property
    def isThisFormat(self):
        """True if on file load I have determined this to
        be a NES rom based on its file header"""
        return self._isThisFormat

    @property
    def numPRGBanks(self):
        """Number of 16KB Program Data banks"""
        return self._numPRGBanks
    
    @property
    def numCHRBanks(self):
        """Number of 8KB Character Data banks"""
        return self._numCHRBanks

    @property
    def mirroringValue(self):
        """The type of mirroring used"""
        return self._mirroringValue

    @property
    def mapper(self):
        """The mapper used"""
        return self._mapper

    @property
    def extendedMapper(self):        
        return self._extendedMapper

    @property
    def numROMBanks(self):
        """Number of additional 8KB rom banks"""
        return self._numROMBanks

    @property
    def isNTSC(self):
        """If true this is an NTSC rom. If not it's PAL."""
        return self._isNTSC

    @property
    def titleData(self):
        """Title metadata from the file footer"""
        return self._titleData

    def readRom(self):
        """Sets the object state dpeending on what's found in file header/footer"""
        # The first 16 bytes in the file is header info:
        #  Field 1: 4 bytes: NES^Z
        #  Field 2: 1 byte: Number of 16KB pages of program code
        #  Field 3: 1 byte: Number of 8KB pages of characters (sprites)
        #  Field 4: 1 byte: First hex digit: mirroring value. Second hex digit: mapper
        #  Field 5: 1 byte: First hex digit only: extended mapper (I think)
        #  Field 6: 1 byte: Number of 8KB rom banks. If 0 then it's really 1.
        #  Field 7: 1 byte: First bit: 1 for a PAL cartridge else NTSC. Other bits: zero
        #  Field 8: 6 bytes: All zeroes.
        #  ... program and sprite data ...
        #  Final 128 bytes: title data if present
        fieldOffsets = [0, 4, 5, 6, 7, 8, 9, 10]
        headerField1Expected = ord("N"), ord("E"), ord("S"), ord("\x1a")       
            
        # unpack first four bytes as chars to make sure the rom starts "NES^Z". 
        # If it does then I say that this is a valid rom format file and 
        # continue processing.
        if struct.unpack("BBBB", self._fileData[fieldOffsets[0]:fieldOffsets[1]]) == headerField1Expected:        
            self._isThisFormat = True
            
            # _prgLength and _chrLength represent bytes.
            self._numPRGBanks = ord(self._fileData[fieldOffsets[1]:fieldOffsets[2]])
            self._prgLength = self._numPRGBanks * self.PRG_PAGE_LENGTH
                
            self._numCHRBanks = ord(self._fileData[fieldOffsets[2]:fieldOffsets[3]])
            self._chrLength = self._numCHRBanks * self.CHR_PAGE_LENGTH
            
            field4 = str(ord(self._fileData[fieldOffsets[3]:fieldOffsets[4]]))
            self._mirroringValue = field4[0]
            self._mapper = field4[1]
            
            _extendedMapper = str(ord(self._fileData[fieldOffsets[4]:fieldOffsets[5]]))
            
            field6 = ord(self._fileData[fieldOffsets[5]:fieldOffsets[6]])
            self._numROMBanks = 1 if field6 == 0 else field6
            
            self._isNTSC = ord(self._fileData[fieldOffsets[6]:fieldOffsets[7]]) == 0
            
            field8 = self._fileData[fieldOffsets[7]:fieldOffsets[7]+6]
            
            counter = 0
            while counter < 6:
                if ord(field8[counter]) != 0:
                    self._isThisFormat = False
                counter += 1

            # Check for title data
            otherStuff = self.HEADER_LENGTH + self._prgLength + self._chrLength
            
            if len(self._fileData) - otherStuff == self.TITLE_DATA_LENGTH:
                _titleData = self._fileData[otherStuff:]
            
                # The title data is padded with ASCII 0s so we know where it ends.
                counter = 0
                while ord(_titleData[counter]) != 0:
                    self._titleData += _titleData[counter]
                    counter += 1
        else:
            self._isThisFormat = False

    def LoadRomIntoMemory(self, rom):
        rom.seek(16)
        self.RomData.fromfile(rom, self._prgLength)
