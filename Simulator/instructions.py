# python3
# -*- coding: utf-8 -*-
# @File    : instructions.py
# @Desc    :
# @Project : MIPSAssembler
# @Time    : 10/17/19 6:48 PM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)

from Hardware.Memory import Memory
from Hardware.Registers import Registers


def lw(rt,add,rs):
    dw = Memory.get_dw(Registers.reg_get(rs) + add)
    Registers.reg_set(rt, dw)


def sw(rs, add, rt):
    dw = Registers.reg_get(rs)
    Memory.set_dw(Registers.reg_get(rt) + add, dw)


def add(rt, rs, rd):
    res = Registers.reg_get(rd) + Registers.reg_get(rs)
    Registers.reg_set(rt, res)


def sub(rt, rs, rd):
    res = Registers.reg_get(rd) - Registers.reg_get(rs)
    Registers.reg_set(rt, res)

# TODO: many more instructions
