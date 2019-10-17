# python3
# -*- coding: utf-8 -*-
# @File    : Registers.py
# @Desc    :
# @Project : MIPSAssembler
# @Time    : 10/17/19 6:47 PM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)

from misc.RegData import RegData


class Registers:
    """
    Registers in singleton mode
    """
    __data = {
        "$0": RegData("0", 32),  # 0
        "$at": RegData("0", 32),  # 由编译器生成的复合指令使用
        "$v0": RegData("0", 32),  # 计算结果和表达式求值
        "$v1": RegData("0", 32),
        "$a0": RegData("0", 32),  # 参数
        "$a1": RegData("0", 32),
        "$a2": RegData("0", 32),
        "$a3": RegData("0", 32),
        "$t0": RegData("0", 32),  # 临时变量
        "$t1": RegData("0", 32),
        "$t2": RegData("0", 32),
        "$t3": RegData("0", 32),
        "$t4": RegData("0", 32),
        "$t5": RegData("0", 32),
        "$t6": RegData("0", 32),
        "$t7": RegData("0", 32),
        "$s0": RegData("0", 32),  # 保留寄存器
        "$s1": RegData("0", 32),
        "$s2": RegData("0", 32),
        "$s3": RegData("0", 32),
        "$s4": RegData("0", 32),
        "$s5": RegData("0", 32),
        "$s6": RegData("0", 32),
        "$s7": RegData("0", 32),  # 更多临时变量
        "$t8": RegData("0", 32),
        "$t9": RegData("0", 32),
        "$gp": RegData("0", 32),  # 全局指针
        "$sp": RegData("0", 32),  # 栈指针
        "$fp": RegData("0", 32),  # 帧指针
        "$ra": RegData("0", 32),  # 返回地址
    }

    def __init__(self):
        raise SyntaxError("Register can not instance, please use class method")

    @classmethod
    def reg_set(cls, reg_name, value):
        if reg_name not in cls.__data.keys():
            raise ValueError("Unknown register:{}".format(reg_name))
        elif not isinstance(value, RegData):
            raise TypeError(
                "Register can only save RegData, got {} instead.".format(type(value))
            )
        elif value.bin_length > 32:
            raise OverflowError("32-bit Register can't hold data:{}".format(value.bin))
        else:
            cls.__data[reg_name] = value

    @classmethod
    def reg_get(cls, reg_name):
        if reg_name not in cls.__data.keys():
            raise ValueError("Unknown register:{}".format(reg_name))
        else:
            return cls.__data[reg_name]

    @classmethod
    def clear(cls):
        cls.__data = {
            "$0": RegData("0", 32),  # 0
            "$at": RegData("0", 32),  # 由编译器生成的复合指令使用
            "$v0": RegData("0", 32),  # 计算结果和表达式求值
            "$v1": RegData("0", 32),
            "$a0": RegData("0", 32),  # 参数
            "$a1": RegData("0", 32),
            "$a2": RegData("0", 32),
            "$a3": RegData("0", 32),
            "$t0": RegData("0", 32),  # 临时变量
            "$t1": RegData("0", 32),
            "$t2": RegData("0", 32),
            "$t3": RegData("0", 32),
            "$t4": RegData("0", 32),
            "$t5": RegData("0", 32),
            "$t6": RegData("0", 32),
            "$t7": RegData("0", 32),
            "$s0": RegData("0", 32),  # 保留寄存器
            "$s1": RegData("0", 32),
            "$s2": RegData("0", 32),
            "$s3": RegData("0", 32),
            "$s4": RegData("0", 32),
            "$s5": RegData("0", 32),
            "$s6": RegData("0", 32),
            "$s7": RegData("0", 32),  # 更多临时变量
            "$t8": RegData("0", 32),
            "$t9": RegData("0", 32),
            "$gp": RegData("0", 32),  # 全局指针
            "$sp": RegData("0", 32),  # 栈指针
            "$fp": RegData("0", 32),  # 帧指针
            "$ra": RegData("0", 32),  # 返回地址
        }
