from LuLu2.Symbol import Symbol
from LuLu2.SymbolEnum import SymbolEnum
from LuLu2.Type import Type


class Variable(Symbol):

    def __init__(self, key: str, line: int, column: int, type_: str):
        super().__init__(key, line, column)
        self._type_ : str = type_

    @property
    def Type(self):
        return self._type_