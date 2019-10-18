from misc.RegData import RegData


class Memory:
    """
    Sparse memory in singleton mode
    """

    __space = {}
    __max_size = 2 ** 32

    def __init__(self):
        raise SyntaxError("Memory can not instance, please use class method")

    @classmethod
    def clear(cls):
        cls.__space = {}

    @classmethod
    def set_dw(cls, add, value):
        if not (isinstance(add, RegData) and isinstance(value, RegData)):
            raise TypeError("Memory.set_dw only support RegData")
        if add > 2 * 32:
            raise OverflowError("Memory overflow with address:{}".format(add.bin))
        elif value > 2 ** 32:
            raise OverflowError("Word overflow with value:{}".format(value.bin))
        else:
            cls.__space[add.resize(32)] = value.resize(32)

    @classmethod
    def get_dw(cls, add):
        if not isinstance(add, RegData):
            raise TypeError("Memory.get_dw only support RegData")
        if add > 2 * 32:
            raise OverflowError("Memory overflow with address:{}".format(add.bin))
        elif add.hash not in cls.__space.keys():
            raise ValueError("Unable to access Address:{}".format(add.bin))
        return cls.__space[add.hash]

    @classmethod
    def save_buffer(cls, add, buffer):
        if not (isinstance(add, RegData) and isinstance(buffer, RegData)):
            raise TypeError("Memory.save_buffer only support RegData")
        if add + len(buffer.bin) > 2 ** 32:
            raise OverflowError(
                "Memory overflow with address:{}".format(add + len(buffer.bin))
            )
        dw_list = buffer.split([i * 32 for i in range(len(buffer.bin) // 32)])
        for dw in dw_list:
            cls.set_dw(add, dw)
            add += 4

    @classmethod
    def load_buffer(cls, add, dw_size):
        if not (isinstance(add, RegData)):
            raise TypeError("Memory.load_buffer only support RegData")
        if add + dw_size * 4 > 2 ** 32:
            raise OverflowError(
                "Memory overflow with address:{}".format(add + dw_size * 4)
            )
        buffer = ""
        for i in range(dw_size):
            buffer += cls.get_dw(add).bin
            add += 4
        return buffer
