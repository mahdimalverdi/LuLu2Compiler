from typing import List, Tuple, Dict

from LuLu2.ErrorManager import errorManager
from LuLu2.Function import Function
from LuLu2.Operators import operators
from LuLu2.Variable import Variable
from LuLu2.Type import Type


class Scope:
    def __init__(self, start_line: int, start_column: int, parent=None, keywords: List[str] = []):
        self.__children__: List[Scope] = []
        self.__start_line__: int = start_line
        self.__start_column__: int = start_column
        self._parent_: Scope = parent
        self.__keywords__: set[str] = set()
        self.__variables__: Dict[str, Variable] = {}
        self.__functions__: Dict[str, Dict[str, Function]] = {}
        self.__types__: Dict[str, Type] = {}

        for keyword in keywords:
            self.__keywords__.add(keyword)

        if parent is None:
            int_type = Type("int", 0, 0, 4, True, operators.get_int_operators(), ["int", "bool", "float", "string"])
            self.__types__.setdefault("int", int_type)

            bool_type = Type("bool", 0, 0, 1, True, operators.get_bool_operators(), ["bool", "int", "float", "string"])
            self.__types__.setdefault("bool", bool_type)

            float_type = Type("float", 0, 0, 1, True, operators.get_float_operators(), ["float"])
            self.__types__.setdefault("float", float_type)

            string_type = Type("string", 0, 0, 4, True, operators.get_string_operators(), ["string"])
            self.__types__.setdefault("string", string_type)

            NoneType_type = Type("NoneType", 0, 0, 0, True, {}, [])
            self.__types__.setdefault("NoneType", NoneType_type)

            self.insert_function("read", 0, 0, "int", [], True, 0)
            self.insert_function("read", 0, 0, "bool", [], True, 0)
            self.insert_function("read", 0, 0, "float", [], True, 0)
            self.insert_function("read", 0, 0, "string", [], True, 0)

            self.insert_function("write", 0, 0, "int", [], True, 0)
            self.insert_function("write", 0, 0, "bool", [], True, 0)
            self.insert_function("write", 0, 0, "float", [], True, 0)
            self.insert_function("write", 0, 0, "string", [], True, 0)
    @property
    def start_line(self):
        return self.__start_line__

    @property
    def start_column(self):
        return self.__start_column__

    @property
    def variables(self):
        return self.__variables__

    @property
    def functions(self):
        return self.__functions__

    @property
    def children(self):
        return self.__children__

    @property
    def types(self):
        return self.__types__

    def is_valid_variable_name(self, key: str, is_local: bool = True):
        if is_local is True:
            tmp = self.__variables__.get(key)
            if self.__variables__.get(key) is not None:
                return tmp

        if key in self.__keywords__:
            return key

        tmp = self.__functions__.get(key)
        if tmp is not None:
            return next(iter(tmp.values()))

        tmp = self.__types__.get(key)
        if tmp is not None:
            return tmp

        if is_local is True:
            parent = self._parent_
            while parent is not None:
                tmp = parent.is_valid_variable_name(key, False)
                if tmp is not True:
                    return tmp
                parent = parent._parent_

        return True

    def is_valid_function_name(self, key: str, input: str, is_defined: bool, is_local: bool = True):
        if is_local is True:
            tmp = self.__variables__.get(key)
            if self.__variables__.get(key) is not None:
                return tmp

            tmp = self.__functions__.get(key)
            if tmp is not None:
                t = tmp.get(input)
                if t is not None:
                    if t.is_defined is is_defined:
                        return tmp.get(input)

        if key in self.__keywords__:
            return key

        tmp = self.__types__.get(key)
        if tmp is not None:
            return tmp

        if is_local is True:
            parent = self._parent_
            while parent is not None:
                tmp = parent.is_valid_function_name(key, input, is_defined, False)
                if tmp is not True:
                    return tmp
                parent = parent._parent_

        return True

    def is_valid_type_name(self, key: str, is_defined: bool, is_local: bool = True):

        if is_local is True:
            parent = self._parent_
            if parent is not None:
                while parent._parent_ is not None:
                    parent = parent._parent_
                return parent.is_valid_type_name(key, is_defined, False)

        if key in self.__keywords__:
            return key

        tmp = self.__variables__.get(key)
        if tmp is not None:
            return tmp

        tmp = self.__functions__.get(key)
        if tmp is not None:
            return next(iter(tmp.values()))

        tmp = self.__types__.get(key)
        if tmp is not None:
            if tmp.is_defined is is_defined:
                return tmp

        for child in self.__children__:
            tmp = child.is_valid_type_name(key, is_defined, False)
            if tmp is not True:
                return tmp

        return True

    def insert_scope(self, start_line: int, start_column: int):
        self.__children__.append(Scope(start_line, start_column, self))
        inserted = self.__children__[len(self.__children__) - 1]
        return inserted

    def insert_variable(self, key: str, line: int, column: int, type_: str):
        tmp = self.is_valid_variable_name(key)
        if tmp is not True:
            errorManager.print_error(line, column, "Identifier \"" + key + "\" is duplicated!")

            if not isinstance(tmp, Type):
                errorManager.print_error(tmp.line, tmp.column, "Identifier \"" + key + "\" is duplicated!")
        self.__variables__.setdefault(key, Variable(key, line, column, type_))

    def insert_variable_without_check(self, key: str, line: int, column: int, type_: str):
        self.__variables__.setdefault(key, Variable(key, line, column, type_))

    def get_variable(self, key: str, line: int, column: int):
        tmp = self.__variables__.get(key)

        if tmp is not None:
            if line > tmp.line:
                return tmp
            elif line is tmp.line and column >= tmp.column:
                return tmp
            tmp = None

        if tmp is None and self._parent_ is not None:
            return self._parent_.get_variable(key, line, column)

        if tmp is None:
            errorManager.print_error(line, column, "Identifier \"" + key + "\" is not defined!")
        return tmp

    def get_local_variable(self, key: str, line: int, column: int):
        tmp = self.__variables__.get(key)

        if tmp is None:
            errorManager.print_error(line, column, "Identifier \"" + key + "\" is not defined!")
        return tmp

    def insert_function(self, key: str, line: int, column: int, input: str, output: str, is_defined: bool, width: int):
        tmp = self.is_valid_function_name(key, input, is_defined)
        if tmp is not True:
            errorManager.print_error(line, column, "Identifier \"" + key + "(" + input + ")" + "\" is duplicated!")

            if isinstance(tmp, Function):
                errorManager.print_error(tmp.line, tmp.column, "Identifier \"" + tmp.key + "(" + tmp.input + ")" +
                                         "\" is duplicated!")
            elif not isinstance(tmp, Type):
                errorManager.print_error(tmp.line, tmp.column, "Identifier \"" + key + "\" is duplicated!")

        if self.__functions__.get(key) is None:
            self.__functions__.setdefault(key, {str(input): Function(key, line, column, input, output, is_defined, width)})
        else:
            self.__functions__.get(key).setdefault(str(input), Function(key, line, column, input, output, is_defined, width))

    def get_function(self, key: str, input, line: int, column: int):
        fun = self.__functions__.get(key)
        tmp = None
        if fun is not None:
            for key1 in fun:
                if is_convert_to(fun[key1].input, input, line, column) is True:
                    if line > fun[key1].line:
                        return fun[key1]
                    elif line is fun[key1].line and column >=  fun[key1].column:
                        return fun[key1]

        if tmp is None and self._parent_ is not None:
            return self._parent_.get_function(key, input, line, column)

        if tmp is None:
            errorManager.print_error(line, column, "Identifier \"" + "{0}({1})".format(key,input) + "\" is not defined!")
        return tmp

    def insert_type(self, key: str, line: int, column: int, width: int, is_defined: bool, parent: Type = None):
        tmp = self.is_valid_type_name(key, is_defined)
        if tmp is not True:
            errorManager.print_error(line, column, "Identifier \"" + key + "\" is duplicated!")

            if not isinstance(tmp, Type):
                errorManager.print_error(tmp.line, tmp.column, "Identifier \"" + key + "\" is duplicated!")

        tmp = Type(key, line, column, width, is_defined, parent)
        self.__types__.setdefault(key, tmp)

    def get_type(self, key: str, line: int, column: int, is_defined: bool = False):
        tmp = self.__types__.get(key)

        if (tmp is None or tmp.is_defined is is_defined)and self._parent_ is not None :
            return self._parent_.get_type(key, line, column)

        if tmp is None:
            errorManager.print_error(line, column, "Identifier \"" + key + "\" is not declared!")
        return tmp

    def get_define_type(self, key: str, line: int, column: int):
        tmp = self.get_type(key , line, column)
        if tmp is not None:
            tmp = self.get_type(key, line, column, True)
            if tmp is None:
                errorManager.print_error(line, column, "Identifier \"" + key + "\" is not defined!")
            return tmp
        return tmp

    def is_defined_type(self, key: str):
        tmp = self.__types__.get(key)

        if tmp is None and self._parent_ is not None:
            return self._parent_.is_defined_type(key)

        if tmp is None:
            return False
        return True

    def get_current_scope(self,line:int , column:int):
        if self.__start_line__ is line and self.__start_column__ is column:
            return self
        for item in self.__children__:
            current_scope = item.get_current_scope(line, column)
            if current_scope is not None:
                return current_scope

        return None

    def print_all_children(self):
        print(self.start_line,self.start_column)
        for item in self.__children__:
            item.print_all_children()

