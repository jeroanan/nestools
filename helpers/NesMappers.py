class NesMappers:

    @staticmethod
    def mapperToString(mapperNumber):
        """Takes a number in and gives a textual description of the mapper concerned"""
        
        mapperDesc = "None";
        
        mappers = {"1": "Nintendo MMC1",
                   "2": "CNROM switch",
                   "3": "UNROM switch",
                   "4": "Nintendo MMC3",
                   "5": "Nintendo MMC5",
                   "6": "FFE F4xxx",
                   "7": "AOROM switch",
                   "8": "FFE F3xxx",
                   "9": "Nintendo MMC2",
                   "10": "Nintendo MMC4",
                   "11": "ColorDreams chip",
                   "12": "- FFE F6xxx",
                   "13": "CPROM switch",
                   "15": "100-in-1 switch",
                   "16": "Bandai chip",
                   "17": "FFE F8xxx",
                   "18": "Jaleco SS8806 chip",
                   "19": "Namcot 106 chip",
                   "20": "Nintendo DiskSystem",
                   "21": "Konami VRC4a",
                   "22": "Konami VRC2a",
                   "23": "Konami VRC2a",
                   "24": "Konami VRC6",
                   "25": "Konami VRC4b",
                   "32": "Irem G-101 chip",
                   "33": "Taito TC0190/TC0350",
                   "34": "Nina-1 board",
                   "64": "Tengen RAMBO-1 chip",
                   "65": "Irem H-3001 chip",
                   "66": "GNROM switch",
                   "67": "SunSoft3 chip",
                   "68": "SunSoft4 chip",
                   "69": "SunSoft5 FME-7 chip",
                   "71": "Camerica chip",
                   "78": "Irem 74HC161Irem 74HC161/32-based]]",
                   "79": "AVE Nina-3 board",
                   "81": "AVE Nina-6 board",
                   "91": "Pirate HK-SF3 chip"}

        if mappers.has_key(mapperNumber):
            mapperDesc = mappers[mapperNumber]
      
        return mapperDesc

