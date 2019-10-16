# python3
# -*- coding: utf-8 -*-
# @File    : Assembler.py
# @Desc    :
# @Project : MIPSAssembler
# @Time    : 10/16/19 8:14 PM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)

from tools.RegData import RegData
from tools import static


class Assembler:
    @staticmethod
    def decode(instrcutions):
        machine_code = RegData(None)
        for inst in instrcutions.split("\n"):
            inst = list(
                filter(
                    lambda x: x != "",
                    inst.replace(",", " ")
                    .replace("(", " ")
                    .replace(")", "")
                    .split(" "),
                )
            )
            if inst[0] in static.R_inst_to_index.keys():
                machine_code = machine_code.concat(Assembler.r_decode(inst))
            elif inst[0] in static.I_inst_to_index.keys():
                machine_code = machine_code.concat(Assembler.i_decode(inst))
            elif inst[0] in static.J_inst_to_index.keys():
                machine_code = machine_code.concat(Assembler.j_decode(inst))
            else:
                raise ValueError("Unknown mips instruction:{}".format(inst[0]))
        return machine_code

    @staticmethod
    def r_decode(instruction_list):
        """
        R-type instruction decoder
        :param instruction_list: one inst
        :return: RegData
        """
        try:
            # TODO: if op/rs not in keys(),throw error
            if len(instruction_list) == 4:
                op = RegData("0b000000")
                rs = static.reg_to_index[instruction_list[2]]
                rt = static.reg_to_index[instruction_list[3]]
                rd = static.reg_to_index[instruction_list[1]]
                shamt = RegData("0b00000")
                funct = static.R_inst_to_index[instruction_list[0]]

                return RegData.concat_list([op, rs, rt, rd, shamt, funct])
            else:
                op = RegData("0b000000")
                rs = static.reg_to_index[instruction_list[1]]
                rt = RegData("0b00000")
                rd = RegData("0b00000")
                shamt = RegData("0b00000")
                funct = static.R_inst_to_index[instruction_list[0]]

                return RegData.concat_list([op, rs, rt, rd, shamt, funct])
        except Exception as e:
            raise ValueError(
                'Unable to decode r_instruction:"{}",{}'.format(instruction_list, e)
            )

    @staticmethod
    def i_decode(instruction_list):
        """
        R-type instruction decoder
        :param instruction_list: one inst
        :return: RegData
        """

        try:
            # TODO: jump to inst unsupported
            if instruction_list[-1][0] == "$":
                op = static.I_inst_to_index[instruction_list[0]]
                rs = static.reg_to_index[instruction_list[3]]
                rt = static.reg_to_index[instruction_list[1]]
                add = RegData(instruction_list[2], 16)

                return RegData.concat_list([op, rs, rt, add])
            else:
                op = static.I_inst_to_index[instruction_list[0]]
                rs = static.reg_to_index[instruction_list[2]]
                rt = static.reg_to_index[instruction_list[1]]
                add = RegData(instruction_list[3], 16)

                return RegData.concat_list([op, rs, rt, add])
        except Exception as e:
            raise ValueError(
                'Unable to decode i_instruction:"{}",{}'.format(instruction_list, e)
            )

    @staticmethod
    def j_decode(instruction_list):
        """
        R-type instruction decoder
        :param instruction_list: one inst
        :return: RegData
        """
        # TODO: jump to label unsupported
        try:
            op = static.J_inst_to_index[instruction_list[0]]
            address = RegData(instruction_list[1], 26)
            return RegData.concat_list([op, address])

        except Exception as e:
            raise ValueError(
                'Unable to decode j_instruction:"{}",{}'.format(instruction_list, e)
            )


if __name__ == "__main__":
    inst = "j 10000\nadd $s0,$a1,$t7\nsw $s1,10($s2)"
    print(Assembler.decode(inst).bin, Assembler.decode(inst).value_base(16))
