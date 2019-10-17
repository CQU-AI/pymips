# python3
# -*- coding: utf-8 -*-
# @File    : Preprocessor.py
# @Desc    :
# @Project : MIPSAssembler
# @Time    : 10/17/19 7:58 PM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)

import re


class Preprocessor:
    def __init__(self):
        raise SyntaxError("Preprocessor can not instance, please use static method")

    @staticmethod
    def preprocess(mips_code, return_label=True):

        mips_code = re.sub("#.+?\n", "\n", mips_code)  # remove annotation
        mips_code = re.sub("\n+", "\n", mips_code)  # remove empty line
        mips_code = re.sub(" +", " ", mips_code)  # remove redundant space
        mips_code = re.sub("\n | \n", "\n", mips_code)  # remove space at line_start_end

        inst_list = mips_code.split("\n")

        # deal with jump label
        label = {}
        index = 0
        while True:
            if inst_list[index] == "":
                del inst_list[index]
            elif ":" not in inst_list[index]:
                index += 1
            else:
                this_line = inst_list[index].split(":")
                label[this_line[0]] = index
                if len(this_line) > 1:
                    inst_list[index] = this_line[1]
                else:
                    del inst_list[index]
            if index >= len(inst_list):
                break

        if return_label:
            return inst_list, label
        else:
            return inst_list
