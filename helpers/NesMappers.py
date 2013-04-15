class NesMappers:

    @staticmethod
    def mapperToString(mapperNumber):
        """Takes a number in and gives a textual description of the mapper concerned"""
        
        mapperDesc = "None";

        if mapperNumber==1: 
            mapperDesc="Nintendo MMC1"
        if mapperNumber==2: 
            mapperDesc="CNROM switch"
        if mapperNumber== 3: 
            mapperDesc="UNROM switch"
        if mapperNumber==4: 
            mapperDesc="Nintendo MMC3"
        if mapperNumber==5: 
            mapperDesc="Nintendo MMC5"
        if mapperNumber==6: 
            mapperDesc="FFE F4xxx"
        if mapperNumber==7: 
            mapperDesc="AOROM switch"
        if mapperNumber==8: 
            mapperDesc="FFE F3xxx"
        if mapperNumber==9: 
            mapperDesc="Nintendo MMC2"
        if mapperNumber==10: 
            mapperDesc="Nintendo MMC4"
        if mapperNumber==11: 
            mapperDesc="ColorDreams chip"
        if mapperNumber==12: 
            mapperDesc="- FFE F6xxx"
        if mapperNumber==13: 
            mapperDesc="CPROM switch"
        if mapperNumber==15: 
            mapperDesc="100-in-1 switch"
        if mapperNumber==16: 
            mapperDesc="Bandai chip"
        if mapperNumber==17: 
            mapperDesc="FFE F8xxx"
        if mapperNumber==18: 
            mapperDesc="Jaleco SS8806 chip"
        if mapperNumber==19: 
            mapperDesc="Namcot 106 chip"
        if mapperNumber==20: 
            mapperDesc="Nintendo DiskSystem"
        if mapperNumber==21: 
            mapperDesc="Konami VRC4a"
        if mapperNumber==22: 
            mapperDesc="Konami VRC2a"
        if mapperNumber==23: 
            mapperDesc="Konami VRC2a"
        if mapperNumber==24: 
            mapperDesc="Konami VRC6"
        if mapperNumber==25: 
            mapperDesc="Konami VRC4b"
        if mapperNumber==32: 
            mapperDesc="Irem G-101 chip"
        if mapperNumber==33: 
            mapperDesc="Taito TC0190/TC0350"
        if mapperNumber==34: 
            mapperDesc="Nina-1 board"
        if mapperNumber==64: 
            mapperDesc="Tengen RAMBO-1 chip"
        if mapperNumber==65: 
            mapperDesc="Irem H-3001 chip"
        if mapperNumber==66: 
            mapperDesc="GNROM switch"
        if mapperNumber==67: 
            mapperDesc="SunSoft3 chip"
        if mapperNumber==68: 
            mapperDesc="SunSoft4 chip"
        if mapperNumber==69: 
            mapperDesc="SunSoft5 FME-7 chip"
        if mapperNumber==71: 
            mapperDesc="Camerica chip"
        if mapperNumber==78: 
            mapperDesc="Irem 74HC161Irem 74HC161/32-based]]"
        if mapperNumber==79: 
            mapperDesc="AVE Nina-3 board"
        if mapperNumber==81: 
            mapperDesc="AVE Nina-6 board"
        if mapperNumber==91: 
            mapperDesc="Pirate HK-SF3 chip "
      
        return mapperDesc
