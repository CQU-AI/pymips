from Assemble.Preprocessor import Preprocessor
from Simulate.Interpreter import Interpreter


class Simulator(Interpreter):
    def __init__(self):
        raise SyntaxError("Simulate can not be instantiate. Please use static method.")

    @classmethod
    def run_file(cls, path):
        with open(path, "r") as f:
            insts = f.read()
        cls.hist_inst, cls.label = Preprocessor.prep(insts, return_label=True)
        while cls.curr_inst <= len(cls.hist_inst):
            cls.run_line(cls.hist_inst[cls.curr_inst])

if __name__ == '__main__':
    Simulator.run_file("../drings.txt")