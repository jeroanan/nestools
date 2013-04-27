"""The main class for emulating the 6502."""
class NesCpu(object):

    MEM_IMM = "imm" # Immediate
    MEM_ABS = "abs" # absolute
    MEM_ZP = "zep" # Zero Page  
    MEM_IMP = "imp" # Implied
    MEM_ABS = "abs" # Absolute
    MEM_ABSX = "abx"
    MEM_ABSY = "aby"
    MEM_INDX = "idx" # Indexed X    
    MEM_INDY = "idy" # Indexed Y
    MEM_ZPX = "zpx" # Zero Page X
    MEM_ZPY = "zpy" # Zero Page Y
    

    # (opcodeHex, Mnemomic
    OpCodes = {(0x00, 'BRK'),
               (0x01, 'ORA', MEM_INDX),
               (0x05, 'ORA', MEM_ZPY),
               (0x06, 'ASL', MEM_ZPY),
               (0x08, 'PHP', MEM_IMP),
               (0x09, 'ORA', MEM_IMM),
               (0x0A, 'ASL', MEM_IMP),
               (0x0D, 'ORA', MEM_ABS),
               (0x0E, 'ASL'),
               (0x10, 'BPL', MEM_IMP),
               (0x11, 'ORA', MEM_INDY),
               (0x15, 'ORA', MEM_ZPX),
               (0x16, 'ASL', MEM_ZPX,
               (0x18, 'CLC', MEM_IMP),
               (0x19, 'ORA', MEM_ABSY),
               (0x1D, 'ORA', MEM_ABSX),
               (0x1E, 'ASL'),
               (0x20, 'JSR', MEM_IMP),
               (0x21, 'AND', MEM_INDX),
               (0x24, 'BIT', MEM_ZPY),
               (0x25, 'AND', MEM_ZPY),
               (0x26, 'ROL', MEM_ZPY),
               (0x28, 'PLP', MEM_IMP),
               (0x29, 'AND', MEM_IMM),
               (0x2A, 'ROL', MEM_IMP),
               (0x2C, 'BIT', MEM_ABS),
               (0x2D, 'AND', MEM_ABS),
               (0x2E, 'ROL', MEM_ABS),
               (0x30, 'BMI', MEM_IMP),
               (0x31, 'AND', MEM_INDY),
               (0x35, 'AND', MEM_ZPX),
               (0x36, 'ROL', MEM_ZPX),
               (0x38, 'SEC', MEM_IMP),
               (0x39, 'AND', MEM_ABSY),
               (0x3D, 'AND', MEM_ABSX),
               (0x3E, 'ROL'),
               (0x40, 'RTI', MEM_IMP),
               (0x41, 'EOR', MEM_INDX),
               (0x45, 'EOR', MEM_ZPY),
               (0x46, 'LSR', MEM_ZPY),
               (0x48, 'PHA', MEM_IMP),
               (0x49, 'EOR', MEM_IMM),
               (0x4A, 'LSR', MEM_IMP),
               (0x4C, 'JMP', MEM_ABS),
               (0x4D, 'EOR', MEM_ABS),
               (0x4E, 'LSR', MEM_ABS),
               (0x50, 'BVC', MEM_IMP),
               (0x51, 'EOR', MEM_INDY),
               (0x55, 'EOR', MEM_ZPX),
               (0x56, 'LSR'),
               (0x58, 'CLI', MEM_IMP),
               (0x59, 'EOR', MEM_ABSY),
               (0x5D, 'EOR', MEM_ABSX),
               (0x5E, 'LSR', MEM_ABSX),
               (0x60, 'RTS', MEM_IMP),
               (0x61, 'ADC', MEM_INDX),
               (0x65, 'ADC', MEM_ZPY),
               (0x66, 'ROR', MEM_ZPY),
               (0x68, 'PLA', MEM_IMP),
               (0x69, 'ADC', MEM_IMM),
               (0x6A, 'ROR', MEM_IMP),
               (0x6C, 'JMP', MEM_IMP),
               (0x6D, 'ADC', MEM_ABS),
               (0x6E, 'ROR', MEM_ABS),
               (0x70, 'BVS', MEM_IMP),
               (0x71, 'ADC', MEM_INDY),
               (0x75, 'ADC', MEM_ZPZ),
               (0x76, 'ROR', MEM_ZPX),
               (0x78, 'SEI', MEM_IMP),
               (0x79, 'ADC', MEM_ABSY),
               (0x7D, 'ADC', MEM_ABSX),
               (0x7E, 'ROR', MEM_ABSX),
               (0x81, 'STA', MEM_INDX),
               (0x84, 'STY', MEM_ZPY),
               (0x85, 'STA', MEM_ZPY),
               (0x86, 'STX', MEM_ZPY),
               (0x88, 'DEY', MEM_IMP),
               (0x8A, 'TXA', MEM_IMP),
               (0x8C, 'STY', MEM_ABS),
               (0x8D, 'STA', MEM_ABS),
               (0x8E, 'STX', MEM_ABS),
               (0x90, 'BCC', MEM_IMP),
               (0x91, 'STA', MEM_INDY),
               (0x94, 'STY', MEM_ZPX),
               (0x95, 'STA', MEM_ZPX),
               (0x96, 'STX', MEM_ZPX),
               (0x98, 'TYA', MEM_IMP),
               (0x99, 'STA', MEM_ABSY),
               (0x9A, 'TXS', MEM_IMP),
               (0x9D, 'STA', MEM_ABSX),
               (0xA0, 'LDY', MEM_IMM),
               (0xA1, 'LDA', MEM_INDX),
               (0xA2, 'LDX', MEM_IMM),
               (0xA4, 'LDY', MEM_ZPY),
               (0xA5, 'LDA', MEM_ZPY),
               (0xA6, 'LDX', MEM_ZPY),
               (0xA8, 'TAY', MEM_IMP),
               (0xA9, 'LDA', MEM_IMM),
               (0xAA, 'TAX', MEM_IMP),
               (0xAC, 'LDY', MEM_ABS),
               (0xAD, 'LDA', MEM_ABS),
               (0xAE, 'LDX', MEM_ABS),
               (0xB0, 'BCS', MEM_IMP),
               (0xB1, 'LDA', MEM_INDY),
               (0xB4, 'LDY', MEM_ZPX),
               (0xB5, 'LDA', MEM_ZPX),
               (0xB6, 'LDX', MEM_ZPX),
               (0xB8, 'CLV', MEM_IMP),
               (0xB9, 'LDA', MEM_ABSY),
               (0xBA, 'TSX', MEM_IMP),
               (0xBC, 'LDY', MEM_ABSX),
               (0xBD, 'LDA', MEM_ABSX),
               (0xBE, 'LDX', MEM_ABSY),
               (0xC0, 'CPY', MEM_IMM),
               (0xC1, 'CMP', MEM_INDX),
               (0xC4, 'CPY', MEM_ZPY),
               (0xC5, 'CMP', MEM_ZPY),
               (0xC6, 'DEC', MEM_ZPY),
               (0xC8, 'INY', MEM_IMP),
               (0xC9, 'CMP', MEM_IMM),
               (0xCA, 'DEX', MEM_IMP),
               (0xCC, 'CPY', MEM_ABS),
               (0xCD, 'CMP', MEM_ABS),
               (0xCE, 'DEC', MEM_ABS),
               (0xD0, 'BNE', MEM_IMP),
               (0xD1, 'CMP', MEM_INDY),
               (0xD5, 'CMP', MEM_ZPX),
               (0xD6, 'DEC', MEM_ZPX),
               (0xD8, 'CLD', MEM_IMP),
               (0xD9, 'CMP', MEM_ABSY),
               (0xDD, 'CMP', MEM_ABSX),
               (0xDE, 'DEC', MEM_ABSX),
               (0xE0, 'CPX', MEM_IMM),
               (0xE1, 'SBC', MEM_INDX),
               (0xE4, 'CPX', MEM_ZPY),
               (0xE5, 'SBC', MEM_ZPY),
               (0xE6, 'INC', MEM_ZPY),
               (0xE8, 'INX', MEM_IMP),
               (0xE9, 'SBC', MEM_IMM),
               (0xEA, 'NOP', MEM_IMP),
               (0xEC, 'CPX', MEM_ABS),
               (0xED, 'SBC', MEM_ABS),
               (0xEE, 'INC', MEM_ABS),
               (0xF0, 'BEQ', MEM_IMP),
               (0xF1, 'SBC', MEM_INDY),
               (0xF5, 'SBC', MEM_ZPX),
               (0xF6, 'INC', MEM_ZPX),
               (0xF8, 'SED', MEM_IMP),
               (0xF9, 'SBC', MEM_ABSY),
               (0xFD, 'SBC', MEM_ABSX),
               (0xFE, 'INC', MEM_ABSX)}
    
    pc = 0x0 # program counter
    
    a = 0   # accumulator
    x = 0   # x register
    y = 0   # y register
    s = 0   # stack pointer
    p = 0x0 # processor status    
    
    mem = [0]

    def set_z_and_n(self, value):
        """Sets the Z and N processor flags based on the given value. If Z is 
        zero, set the Z flag. If the 7th bit of value is 1, set the N flag."""
        # Z Flag
        if value:
            self.p &= ~0x2
        else:
            self.p |= 0x2

        # N Flag
        if value & (1 << 7) == 128:
            self.p |= 0x80
        else:
            self.p &= ~0x80

    # instruction processing
    def clc(self):
        """Clear the Processor Status Carry Flag"""
        self.p &= ~0x1

    def sec(self):
        """Set the Processor Status Carry Flag"""
        self.p |= 0x1

    def sei(self):
        """Sets the Processor Status Interrupt Disable Flag"""
        self.p |= 0x4

    def cli(self):
        """Clear the Processor Status Interrupt Disable Flag"""
        self.p &= ~0x4

    def adc(self, value):
        """Add the given value to the accumulator. 
        Set N and Z flags as needed."""
        # todo: pretty sure i've oversimplified here. revisit.
        self.a += value
        self.set_z_and_n(self.a)

    def dey(self):
        """decrement y register. If after dec it is < 0 or >255 it 
        needs to become 255 and 0 respectively. If it ends up as 0 we
        set the Z flag. Set N flag if bit 7 of the result == 1"""
        self.y -=1
        self.y &= 0xFF
        self.set_z_and_n(self.y)

    def txa(self):
        """Transfer the x register to the accumulator. If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.a = self.x
        self.set_z_and_n(self.a)

    def tya(self):
        """Transfer the y register to the accumulator. If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.a = self.y
        self.set_z_and_n(self.a)

    def lda(self, value):
        """Loads the given value into the accumulator If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.a = value
        self.set_z_and_n(self.a)

    def ldx(self, value):
        """Loads the given value into the x register If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.x = value
        self.set_z_and_n(self.x)

    def ldy(self, value):
        """Loads the given value into the y register If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.y = value
        self.set_z_and_n(self.y)

    def tay(self):
        """Transfer the accumulator to the y register. If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.y = self.a
        self.set_z_and_n(self.y)

    def txs(self):
        """Transfer the x register to the stack pointer. If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.s = self.x
        self.set_z_and_n(self.s)

    def tax(self):
        """Transfer the accumulator to the x register. If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.x = self.a
        self.set_z_and_n(self.x)

    def clv(self):
        """Clear the Processor Status Overflow Flag"""
        self.p &= ~0x40

    def tsx(self):
        """Transfer the stack pointer to the x register. If the value is 0,
        set the Z flag. If bit 7 is 1, set N."""
        self.x = self.s
        self.set_z_and_n(self.x)

    def iny(self):
        """increment y register. If after dec it is < 0 or >255 it 
        needs to become 255 and 0 respectively. If it ends up as 0 we
        set the Z flag. Set N flag if bit 7 of the result == 1"""
        self.y += 1
        self.y &= 0xFF
        self.set_z_and_n(self.y)

    def dex(self):
        """decrement x register. If after dec it is < 0 or >255 it 
        needs to become 255 and 0 respectively. If it ends up as 0 we
        set the Z flag. Set N flag if bit 7 of the result == 1"""
        self.x -= 1
        self.x &= 0XFF
        self.set_z_and_n(self.x)

    def cld(self):
        """Clear processor decimal mode status flag"""        
        self.p &= ~0x8

    def nop(self):
        """nop: no operation. do nothing."""
        pass

    def sed(self):
        """Sets the Processor Status Decimal Flag"""
        self.p |= 0x8

