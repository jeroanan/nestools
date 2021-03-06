import sys
import unittest

sys.path.append("..")
import NesCpu

class TestCLC(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x1

    def test_clc_progCounter(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_clc_accumulator(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.a, 0)

    def test_clc_xreg(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.x, 0)

    def test_clc_xregLoopsFromZero(self):
        self.cpu.x = 0
        self.cpu.clc()
        self.assertEqual(self.cpu.x, 0)

    def test_clc_yreg(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.y, 0)

    def test_clc_stackPointer(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.s, 0)

    def test_clc_processorStauts(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p, 0x0)

class TestSEC(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x0

    def test_sec_progCounter(self):
        self.cpu.sec()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_sec_accumulator(self):
        self.cpu.sec()
        self.assertEqual(self.cpu.a, 0)

    def test_sec_xreg(self):
        self.cpu.sec()
        self.assertEqual(self.cpu.x, 0)

    def test_sec_xregLoopsFromZero(self):
        self.cpu.x = 0
        self.cpu.sec()
        self.assertEqual(self.cpu.x, 0)

    def test_sec_yreg(self):
        self.cpu.sec()
        self.assertEqual(self.cpu.y, 0)

    def test_sec_stackPointer(self):
        self.cpu.sec()
        self.assertEqual(self.cpu.s, 0)        

    def test_sec_processorStatus(self):
        self.cpu.sec()
        self.assertEqual(self.cpu.p, 0x1)

class TestSEI(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x0        

    def test_sei_progCounter(self):
        self.cpu.sei()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_sei_accumulator(self):
        self.cpu.sei()
        self.assertEqual(self.cpu.a, 0)
        
    def test_sei_xreg(self):
        self.cpu.sei()
        self.assertEqual(self.cpu.x, 0)

    def test_sei_yreg(self):
        self.cpu.sei()
        self.assertEqual(self.cpu.y, 0)

    def test_sei_stackPointer(self):
        self.cpu.sei()
        self.assertEqual(self.cpu.s, 0)

    def test_sei_processorStatus(self):
        self.cpu.sei()
        self.assertEqual(self.cpu.p, 0x4)

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x4

    def test_cli_progCounter(self):
        self.cpu.cli()
        self.assertEqual(self.cpu.pc, 0x0)
    
    def test_cli_accumulator(self):
        self.cpu.cli()
        self.assertEqual(self.cpu.a, 0)

    def test_cli_xreg(self):
        self.cpu.cli()
        self.assertEqual(self.cpu.x, 0)

    def test_cli_yreg(self):
        self.cpu.cli()
        self.assertEqual(self.cpu.y, 0)
        
    def test_cli_stackPointer(self):
        self.cpu.cli()
        self.assertEqual(self.cpu.s, 0)

    def test_cli_processorStatus(self):
        self.cpu.cli()
        self.assertEqual(self.cpu.p, 0x0)        

class TestADC(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.a = 0
        self.x = 0
        self.y = 0
        self.s = 0
        self.p = 0x0

    def test_adc_accumulator(self):
        self.cpu.adc(2)
        self.assertEqual(self.cpu.a, 2)

    def test_adc_xreg(self):
        self.cpu.adc(2)
        self.assertEqual(self.cpu.x, 0)

    def test_adc_yreg(self):
        self.cpu.adc(2)
        self.assertEqual(self.cpu.y, 0)

    def test_adc_stackPointer(self):
        self.cpu.adc(2)
        self.assertEqual(self.cpu.s, 0)
        
    def test_adc_processorStatus(self):
        self.cpu.adc(2)
        self.assertEqual(self.cpu.p, 0x0)

    def test_adc_processorStatusBit7Set(self):
        self.cpu.adc(255)
        self.assertEqual(self.cpu.p, 0x80)    

class TestTYA(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 1
        self.cpu.s = 0
        self.cpu.p = 0x0
        
    def test_tya_progCounter(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_tya_accumulator(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.a, 1)

    def test_tya_xreg(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.x, 0)

    def test_tya_yreg(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.y, 1)

    def test_tya_stackPointer(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.s, 0)

    def test_tya_processorStatusBit1ShouldBeUnSet(self):
        self.cpu.y = 1
        self.cpu.tya()
        self.assertEqual(self.cpu.p, 0x0)

    def test_tya_processorStatusBit1ShouldBeSet(self):
        self.cpu.y = 0
        self.cpu.tya()
        self.assertEqual(self.cpu.p, 0x2)

    def test_tya_processorStatusBit7ShouldBeSet(self):
        self.cpu.y = 255
        self.cpu.tya()
        self.assertEqual(self.cpu.p, 0x80)

class TestLDA(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.a = 0
        self.cpu.p = 0x0

    def test_lda(self):
        self.cpu.lda(42)
        self.assertEqual(self.cpu.a, 42)
        
    def test_lda_bit1Set(self):
        self.cpu.lda(0)
        self.assertEqual(self.cpu.p, 0x2)

    def test_lda_bit7Set(self):
        self.cpu.lda(128)
        self.assertEqual(self.cpu.p, 0x80)

class TestLDX(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.x = 0
        self.cpu.p = 0x0

    def test_ldx(self):
        self.cpu.ldx(42)
        self.assertEqual(self.cpu.x, 42)
    
    def test_ldx_bit1Set(self):
        self.cpu.ldx(0)
        self.assertEqual(self.cpu.p, 0x2)
    
    def test_ldx_bit7Set(self):
        self.cpu.ldx(255)
        self.assertEqual(self.cpu.p, 0x80)

class TestLDY(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.y = 0
        self.cpu.p = 0x0

    def test_ldy(self):
        self.cpu.ldy(42)
        self.assertEqual(self.cpu.y, 42)
    
    def test_ldy_bit1Set(self):
        self.cpu.ldy(0)
        self.assertEqual(self.cpu.p, 0x2)
    
    def test_ldy_bit7Set(self):
        self.cpu.ldy(255)
        self.assertEqual(self.cpu.p, 0x80)

class TestTAY(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 1
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x00

    def test_tay_progCounter(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_tay_accumulator(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.a, 1)

    def test_tay_xreg(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.x, 0)

    def test_tay_yreg(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.y, 1)

    def test_tay_stackPointer(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.s, 0)

    def test_tay_processorStatusBit1ShouldBeUnSet(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.p, 0)

    def test_tay_processorStatusBit1ShouldBeSet(self):
        self.cpu.a = 0
        self.cpu.tay()
        self.assertEqual(self.cpu.p, 0x2)

    def test_tay_processorStatusBit7ShouldBeSet(self):
        self.cpu.a = 255
        self.cpu.tay()
        self.assertEqual(self.cpu.p, 128)                                                 

class TestTXS(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0x1FF
        self.cpu.y = 0
        self.cpu.s = 0x100
        self.cpu.p = 0x0
        
    def test_txs_progCounter(self):
        self.cpu.txs()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_txs_accumulator(self):
        self.cpu.txs()
        self.assertEqual(self.cpu.a, 0)

    def test_txs_xreg(self):
        self.cpu.txs()
        self.assertEqual(self.cpu.x, 0x1FF)

    def test_txs_yreg(self):
        self.cpu.txs()
        self.assertEqual(self.cpu.y, 0)

    def test_txs_stackPointer(self):
        self.cpu.txs()
        self.assertEqual(self.cpu.s, 0X1FF)
        
    def test_txs_processorStatus(self):
        self.cpu.txs()
        self.assertEqual(self.cpu.p, 0x80)      

    def test_txs_processorStatusBit7ShouldBeUnSet(self):
        self.cpu.x = 0x01
        self.cpu.txs()
        self.assertEqual(self.cpu.p, 0x0)      

class TestTAX(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 1
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x0

    def test_tax_progCounter(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_tax_accumulator(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.a, 1)

    def test_tax_xreg(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.x, 1)

    def test_tax_yreg(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.y, 0)

    def test_tax_stackPointer(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.s, 0)
        
    def test_tax_processorStatusBit1ShouldBeSet(self):
        self.cpu.a = 0
        self.cpu.tax()
        self.assertEqual(self.cpu.p, 0x2)

    def test_tax_processorStatusBit7ShouldBeSet(self):
        self.cpu.a = 255
        self.cpu.tax()
        self.assertEqual(self.cpu.p, 0x80)                                                 

class TestCLV(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0x0
        self.cpu.p = 0x40

    def test_clv_progCounter(self):
        self.cpu.clv()
        self.assertEqual(self.cpu.pc, 0x0)
        
    def test_clv_accumulator(self):
        self.cpu.clv()
        self.assertEqual(self.cpu.a, 0)

    def test_clv_xreg(self):
        self.cpu.clv()
        self.assertEqual(self.cpu.x, 0)

    def test_clv_yreg(self):
        self.cpu.clv()
        self.assertEqual(self.cpu.y, 0)

    def test_clv_stackPointer(self):
        self.cpu.clv()
        self.assertEqual(self.cpu.s, 0x0)

    def test_clv_processorStatus(self):
        self.cpu.clv()
        self.assertEqual(self.cpu.p, 0x0)        

class TestTSX(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0x1FF
        self.cpu.p = 0x0
        
    def test_tsx_progCounter(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_tsx_accumulator(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.a, 0)

    def test_tsx_xreg(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.x, 0x1FF)

    def test_tsx_yreg(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.y, 0)

    def test_tsx_stackPointer(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.s, 0X1FF)

    def test_tsx_processorStatusBit1ShouldBeUnSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_tsx_processorStatusBit7ShouldBeSet(self):
        self.cpu.s = 0xFF
        self.cpu.tsx()
        self.assertEqual(self.cpu.p, 0x80)      

    def test_tsx_processorStatusBit7ShouldBeUnSet(self):
        self.cpu.s = 0x100
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 7), 0)      

class TestIny(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 1
        self.cpu.y = 1
        self.cpu.s = 0
        self.cpu.p = 0x0

    def test_iny_progCounter(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_iny_accumulator(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.a, 0)
        
    def test_iny_xreg(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.x, 1)    

    def test_iny_yreg(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.y, 2)

    def test_iny_yregLoopsFromMax(self):
        self.cpu.y = 255
        self.cpu.iny()
        self.assertEqual(self.cpu.y, 0)

    def test_iny_stackPointer(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.s, 0)

    def test_iny_processorStauts(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p, 0x0)

    def test_iny_processorStatusBit1ShouldBeSetAfterLoopRound(self):
        self.cpu.y = 255
        self.cpu.iny()
        self.assertEqual(self.cpu.p, 0x2)

    def test_iny_processorStatusBit7ShouldBeSet(self):
        self.cpu.y = 254
        self.cpu.iny()
        self.assertEqual(self.cpu.p, 0x80)

class TestDex(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 1
        self.cpu.y = 1
        self.cpu.s = 0
        self.cpu.p = 0x0

    def test_dex_progCounter(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_dex_accumulator(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.a, 0)
        
    def test_dex_xreg(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.x, 0)

    def test_dex_xregLoopsFromZero(self):
        self.cpu.x = 0
        self.cpu.dex()
        self.assertEqual(self.cpu.x, 255)

    def test_dex_yreg(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.y, 1)

    def test_dex_stackPointer(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.s, 0)

    def test_dex_processorStatus(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p, 0x2)

    def test_dex_processorStatusBit1ShouldBeUnSet(self):
        self.cpu.x = 2
        self.cpu.dex()
        self.assertEqual(self.cpu.p, 0x0)

    def test_dex_processorStatusBit1ShouldBeUnsetAfterLoopRound(self):
        self.cpu.x = 0
        self.cpu.p = 0x2
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 1), 0x0)

class TestDey(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 1
        self.cpu.y = 1
        self.cpu.s = 0
        self.cpu.p = 0x0

    def test_dey_progCounter(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_dey_accumulator(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.a, 0)
        
    def test_dey_xreg(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.x, 1)    

    def test_dey_yreg(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.y, 0)

    def test_dey_yregLoopsFromZero(self):
        self.cpu.y = 0
        self.cpu.dey()
        self.assertEqual(self.cpu.y, 255)

    def test_dey_stackPointer(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.s, 0)

    def test_dey_processorStauts(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p, 0x2)

    def test_dey_processorStatusBit1ShouldBeUnset(self):
        self.cpu.y = 2
        self.cpu.dey()
        self.assertEqual(self.cpu.p, 0x0)

    def test_dey_processorStatusBit7LoopRound(self):
        self.cpu.y = 0
        self.cpu.p = 0x0
        self.cpu.dey()
        self.assertEqual(self.cpu.p, 0x80)

class TestTXA(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 1
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x0

    def test_txa_procCounter(self):
        self.cpu.txa()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_txa_accumulator(self):
        self.cpu.txa()
        self.assertEqual(self.cpu.a, 1)

    def test_txa_xreg(self):
        self.cpu.txa()
        self.assertEqual(self.cpu.x, 1)

    def test_txa_yreg(self):
        self.cpu.txa()
        self.assertEqual(self.cpu.y, 0)

    def test_txa_stackPointer(self):
        self.cpu.txa()
        self.assertEqual(self.cpu.s, 0)
        
    def test_txa_processorStatus(self):
        self.cpu.txa()
        self.assertEqual(self.cpu.p, 0x0)

    def test_txa_processorStatusBit1Set(self):
        self.cpu.x = 0
        self.cpu.txa()
        self.assertEqual(self.cpu.p, 0x2)

    def test_txa_processorStatusBit7Set(self):
        self.cpu.x = 255
        self.cpu.txa()
        self.assertEqual(self.cpu.p, 0x80)

class TestCLD(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x8

    def test_cld_progCounter(self):
        self.cpu.cld()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_cld_accumulator(self):
        self.cpu.cld()
        self.assertEqual(self.cpu.a, 0)
        
    def test_cld_xreg(self):
        self.cpu.cld()
        self.assertEqual(self.cpu.x, 0)

    def test_cld_yreg(self):
        self.cpu.cld()
        self.assertEqual(self.cpu.y, 0)

    def test_cld_stackPointer(self):
        self.cpu.cld()
        self.assertEqual(self.cpu.s, 0)

    def test_cld_processorStatus(self):
        self.cpu.cld()
        self.assertEqual(self.cpu.p, 0x0)

class TestNop(unittest.TestCase):
    
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x0

    def test_nop_progCounter(self):
        self.cpu.nop()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_nop_accumulator(self):
        self.cpu.nop()
        self.assertEqual(self.cpu.a, 0)

    def test_nop_xreg(self):
        self.cpu.nop()
        self.assertEqual(self.cpu.x, 0)
    
    def test_nop_stackPointer(self):
        self.cpu.nop()
        self.assertEqual(self.cpu.s, 0)

    def test_nop_processorStatus(self):
        self.cpu.nop()
        self.assertEqual(self.cpu.p, 0x0)

class TestSED(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x0

    def test_sed_progCounter(self):
        self.cpu.sed()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_sed_accumulator(self):
        self.cpu.sed()
        self.assertEqual(self.cpu.a, 0)

    def test_sed_xreg(self):
        self.cpu.sed()
        self.assertEqual(self.cpu.x, 0)
    
    def test_sed_stackPointer(self):
        self.cpu.sed()
        self.assertEqual(self.cpu.s, 0)

    def test_sed_processorStatus(self):
        self.cpu.sed()
        self.assertEqual(self.cpu.p, 0x8)    

class TestImmediateAddressing(unittest.TestCase):
    
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        
    def test_immediate_addressing(self):
        self.assertEqual(self.cpu.get_operand(("CPX", self.cpu.MEM_IMM), 0x80))

class TestAbsoluteAddressing(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.mem = [0xff] * (0x800)
        self.cpu.mem[128] = 0x5

    def test_absolute_addressing(self):
        self.assertEqual(self.cpu.get_operand(('ORA', self.cpu.MEM_ABS), 0x80))

if __name__=="__main__":
    unittest.main()
