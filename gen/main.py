import sys
from antlr4 import *
from LuLu2GrammarLexer import LuLu2GrammarLexer
from LuLu2GrammarListener import LuLu2GrammarListener
from LuLu2GrammarParser import LuLu2GrammarParser
from antlr4 import tree

import plotly.plotly as py
import plotly.graph_objs as go

import igraph
from igraph import *
igraph.__version__


def handleExpression(expr, level=0):
    adding = True
    value = 0
    for child in expr.getChildren():
        if isinstance(child, tree.Tree.TerminalNode):
            print("| "*(level-1)+"|_",child)
        else:
            print("| "*(level-1)+"|_","start", LuLu2GrammarParser.ruleNames[expr.getRuleIndex()])
            handleExpression(child, level+1)
            print("| "*(level-1)+"|_","end", LuLu2GrammarParser.ruleNames[expr.getRuleIndex()])



def main():
    input = FileStream("test10.lulu")
    lexer = LuLu2GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LuLu2GrammarParser(stream)
    tree = parser.program()
    handleExpression(tree)


if __name__ == '__main__':
    main()
