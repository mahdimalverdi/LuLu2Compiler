# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammer.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\13\4\2\t\2\3\2\7\2\6\n\2\f\2\16\2\t\13\2\3\2\2\2\3\2")
        buf.write("\2\2\2\n\2\7\3\2\2\2\4\6\7\7\2\2\5\4\3\2\2\2\6\t\3\2\2")
        buf.write("\2\7\5\3\2\2\2\7\b\3\2\2\2\b\3\3\2\2\2\t\7\3\2\2\2\3\7")
        return buf.getvalue()


class LuLu2GrammerParser ( Parser ):

    grammarFileName = "LuLu2Grammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "ID", "KEYWORD", "INT_CONST", "REAL_CONST", 
                      "STRING_CONST" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    KEYWORD=2
    INT_CONST=3
    REAL_CONST=4
    STRING_CONST=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_CONST(self, i:int=None):
            if i is None:
                return self.getTokens(LuLu2GrammerParser.STRING_CONST)
            else:
                return self.getToken(LuLu2GrammerParser.STRING_CONST, i)

        def getRuleIndex(self):
            return LuLu2GrammerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LuLu2GrammerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuLu2GrammerParser.STRING_CONST:
                self.state = 2
                self.match(LuLu2GrammerParser.STRING_CONST)
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





