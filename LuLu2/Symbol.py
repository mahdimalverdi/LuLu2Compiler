from LuLu2.SymbolEnum import SymbolEnum


class Symbol:
    _column_: int
    _line_: int
    _key_: str
    _is_defined_: bool

    def __init__(self, key: str, line: int, column: int, is_defined: bool = True):
        self._key_ = key
        self._line_ = line
        self._column_ = column
        self._is_defined_ = is_defined

    @property
    def key(self):
        return self._key_

    @property
    def line(self):
        return self._line_

    @property
    def column(self):
        return self._column_

    @property
    def is_defined(self):
        return self._is_defined_
