# python3
# -*- coding: utf-8 -*-
# @File    : sample1.py
# @Desc    :
# @Project : MIPSAssembler
# @Time    : 10/18/19 9:56 PM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)


# Let A=-1.278*10^3, B=-3.90625*10^-1, the two numbers store in 16-digit NVIDIA mode. \
# Assume that the Storage mode contains guard,round and sticky bit, and round to nearest even. \
# Load A,B to registers in 16-digit NVIDIA mode and calculate the sum of A and B.


################################################################
# import
from Assemble.Assembler import Assembler
from Assemble.DisAssembler import DisAssembler

from Simulate.Simulator import Simulator
from Hardware.Registers import Registers

path = "./sample1.asm"
################################################################
# Assemble & DisAssemble
with open(path, "r") as f:
    asm = f.read()

machine_code = Assembler.encode(asm)

with open("code_" + path, "w") as f:
    f.write(machine_code.bin)

instructions = DisAssembler.decode(machine_code)

with open("check_" + path, "w") as f:
    f.write(instructions)

################################################################
# Simulate
Simulator.run_file("./sample1.asm")
Registers.print()
