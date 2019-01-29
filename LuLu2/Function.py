from LuLu2.Symbol import Symbol
from LuLu2.SymbolEnum import SymbolEnum


class Function(Symbol):

    def __init__(self, key: str, line: int, column: int, input, output, is_defined: bool, width: int):
        super().__init__(key, line, column, is_defined)
        self._output_ = output
        self._input_ = input
        self._width_: int = width

    @property
    def output(self):
        return self._output_

    @property
    def input(self):
        return self._input_
