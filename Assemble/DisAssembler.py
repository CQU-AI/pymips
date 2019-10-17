# python3
# -*- coding: utf-8 -*-
# @File    : DisAssembler.py
# @Desc    :
# @Project : MIPSAssembler
# @Time    : 10/17/19 10:55 AM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)

from misc.RegData import RegData
from misc import static


class DisAssembler:
    def __init__(self):
        raise SyntaxError("DisAssembler can not instance, please use static method")

    @staticmethod
    def decode(codes):
        instructions = ""
        codes = RegData(codes).bin

        while len(codes) >= 32:
            code = RegData("0b" + codes[:32], 32)
            codes = codes[32:]
            if code.bin[:6] == "000000":
                instructions += DisAssembler.r_decode(code) + "\n"
            elif RegData("0b" + code.bin[:6]).hash in static.I_index_to_inst.keys():
                instructions += DisAssembler.i_decode(code) + "\n"
            elif RegData("0b" + code.bin[:6]).hash in static.J_index_to_inst.keys():
                instructions += DisAssembler.j_decode(code) + "\n"
            else:
                raise ValueError("Unknown machiche code:{}".format(code.bin))
        return instructions

    @staticmethod
    def r_decode(code):
        op, rs, rt, rd, shamt, funct = code.split([6, 11, 16, 21, 26, 32])
        if rt == 0 and rd == 0:
            inst = "{} {}".format(
                static.R_index_to_inst[funct.hash], static.index_to_reg[rs.hash]
            )
        else:
            inst = "{} {}, {}, {}".format(
                static.R_index_to_inst[funct.hash],
                static.index_to_reg[rd.hash],
                static.index_to_reg[rs.hash],
                static.index_to_reg[rt.hash],
            )
        return inst

    @staticmethod
    def i_decode(code):
        op, rs, rt, add = code.split([6, 11, 16, 32])
        if static.I_index_to_inst[op.hash] in ["lw", "sw"]:
            inst = "{} {}, {}({})".format(
                static.I_index_to_inst[op.hash],
                static.index_to_reg[rt.hash],
                add.value_base(10),
                static.index_to_reg[rs.hash],
            )
        else:
            inst = "{} {}, {}, {}".format(
                static.I_index_to_inst[op.hash],
                static.index_to_reg[rt.hash],
                static.index_to_reg[rs.hash],
                static.index_to_reg[add.hash],
            )
        return inst

    @staticmethod
    def j_decode(code):
        op, addr = code.split([6, 32])
        inst = "{} {}".format(static.J_index_to_inst[op.hash], addr.value_base(10))
        return inst


if __name__ == "__main__":
    print(DisAssembler.decode("0x0800271000af8020ae51000a"))
