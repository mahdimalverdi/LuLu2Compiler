from typing import List

from LuLu2.SymbolEnum import *
from LuLu2.Symbol import *
from LuLu2.Variable import *
from LuLu2.Type import *


class SymbolTable:

    def __init__(self) -> None:
        self._heads_: List[List[Symbol]] = []

        for i in range(0, 1000):
            self._heads_.insert([])

    def set_global_scope(self):
        self.__type_table__ = {"bool": Type("bool", None, 1), "int": Type("int", None, 4),
                               "float": Type("float", None, 8),
                               "string": Type("string", None, 2)}

        keywords = ["allocate", "break", "case", "const", "continue", "declare", "default", "destruct", "else",
                    "false", "function", "for", "if", "nil", "of", "private", "protected", "public",
                    "read", "return", "super", "switch", "this", "true", "type", "while", "write"]

        for item in keywords:
            self.insert(item, SymbolEnum.Keyword)

        for item in ["bool", "int", "float", "string"]:
            self.insert(item, SymbolEnum.Type)


# st = SymbolTable()
# st.insert("if", 0, SymbolEnum.Keyword, "")
# print("---------")
# st.insert("number", 0, SymbolEnum.Variable, "int")
# print("---------")
# st.insert("Student", 0, SymbolEnum.Type, "int")
# print("---------")
# check = st.find("if")
#
# if check is not None:
#     print("Identifier Is present")
# else:
#     print("Identifier Not Present")
# print("---------")
# if st.delete_record("if"):
#     print("if Identifier is deleted");
# else:
#     print("Failed to delete")
# print("---------")
# st.insert("if", 0, SymbolEnum.Keyword, "")
# print("---------")
# print(st.type_table)
# print("---------")
# st.delete_record("Student")
# print("---------")
# print(st.type_table)
# print("---------")
# print(st.scopes)
# print("---------")
# st.scopes.setdefault(1, Scope())
# print("---------")
# print(st.scopes)