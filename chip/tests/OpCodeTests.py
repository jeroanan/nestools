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
        self.cpu.p = 0xFF

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

    def test_clc_processorStautsBit0ShouldBeUnset(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 0), 0)

    def test_clc_processorStatusBit1ShouldBeSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 1), 2)

    def test_clc_processorStatusBit2ShouldBeSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 2), 4)

    def test_clc_processorStatusBit3ShouldBeSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 3), 8)

    def test_clc_processorStatusBit4ShouldBeSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 4), 16)

    def test_clc_processorStatusBit5ShouldBeSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 5), 32)

    def test_clc_processorStatusBit6ShouldBeSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 6), 64)

    def test_clc_processorStatusBit7ShouldBeSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 7), 128)                                                 

class TestSEC(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0x00

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

    def test_sec_processorStautsBit0ShouldBeSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 0), 1)

    def test_sec_processorStatusBit1ShouldBeUnSet(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_sec_processorStatusBit2ShouldBeUnset(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 2), 0)

    def test_sec_processorStatusBit3ShouldBeUnset(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 3), 0)

    def test_sec_processorStatusBit4ShouldBeUnset(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 4), 0)

    def test_sec_processorStatusBit5ShouldBeUnset(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 5), 0)

    def test_sec_processorStatusBit6ShouldBeUnset(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 6), 0)

    def test_sec_processorStatusBit7ShouldBeUnset(self):
        self.cpu.clc()
        self.assertEqual(self.cpu.p & (1 << 7), 0)

class TestTYA(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 0
        self.cpu.x = 0
        self.cpu.y = 1
        self.cpu.s = 0
        self.cpu.p = 0xFF
        
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

    def test_tya_processorStautsBit0ShouldBeSet(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 0), 1)
    
    def test_tya_processorStatusBit1ShouldBeUnSet(self):
        self.cpu.y = 1
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_tya_processorStatusBit1ShouldBeSet(self):
        self.cpu.y = 0
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 1), 2)

    def test_tya_processorStatusBit2ShouldBeSet(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 2), 4)

    def test_tya_processorStatusBit3ShouldBeSet(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 3), 8)

    def test_tya_processorStatusBit4ShouldBeSet(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 4), 16)

    def test_tya_processorStatusBit5ShouldBeSet(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 5), 32)

    def test_tya_processorStatusBit6ShouldBeSet(self):
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 6), 64)

    def test_tya_processorStatusBit7ShouldBeSet(self):
        self.cpu.y = 255
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 7), 128)                                                 

    def test_tya_processorStatusBit7ShouldBeUnSet(self):
        self.cpu.y = 1
        self.cpu.tya()
        self.assertEqual(self.cpu.p & (1 << 7), 0)      

class TestTAY(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 1
        self.cpu.x =	0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0xFF

    def test_tay_progCounter(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_tay_accumulator(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.a, 0)

    def test_tay_xreg(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.x, 0)

    def test_tay_yreg(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.y, 1)

    def test_tay_stackPointer(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.s, 0)

    def test_tay_processorStautsBit0ShouldBeSet(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 0), 1)
    
    def test_tay_processorStatusBit1ShouldBeSet(self):
        self.cpu.a = 1
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_tay_processorStatusBit1ShouldBeSet(self):
        self.cpu.a = 0
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 1), 2)

    def test_tay_processorStatusBit2ShouldBeSet(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 2), 4)

    def test_tay_processorStatusBit3ShouldBeSet(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 3), 8)

    def test_tay_processorStatusBit4ShouldBeSet(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 4), 16)

    def test_tay_processorStatusBit5ShouldBeSet(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 5), 32)

    def test_tay_processorStatusBit6ShouldBeSet(self):
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 6), 64)

    def test_tay_processorStatusBit7ShouldBeSet(self):
        self.cpu.a = 255
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 7), 128)                                                 

    def test_tay_processorStatusBit7ShouldBeUnSet(self):
        self.cpu.a = 1
        self.cpu.tay()
        self.assertEqual(self.cpu.p & (1 << 7), 0)  

