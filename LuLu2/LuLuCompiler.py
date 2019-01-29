import sys
import os
from antlr4 import *
from antlr4.error import ErrorListener

from LuLu2.ErrorManager import errorManager
from LuLu2.LuLu2GrammarErrorListener import LuLu2GrammarErrorListener
from LuLu2.LuLu2GrammarParser import LuLu2GrammarParser
from LuLu2.LuLu2GrammarListener import LuLu2GrammarListener
from LuLu2.LuLu2GrammarLexer import LuLu2GrammarLexer
from LuLu2.LuLu2GrammarVisitorDeclaration import LuLu2GrammarVisitorDeclaration
from pptree import *

from LuLu2.LuLu2GrammarVisitorUsage import LuLu2GrammarVisitorUsage
from LuLu2.Scope import Scope, global_scope

# root = Node("ROOT")
#
# def handleExpression(scope : Scope, level=0):
#     global root
#     for child in scope.children:
#         newNode = Node(str(child.start_line)+"-"+str(child.start_column), root)
#         for type_ in child.types:
#             t = child.types[type_]
#             newVariable = Node("type : {0}".format(t.key), newNode)
#         for variable in child.variables:
#             v = child.variables[variable]
#             newVariable = Node("variable : {0} {1}".format(v.Type ,v.key), newNode)
#         for function in child.functions:
#             for key1 in child.functions[function]:
#                 f = child.functions[function][key1]
#                 newFunction = Node("function : {0} {1}({2})".format(f.output,f.key,f.input), newNode)
#         for type_ in scope.variables:
#             v = scope.variables[variable]
#             newVariable = Node("variable : {0} {1}".format(v.Type ,v.key), newNode)
#         tmp = root
#         root = newNode
#         handleExpression(child, level+1)
#         root = tmp



def main():
    path = "test10.lulu"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    input = FileStream(path)
    lexer = LuLu2GrammarLexer(input)
    commonTokenStream = CommonTokenStream(lexer)
    stream = CommonTokenStream(lexer)
    parser = LuLu2GrammarParser(stream)
    error_listener = LuLu2GrammarErrorListener(path)
    listener = LuLu2GrammarListener()
    parser.removeErrorListeners()

    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    file = open("test.cpp", "w+")

    errorManager.path = path

    visitor = LuLu2GrammarVisitorDeclaration(file)
    visitor.visit(parser.program())

    input = FileStream(path)
    lexer = LuLu2GrammarLexer(input)
    commonTokenStream = CommonTokenStream(lexer)
    stream = CommonTokenStream(lexer)
    parser = LuLu2GrammarParser(stream)
    error_listener = LuLu2GrammarErrorListener(path)
    listener = LuLu2GrammarListener()
    parser.removeErrorListeners()

    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)


    errorManager.path = path

    visitor = LuLu2GrammarVisitorUsage()
    visitor.visit(parser.program())

    # handleExpression(global_scope)
    # print_tree(root)

    file.close()


    if errorManager.error_count is not 0 or parser.getNumberOfSyntaxErrors() is not 0:
        sys.exit(1)
    else:
        os.system('g++ test.cpp -o text.exe')
        sys.exit(0)


if __name__ == '__main__':
    main()
