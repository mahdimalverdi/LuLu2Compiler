# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammar.g4 by ANTLR 4.7
import sys
from antlr4.error import ErrorListener

# This class defines a complete listener for a parse tree produced by LuLu2GrammarParser.
class LuLu2GrammarErrorListener(ErrorListener.ConsoleErrorListener):
    def __init__(self, path):
        self._path = path

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(self._path + ":" + str(line) + ":" + str(column) + ": error: " " " + msg, file=sys.stderr)