class TestTAX(unittest.TestCase):
    def setUp(self):
        self.cpu = NesCpu.NesCpu()
        self.cpu.pc = 0x0
        self.cpu.a = 1
        self.cpu.x =	0
        self.cpu.y = 0
        self.cpu.s = 0
        self.cpu.p = 0xFF

    def test_tax_progCounter(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.pc, 0x0)

    def test_tax_accumulator(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.a, 0)

    def test_tax_xreg(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.x, 1)

    def test_tax_yreg(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.y, 0)

    def test_tax_stackPointer(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.s, 0)

    def test_tax_processorStautsBit0ShouldBeSet(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 0), 1)
    
    def test_tax_processorStatusBit1ShouldBeSet(self):
        self.cpu.a = 1
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_tax_processorStatusBit1ShouldBeSet(self):
        self.cpu.a = 0
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 1), 2)

    def test_tax_processorStatusBit2ShouldBeSet(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 2), 4)

    def test_tax_processorStatusBit3ShouldBeSet(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 3), 8)

    def test_tax_processorStatusBit4ShouldBeSet(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 4), 16)

    def test_tax_processorStatusBit5ShouldBeSet(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 5), 32)

    def test_tax_processorStatusBit6ShouldBeSet(self):
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 6), 64)

    def test_tax_processorStatusBit7ShouldBeSet(self):
        self.cpu.a = 255
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 7), 128)                                                 

    def test_tax_processorStatusBit7ShouldBeUnSet(self):
        self.cpu.a = 1
        self.cpu.tax()
        self.assertEqual(self.cpu.p & (1 << 7), 0)  

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
        self.assertEqual(self.cpu.a, 1)

    def test_tsx_xreg(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.x, 0xFF)

    def test_tsx_yreg(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.y, 0)

    def test_tsx_stackPointer(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.s, 0XFF)

    def test_tsx_processorStautsBit0ShouldBeUnSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 0), 0)
    
    def test_tsx_processorStatusBit1ShouldBeUnSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_tsx_processorStatusBit2ShouldBeUnSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 2), 0)

    def test_tsx_processorStatusBit3ShouldBeUnSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 3), 0)

    def test_tsx_processorStatusBit4ShouldBeUnSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 4), 0)

    def test_tsx_processorStatusBit5ShouldBeUnSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 5), 0)

    def test_tsx_processorStatusBit6ShouldBeUnSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 6), 0)

    def test_tsx_processorStatusBit7ShouldBeSet(self):
        self.cpu.tsx()
        self.assertEqual(self.cpu.p & (1 << 7), 128)      

    def test_tsx_processorStatusBit7ShouldBeUnSet(self):
        self.s = 0x100
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

    def test_iny_processorStautsBit0ShouldBeUnset(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 0), 0)

    def test_iny_processorStatusBit1ShouldBeSet(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 1), 2)

    def test_iny_processorStatusBit1ShouldBeUnset(self):
        self.cpu.y = 1
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_iny_processorStatusBit1ShouldBeSetAfterLoopRound(self):
        self.cpu.y = 255
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 1), 1)

    def test_iny_processorStatusBit2ShouldBeUnset(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 2), 0)

    def test_iny_processorStatusBit3ShouldBeUnset(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 3), 0)

    def test_iny_processorStatusBit4ShouldBeUnset(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 4), 0)

    def test_iny_processorStatusBit5ShouldBeUnset(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 5), 0)

    def test_iny_processorStatusBit6ShouldBeUnset(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 6), 0)

    def test_iny_processorStatusBit7ShouldBeUnset(self):
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 7), 0)

    def test_iny_processorStatusBit7ShouldBeSet(self):
        self.cpu.x = 254
        self.cpu.iny()
        self.assertEqual(self.cpu.p & (1 << 7), 128)

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

    def test_dex_processorStautsBit0ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 0), 0)

    def test_dex_processorStatusBit1ShouldBeSet(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 1), 2)

    def test_dex_processorStatusBit1ShouldBeUnset(self):
        self.cpu.x = 2
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_dex_processorStatusBit1ShouldBeUnsetAfterLoopRound(self):
        self.cpu.x = 0
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_dex_processorStatusBit2ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 2), 0)

    def test_dex_processorStatusBit3ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 3), 0)

    def test_dex_processorStatusBit4ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 4), 0)

    def test_dex_processorStatusBit5ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 5), 0)

    def test_dex_processorStatusBit6ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 6), 0)

    def test_dex_processorStatusBit7ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 7), 0)

    def test_dex_processorStatusBit7ShouldBeSet(self):
        self.cpu.x = 0
        self.cpu.dex()
        self.assertEqual(self.cpu.p & (1 << 7), 128)

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

    def test_dey_processorStautsBit0ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 0), 0)

    def test_dey_processorStatusBit1ShouldBeSet(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 1), 2)

    def test_dey_processorStatusBit1ShouldBeUnset(self):
        self.cpu.y = 2
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_dey_processorStatusBit1ShouldBeUnsetAfterLoopRound(self):
        self.cpu.y = 0
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 1), 0)

    def test_dey_processorStatusBit2ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 2), 0)

    def test_dey_processorStatusBit3ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 3), 0)

    def test_dey_processorStatusBit4ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 4), 0)

    def test_dey_processorStatusBit5ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 5), 0)

    def test_dey_processorStatusBit6ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 6), 0)

    def test_dey_processorStatusBit7ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 7), 0)

    def test_dex_processorStatusBit7ShouldBeSet(self):
        self.cpu.y = 0
        self.cpu.dey()
        self.assertEqual(self.cpu.p & (1 << 7), 128)

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

if __name__=="__main__":
    unittest.main()
