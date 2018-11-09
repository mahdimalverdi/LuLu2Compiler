# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammer.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LuLu2GrammerParser import LuLu2GrammerParser
else:
    from LuLu2GrammerParser import LuLu2GrammerParser

# This class defines a complete generic visitor for a parse tree produced by LuLu2GrammerParser.

class LuLu2GrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LuLu2GrammerParser#program.
    def visitProgram(self, ctx:LuLu2GrammerParser.ProgramContext):
        return self.visitChildren(ctx)



del LuLu2GrammerParser