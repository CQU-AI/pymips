from ..Hardware.Memory import Memory
from ..Hardware.Registers import Registers
from ..misc.RegData import RegData


def lw_(rt, add, rs):
    dw = Memory.get_dw(Registers.reg_get(rs) + add)
    Registers.reg_set(rt, dw)


def sw_(rt, add, rs):
    dw = Registers.reg_get(rt)
    Memory.set_dw(Registers.reg_get(rs) + add, dw)


def add_(rd, rs, rt):
    res = Registers.reg_get(rt) + Registers.reg_get(rs)
    Registers.reg_set(rd, res)


def addi_(rt, rs, imme):
    res = Registers.reg_get(rs) + int(imme)
    Registers.reg_set(rt, res)


def and_(rd, rs, rt):
    res = Registers.reg_get(rt) & Registers.reg_get(rs)
    Registers.reg_set(rd, res)


def beq_(rt, rs, LABEL):
    return LABEL if Registers.reg_get(rt) == Registers.reg_get(rs) else None


def j_(LABEL):
    return LABEL


def or_(rd, rs, rt):
    res = Registers.reg_get(rt) | Registers.reg_get(rs)
    Registers.reg_set(rd, res)


def sub_(rd, rs, rt):
    res = Registers.reg_get(rt) - Registers.reg_get(rs)
    Registers.reg_set(rd, res)


def sll_(rt, rs, imme):
    res = Registers.reg_get(rs) << int(imme)
    Registers.reg_set(rt, res)


def slt_(rd, rs, rt):
    Registers.reg_set(rd, RegData(Registers.reg_get(rs) < Registers.reg_get(rt)))


def slti_(rt, rs, imme):
    Registers.reg_set(rt, RegData(Registers.reg_get(rs) < int(imme)))


def srl_(rt, rs, imme):
    res = Registers.reg_get(rs) >> int(imme)
    Registers.reg_set(rt, res)


# TODO: many more instructions
