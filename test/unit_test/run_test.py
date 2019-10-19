import unittest
from fengyong import Assembler
from fengyong import DisAssembler
from fengyong import Simulator
from fengyong import Registers


class MyTestCase(unittest.TestCase):
    def test_assemble(self):
        instructions = "j 10000\nadd $s0, $a1, $t7\nsw $s1, 10($s2)\n"
        machine_code = Assembler.encode(instructions)

        self.assertEqual("0x0800271000af8020ae51000a", machine_code.value_base(16))
        self.assertEqual(instructions, DisAssembler.decode(machine_code))

    def test_simulate(self):
        path = "../sample1/sample1.asm"
        Simulator.run_file(path)
        self.assertEqual(Registers.reg_get("$s0"), 468968)


if __name__ == "__main__":
    unittest.main()
