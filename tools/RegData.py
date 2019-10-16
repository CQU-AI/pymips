# python3
# -*- coding: utf-8 -*-
# @File    : RegData.py
# @Desc    :
# @Project : MIPSAssembler
# @Time    : 10/16/19 7:19 PM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)

import math


class RegData:
    __data_base = 10

    @classmethod
    def set_base(cls, data_base):
        if data_base in [2, 8, 16, 10]:
            cls.__data_base = data_base
        else:
            raise ValueError("Unsupported data base: {}".format(data_base))

    def __init__(self, value, length=None):
        self.value = value
        self.bin_length = length if length is not None else self.bin_length

    def __repr__(self):
        return str(self.value)

    def __add__(self, other_data):
        if isinstance(other_data, int):
            return RegData(self.value_base() + other_data)
        elif isinstance(other_data, str):
            return RegData(self.value_base() + RegData(other_data).value_base())
        elif isinstance(other_data, RegData):
            return RegData(self.value_base() + other_data.value)
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __sub__(self, other_data):
        if isinstance(other_data, int):
            return RegData(self.value_base() - other_data)
        elif isinstance(other_data, str):
            return RegData(self.value_base() - RegData(other_data).value_base())
        elif isinstance(other_data, RegData):
            return RegData(self.value_base() - other_data.value_base())
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __lt__(self, other_data):
        if isinstance(other_data, int):
            return self.value_base() < other_data
        elif isinstance(other_data, str):
            return self.value_base() < RegData(other_data).value_base()
        elif isinstance(other_data, RegData):
            return self.value_base() < other_data.value
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __gt__(self, other_data):
        if isinstance(other_data, int):
            return self.value_base() > other_data
        elif isinstance(other_data, str):
            return self.value_base() > RegData(other_data).value_base()
        elif isinstance(other_data, RegData):
            return self.value_base() > other_data.value
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __le__(self, other_data):
        if isinstance(other_data, int):
            return self.value_base() <= other_data
        elif isinstance(other_data, str):
            return self.value_base() <= RegData(other_data).value_base()
        elif isinstance(other_data, RegData):
            return self.value_base() <= other_data.value
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __ge__(self, other_data):
        if isinstance(other_data, int):
            return self.value_base() >= other_data
        elif isinstance(other_data, str):
            return self.value_base() >= RegData(other_data).value_base()
        elif isinstance(other_data, RegData):
            return self.value_base() >= other_data.value
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __eq__(self, other_data):
        if isinstance(other_data, int):
            return self.value_base() == other_data
        elif isinstance(other_data, str):
            return self.value_base() == RegData(other_data).value_base()
        elif isinstance(other_data, RegData):
            return self.value_base() == other_data.value
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __ne__(self, other_data):
        if isinstance(other_data, int):
            return self.value_base() != other_data
        elif isinstance(other_data, str):
            return self.value_base() != RegData(other_data).value_base()
        elif isinstance(other_data, RegData):
            return self.value_base() != other_data.value
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __or__(self, other_data):
        if isinstance(other_data, int):
            return RegData(self.value_base() | other_data)
        elif isinstance(other_data, str):
            return RegData(self.value_base() | RegData(other_data).value_base())
        elif isinstance(other_data, RegData):
            return RegData(self.value_base() | other_data.value_base())
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __and__(self, other_data):
        if isinstance(other_data, int):
            return RegData(self.value_base() & other_data)
        elif isinstance(other_data, str):
            return RegData(self.value_base() & RegData(other_data).value_base())
        elif isinstance(other_data, RegData):
            return RegData(self.value_base() & other_data.value_base())
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    def __rshift__(self, n):
        return RegData(self.value_base() >> n)

    def __lshift__(self, n):
        return RegData(self.value_base() << n)

    def __hash__(self):
        return self.value_base().__hash__()

    def concat(self, other_data):
        if self._value is None:
            return other_data
        if isinstance(other_data, int) or isinstance(other_data, str):
            return RegData("0b" + self.bin + RegData(other_data).bin)
        elif isinstance(other_data, RegData):
            return RegData("0b" + self.bin + other_data.bin)
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    @staticmethod
    def concat_list(data_list):
        res = data_list[0]
        for i in data_list[1:]:
            res = res.concat(i)
        return res

    @property
    def value(self):
        return str(self.value_base(RegData.__data_base))

    @value.setter
    def value(self, value):
        if value is None:
            self._value = None
            self.bin_length = None
            return
        try:
            value = str(value)
            if value[:2] == "0x":
                self.bin_length = (len(value) - 2) * 4
                self._value = int(value[2:], 16)
            elif value[:2] == "0b":
                self.bin_length = len(value) - 2
                self._value = int(value[2:], 2)
            elif value[:2] == "0o":
                self.bin_length = (len(value) - 2) * 2
                self._value = int(value[2:], 8)
            else:
                self.bin_length = (len(bin(int(value))) - 2) * 2
                self._value = int(value)
        except Exception as e:
            raise ValueError("Unknown data value: {},{}".format(value, e))

    @property
    def bin(self):
        if self._value is None:
            return None
        return self.value_base(2)[2:]

    def value_base(self, base=10):
        if self._value is None:
            return None
        if base == 2:
            return "0b" + bin(self._value)[2:].zfill(self.bin_length)
        elif base == 8:
            res = "0o" + oct(self._value)[2:].zfill(math.ceil(self.bin_length // 3))
        elif base == 16:
            res = "0x" + hex(self._value)[2:].zfill(math.ceil(self.bin_length // 4))
        elif base == 10:
            return self._value
        else:
            raise ValueError("Unsupported data base: {}".format(base))
        return str(res)
