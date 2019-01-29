

class Operators:
    def get_int_operators(self):
        operators: dict[str, str] = {}
        operators.setdefault("int+int", "int")
        operators.setdefault("int-int", "int")
        operators.setdefault("int*int", "int")
        operators.setdefault("int/int", "int")
        operators.setdefault("int%int", "int")
        operators.setdefault("int<=int", "bool")
        operators.setdefault("int<int", "bool")
        operators.setdefault("int>int", "bool")
        operators.setdefault("int>=int", "bool")
        operators.setdefault("int==int", "bool")
        operators.setdefault("int!=int", "bool")
        operators.setdefault("int&int", "int")
        operators.setdefault("int^int", "int")
        operators.setdefault("int|int", "int")
        operators.setdefault("int&&int", "bool")
        operators.setdefault("int||int", "bool")
        operators.setdefault("-int", "int")
        operators.setdefault("!int", "int")
        operators.setdefault("~int", "int")
        return operators

    def get_float_operators(self):
        operators:dict[str, str] = {}
        operators.setdefault("float+float", "float")
        operators.setdefault("float-float", "float")
        operators.setdefault("float*float", "float")
        operators.setdefault("float/float", "float")
        operators.setdefault("float%float", "float")
        operators.setdefault("float<=float", "bool")
        operators.setdefault("float<float", "bool")
        operators.setdefault("float>float", "bool")
        operators.setdefault("float>=float", "bool")
        operators.setdefault("float==float", "bool")
        operators.setdefault("float!=float", "bool")
        operators.setdefault("-float", "float")
        return operators

    def get_string_operators(self) -> dict:
        operators:dict[str, str] = {}
        operators.setdefault("string+string", "string")
        operators.setdefault("string-string", "string")
        operators.setdefault("string*string", "string")
        operators.setdefault("string/string", "string")
        operators.setdefault("string%string", "string")
        operators.setdefault("string<=string", "bool")
        operators.setdefault("string<string", "bool")
        operators.setdefault("string>string", "bool")
        operators.setdefault("string>=string", "bool")
        operators.setdefault("string==string", "bool")
        operators.setdefault("string!=string", "bool")
        return operators

    def get_bool_operators(self) -> dict:
        operators:dict[str, str] = {}
        operators.setdefault("bool+bool", "bool")
        operators.setdefault("bool-bool", "bool")
        operators.setdefault("bool*bool", "bool")
        operators.setdefault("bool/bool", "bool")
        operators.setdefault("bool%bool", "bool")
        operators.setdefault("bool<=bool", "bool")
        operators.setdefault("bool<bool", "bool")
        operators.setdefault("bool>bool", "bool")
        operators.setdefault("bool>=bool", "bool")
        operators.setdefault("bool==bool", "bool")
        operators.setdefault("bool!=bool", "bool")
        operators.setdefault("bool&bool", "bool")
        operators.setdefault("bool^bool", "bool")
        operators.setdefault("bool|bool", "bool")
        operators.setdefault("bool&&bool", "bool")
        operators.setdefault("bool||bool", "bool")
        operators.setdefault("-bool", "bool")
        operators.setdefault("!bool", "bool")
        operators.setdefault("~bool", "bool")
        return operators


operators = Operators()
