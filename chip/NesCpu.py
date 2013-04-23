"""The main class for emulating the 6502."""
class NesCpu(object):

    # (opcodeHex, Mnemomic
    OpCodes = {(0x00, 'BRK'),
               (0x01, 'ORA'),
               (0x05, 'ORA'),
               (0x06, 'ASL'),
               (0x08, 'PHP'),
               (0x09, 'ORA'),
               (0x0A, 'ASL'),
               (0x0D, 'ORA'),
               (0x0E, 'ASL'),
               (0x10, 'BPL'),
               (0x11, 'ORA'),
               (0x15, 'ORA'),
               (0x16, 'ASL'),
               (0x18, 'CLC'),
               (0x19, 'ORA'),
               (0x1D, 'ORA'),
               (0x1E, 'ASL'),
               (0x20, 'JSR'),
               (0x21, 'AND'),
               (0x24, 'BIT'),
               (0x25, 'AND'),
               (0x26, 'ROL'),
               (0x28, 'PLP'),
               (0x29, 'AND'),
               (0x2A, 'ROL'),
               (0x2C, 'BIT'),
               (0x2D, 'AND'),
               (0x2E, 'ROL'),
               (0x30, 'BMI'),
               (0x31, 'AND'),
               (0x35, 'AND'),
               (0x36, 'ROL'),
               (0x38, 'SEC'),
               (0x39, 'AND'),
               (0x3D, 'AND'),
               (0x3E, 'ROL'),
               (0x40, 'RTI'),
               (0x41, 'EOR'),
               (0x45, 'EOR'),
               (0x46, 'LSR'),
               (0x48, 'PHA'),
               (0x49, 'EOR'),
               (0x4A, 'LSR'),
               (0x4C, 'JMP'),
               (0x4D, 'EOR'),
               (0x4E, 'LSR'),
               (0x50, 'BVC'),
               (0x51, 'EOR'),
               (0x55, 'EOR'),
               (0x56, 'LSR'),
               (0x58, 'CLI'),
               (0x59, 'EOR'),
               (0x5D, 'EOR'),
               (0x5E, 'LSR'),
               (0x60, 'RTS'),
               (0x61, 'ADC'),
               (0x65, 'ADC'),
               (0x66, 'ROR'),
               (0x68, 'PLA'),
               (0x69, 'ADC'),
               (0x6A, 'ROR'),
               (0x6C, 'JMP'),
               (0x6D, 'ADC'),
               (0x6E, 'ROR'),
               (0x70, 'BVS'),
               (0x71, 'ADC'),
               (0x75, 'ADC'),
               (0x76, 'ROR'),
               (0x78, 'SEI'),
               (0x79, 'ADC'),
               (0x7D, 'ADC'),
               (0x7E, 'ROR'),
               (0x81, 'STA'),
               (0x84, 'STY'),
               (0x85, 'STA'),
               (0x86, 'STX'),
               (0x88, 'DEY'),
               (0x8A, 'TXA'),
               (0x8C, 'STY'),
               (0x8D, 'STA'),
               (0x8E, 'STX'),
               (0x90, 'BCC'),
               (0x91, 'STA'),
               (0x94, 'STY'),
               (0x95, 'STA'),
               (0x96, 'STX'),
               (0x98, 'TYA'),
               (0x99, 'STA'),
               (0x9A, 'TXS'),
               (0x9D, 'STA'),
               (0xA0, 'LDY'),
               (0xA1, 'LDA'),
               (0xA2, 'LDX'),
               (0xA4, 'LDY'),
               (0xA5, 'LDA'),
               (0xA6, 'LDX'),
               (0xA8, 'TAY'),
               (0xA9, 'LDA'),
               (0xAA, 'TAX'),
               (0xAC, 'LDY'),
               (0xAD, 'LDA'),
               (0xAE, 'LDX'),
               (0xB0, 'BCS'),
               (0xB1, 'LDA'),
               (0xB4, 'LDY'),
               (0xB5, 'LDA'),
               (0xB6, 'LDX'),
               (0xB8, 'CLV'),
               (0xB9, 'LDA'),
               (0xBA, 'TSX'),
               (0xBC, 'LDY'),
               (0xBD, 'LDA'),
               (0xBE, 'LDX'),
               (0xC0, 'CPY'),
               (0xC1, 'CMP'),
               (0xC4, 'CPY'),
               (0xC5, 'CMP'),
               (0xC6, 'DEC'),
               (0xC8, 'INY'),
               (0xC9, 'CMP'),
               (0xCA, 'DEX'),
               (0xCC, 'CPY'),
               (0xCD, 'CMP'),
               (0xCE, 'DEC'),
               (0xD0, 'BNE'),
               (0xD1, 'CMP'),
               (0xD5, 'CMP'),
               (0xD6, 'DEC'),
               (0xD8, 'CLD'),
               (0xD9, 'CMP'),
               (0xDD, 'CMP'),
               (0xDE, 'DEC'),
               (0xE0, 'CPX'),
               (0xE1, 'SBC'),
               (0xE4, 'CPX'),
               (0xE5, 'SBC'),
               (0xE6, 'INC'),
               (0xE8, 'INX'),
               (0xE9, 'SBC'),
               (0xEA, 'NOP'),
               (0xEC, 'CPX'),
               (0xED, 'SBC'),
               (0xEE, 'INC'),
               (0xF0, 'BEQ'),
               (0xF1, 'SBC'),
               (0xF5, 'SBC'),
               (0xF6, 'INC'),
               (0xF8, 'SED'),
               (0xF9, 'SBC'),
               (0xFD, 'SBC'),
               (0xFE, 'INC')}
    
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

