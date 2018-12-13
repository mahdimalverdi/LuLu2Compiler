# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammar.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01f1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u00f7\n\35\3")
        buf.write("\36\3\36\5\36\u00fb\n\36\3\37\3\37\3\37\3\37\5\37\u0101")
        buf.write("\n\37\3 \3 \3 \3 \3 \5 \u0108\n \3!\3!\3!\3!\3!\3!\3!")
        buf.write("\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\3")
        buf.write(":\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3@\3@\7@\u01ce\n@\f")
        buf.write("@\16@\u01d1\13@\3A\3A\3A\3A\7A\u01d7\nA\fA\16A\u01da\13")
        buf.write("A\3A\3A\3A\3A\7A\u01e0\nA\fA\16A\u01e3\13A\3A\3A\5A\u01e7")
        buf.write("\nA\3A\3A\3B\6B\u01ec\nB\rB\16B\u01ed\3B\3B\4\u00df\u01e1")
        buf.write("\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\3\2\16\3\2\62\62\4\2")
        buf.write("ZZzz\5\2\62;CHch\3\2\62;\4\2GGgg\3\2))\3\2^^\4\2>>@@\6")
        buf.write("\2%%C\\aac|\7\2%%\62;C\\aac|\3\2\f\f\5\2\13\f\17\17\"")
        buf.write("\"\2\u020a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u0087\3\2\2")
        buf.write("\2\7\u0089\3\2\2\2\t\u008b\3\2\2\2\13\u008d\3\2\2\2\r")
        buf.write("\u008f\3\2\2\2\17\u0091\3\2\2\2\21\u0093\3\2\2\2\23\u0095")
        buf.write("\3\2\2\2\25\u0097\3\2\2\2\27\u0099\3\2\2\2\31\u009b\3")
        buf.write("\2\2\2\33\u009d\3\2\2\2\35\u009f\3\2\2\2\37\u00a1\3\2")
        buf.write("\2\2!\u00a3\3\2\2\2#\u00a5\3\2\2\2%\u00a7\3\2\2\2\'\u00a9")
        buf.write("\3\2\2\2)\u00ac\3\2\2\2+\u00af\3\2\2\2-\u00b1\3\2\2\2")
        buf.write("/\u00b3\3\2\2\2\61\u00c1\3\2\2\2\63\u00c3\3\2\2\2\65\u00ce")
        buf.write("\3\2\2\2\67\u00da\3\2\2\29\u00f6\3\2\2\2;\u00fa\3\2\2")
        buf.write("\2=\u0100\3\2\2\2?\u0107\3\2\2\2A\u0109\3\2\2\2C\u0111")
        buf.write("\3\2\2\2E\u0118\3\2\2\2G\u011e\3\2\2\2I\u0127\3\2\2\2")
        buf.write("K\u0130\3\2\2\2M\u0135\3\2\2\2O\u013b\3\2\2\2Q\u0141\3")
        buf.write("\2\2\2S\u0149\3\2\2\2U\u0150\3\2\2\2W\u015a\3\2\2\2Y\u015e")
        buf.write("\3\2\2\2[\u0163\3\2\2\2]\u0169\3\2\2\2_\u0170\3\2\2\2")
        buf.write("a\u0179\3\2\2\2c\u017e\3\2\2\2e\u0186\3\2\2\2g\u018b\3")
        buf.write("\2\2\2i\u0191\3\2\2\2k\u0197\3\2\2\2m\u01a0\3\2\2\2o\u01a6")
        buf.write("\3\2\2\2q\u01aa\3\2\2\2s\u01ad\3\2\2\2u\u01b2\3\2\2\2")
        buf.write("w\u01b9\3\2\2\2y\u01bd\3\2\2\2{\u01c3\3\2\2\2}\u01c8\3")
        buf.write("\2\2\2\177\u01cb\3\2\2\2\u0081\u01e6\3\2\2\2\u0083\u01eb")
        buf.write("\3\2\2\2\u0085\u0086\7}\2\2\u0086\4\3\2\2\2\u0087\u0088")
        buf.write("\7\177\2\2\u0088\6\3\2\2\2\u0089\u008a\7*\2\2\u008a\b")
        buf.write("\3\2\2\2\u008b\u008c\7+\2\2\u008c\n\3\2\2\2\u008d\u008e")
        buf.write("\7]\2\2\u008e\f\3\2\2\2\u008f\u0090\7_\2\2\u0090\16\3")
        buf.write("\2\2\2\u0091\u0092\7\60\2\2\u0092\20\3\2\2\2\u0093\u0094")
        buf.write("\7?\2\2\u0094\22\3\2\2\2\u0095\u0096\7=\2\2\u0096\24\3")
        buf.write("\2\2\2\u0097\u0098\7<\2\2\u0098\26\3\2\2\2\u0099\u009a")
        buf.write("\7.\2\2\u009a\30\3\2\2\2\u009b\u009c\7/\2\2\u009c\32\3")
        buf.write("\2\2\2\u009d\u009e\7-\2\2\u009e\34\3\2\2\2\u009f\u00a0")
        buf.write("\7,\2\2\u00a0\36\3\2\2\2\u00a1\u00a2\7`\2\2\u00a2 \3\2")
        buf.write("\2\2\u00a3\u00a4\7\61\2\2\u00a4\"\3\2\2\2\u00a5\u00a6")
        buf.write("\7\'\2\2\u00a6$\3\2\2\2\u00a7\u00a8\7#\2\2\u00a8&\3\2")
        buf.write("\2\2\u00a9\u00aa\7(\2\2\u00aa\u00ab\7(\2\2\u00ab(\3\2")
        buf.write("\2\2\u00ac\u00ad\7~\2\2\u00ad\u00ae\7~\2\2\u00ae*\3\2")
        buf.write("\2\2\u00af\u00b0\7(\2\2\u00b0,\3\2\2\2\u00b1\u00b2\7~")
        buf.write("\2\2\u00b2.\3\2\2\2\u00b3\u00b4\7\u0080\2\2\u00b4\60\3")
        buf.write("\2\2\2\u00b5\u00b6\t\2\2\2\u00b6\u00b8\t\3\2\2\u00b7\u00b9")
        buf.write("\t\4\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00c2\3\2\2\2")
        buf.write("\u00bc\u00be\t\5\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3")
        buf.write("\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2")
        buf.write("\3\2\2\2\u00c1\u00b5\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c2")
        buf.write("\62\3\2\2\2\u00c3\u00c6\t\6\2\2\u00c4\u00c7\5\33\16\2")
        buf.write("\u00c5\u00c7\5\31\r\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8")
        buf.write("\u00ca\t\5\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\64\3\2")
        buf.write("\2\2\u00cd\u00cf\5\61\31\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d4\5\17\b\2\u00d1")
        buf.write("\u00d3\t\5\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d8\3")
        buf.write("\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d9\5\63\32\2\u00d8")
        buf.write("\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\66\3\2\2\2\u00da")
        buf.write("\u00df\t\7\2\2\u00db\u00de\n\b\2\2\u00dc\u00de\59\35\2")
        buf.write("\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3")
        buf.write("\2\2\2\u00df\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e2")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\t\7\2\2\u00e3")
        buf.write("8\3\2\2\2\u00e4\u00e5\7^\2\2\u00e5\u00f7\7p\2\2\u00e6")
        buf.write("\u00e7\7^\2\2\u00e7\u00f7\7t\2\2\u00e8\u00e9\7^\2\2\u00e9")
        buf.write("\u00f7\7^\2\2\u00ea\u00eb\7^\2\2\u00eb\u00f7\7v\2\2\u00ec")
        buf.write("\u00ed\7^\2\2\u00ed\u00f7\7\62\2\2\u00ee\u00ef\7^\2\2")
        buf.write("\u00ef\u00f0\7\u00e4\2\2\u00f0\u00f1\7\u20ae\2\2\u00f1")
        buf.write("\u00f7\7\u2124\2\2\u00f2\u00f3\7^\2\2\u00f3\u00f4\t\3")
        buf.write("\2\2\u00f4\u00f5\t\4\2\2\u00f5\u00f7\t\4\2\2\u00f6\u00e4")
        buf.write("\3\2\2\2\u00f6\u00e6\3\2\2\2\u00f6\u00e8\3\2\2\2\u00f6")
        buf.write("\u00ea\3\2\2\2\u00f6\u00ec\3\2\2\2\u00f6\u00ee\3\2\2\2")
        buf.write("\u00f6\u00f2\3\2\2\2\u00f7:\3\2\2\2\u00f8\u00fb\5{>\2")
        buf.write("\u00f9\u00fb\5y=\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2")
        buf.write("\2\2\u00fb<\3\2\2\2\u00fc\u00fd\7?\2\2\u00fd\u0101\7?")
        buf.write("\2\2\u00fe\u00ff\7#\2\2\u00ff\u0101\7?\2\2\u0100\u00fc")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0101>\3\2\2\2\u0102\u0103")
        buf.write("\7>\2\2\u0103\u0108\7?\2\2\u0104\u0108\t\t\2\2\u0105\u0106")
        buf.write("\7@\2\2\u0106\u0108\7?\2\2\u0107\u0102\3\2\2\2\u0107\u0104")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0108@\3\2\2\2\u0109\u010a")
        buf.write("\7f\2\2\u010a\u010b\7g\2\2\u010b\u010c\7e\2\2\u010c\u010d")
        buf.write("\7n\2\2\u010d\u010e\7c\2\2\u010e\u010f\7t\2\2\u010f\u0110")
        buf.write("\7g\2\2\u0110B\3\2\2\2\u0111\u0112\7t\2\2\u0112\u0113")
        buf.write("\7g\2\2\u0113\u0114\7v\2\2\u0114\u0115\7w\2\2\u0115\u0116")
        buf.write("\7t\2\2\u0116\u0117\7p\2\2\u0117D\3\2\2\2\u0118\u0119")
        buf.write("\7d\2\2\u0119\u011a\7t\2\2\u011a\u011b\7g\2\2\u011b\u011c")
        buf.write("\7c\2\2\u011c\u011d\7m\2\2\u011dF\3\2\2\2\u011e\u011f")
        buf.write("\7e\2\2\u011f\u0120\7q\2\2\u0120\u0121\7p\2\2\u0121\u0122")
        buf.write("\7v\2\2\u0122\u0123\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125")
        buf.write("\7w\2\2\u0125\u0126\7g\2\2\u0126H\3\2\2\2\u0127\u0128")
        buf.write("\7f\2\2\u0128\u0129\7g\2\2\u0129\u012a\7u\2\2\u012a\u012b")
        buf.write("\7v\2\2\u012b\u012c\7t\2\2\u012c\u012d\7w\2\2\u012d\u012e")
        buf.write("\7e\2\2\u012e\u012f\7v\2\2\u012fJ\3\2\2\2\u0130\u0131")
        buf.write("\7v\2\2\u0131\u0132\7j\2\2\u0132\u0133\7k\2\2\u0133\u0134")
        buf.write("\7u\2\2\u0134L\3\2\2\2\u0135\u0136\7u\2\2\u0136\u0137")
        buf.write("\7w\2\2\u0137\u0138\7r\2\2\u0138\u0139\7g\2\2\u0139\u013a")
        buf.write("\7t\2\2\u013aN\3\2\2\2\u013b\u013c\7e\2\2\u013c\u013d")
        buf.write("\7q\2\2\u013d\u013e\7p\2\2\u013e\u013f\7u\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140P\3\2\2\2\u0141\u0142\7r\2\2\u0142\u0143")
        buf.write("\7t\2\2\u0143\u0144\7k\2\2\u0144\u0145\7x\2\2\u0145\u0146")
        buf.write("\7c\2\2\u0146\u0147\7v\2\2\u0147\u0148\7g\2\2\u0148R\3")
        buf.write("\2\2\2\u0149\u014a\7r\2\2\u014a\u014b\7w\2\2\u014b\u014c")
        buf.write("\7d\2\2\u014c\u014d\7n\2\2\u014d\u014e\7k\2\2\u014e\u014f")
        buf.write("\7e\2\2\u014fT\3\2\2\2\u0150\u0151\7r\2\2\u0151\u0152")
        buf.write("\7t\2\2\u0152\u0153\7q\2\2\u0153\u0154\7v\2\2\u0154\u0155")
        buf.write("\7g\2\2\u0155\u0156\7e\2\2\u0156\u0157\7v\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158\u0159\7f\2\2\u0159V\3\2\2\2\u015a\u015b")
        buf.write("\7k\2\2\u015b\u015c\7p\2\2\u015c\u015d\7v\2\2\u015dX\3")
        buf.write("\2\2\2\u015e\u015f\7d\2\2\u015f\u0160\7q\2\2\u0160\u0161")
        buf.write("\7q\2\2\u0161\u0162\7n\2\2\u0162Z\3\2\2\2\u0163\u0164")
        buf.write("\7h\2\2\u0164\u0165\7n\2\2\u0165\u0166\7q\2\2\u0166\u0167")
        buf.write("\7c\2\2\u0167\u0168\7v\2\2\u0168\\\3\2\2\2\u0169\u016a")
        buf.write("\7u\2\2\u016a\u016b\7v\2\2\u016b\u016c\7t\2\2\u016c\u016d")
        buf.write("\7k\2\2\u016d\u016e\7p\2\2\u016e\u016f\7i\2\2\u016f^\3")
        buf.write("\2\2\2\u0170\u0171\7h\2\2\u0171\u0172\7w\2\2\u0172\u0173")
        buf.write("\7p\2\2\u0173\u0174\7e\2\2\u0174\u0175\7v\2\2\u0175\u0176")
        buf.write("\7k\2\2\u0176\u0177\7q\2\2\u0177\u0178\7p\2\2\u0178`\3")
        buf.write("\2\2\2\u0179\u017a\7e\2\2\u017a\u017b\7c\2\2\u017b\u017c")
        buf.write("\7u\2\2\u017c\u017d\7g\2\2\u017db\3\2\2\2\u017e\u017f")
        buf.write("\7f\2\2\u017f\u0180\7g\2\2\u0180\u0181\7h\2\2\u0181\u0182")
        buf.write("\7c\2\2\u0182\u0183\7w\2\2\u0183\u0184\7n\2\2\u0184\u0185")
        buf.write("\7v\2\2\u0185d\3\2\2\2\u0186\u0187\7t\2\2\u0187\u0188")
        buf.write("\7g\2\2\u0188\u0189\7c\2\2\u0189\u018a\7f\2\2\u018af\3")
        buf.write("\2\2\2\u018b\u018c\7y\2\2\u018c\u018d\7t\2\2\u018d\u018e")
        buf.write("\7k\2\2\u018e\u018f\7v\2\2\u018f\u0190\7g\2\2\u0190h\3")
        buf.write("\2\2\2\u0191\u0192\7y\2\2\u0192\u0193\7j\2\2\u0193\u0194")
        buf.write("\7k\2\2\u0194\u0195\7n\2\2\u0195\u0196\7g\2\2\u0196j\3")
        buf.write("\2\2\2\u0197\u0198\7c\2\2\u0198\u0199\7n\2\2\u0199\u019a")
        buf.write("\7n\2\2\u019a\u019b\7q\2\2\u019b\u019c\7e\2\2\u019c\u019d")
        buf.write("\7c\2\2\u019d\u019e\7v\2\2\u019e\u019f\7g\2\2\u019fl\3")
        buf.write("\2\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2\7{\2\2\u01a2\u01a3")
        buf.write("\7r\2\2\u01a3\u01a4\7g\2\2\u01a4\u01a5\7a\2\2\u01a5n\3")
        buf.write("\2\2\2\u01a6\u01a7\7p\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9")
        buf.write("\7n\2\2\u01a9p\3\2\2\2\u01aa\u01ab\7k\2\2\u01ab\u01ac")
        buf.write("\7h\2\2\u01acr\3\2\2\2\u01ad\u01ae\7g\2\2\u01ae\u01af")
        buf.write("\7n\2\2\u01af\u01b0\7u\2\2\u01b0\u01b1\7g\2\2\u01b1t\3")
        buf.write("\2\2\2\u01b2\u01b3\7u\2\2\u01b3\u01b4\7y\2\2\u01b4\u01b5")
        buf.write("\7k\2\2\u01b5\u01b6\7v\2\2\u01b6\u01b7\7e\2\2\u01b7\u01b8")
        buf.write("\7j\2\2\u01b8v\3\2\2\2\u01b9\u01ba\7h\2\2\u01ba\u01bb")
        buf.write("\7q\2\2\u01bb\u01bc\7t\2\2\u01bcx\3\2\2\2\u01bd\u01be")
        buf.write("\7h\2\2\u01be\u01bf\7c\2\2\u01bf\u01c0\7n\2\2\u01c0\u01c1")
        buf.write("\7u\2\2\u01c1\u01c2\7g\2\2\u01c2z\3\2\2\2\u01c3\u01c4")
        buf.write("\7v\2\2\u01c4\u01c5\7t\2\2\u01c5\u01c6\7w\2\2\u01c6\u01c7")
        buf.write("\7g\2\2\u01c7|\3\2\2\2\u01c8\u01c9\7q\2\2\u01c9\u01ca")
        buf.write("\7h\2\2\u01ca~\3\2\2\2\u01cb\u01cf\t\n\2\2\u01cc\u01ce")
        buf.write("\t\13\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u0080\3\2\2\2")
        buf.write("\u01d1\u01cf\3\2\2\2\u01d2\u01d3\7\'\2\2\u01d3\u01d4\7")
        buf.write("\'\2\2\u01d4\u01d8\3\2\2\2\u01d5\u01d7\n\f\2\2\u01d6\u01d5")
        buf.write("\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d9\3\2\2\2\u01d9\u01e7\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01db\u01dc\7\'\2\2\u01dc\u01dd\7\u0080\2\2\u01dd\u01e1")
        buf.write("\3\2\2\2\u01de\u01e0\13\2\2\2\u01df\u01de\3\2\2\2\u01e0")
        buf.write("\u01e3\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u01e5\7")
        buf.write("\u0080\2\2\u01e5\u01e7\7\'\2\2\u01e6\u01d2\3\2\2\2\u01e6")
        buf.write("\u01db\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\bA\2\2")
        buf.write("\u01e9\u0082\3\2\2\2\u01ea\u01ec\t\r\2\2\u01eb\u01ea\3")
        buf.write("\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0\bB\2\2\u01f0")
        buf.write("\u0084\3\2\2\2\26\2\u00ba\u00bf\u00c1\u00c6\u00cb\u00ce")
        buf.write("\u00d4\u00d8\u00dd\u00df\u00f6\u00fa\u0100\u0107\u01cf")
        buf.write("\u01d8\u01e1\u01e6\u01ed\3\b\2\2")
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
            "'read'", "'write'", "'while'", "'allocate'", "'type_'", "'nil'", 
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


