# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammar.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\6\31\u00b5\n\31\r\31\16\31\u00b6\3\31\6\31\u00ba\n\31")
        buf.write("\r\31\16\31\u00bb\5\31\u00be\n\31\3\32\3\32\3\32\5\32")
        buf.write("\u00c3\n\32\3\32\6\32\u00c6\n\32\r\32\16\32\u00c7\3\33")
        buf.write("\5\33\u00cb\n\33\3\33\3\33\7\33\u00cf\n\33\f\33\16\33")
        buf.write("\u00d2\13\33\3\33\5\33\u00d5\n\33\3\34\3\34\3\34\7\34")
        buf.write("\u00da\n\34\f\34\16\34\u00dd\13\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u00f1\n\35\3\36\3\36\5\36\u00f5\n")
        buf.write("\36\3\37\3\37\3\37\3\37\5\37\u00fb\n\37\3 \3 \3 \3 \3")
        buf.write(" \5 \u0102\n \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\39\39\39\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3")
        buf.write("<\3<\3<\3<\3<\3=\3=\3=\3>\3>\7>\u01bc\n>\f>\16>\u01bf")
        buf.write("\13>\3?\3?\3?\3?\7?\u01c5\n?\f?\16?\u01c8\13?\3?\3?\3")
        buf.write("?\3?\7?\u01ce\n?\f?\16?\u01d1\13?\3?\3?\5?\u01d5\n?\3")
        buf.write("?\3?\3@\6@\u01da\n@\r@\16@\u01db\3@\3@\4\u00db\u01cf\2")
        buf.write("A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;")
        buf.write("u<w=y>{?}@\177A\3\2\16\3\2\62\62\4\2ZZzz\5\2\62;CHch\3")
        buf.write("\2\62;\4\2GGgg\3\2))\3\2^^\4\2>>@@\6\2%%C\\aac|\7\2%%")
        buf.write("\62;C\\aac|\3\2\f\f\5\2\13\f\17\17\"\"\2\u01f8\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u0083\3")
        buf.write("\2\2\2\7\u0085\3\2\2\2\t\u0087\3\2\2\2\13\u0089\3\2\2")
        buf.write("\2\r\u008b\3\2\2\2\17\u008d\3\2\2\2\21\u008f\3\2\2\2\23")
        buf.write("\u0091\3\2\2\2\25\u0093\3\2\2\2\27\u0095\3\2\2\2\31\u0097")
        buf.write("\3\2\2\2\33\u0099\3\2\2\2\35\u009b\3\2\2\2\37\u009d\3")
        buf.write("\2\2\2!\u009f\3\2\2\2#\u00a1\3\2\2\2%\u00a3\3\2\2\2\'")
        buf.write("\u00a5\3\2\2\2)\u00a8\3\2\2\2+\u00ab\3\2\2\2-\u00ad\3")
        buf.write("\2\2\2/\u00af\3\2\2\2\61\u00bd\3\2\2\2\63\u00bf\3\2\2")
        buf.write("\2\65\u00ca\3\2\2\2\67\u00d6\3\2\2\29\u00f0\3\2\2\2;\u00f4")
        buf.write("\3\2\2\2=\u00fa\3\2\2\2?\u0101\3\2\2\2A\u0103\3\2\2\2")
        buf.write("C\u010b\3\2\2\2E\u0112\3\2\2\2G\u0118\3\2\2\2I\u0121\3")
        buf.write("\2\2\2K\u012a\3\2\2\2M\u012f\3\2\2\2O\u0135\3\2\2\2Q\u013b")
        buf.write("\3\2\2\2S\u0143\3\2\2\2U\u014a\3\2\2\2W\u0154\3\2\2\2")
        buf.write("Y\u0158\3\2\2\2[\u015d\3\2\2\2]\u0163\3\2\2\2_\u016a\3")
        buf.write("\2\2\2a\u0173\3\2\2\2c\u0178\3\2\2\2e\u0180\3\2\2\2g\u0186")
        buf.write("\3\2\2\2i\u018f\3\2\2\2k\u0194\3\2\2\2m\u0198\3\2\2\2")
        buf.write("o\u019b\3\2\2\2q\u01a0\3\2\2\2s\u01a7\3\2\2\2u\u01ab\3")
        buf.write("\2\2\2w\u01b1\3\2\2\2y\u01b6\3\2\2\2{\u01b9\3\2\2\2}\u01d4")
        buf.write("\3\2\2\2\177\u01d9\3\2\2\2\u0081\u0082\7}\2\2\u0082\4")
        buf.write("\3\2\2\2\u0083\u0084\7\177\2\2\u0084\6\3\2\2\2\u0085\u0086")
        buf.write("\7*\2\2\u0086\b\3\2\2\2\u0087\u0088\7+\2\2\u0088\n\3\2")
        buf.write("\2\2\u0089\u008a\7]\2\2\u008a\f\3\2\2\2\u008b\u008c\7")
        buf.write("_\2\2\u008c\16\3\2\2\2\u008d\u008e\7\60\2\2\u008e\20\3")
        buf.write("\2\2\2\u008f\u0090\7?\2\2\u0090\22\3\2\2\2\u0091\u0092")
        buf.write("\7=\2\2\u0092\24\3\2\2\2\u0093\u0094\7<\2\2\u0094\26\3")
        buf.write("\2\2\2\u0095\u0096\7.\2\2\u0096\30\3\2\2\2\u0097\u0098")
        buf.write("\7/\2\2\u0098\32\3\2\2\2\u0099\u009a\7-\2\2\u009a\34\3")
        buf.write("\2\2\2\u009b\u009c\7,\2\2\u009c\36\3\2\2\2\u009d\u009e")
        buf.write("\7`\2\2\u009e \3\2\2\2\u009f\u00a0\7\61\2\2\u00a0\"\3")
        buf.write("\2\2\2\u00a1\u00a2\7\'\2\2\u00a2$\3\2\2\2\u00a3\u00a4")
        buf.write("\7#\2\2\u00a4&\3\2\2\2\u00a5\u00a6\7(\2\2\u00a6\u00a7")
        buf.write("\7(\2\2\u00a7(\3\2\2\2\u00a8\u00a9\7~\2\2\u00a9\u00aa")
        buf.write("\7~\2\2\u00aa*\3\2\2\2\u00ab\u00ac\7(\2\2\u00ac,\3\2\2")
        buf.write("\2\u00ad\u00ae\7~\2\2\u00ae.\3\2\2\2\u00af\u00b0\7\u0080")
        buf.write("\2\2\u00b0\60\3\2\2\2\u00b1\u00b2\t\2\2\2\u00b2\u00b4")
        buf.write("\t\3\2\2\u00b3\u00b5\t\4\2\2\u00b4\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00be\3\2\2\2\u00b8\u00ba\t\5\2\2\u00b9\u00b8\3")
        buf.write("\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc")
        buf.write("\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd\u00b1\3\2\2\2\u00bd")
        buf.write("\u00b9\3\2\2\2\u00be\62\3\2\2\2\u00bf\u00c2\t\6\2\2\u00c0")
        buf.write("\u00c3\5\33\16\2\u00c1\u00c3\5\31\r\2\u00c2\u00c0\3\2")
        buf.write("\2\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5")
        buf.write("\3\2\2\2\u00c4\u00c6\t\5\2\2\u00c5\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\64\3\2\2\2\u00c9\u00cb\5\61\31\2\u00ca\u00c9\3")
        buf.write("\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00d0")
        buf.write("\5\17\b\2\u00cd\u00cf\t\5\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d5\5")
        buf.write("\63\32\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\66\3\2\2\2\u00d6\u00db\t\7\2\2\u00d7\u00da\n\b\2\2\u00d8")
        buf.write("\u00da\59\35\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2")
        buf.write("\u00da\u00dd\3\2\2\2\u00db\u00dc\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df")
        buf.write("\t\7\2\2\u00df8\3\2\2\2\u00e0\u00e1\7^\2\2\u00e1\u00f1")
        buf.write("\7p\2\2\u00e2\u00e3\7^\2\2\u00e3\u00f1\7t\2\2\u00e4\u00e5")
        buf.write("\7^\2\2\u00e5\u00f1\7^\2\2\u00e6\u00e7\7^\2\2\u00e7\u00f1")
        buf.write("\7v\2\2\u00e8\u00e9\7^\2\2\u00e9\u00f1\7\62\2\2\u00ea")
        buf.write("\u00eb\7^\2\2\u00eb\u00f1\7)\2\2\u00ec\u00ed\7^\2\2\u00ed")
        buf.write("\u00ee\t\3\2\2\u00ee\u00ef\t\4\2\2\u00ef\u00f1\t\4\2\2")
        buf.write("\u00f0\u00e0\3\2\2\2\u00f0\u00e2\3\2\2\2\u00f0\u00e4\3")
        buf.write("\2\2\2\u00f0\u00e6\3\2\2\2\u00f0\u00e8\3\2\2\2\u00f0\u00ea")
        buf.write("\3\2\2\2\u00f0\u00ec\3\2\2\2\u00f1:\3\2\2\2\u00f2\u00f5")
        buf.write("\5w<\2\u00f3\u00f5\5u;\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f5<\3\2\2\2\u00f6\u00f7\7?\2\2\u00f7\u00fb")
        buf.write("\7?\2\2\u00f8\u00f9\7#\2\2\u00f9\u00fb\7?\2\2\u00fa\u00f6")
        buf.write("\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb>\3\2\2\2\u00fc\u00fd")
        buf.write("\7>\2\2\u00fd\u0102\7?\2\2\u00fe\u0102\t\t\2\2\u00ff\u0100")
        buf.write("\7@\2\2\u0100\u0102\7?\2\2\u0101\u00fc\3\2\2\2\u0101\u00fe")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0102@\3\2\2\2\u0103\u0104")
        buf.write("\7f\2\2\u0104\u0105\7g\2\2\u0105\u0106\7e\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107\u0108\7c\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010aB\3\2\2\2\u010b\u010c\7t\2\2\u010c\u010d")
        buf.write("\7g\2\2\u010d\u010e\7v\2\2\u010e\u010f\7w\2\2\u010f\u0110")
        buf.write("\7t\2\2\u0110\u0111\7p\2\2\u0111D\3\2\2\2\u0112\u0113")
        buf.write("\7d\2\2\u0113\u0114\7t\2\2\u0114\u0115\7g\2\2\u0115\u0116")
        buf.write("\7c\2\2\u0116\u0117\7m\2\2\u0117F\3\2\2\2\u0118\u0119")
        buf.write("\7e\2\2\u0119\u011a\7q\2\2\u011a\u011b\7p\2\2\u011b\u011c")
        buf.write("\7v\2\2\u011c\u011d\7k\2\2\u011d\u011e\7p\2\2\u011e\u011f")
        buf.write("\7w\2\2\u011f\u0120\7g\2\2\u0120H\3\2\2\2\u0121\u0122")
        buf.write("\7f\2\2\u0122\u0123\7g\2\2\u0123\u0124\7u\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7t\2\2\u0126\u0127\7w\2\2\u0127\u0128")
        buf.write("\7e\2\2\u0128\u0129\7v\2\2\u0129J\3\2\2\2\u012a\u012b")
        buf.write("\7v\2\2\u012b\u012c\7j\2\2\u012c\u012d\7k\2\2\u012d\u012e")
        buf.write("\7u\2\2\u012eL\3\2\2\2\u012f\u0130\7u\2\2\u0130\u0131")
        buf.write("\7w\2\2\u0131\u0132\7r\2\2\u0132\u0133\7g\2\2\u0133\u0134")
        buf.write("\7t\2\2\u0134N\3\2\2\2\u0135\u0136\7e\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137\u0138\7p\2\2\u0138\u0139\7u\2\2\u0139\u013a")
        buf.write("\7v\2\2\u013aP\3\2\2\2\u013b\u013c\7r\2\2\u013c\u013d")
        buf.write("\7t\2\2\u013d\u013e\7k\2\2\u013e\u013f\7x\2\2\u013f\u0140")
        buf.write("\7c\2\2\u0140\u0141\7v\2\2\u0141\u0142\7g\2\2\u0142R\3")
        buf.write("\2\2\2\u0143\u0144\7r\2\2\u0144\u0145\7w\2\2\u0145\u0146")
        buf.write("\7d\2\2\u0146\u0147\7n\2\2\u0147\u0148\7k\2\2\u0148\u0149")
        buf.write("\7e\2\2\u0149T\3\2\2\2\u014a\u014b\7r\2\2\u014b\u014c")
        buf.write("\7t\2\2\u014c\u014d\7q\2\2\u014d\u014e\7v\2\2\u014e\u014f")
        buf.write("\7g\2\2\u014f\u0150\7e\2\2\u0150\u0151\7v\2\2\u0151\u0152")
        buf.write("\7g\2\2\u0152\u0153\7f\2\2\u0153V\3\2\2\2\u0154\u0155")
        buf.write("\7k\2\2\u0155\u0156\7p\2\2\u0156\u0157\7v\2\2\u0157X\3")
        buf.write("\2\2\2\u0158\u0159\7d\2\2\u0159\u015a\7q\2\2\u015a\u015b")
        buf.write("\7q\2\2\u015b\u015c\7n\2\2\u015cZ\3\2\2\2\u015d\u015e")
        buf.write("\7h\2\2\u015e\u015f\7n\2\2\u015f\u0160\7q\2\2\u0160\u0161")
        buf.write("\7c\2\2\u0161\u0162\7v\2\2\u0162\\\3\2\2\2\u0163\u0164")
        buf.write("\7u\2\2\u0164\u0165\7v\2\2\u0165\u0166\7t\2\2\u0166\u0167")
        buf.write("\7k\2\2\u0167\u0168\7p\2\2\u0168\u0169\7i\2\2\u0169^\3")
        buf.write("\2\2\2\u016a\u016b\7h\2\2\u016b\u016c\7w\2\2\u016c\u016d")
        buf.write("\7p\2\2\u016d\u016e\7e\2\2\u016e\u016f\7v\2\2\u016f\u0170")
        buf.write("\7k\2\2\u0170\u0171\7q\2\2\u0171\u0172\7p\2\2\u0172`\3")
        buf.write("\2\2\2\u0173\u0174\7e\2\2\u0174\u0175\7c\2\2\u0175\u0176")
        buf.write("\7u\2\2\u0176\u0177\7g\2\2\u0177b\3\2\2\2\u0178\u0179")
        buf.write("\7f\2\2\u0179\u017a\7g\2\2\u017a\u017b\7h\2\2\u017b\u017c")
        buf.write("\7c\2\2\u017c\u017d\7w\2\2\u017d\u017e\7n\2\2\u017e\u017f")
        buf.write("\7v\2\2\u017fd\3\2\2\2\u0180\u0181\7y\2\2\u0181\u0182")
        buf.write("\7j\2\2\u0182\u0183\7k\2\2\u0183\u0184\7n\2\2\u0184\u0185")
        buf.write("\7g\2\2\u0185f\3\2\2\2\u0186\u0187\7c\2\2\u0187\u0188")
        buf.write("\7n\2\2\u0188\u0189\7n\2\2\u0189\u018a\7q\2\2\u018a\u018b")
        buf.write("\7e\2\2\u018b\u018c\7c\2\2\u018c\u018d\7v\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018eh\3\2\2\2\u018f\u0190\7v\2\2\u0190\u0191")
        buf.write("\7{\2\2\u0191\u0192\7r\2\2\u0192\u0193\7g\2\2\u0193j\3")
        buf.write("\2\2\2\u0194\u0195\7p\2\2\u0195\u0196\7k\2\2\u0196\u0197")
        buf.write("\7n\2\2\u0197l\3\2\2\2\u0198\u0199\7k\2\2\u0199\u019a")
        buf.write("\7h\2\2\u019an\3\2\2\2\u019b\u019c\7g\2\2\u019c\u019d")
        buf.write("\7n\2\2\u019d\u019e\7u\2\2\u019e\u019f\7g\2\2\u019fp\3")
        buf.write("\2\2\2\u01a0\u01a1\7u\2\2\u01a1\u01a2\7y\2\2\u01a2\u01a3")
        buf.write("\7k\2\2\u01a3\u01a4\7v\2\2\u01a4\u01a5\7e\2\2\u01a5\u01a6")
        buf.write("\7j\2\2\u01a6r\3\2\2\2\u01a7\u01a8\7h\2\2\u01a8\u01a9")
        buf.write("\7q\2\2\u01a9\u01aa\7t\2\2\u01aat\3\2\2\2\u01ab\u01ac")
        buf.write("\7h\2\2\u01ac\u01ad\7c\2\2\u01ad\u01ae\7n\2\2\u01ae\u01af")
        buf.write("\7u\2\2\u01af\u01b0\7g\2\2\u01b0v\3\2\2\2\u01b1\u01b2")
        buf.write("\7v\2\2\u01b2\u01b3\7t\2\2\u01b3\u01b4\7w\2\2\u01b4\u01b5")
        buf.write("\7g\2\2\u01b5x\3\2\2\2\u01b6\u01b7\7q\2\2\u01b7\u01b8")
        buf.write("\7h\2\2\u01b8z\3\2\2\2\u01b9\u01bd\t\n\2\2\u01ba\u01bc")
        buf.write("\t\13\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be|\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01c0\u01c1\7\'\2\2\u01c1\u01c2\7\'\2\2")
        buf.write("\u01c2\u01c6\3\2\2\2\u01c3\u01c5\n\f\2\2\u01c4\u01c3\3")
        buf.write("\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01d5\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9")
        buf.write("\u01ca\7\'\2\2\u01ca\u01cb\7\u0080\2\2\u01cb\u01cf\3\2")
        buf.write("\2\2\u01cc\u01ce\13\2\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01d1")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0")
        buf.write("\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\7\u0080")
        buf.write("\2\2\u01d3\u01d5\7\'\2\2\u01d4\u01c0\3\2\2\2\u01d4\u01c9")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7\b?\2\2\u01d7")
        buf.write("~\3\2\2\2\u01d8\u01da\t\r\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("\u01db\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2")
        buf.write("\u01dc\u01dd\3\2\2\2\u01dd\u01de\b@\2\2\u01de\u0080\3")
        buf.write("\2\2\2\26\2\u00b6\u00bb\u00bd\u00c2\u00c7\u00ca\u00d0")
        buf.write("\u00d4\u00d9\u00db\u00f0\u00f4\u00fa\u0101\u01bd\u01c6")
        buf.write("\u01cf\u01d4\u01db\3\b\2\2")
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
    KEYWORD_WHILE = 50
    KEYWORD_ALLOCATE = 51
    KEYWORD_TYPE = 52
    KEYWORD_NIL = 53
    KEYWORD_IF = 54
    KEYWORD_ELSE = 55
    KEYWORD_SWITCH = 56
    KEYWORD_FOR = 57
    KEYWORD_FALSE = 58
    KEYWORD_TRUE = 59
    KEYWORD_OF = 60
    ID = 61
    COMMENT = 62
    WHITESPACE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'('", "')'", "'['", "']'", "'.'", "'='", "';'", 
            "':'", "','", "'-'", "'+'", "'*'", "'^'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'&'", "'|'", "'~'", "'declare'", "'return'", 
            "'break'", "'continue'", "'destruct'", "'this'", "'super'", 
            "'const'", "'private'", "'public'", "'protected'", "'int'", 
            "'bool'", "'float'", "'string'", "'function'", "'case'", "'default'", 
            "'while'", "'allocate'", "'type'", "'nil'", "'if'", "'else'", 
            "'switch'", "'for'", "'false'", "'true'", "'of'" ]

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
            "KEYWORD_DEFAULT", "KEYWORD_WHILE", "KEYWORD_ALLOCATE", "KEYWORD_TYPE", 
            "KEYWORD_NIL", "KEYWORD_IF", "KEYWORD_ELSE", "KEYWORD_SWITCH", 
            "KEYWORD_FOR", "KEYWORD_FALSE", "KEYWORD_TRUE", "KEYWORD_OF", 
            "ID", "COMMENT", "WHITESPACE" ]

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
                  "KEYWORD_DEFAULT", "KEYWORD_WHILE", "KEYWORD_ALLOCATE", 
                  "KEYWORD_TYPE", "KEYWORD_NIL", "KEYWORD_IF", "KEYWORD_ELSE", 
                  "KEYWORD_SWITCH", "KEYWORD_FOR", "KEYWORD_FALSE", "KEYWORD_TRUE", 
                  "KEYWORD_OF", "ID", "COMMENT", "WHITESPACE" ]

    grammarFileName = "LuLu2Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


