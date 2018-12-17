import sys
from antlr4 import *
from LuLu2.LuLu2GrammarParser import LuLu2GrammarParser
from LuLu2.LuLu2GrammarListener import LuLu2GrammarListener
from LuLu2.LuLu2GrammarLexer import LuLu2GrammarLexer
from LuLu2.LuLu2GrammarVisitor import LuLu2GrammarVisitor

from antlr4 import tree

from pptree import *

root = Node("ROOT")

def handleExpression(expr, level=0):
    global root
    for child in expr.getChildren():
        if isinstance(child, tree.Tree.TerminalNode):
            Node(child, root)
        else:
            newNode = Node(LuLu2GrammarParser.ruleNames[child.getRuleIndex()], root)
            tmp = root
            root = newNode
            handleExpression(child, level+1)
            root = tmp



def main():
    input = FileStream("test10.lulu")
    lexer = LuLu2GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LuLu2GrammarParser(stream)
    visitor = LuLu2GrammarVisitor().visit(parser.program())


if __name__ == '__main__':
    main()
