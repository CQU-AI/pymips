from .Preprocessor import Preprocessor
from .Interpreter import Interpreter
from .Memory import Memory
from .Registers import Registers


class Simulator(Interpreter):
    def __init__(self):
        raise SyntaxError("Simulator can not be instantiate. Please use static method.")

    @classmethod
    def run_file(cls, path):
        with open(path, "r") as f:
            insts = f.read()
        cls.hist_inst, cls.label = Preprocessor.prep(insts, return_label=True)
        while cls.curr_inst < len(cls.hist_inst):
            cls.run_line(cls.hist_inst[cls.curr_inst], False)

    # TODO: add shell


if __name__ == "__main__":
    Simulator.run_file("../drings.txt")
    Registers.print("s")
    Registers.print("t")
