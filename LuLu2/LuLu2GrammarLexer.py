# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammar.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01ee\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\6\31\u00b9\n\31\r\31\16\31\u00ba\3\31\6\31")
        buf.write("\u00be\n\31\r\31\16\31\u00bf\5\31\u00c2\n\31\3\32\3\32")
        buf.write("\3\32\5\32\u00c7\n\32\3\32\6\32\u00ca\n\32\r\32\16\32")
        buf.write("\u00cb\3\33\5\33\u00cf\n\33\3\33\3\33\7\33\u00d3\n\33")
        buf.write("\f\33\16\33\u00d6\13\33\3\33\5\33\u00d9\n\33\3\34\3\34")
        buf.write("\3\34\7\34\u00de\n\34\f\34\16\34\u00e1\13\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u00f5\n\35\3\36\3\36\5")
        buf.write("\36\u00f9\n\36\3\37\3\37\3\37\3\37\5\37\u00ff\n\37\3 ")
        buf.write("\3 \3 \3 \3 \5 \u0106\n \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\38\38\39\39\39\3:\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3>\3?\3?\3?\3@\3@\7@\u01cb\n@\f@\16@\u01ce\13")
        buf.write("@\3A\3A\3A\3A\7A\u01d4\nA\fA\16A\u01d7\13A\3A\3A\3A\3")
        buf.write("A\7A\u01dd\nA\fA\16A\u01e0\13A\3A\3A\5A\u01e4\nA\3A\3")
        buf.write("A\3B\6B\u01e9\nB\rB\16B\u01ea\3B\3B\4\u00df\u01de\2C\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081B\u0083C\3\2\16\3\2\62\62\4\2ZZzz\5")
        buf.write("\2\62;CHch\3\2\62;\4\2GGgg\3\2))\3\2^^\4\2>>@@\6\2%%C")
        buf.write("\\aac|\7\2%%\62;C\\aac|\3\2\f\f\5\2\13\f\17\17\"\"\2\u0207")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\3\u0085\3\2\2\2\5\u0087\3\2\2\2\7\u0089\3\2\2")
        buf.write("\2\t\u008b\3\2\2\2\13\u008d\3\2\2\2\r\u008f\3\2\2\2\17")
        buf.write("\u0091\3\2\2\2\21\u0093\3\2\2\2\23\u0095\3\2\2\2\25\u0097")
        buf.write("\3\2\2\2\27\u0099\3\2\2\2\31\u009b\3\2\2\2\33\u009d\3")
        buf.write("\2\2\2\35\u009f\3\2\2\2\37\u00a1\3\2\2\2!\u00a3\3\2\2")
        buf.write("\2#\u00a5\3\2\2\2%\u00a7\3\2\2\2\'\u00a9\3\2\2\2)\u00ac")
        buf.write("\3\2\2\2+\u00af\3\2\2\2-\u00b1\3\2\2\2/\u00b3\3\2\2\2")
        buf.write("\61\u00c1\3\2\2\2\63\u00c3\3\2\2\2\65\u00ce\3\2\2\2\67")
        buf.write("\u00da\3\2\2\29\u00f4\3\2\2\2;\u00f8\3\2\2\2=\u00fe\3")
        buf.write("\2\2\2?\u0105\3\2\2\2A\u0107\3\2\2\2C\u010f\3\2\2\2E\u0116")
        buf.write("\3\2\2\2G\u011c\3\2\2\2I\u0125\3\2\2\2K\u012e\3\2\2\2")
        buf.write("M\u0133\3\2\2\2O\u0139\3\2\2\2Q\u013f\3\2\2\2S\u0147\3")
        buf.write("\2\2\2U\u014e\3\2\2\2W\u0158\3\2\2\2Y\u015c\3\2\2\2[\u0161")
        buf.write("\3\2\2\2]\u0167\3\2\2\2_\u016e\3\2\2\2a\u0177\3\2\2\2")
        buf.write("c\u017c\3\2\2\2e\u0184\3\2\2\2g\u0189\3\2\2\2i\u018f\3")
        buf.write("\2\2\2k\u0195\3\2\2\2m\u019e\3\2\2\2o\u01a3\3\2\2\2q\u01a7")
        buf.write("\3\2\2\2s\u01aa\3\2\2\2u\u01af\3\2\2\2w\u01b6\3\2\2\2")
        buf.write("y\u01ba\3\2\2\2{\u01c0\3\2\2\2}\u01c5\3\2\2\2\177\u01c8")
        buf.write("\3\2\2\2\u0081\u01e3\3\2\2\2\u0083\u01e8\3\2\2\2\u0085")
        buf.write("\u0086\7}\2\2\u0086\4\3\2\2\2\u0087\u0088\7\177\2\2\u0088")
        buf.write("\6\3\2\2\2\u0089\u008a\7*\2\2\u008a\b\3\2\2\2\u008b\u008c")
        buf.write("\7+\2\2\u008c\n\3\2\2\2\u008d\u008e\7]\2\2\u008e\f\3\2")
        buf.write("\2\2\u008f\u0090\7_\2\2\u0090\16\3\2\2\2\u0091\u0092\7")
        buf.write("\60\2\2\u0092\20\3\2\2\2\u0093\u0094\7?\2\2\u0094\22\3")
        buf.write("\2\2\2\u0095\u0096\7=\2\2\u0096\24\3\2\2\2\u0097\u0098")
        buf.write("\7<\2\2\u0098\26\3\2\2\2\u0099\u009a\7.\2\2\u009a\30\3")
        buf.write("\2\2\2\u009b\u009c\7/\2\2\u009c\32\3\2\2\2\u009d\u009e")
        buf.write("\7-\2\2\u009e\34\3\2\2\2\u009f\u00a0\7,\2\2\u00a0\36\3")
        buf.write("\2\2\2\u00a1\u00a2\7`\2\2\u00a2 \3\2\2\2\u00a3\u00a4\7")
        buf.write("\61\2\2\u00a4\"\3\2\2\2\u00a5\u00a6\7\'\2\2\u00a6$\3\2")
        buf.write("\2\2\u00a7\u00a8\7#\2\2\u00a8&\3\2\2\2\u00a9\u00aa\7(")
        buf.write("\2\2\u00aa\u00ab\7(\2\2\u00ab(\3\2\2\2\u00ac\u00ad\7~")
        buf.write("\2\2\u00ad\u00ae\7~\2\2\u00ae*\3\2\2\2\u00af\u00b0\7(")
        buf.write("\2\2\u00b0,\3\2\2\2\u00b1\u00b2\7~\2\2\u00b2.\3\2\2\2")
        buf.write("\u00b3\u00b4\7\u0080\2\2\u00b4\60\3\2\2\2\u00b5\u00b6")
        buf.write("\t\2\2\2\u00b6\u00b8\t\3\2\2\u00b7\u00b9\t\4\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\u00c2\3\2\2\2\u00bc\u00be\t")
        buf.write("\5\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1")
        buf.write("\u00b5\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c2\62\3\2\2\2\u00c3")
        buf.write("\u00c6\t\6\2\2\u00c4\u00c7\5\33\16\2\u00c5\u00c7\5\31")
        buf.write("\r\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00ca\t\5\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\64\3\2\2\2\u00cd\u00cf\5\61")
        buf.write("\31\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d4\5\17\b\2\u00d1\u00d3\t\5\2\2\u00d2")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3")
        buf.write("\2\2\2\u00d7\u00d9\5\63\32\2\u00d8\u00d7\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\66\3\2\2\2\u00da\u00df\t\7\2\2\u00db")
        buf.write("\u00de\n\b\2\2\u00dc\u00de\59\35\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00e0\3")
        buf.write("\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e2\u00e3\t\7\2\2\u00e38\3\2\2\2\u00e4\u00e5")
        buf.write("\7^\2\2\u00e5\u00f5\7p\2\2\u00e6\u00e7\7^\2\2\u00e7\u00f5")
        buf.write("\7t\2\2\u00e8\u00e9\7^\2\2\u00e9\u00f5\7^\2\2\u00ea\u00eb")
        buf.write("\7^\2\2\u00eb\u00f5\7v\2\2\u00ec\u00ed\7^\2\2\u00ed\u00f5")
        buf.write("\7\62\2\2\u00ee\u00ef\7^\2\2\u00ef\u00f5\7)\2\2\u00f0")
        buf.write("\u00f1\7^\2\2\u00f1\u00f2\t\3\2\2\u00f2\u00f3\t\4\2\2")
        buf.write("\u00f3\u00f5\t\4\2\2\u00f4\u00e4\3\2\2\2\u00f4\u00e6\3")
        buf.write("\2\2\2\u00f4\u00e8\3\2\2\2\u00f4\u00ea\3\2\2\2\u00f4\u00ec")
        buf.write("\3\2\2\2\u00f4\u00ee\3\2\2\2\u00f4\u00f0\3\2\2\2\u00f5")
        buf.write(":\3\2\2\2\u00f6\u00f9\5{>\2\u00f7\u00f9\5y=\2\u00f8\u00f6")
        buf.write("\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9<\3\2\2\2\u00fa\u00fb")
        buf.write("\7?\2\2\u00fb\u00ff\7?\2\2\u00fc\u00fd\7#\2\2\u00fd\u00ff")
        buf.write("\7?\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff")
        buf.write(">\3\2\2\2\u0100\u0101\7>\2\2\u0101\u0106\7?\2\2\u0102")
        buf.write("\u0106\t\t\2\2\u0103\u0104\7@\2\2\u0104\u0106\7?\2\2\u0105")
        buf.write("\u0100\3\2\2\2\u0105\u0102\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0106@\3\2\2\2\u0107\u0108\7f\2\2\u0108\u0109\7g\2\2")
        buf.write("\u0109\u010a\7e\2\2\u010a\u010b\7n\2\2\u010b\u010c\7c")
        buf.write("\2\2\u010c\u010d\7t\2\2\u010d\u010e\7g\2\2\u010eB\3\2")
        buf.write("\2\2\u010f\u0110\7t\2\2\u0110\u0111\7g\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7w\2\2\u0113\u0114\7t\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115D\3\2\2\2\u0116\u0117\7d\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7g\2\2\u0119\u011a\7c\2\2\u011a\u011b")
        buf.write("\7m\2\2\u011bF\3\2\2\2\u011c\u011d\7e\2\2\u011d\u011e")
        buf.write("\7q\2\2\u011e\u011f\7p\2\2\u011f\u0120\7v\2\2\u0120\u0121")
        buf.write("\7k\2\2\u0121\u0122\7p\2\2\u0122\u0123\7w\2\2\u0123\u0124")
        buf.write("\7g\2\2\u0124H\3\2\2\2\u0125\u0126\7f\2\2\u0126\u0127")
        buf.write("\7g\2\2\u0127\u0128\7u\2\2\u0128\u0129\7v\2\2\u0129\u012a")
        buf.write("\7t\2\2\u012a\u012b\7w\2\2\u012b\u012c\7e\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012dJ\3\2\2\2\u012e\u012f\7v\2\2\u012f\u0130")
        buf.write("\7j\2\2\u0130\u0131\7k\2\2\u0131\u0132\7u\2\2\u0132L\3")
        buf.write("\2\2\2\u0133\u0134\7u\2\2\u0134\u0135\7w\2\2\u0135\u0136")
        buf.write("\7r\2\2\u0136\u0137\7g\2\2\u0137\u0138\7t\2\2\u0138N\3")
        buf.write("\2\2\2\u0139\u013a\7e\2\2\u013a\u013b\7q\2\2\u013b\u013c")
        buf.write("\7p\2\2\u013c\u013d\7u\2\2\u013d\u013e\7v\2\2\u013eP\3")
        buf.write("\2\2\2\u013f\u0140\7r\2\2\u0140\u0141\7t\2\2\u0141\u0142")
        buf.write("\7k\2\2\u0142\u0143\7x\2\2\u0143\u0144\7c\2\2\u0144\u0145")
        buf.write("\7v\2\2\u0145\u0146\7g\2\2\u0146R\3\2\2\2\u0147\u0148")
        buf.write("\7r\2\2\u0148\u0149\7w\2\2\u0149\u014a\7d\2\2\u014a\u014b")
        buf.write("\7n\2\2\u014b\u014c\7k\2\2\u014c\u014d\7e\2\2\u014dT\3")
        buf.write("\2\2\2\u014e\u014f\7r\2\2\u014f\u0150\7t\2\2\u0150\u0151")
        buf.write("\7q\2\2\u0151\u0152\7v\2\2\u0152\u0153\7g\2\2\u0153\u0154")
        buf.write("\7e\2\2\u0154\u0155\7v\2\2\u0155\u0156\7g\2\2\u0156\u0157")
        buf.write("\7f\2\2\u0157V\3\2\2\2\u0158\u0159\7k\2\2\u0159\u015a")
        buf.write("\7p\2\2\u015a\u015b\7v\2\2\u015bX\3\2\2\2\u015c\u015d")
        buf.write("\7d\2\2\u015d\u015e\7q\2\2\u015e\u015f\7q\2\2\u015f\u0160")
        buf.write("\7n\2\2\u0160Z\3\2\2\2\u0161\u0162\7h\2\2\u0162\u0163")
        buf.write("\7n\2\2\u0163\u0164\7q\2\2\u0164\u0165\7c\2\2\u0165\u0166")
        buf.write("\7v\2\2\u0166\\\3\2\2\2\u0167\u0168\7u\2\2\u0168\u0169")
        buf.write("\7v\2\2\u0169\u016a\7t\2\2\u016a\u016b\7k\2\2\u016b\u016c")
        buf.write("\7p\2\2\u016c\u016d\7i\2\2\u016d^\3\2\2\2\u016e\u016f")
        buf.write("\7h\2\2\u016f\u0170\7w\2\2\u0170\u0171\7p\2\2\u0171\u0172")
        buf.write("\7e\2\2\u0172\u0173\7v\2\2\u0173\u0174\7k\2\2\u0174\u0175")
        buf.write("\7q\2\2\u0175\u0176\7p\2\2\u0176`\3\2\2\2\u0177\u0178")
        buf.write("\7e\2\2\u0178\u0179\7c\2\2\u0179\u017a\7u\2\2\u017a\u017b")
        buf.write("\7g\2\2\u017bb\3\2\2\2\u017c\u017d\7f\2\2\u017d\u017e")
        buf.write("\7g\2\2\u017e\u017f\7h\2\2\u017f\u0180\7c\2\2\u0180\u0181")
        buf.write("\7w\2\2\u0181\u0182\7n\2\2\u0182\u0183\7v\2\2\u0183d\3")
        buf.write("\2\2\2\u0184\u0185\7t\2\2\u0185\u0186\7g\2\2\u0186\u0187")
        buf.write("\7c\2\2\u0187\u0188\7f\2\2\u0188f\3\2\2\2\u0189\u018a")
        buf.write("\7y\2\2\u018a\u018b\7t\2\2\u018b\u018c\7k\2\2\u018c\u018d")
        buf.write("\7v\2\2\u018d\u018e\7g\2\2\u018eh\3\2\2\2\u018f\u0190")
        buf.write("\7y\2\2\u0190\u0191\7j\2\2\u0191\u0192\7k\2\2\u0192\u0193")
        buf.write("\7n\2\2\u0193\u0194\7g\2\2\u0194j\3\2\2\2\u0195\u0196")
        buf.write("\7c\2\2\u0196\u0197\7n\2\2\u0197\u0198\7n\2\2\u0198\u0199")
        buf.write("\7q\2\2\u0199\u019a\7e\2\2\u019a\u019b\7c\2\2\u019b\u019c")
        buf.write("\7v\2\2\u019c\u019d\7g\2\2\u019dl\3\2\2\2\u019e\u019f")
        buf.write("\7v\2\2\u019f\u01a0\7{\2\2\u01a0\u01a1\7r\2\2\u01a1\u01a2")
        buf.write("\7g\2\2\u01a2n\3\2\2\2\u01a3\u01a4\7p\2\2\u01a4\u01a5")
        buf.write("\7k\2\2\u01a5\u01a6\7n\2\2\u01a6p\3\2\2\2\u01a7\u01a8")
        buf.write("\7k\2\2\u01a8\u01a9\7h\2\2\u01a9r\3\2\2\2\u01aa\u01ab")
        buf.write("\7g\2\2\u01ab\u01ac\7n\2\2\u01ac\u01ad\7u\2\2\u01ad\u01ae")
        buf.write("\7g\2\2\u01aet\3\2\2\2\u01af\u01b0\7u\2\2\u01b0\u01b1")
        buf.write("\7y\2\2\u01b1\u01b2\7k\2\2\u01b2\u01b3\7v\2\2\u01b3\u01b4")
        buf.write("\7e\2\2\u01b4\u01b5\7j\2\2\u01b5v\3\2\2\2\u01b6\u01b7")
        buf.write("\7h\2\2\u01b7\u01b8\7q\2\2\u01b8\u01b9\7t\2\2\u01b9x\3")
        buf.write("\2\2\2\u01ba\u01bb\7h\2\2\u01bb\u01bc\7c\2\2\u01bc\u01bd")
        buf.write("\7n\2\2\u01bd\u01be\7u\2\2\u01be\u01bf\7g\2\2\u01bfz\3")
        buf.write("\2\2\2\u01c0\u01c1\7v\2\2\u01c1\u01c2\7t\2\2\u01c2\u01c3")
        buf.write("\7w\2\2\u01c3\u01c4\7g\2\2\u01c4|\3\2\2\2\u01c5\u01c6")
        buf.write("\7q\2\2\u01c6\u01c7\7h\2\2\u01c7~\3\2\2\2\u01c8\u01cc")
        buf.write("\t\n\2\2\u01c9\u01cb\t\13\2\2\u01ca\u01c9\3\2\2\2\u01cb")
        buf.write("\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2")
        buf.write("\u01cd\u0080\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d0\7")
        buf.write("\'\2\2\u01d0\u01d1\7\'\2\2\u01d1\u01d5\3\2\2\2\u01d2\u01d4")
        buf.write("\n\f\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01e4\3\2\2\2")
        buf.write("\u01d7\u01d5\3\2\2\2\u01d8\u01d9\7\'\2\2\u01d9\u01da\7")
        buf.write("\u0080\2\2\u01da\u01de\3\2\2\2\u01db\u01dd\13\2\2\2\u01dc")
        buf.write("\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01de\3")
        buf.write("\2\2\2\u01e1\u01e2\7\u0080\2\2\u01e2\u01e4\7\'\2\2\u01e3")
        buf.write("\u01cf\3\2\2\2\u01e3\u01d8\3\2\2\2\u01e4\u01e5\3\2\2\2")
        buf.write("\u01e5\u01e6\bA\2\2\u01e6\u0082\3\2\2\2\u01e7\u01e9\t")
        buf.write("\r\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("\u01ed\bB\2\2\u01ed\u0084\3\2\2\2\26\2\u00ba\u00bf\u00c1")
        buf.write("\u00c6\u00cb\u00ce\u00d4\u00d8\u00dd\u00df\u00f4\u00f8")
        buf.write("\u00fe\u0105\u01cc\u01d5\u01de\u01e3\u01ea\3\b\2\2")
        return buf.getvalue()


class LuLu2GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OPENING_BRACE = 1
    CLOSING_BRACE = 2
    OPENING_PARENTHEISIS = 3
    CLOSING_PARENTHEISIS = 4
    OPENING_BRACKET = 5
    CLOSING_BRACKET = 6
    SYMBOL_DOT = 7
    SYMBOL_EQUAL = 8
    SYMBOL_SEMICOLON = 9
    SYMBOL_COLON = 10
    SYMBOL_COMMA = 11
    SYMBOL_DASH = 12
    SYMBOL_PLUS = 13
    SYMBOL_STAR = 14
    SYMBOL_XOR = 15
    SYMBOL_SLASH = 16
    SYMBOL_PERCENT = 17
    SYMBOL_EXCLAMATION = 18
    SYMBOL_LOGIC_AND = 19
    SYMBOL_LOGIC_OR = 20
    SYMBOL_AND = 21
    SYMBOL_OR = 22
    SYMBOL_MAD = 23
    INT_CONST = 24
    EXPONENT = 25
    REAL_CONST = 26
    STRING_CONST = 27
    ESCAPE_CHARACTER = 28
    BOOL_CONST = 29
    EQUAL_OPERATORS = 30
    RELATIONAL_OPERATORS = 31
    KEYWORD_DECLARE = 32
    KEYWORD_RETURN = 33
    KEYWORD_BREAK = 34
    KEYWORD_CONTINUE = 35
    KEYWORD_DESTRUCT = 36
    KEYWORD_THIS = 37
    KEYWORD_SUPER = 38
    KEYWORD_CONST = 39
    KEYWORD_PRIVATE = 40
    KEYWORD_PUBLIC = 41
    KEYWORD_PROTECTED = 42
    KEYWORD_INT = 43
    KEYWORD_BOOL = 44
    KEYWORD_FLOAT = 45
    KEYWORD_STRING = 46
    KEYWORD_FUNCTION = 47
    KEYWORD_CASE = 48
    KEYWORD_DEFAULT = 49
    KEYWORD_READ = 50
    KEYWORD_WRITE = 51
    KEYWORD_WHILE = 52
    KEYWORD_ALLOCATE = 53
    KEYWORD_TYPE = 54
    KEYWORD_NIL = 55
    KEYWORD_IF = 56
    KEYWORD_ELSE = 57
    KEYWORD_SWITCH = 58
    KEYWORD_FOR = 59
    KEYWORD_FALSE = 60
    KEYWORD_TRUE = 61
    KEYWORD_OF = 62
    ID = 63
    COMMENT = 64
    WHITESPACE = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'('", "')'", "'['", "']'", "'.'", "'='", "';'", 
            "':'", "','", "'-'", "'+'", "'*'", "'^'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'&'", "'|'", "'~'", "'declare'", "'return'", 
            "'break'", "'continue'", "'destruct'", "'this'", "'super'", 
            "'const'", "'private'", "'public'", "'protected'", "'int'", 
            "'bool'", "'float'", "'string'", "'function'", "'case'", "'default'", 
            "'read'", "'write'", "'while'", "'allocate'", "'type'", "'nil'", 
            "'if'", "'else'", "'switch'", "'for'", "'false'", "'true'", 
            "'of'" ]

    symbolicNames = [ "<INVALID>",
            "OPENING_BRACE", "CLOSING_BRACE", "OPENING_PARENTHEISIS", "CLOSING_PARENTHEISIS", 
            "OPENING_BRACKET", "CLOSING_BRACKET", "SYMBOL_DOT", "SYMBOL_EQUAL", 
            "SYMBOL_SEMICOLON", "SYMBOL_COLON", "SYMBOL_COMMA", "SYMBOL_DASH", 
            "SYMBOL_PLUS", "SYMBOL_STAR", "SYMBOL_XOR", "SYMBOL_SLASH", 
            "SYMBOL_PERCENT", "SYMBOL_EXCLAMATION", "SYMBOL_LOGIC_AND", 
            "SYMBOL_LOGIC_OR", "SYMBOL_AND", "SYMBOL_OR", "SYMBOL_MAD", 
            "INT_CONST", "EXPONENT", "REAL_CONST", "STRING_CONST", "ESCAPE_CHARACTER", 
            "BOOL_CONST", "EQUAL_OPERATORS", "RELATIONAL_OPERATORS", "KEYWORD_DECLARE", 
            "KEYWORD_RETURN", "KEYWORD_BREAK", "KEYWORD_CONTINUE", "KEYWORD_DESTRUCT", 
            "KEYWORD_THIS", "KEYWORD_SUPER", "KEYWORD_CONST", "KEYWORD_PRIVATE", 
            "KEYWORD_PUBLIC", "KEYWORD_PROTECTED", "KEYWORD_INT", "KEYWORD_BOOL", 
            "KEYWORD_FLOAT", "KEYWORD_STRING", "KEYWORD_FUNCTION", "KEYWORD_CASE", 
            "KEYWORD_DEFAULT", "KEYWORD_READ", "KEYWORD_WRITE", "KEYWORD_WHILE", 
            "KEYWORD_ALLOCATE", "KEYWORD_TYPE", "KEYWORD_NIL", "KEYWORD_IF", 
            "KEYWORD_ELSE", "KEYWORD_SWITCH", "KEYWORD_FOR", "KEYWORD_FALSE", 
            "KEYWORD_TRUE", "KEYWORD_OF", "ID", "COMMENT", "WHITESPACE" ]

    ruleNames = [ "OPENING_BRACE", "CLOSING_BRACE", "OPENING_PARENTHEISIS", 
                  "CLOSING_PARENTHEISIS", "OPENING_BRACKET", "CLOSING_BRACKET", 
                  "SYMBOL_DOT", "SYMBOL_EQUAL", "SYMBOL_SEMICOLON", "SYMBOL_COLON", 
                  "SYMBOL_COMMA", "SYMBOL_DASH", "SYMBOL_PLUS", "SYMBOL_STAR", 
                  "SYMBOL_XOR", "SYMBOL_SLASH", "SYMBOL_PERCENT", "SYMBOL_EXCLAMATION", 
                  "SYMBOL_LOGIC_AND", "SYMBOL_LOGIC_OR", "SYMBOL_AND", "SYMBOL_OR", 
                  "SYMBOL_MAD", "INT_CONST", "EXPONENT", "REAL_CONST", "STRING_CONST", 
                  "ESCAPE_CHARACTER", "BOOL_CONST", "EQUAL_OPERATORS", "RELATIONAL_OPERATORS", 
                  "KEYWORD_DECLARE", "KEYWORD_RETURN", "KEYWORD_BREAK", 
                  "KEYWORD_CONTINUE", "KEYWORD_DESTRUCT", "KEYWORD_THIS", 
                  "KEYWORD_SUPER", "KEYWORD_CONST", "KEYWORD_PRIVATE", "KEYWORD_PUBLIC", 
                  "KEYWORD_PROTECTED", "KEYWORD_INT", "KEYWORD_BOOL", "KEYWORD_FLOAT", 
                  "KEYWORD_STRING", "KEYWORD_FUNCTION", "KEYWORD_CASE", 
                  "KEYWORD_DEFAULT", "KEYWORD_READ", "KEYWORD_WRITE", "KEYWORD_WHILE", 
                  "KEYWORD_ALLOCATE", "KEYWORD_TYPE", "KEYWORD_NIL", "KEYWORD_IF", 
                  "KEYWORD_ELSE", "KEYWORD_SWITCH", "KEYWORD_FOR", "KEYWORD_FALSE", 
                  "KEYWORD_TRUE", "KEYWORD_OF", "ID", "COMMENT", "WHITESPACE" ]

    grammarFileName = "LuLu2Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


