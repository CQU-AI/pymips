from misc.RegData import RegData


def reverse_dict(d):
    return {v: k for k, v in d.items()}


index_to_reg = {
    RegData(0, 5): "$0",  # 0
    RegData(1, 5): "$at",  # 由编译器生成的复合指令使用
    RegData(2, 5): "$v0",  # 计算结果和表达式求值
    RegData(3, 5): "$v1",
    RegData(4, 5): "$a0",  # 参数
    RegData(5, 5): "$a1",
    RegData(6, 5): "$a2",
    RegData(7, 5): "$a3",
    RegData(8, 5): "$t0",  # 临时变量
    RegData(9, 5): "$t1",
    RegData(10, 5): "$t2",
    RegData(11, 5): "$t3",
    RegData(12, 5): "$t4",
    RegData(13, 5): "$t5",
    RegData(14, 5): "$t6",
    RegData(15, 5): "$t7",
    RegData(16, 5): "$s0",  # 保留寄存器
    RegData(17, 5): "$s1",
    RegData(18, 5): "$s2",
    RegData(19, 5): "$s3",
    RegData(20, 5): "$s4",
    RegData(21, 5): "$s5",
    RegData(22, 5): "$s6",
    RegData(23, 5): "$s7",  # 更多临时变量
    RegData(24, 5): "$t8",
    RegData(25, 5): "$t9",
    RegData(28, 5): "$gp",  # 全局指针
    RegData(29, 5): "$sp",  # 栈指针
    RegData(30, 5): "$fp",  # 帧指针
    RegData(31, 5): "$ra",  # 返回地址
}

reg_to_index = reverse_dict(index_to_reg)

R_index_to_inst = {
    RegData("0b100000"): "add",
    RegData("0b100010"): "sub",
    RegData("0b100100"): "and",
    RegData("0b100101"): "or",
    RegData("0b100111"): "nor",
    RegData("0b101010"): "slt",
    RegData("0b101011"): "sltu",
    RegData("0b000000"): "sll",
    RegData("0b000010"): "srl",
    RegData("0b001000"): "jr",
}

R_inst_to_index = reverse_dict(R_index_to_inst)

I_index_to_inst = {
    RegData("0b001000"): "addi",
    RegData("0b100011"): "lw",
    RegData("0b101011"): "sw",
    RegData("0b000100"): "beq",
    RegData("0b000101"): "bne",
    RegData("0b001010"): "slti",
    RegData("0b001011"): "sltiu",
}

I_inst_to_index = reverse_dict(I_index_to_inst)

J_index_to_inst = {RegData("0b000010"): "j", RegData("0b000011"): "jal"}

J_inst_to_index = reverse_dict(J_index_to_inst)
