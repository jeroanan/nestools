import unittest
import NesCpu

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
        self.assertEqual(self.cpu.p & 0x0, 0)

    def test_dex_processorStatusBit1ShouldBeSet(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x2, 2)

    def test_dex_processorStatusBit1ShouldBeUnset(self):
        self.cpu.x = 2
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x2, 0)

    def test_dex_processorStatusBit1ShouldBeUnsetAfterLoopRound(self):
        self.cpu.x = 0
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x2, 0)

    def test_dex_processorStatusBit2ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x4, 0)

    def test_dex_processorStatusBit3ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x8, 0)

    def test_dex_processorStatusBit4ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x16, 0)

    def test_dex_processorStatusBit5ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x32, 0)

    def test_dex_processorStatusBit6ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x64, 0)

    def test_dex_processorStatusBit7ShouldBeUnset(self):
        self.cpu.dex()
        self.assertEqual(self.cpu.p & 0x128, 0)

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
        self.assertEqual(self.cpu.p & 0x0, 0)

    def test_dey_processorStatusBit1ShouldBeSet(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x2, 2)

    def test_dey_processorStatusBit1ShouldBeUnset(self):
        self.cpu.y = 2
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x2, 0)

    def test_dey_processorStatusBit1ShouldBeUnsetAfterLoopRound(self):
        self.cpu.y = 0
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x2, 0)

    def test_dey_processorStatusBit2ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x4, 0)

    def test_dey_processorStatusBit3ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x8, 0)

    def test_dey_processorStatusBit4ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x16, 0)

    def test_dey_processorStatusBit5ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x32, 0)

    def test_dey_processorStatusBit6ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x64, 0)

    def test_dey_processorStatusBit7ShouldBeUnset(self):
        self.cpu.dey()
        self.assertEqual(self.cpu.p & 0x128, 0)

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
        self.assertEqual(self.cpu.p & 0x0, 0x0)

if __name__=="__main__":
    unittest.main()
