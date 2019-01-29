from LuLu2.ErrorManager import errorManager
from LuLu2.Symbol import Symbol
from LuLu2.SymbolEnum import SymbolEnum


class Type(Symbol):

    def __init__(self, key: str, line: int, column: int, width: int, is_defined: bool, operators= {}, other_types= [], parent=None):
        super().__init__(key, line, column, is_defined)
        self._parent_: Type = parent
        self._width_: int = width
        self._operators_ : dict[str, str] = operators
        self._other_types_ : list[str] = other_types

    @property
    def width(self):
        return self._width_

    def get_output_type(self, type1: str, type2: str, operator: str, line:int , column:int, global_scope):
        text = "{0}{1}{2}".format(type1, operator, type2)
        t = self._operators_.get(text)

        t1 = global_scope.get_type(type1, line, column)
        t2 = global_scope.get_type(type2, line, column)

        if t is None:
            for item1 in t1.other_types:
                for item2 in t2.other_types:
                    text = "{0}{1}{2}".format(item1, operator, item2)
                    t = global_scope.get_type(item1,line,column)._operators_.get(text)
                    if t is not None:
                        break

                if t is not None:
                    break

        if t is None:
            errorManager.print_error(line, column, "The operator " + "{0}{1}{2}".format(type1, operator, type2) + " is not defined")
            return "NoneType"

        return t

    @property
    def other_types(self):
        return self._other_types_

    def is_convert_to(self, name:str, line:int , column:int):
        for item in self.other_types:
            if item == name:
                return True

        # errorManager.print_error(line, column,
        #                          "\"{0}\" can not convert to \"{1}\"".format(name,self.key) )
        return False


