# python3
# -*- coding: utf-8 -*-
# @File    : sample1.py
# @Desc    : Let A=-1.278*10^3, B=-3.90625*10^-1, the two numbers store in 16-digit NVIDIA mode. \
#               Assume that the Storage mode contains guard,round and sticky bit, and round to nearest even. \
#               Load A,B to registers in 16-digit NVIDIA mode and calculate the sum of A and B.
# @Project : MIPSAssembler
# @Time    : 10/18/19 9:56 PM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)

################################################################
# import
from Fengyong import Simulator
from Fengyong import Registers

path = "./sample1.asm"

################################################################
# Simulate
Simulator.run_file("./sample1.asm")
Registers.print()

################################################################
# return
# $0 0
# $at 0
# $v0 0
# $v1 0
# $a0 0
# $a1 0
# $a2 0
# $a3 0
# $t0 31
# $t1 25
# $t2 2
# $t3 5
# $t4 0
# $t5 0
# $t6 0
# $t7 0
# $s0 468968
# $s1 468968
# $s2 466947
# $s3 3
# $s4 2024
# $s5 1
# $s6 1
# $s7 2027
# $t8 4095
# $t9 0
# $gp 0
# $sp 0
# $fp 0
# $ra 0