keywords = ["allocate", "break", "case", "const", "continue", "declare", "default", "destruct", "else", "false",
            "function", "for", "if", "nil", "of", "private", "protected", "public", "return", "super",
            "switch", "this", "true", "type", "while"]

global_scope : Scope = Scope(0, 0, keywords=keywords)

def is_convert_to(type1, type2, line: int, column: int):
    if isinstance(type2, str):
        if isinstance(type1, str):
            tmp = global_scope.get_type(type2, line, column).is_convert_to(type1, line, column)
            if tmp is not None:
                return True

    if isinstance(type2, list):
        if isinstance(type1, list):
            if len(type2) is len(type1):
                for i in range(0, len(type2)):
                    tmp = global_scope.get_type(type2[i], line, column).is_convert_to(type1[i], line, column)
                    if tmp is not None:
                        return True

    if isinstance(type2, str):
        if isinstance(type1, list) and len(type1) is 1:
            tmp = global_scope.get_type(type2, line, column).is_convert_to(type1[0], line, column)
            if tmp is not None:
                return True

    if isinstance(type2, list) and len(type2) is 1:
        if isinstance(type1, str):
            tmp = global_scope.get_type(type2[0], line, column).is_convert_to(type1, line, column)
            if tmp is not None:
                return True
    return False

def convert_to(type1, type2, line: int, column: int):
    if is_convert_to(type1,type2,line,column) is False:
        errorManager.print_error(line, column,
                             "\"{0}\" can not convert to \"{1}\"".format(type2, type1))