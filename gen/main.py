import sys
from antlr4 import *
from LuLu2GrammarLexer import LuLu2GrammarLexer
from LuLu2GrammarListener import LuLu2GrammarListener
from LuLu2GrammarParser import LuLu2GrammarParser
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
    global root
    input = FileStream("test10.lulu")
    lexer = LuLu2GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LuLu2GrammarParser(stream)
    tree = parser.program()
    root = Node(LuLu2GrammarParser.ruleNames[tree.getRuleIndex()])
    handleExpression(tree)
    print_tree(root)

if __name__ == '__main__':
    main()
