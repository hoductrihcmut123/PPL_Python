# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u020e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3x\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\5\5\u0084\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u008b\n\6")
        buf.write("\3\7\3\7\5\7\u008f\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0097")
        buf.write("\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u00a0\n\t\3\n\3\n")
        buf.write("\3\n\5\n\u00a5\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b5\n\f\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00bb\n\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00d4\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u00e3")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00f9\n\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0101\n")
        buf.write("\26\3\27\3\27\3\27\3\27\5\27\u0107\n\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0117\n\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u0125\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u013d\n")
        buf.write("\35\3\36\3\36\5\36\u0141\n\36\3\37\3\37\3\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\5!\u0153\n!\3\"\3\"\3\"")
        buf.write("\3#\3#\3$\3$\3%\3%\3%\5%\u015f\n%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\5&\u016f\n&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u0176\n\'\3(\3(\3(\3(\3(\5(\u017d\n(\3)\3)\3)\3)")
        buf.write("\3)\3)\7)\u0185\n)\f)\16)\u0188\13)\3*\3*\3*\3*\3*\3*")
        buf.write("\7*\u0190\n*\f*\16*\u0193\13*\3+\3+\3+\3+\3+\3+\7+\u019b")
        buf.write("\n+\f+\16+\u019e\13+\3,\3,\3,\5,\u01a3\n,\3-\3-\3-\5-")
        buf.write("\u01a8\n-\3.\3.\3.\3.\3.\3.\3.\3.\7.\u01b2\n.\f.\16.\u01b5")
        buf.write("\13.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u01c4\n")
        buf.write("/\f/\16/\u01c7\13/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\5\60\u01d4\n\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\5\61\u01de\n\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u01e5\n\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u01ee\n\63\3\64\3\64\5\64\u01f2\n\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u01f9\n\65\3\66\3\66\3\67\3")
        buf.write("\67\3\67\3\67\3\67\7\67\u0202\n\67\f\67\16\67\u0205\13")
        buf.write("\67\3\67\5\67\u0208\n\67\3\67\3\67\38\38\38\2\7PRTZ\\")
        buf.write("9\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\r\4\2\27\27\34\34")
        buf.write("\6\2\f\f\21\21\26\26\33\33\5\2\16\16\23\23?@\4\2!!@@\3")
        buf.write("\2;<\4\2\64\64\66:\3\2\62\63\3\2,-\3\2.\60\3\2\4\5\3\2")
        buf.write("?@\2\u020f\2p\3\2\2\2\4w\3\2\2\2\6y\3\2\2\2\b\u0083\3")
        buf.write("\2\2\2\n\u008a\3\2\2\2\f\u008e\3\2\2\2\16\u0090\3\2\2")
        buf.write("\2\20\u009f\3\2\2\2\22\u00a4\3\2\2\2\24\u00a6\3\2\2\2")
        buf.write("\26\u00b4\3\2\2\2\30\u00b6\3\2\2\2\32\u00c0\3\2\2\2\34")
        buf.write("\u00c5\3\2\2\2\36\u00c7\3\2\2\2 \u00d3\3\2\2\2\"\u00d5")
        buf.write("\3\2\2\2$\u00d9\3\2\2\2&\u00e2\3\2\2\2(\u00f8\3\2\2\2")
        buf.write("*\u00fa\3\2\2\2,\u0106\3\2\2\2.\u0108\3\2\2\2\60\u0116")
        buf.write("\3\2\2\2\62\u0118\3\2\2\2\64\u0124\3\2\2\2\66\u0126\3")
        buf.write("\2\2\28\u013c\3\2\2\2:\u0140\3\2\2\2<\u0142\3\2\2\2>\u0145")
        buf.write("\3\2\2\2@\u0152\3\2\2\2B\u0154\3\2\2\2D\u0157\3\2\2\2")
        buf.write("F\u0159\3\2\2\2H\u015b\3\2\2\2J\u016e\3\2\2\2L\u0175\3")
        buf.write("\2\2\2N\u017c\3\2\2\2P\u017e\3\2\2\2R\u0189\3\2\2\2T\u0194")
        buf.write("\3\2\2\2V\u01a2\3\2\2\2X\u01a7\3\2\2\2Z\u01a9\3\2\2\2")
        buf.write("\\\u01b6\3\2\2\2^\u01d3\3\2\2\2`\u01dd\3\2\2\2b\u01e4")
        buf.write("\3\2\2\2d\u01ed\3\2\2\2f\u01f1\3\2\2\2h\u01f8\3\2\2\2")
        buf.write("j\u01fa\3\2\2\2l\u01fc\3\2\2\2n\u020b\3\2\2\2pq\5\4\3")
        buf.write("\2qr\7\2\2\3r\3\3\2\2\2st\5\6\4\2tu\5\4\3\2ux\3\2\2\2")
        buf.write("vx\5\6\4\2ws\3\2\2\2wv\3\2\2\2x\5\3\2\2\2yz\7\22\2\2z")
        buf.write("{\7@\2\2{|\5\b\5\2|}\7$\2\2}~\5\n\6\2~\177\7%\2\2\177")
        buf.write("\7\3\2\2\2\u0080\u0081\7*\2\2\u0081\u0084\7@\2\2\u0082")
        buf.write("\u0084\3\2\2\2\u0083\u0080\3\2\2\2\u0083\u0082\3\2\2\2")
        buf.write("\u0084\t\3\2\2\2\u0085\u0086\5\f\7\2\u0086\u0087\5\n\6")
        buf.write("\2\u0087\u008b\3\2\2\2\u0088\u008b\5\f\7\2\u0089\u008b")
        buf.write("\3\2\2\2\u008a\u0085\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\13\3\2\2\2\u008c\u008f\5\16\b\2\u008d")
        buf.write("\u008f\5\36\20\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2")
        buf.write("\2\u008f\r\3\2\2\2\u0090\u0096\t\2\2\2\u0091\u0092\5\20")
        buf.write("\t\2\u0092\u0093\7*\2\2\u0093\u0094\5\22\n\2\u0094\u0097")
        buf.write("\3\2\2\2\u0095\u0097\5\24\13\2\u0096\u0091\3\2\2\2\u0096")
        buf.write("\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\7(\2\2")
        buf.write("\u0099\17\3\2\2\2\u009a\u009b\5n8\2\u009b\u009c\7)\2\2")
        buf.write("\u009c\u009d\5\20\t\2\u009d\u00a0\3\2\2\2\u009e\u00a0")
        buf.write("\5n8\2\u009f\u009a\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\21")
        buf.write("\3\2\2\2\u00a1\u00a5\5\34\17\2\u00a2\u00a5\5\30\r\2\u00a3")
        buf.write("\u00a5\5\32\16\2\u00a4\u00a1\3\2\2\2\u00a4\u00a2\3\2\2")
        buf.write("\2\u00a4\u00a3\3\2\2\2\u00a5\23\3\2\2\2\u00a6\u00a7\5")
        buf.write("n8\2\u00a7\u00a8\5\26\f\2\u00a8\u00a9\5L\'\2\u00a9\25")
        buf.write("\3\2\2\2\u00aa\u00ab\7)\2\2\u00ab\u00ac\5n8\2\u00ac\u00ad")
        buf.write("\5\26\f\2\u00ad\u00ae\5L\'\2\u00ae\u00af\7)\2\2\u00af")
        buf.write("\u00b5\3\2\2\2\u00b0\u00b1\7*\2\2\u00b1\u00b2\5\22\n\2")
        buf.write("\u00b2\u00b3\7\65\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00aa")
        buf.write("\3\2\2\2\u00b4\u00b0\3\2\2\2\u00b5\27\3\2\2\2\u00b6\u00b7")
        buf.write("\7\32\2\2\u00b7\u00ba\7&\2\2\u00b8\u00bb\5\34\17\2\u00b9")
        buf.write("\u00bb\5\30\r\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2")
        buf.write("\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\7)\2\2\u00bd\u00be")
        buf.write("\7\4\2\2\u00be\u00bf\7\'\2\2\u00bf\31\3\2\2\2\u00c0\u00c1")
        buf.write("\7\30\2\2\u00c1\u00c2\5n8\2\u00c2\u00c3\7\"\2\2\u00c3")
        buf.write("\u00c4\7#\2\2\u00c4\33\3\2\2\2\u00c5\u00c6\t\3\2\2\u00c6")
        buf.write("\35\3\2\2\2\u00c7\u00c8\t\4\2\2\u00c8\u00c9\7\"\2\2\u00c9")
        buf.write("\u00ca\5 \21\2\u00ca\u00cb\7#\2\2\u00cb\u00cc\5$\23\2")
        buf.write("\u00cc\37\3\2\2\2\u00cd\u00ce\5\"\22\2\u00ce\u00cf\7(")
        buf.write("\2\2\u00cf\u00d0\5 \21\2\u00d0\u00d4\3\2\2\2\u00d1\u00d4")
        buf.write("\5\"\22\2\u00d2\u00d4\3\2\2\2\u00d3\u00cd\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4!\3\2\2\2\u00d5")
        buf.write("\u00d6\5,\27\2\u00d6\u00d7\7*\2\2\u00d7\u00d8\5\22\n\2")
        buf.write("\u00d8#\3\2\2\2\u00d9\u00da\7$\2\2\u00da\u00db\5&\24\2")
        buf.write("\u00db\u00dc\7%\2\2\u00dc%\3\2\2\2\u00dd\u00de\5(\25\2")
        buf.write("\u00de\u00df\5&\24\2\u00df\u00e3\3\2\2\2\u00e0\u00e3\5")
        buf.write("(\25\2\u00e1\u00e3\3\2\2\2\u00e2\u00dd\3\2\2\2\u00e2\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\'\3\2\2\2\u00e4\u00e5")
        buf.write("\5*\26\2\u00e5\u00e6\7(\2\2\u00e6\u00f9\3\2\2\2\u00e7")
        buf.write("\u00e8\5\62\32\2\u00e8\u00e9\7(\2\2\u00e9\u00f9\3\2\2")
        buf.write("\2\u00ea\u00f9\5\66\34\2\u00eb\u00f9\5> \2\u00ec\u00ed")
        buf.write("\5D#\2\u00ed\u00ee\7(\2\2\u00ee\u00f9\3\2\2\2\u00ef\u00f0")
        buf.write("\5F$\2\u00f0\u00f1\7(\2\2\u00f1\u00f9\3\2\2\2\u00f2\u00f3")
        buf.write("\5H%\2\u00f3\u00f4\7(\2\2\u00f4\u00f9\3\2\2\2\u00f5\u00f6")
        buf.write("\5J&\2\u00f6\u00f7\7(\2\2\u00f7\u00f9\3\2\2\2\u00f8\u00e4")
        buf.write("\3\2\2\2\u00f8\u00e7\3\2\2\2\u00f8\u00ea\3\2\2\2\u00f8")
        buf.write("\u00eb\3\2\2\2\u00f8\u00ec\3\2\2\2\u00f8\u00ef\3\2\2\2")
        buf.write("\u00f8\u00f2\3\2\2\2\u00f8\u00f5\3\2\2\2\u00f9)\3\2\2")
        buf.write("\2\u00fa\u0100\t\2\2\2\u00fb\u00fc\5,\27\2\u00fc\u00fd")
        buf.write("\7*\2\2\u00fd\u00fe\5\22\n\2\u00fe\u0101\3\2\2\2\u00ff")
        buf.write("\u0101\5.\30\2\u0100\u00fb\3\2\2\2\u0100\u00ff\3\2\2\2")
        buf.write("\u0101+\3\2\2\2\u0102\u0103\7@\2\2\u0103\u0104\7)\2\2")
        buf.write("\u0104\u0107\5,\27\2\u0105\u0107\7@\2\2\u0106\u0102\3")
        buf.write("\2\2\2\u0106\u0105\3\2\2\2\u0107-\3\2\2\2\u0108\u0109")
        buf.write("\7@\2\2\u0109\u010a\5\60\31\2\u010a\u010b\5L\'\2\u010b")
        buf.write("/\3\2\2\2\u010c\u010d\7)\2\2\u010d\u010e\7@\2\2\u010e")
        buf.write("\u010f\5\60\31\2\u010f\u0110\5L\'\2\u0110\u0111\7)\2\2")
        buf.write("\u0111\u0117\3\2\2\2\u0112\u0113\7*\2\2\u0113\u0114\5")
        buf.write("\22\n\2\u0114\u0115\7\65\2\2\u0115\u0117\3\2\2\2\u0116")
        buf.write("\u010c\3\2\2\2\u0116\u0112\3\2\2\2\u0117\61\3\2\2\2\u0118")
        buf.write("\u0119\5\64\33\2\u0119\u011a\7\65\2\2\u011a\u011b\5L\'")
        buf.write("\2\u011b\63\3\2\2\2\u011c\u0125\5n8\2\u011d\u011e\5L\'")
        buf.write("\2\u011e\u011f\7=\2\2\u011f\u0120\7@\2\2\u0120\u0125\3")
        buf.write("\2\2\2\u0121\u0122\t\5\2\2\u0122\u0123\7>\2\2\u0123\u0125")
        buf.write("\7?\2\2\u0124\u011c\3\2\2\2\u0124\u011d\3\2\2\2\u0124")
        buf.write("\u0121\3\2\2\2\u0125\65\3\2\2\2\u0126\u0127\7\24\2\2\u0127")
        buf.write("\u0128\7\"\2\2\u0128\u0129\5L\'\2\u0129\u012a\7#\2\2\u012a")
        buf.write("\u012b\5$\23\2\u012b\u012c\58\35\2\u012c\u012d\5:\36\2")
        buf.write("\u012d\67\3\2\2\2\u012e\u012f\7\31\2\2\u012f\u0130\7\"")
        buf.write("\2\2\u0130\u0131\5L\'\2\u0131\u0132\7#\2\2\u0132\u0133")
        buf.write("\5$\23\2\u0133\u0134\58\35\2\u0134\u013d\3\2\2\2\u0135")
        buf.write("\u0136\7\31\2\2\u0136\u0137\7\"\2\2\u0137\u0138\5L\'\2")
        buf.write("\u0138\u0139\7#\2\2\u0139\u013a\5$\23\2\u013a\u013d\3")
        buf.write("\2\2\2\u013b\u013d\3\2\2\2\u013c\u012e\3\2\2\2\u013c\u0135")
        buf.write("\3\2\2\2\u013c\u013b\3\2\2\2\u013d9\3\2\2\2\u013e\u0141")
        buf.write("\5<\37\2\u013f\u0141\3\2\2\2\u0140\u013e\3\2\2\2\u0140")
        buf.write("\u013f\3\2\2\2\u0141;\3\2\2\2\u0142\u0143\7\36\2\2\u0143")
        buf.write("\u0144\5$\23\2\u0144=\3\2\2\2\u0145\u0146\7\13\2\2\u0146")
        buf.write("\u0147\7\"\2\2\u0147\u0148\5n8\2\u0148\u0149\7\37\2\2")
        buf.write("\u0149\u014a\5L\'\2\u014a\u014b\7+\2\2\u014b\u014c\5L")
        buf.write("\'\2\u014c\u014d\5@!\2\u014d\u014e\7#\2\2\u014e\u014f")
        buf.write("\5$\23\2\u014f?\3\2\2\2\u0150\u0153\5B\"\2\u0151\u0153")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("A\3\2\2\2\u0154\u0155\7\35\2\2\u0155\u0156\5L\'\2\u0156")
        buf.write("C\3\2\2\2\u0157\u0158\7\n\2\2\u0158E\3\2\2\2\u0159\u015a")
        buf.write("\7\17\2\2\u015aG\3\2\2\2\u015b\u015e\7 \2\2\u015c\u015f")
        buf.write("\5L\'\2\u015d\u015f\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015fI\3\2\2\2\u0160\u0161\5L\'\2\u0161")
        buf.write("\u0162\7=\2\2\u0162\u0163\5n8\2\u0163\u0164\7\"\2\2\u0164")
        buf.write("\u0165\5f\64\2\u0165\u0166\7#\2\2\u0166\u016f\3\2\2\2")
        buf.write("\u0167\u0168\7@\2\2\u0168\u0169\7>\2\2\u0169\u016a\7?")
        buf.write("\2\2\u016a\u016b\7\"\2\2\u016b\u016c\5f\64\2\u016c\u016d")
        buf.write("\7#\2\2\u016d\u016f\3\2\2\2\u016e\u0160\3\2\2\2\u016e")
        buf.write("\u0167\3\2\2\2\u016fK\3\2\2\2\u0170\u0171\5N(\2\u0171")
        buf.write("\u0172\t\6\2\2\u0172\u0173\5N(\2\u0173\u0176\3\2\2\2\u0174")
        buf.write("\u0176\5N(\2\u0175\u0170\3\2\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("M\3\2\2\2\u0177\u0178\5P)\2\u0178\u0179\t\7\2\2\u0179")
        buf.write("\u017a\5P)\2\u017a\u017d\3\2\2\2\u017b\u017d\5P)\2\u017c")
        buf.write("\u0177\3\2\2\2\u017c\u017b\3\2\2\2\u017dO\3\2\2\2\u017e")
        buf.write("\u017f\b)\1\2\u017f\u0180\5R*\2\u0180\u0186\3\2\2\2\u0181")
        buf.write("\u0182\f\4\2\2\u0182\u0183\t\b\2\2\u0183\u0185\5R*\2\u0184")
        buf.write("\u0181\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0186\u0187\3\2\2\2\u0187Q\3\2\2\2\u0188\u0186\3\2\2")
        buf.write("\2\u0189\u018a\b*\1\2\u018a\u018b\5T+\2\u018b\u0191\3")
        buf.write("\2\2\2\u018c\u018d\f\4\2\2\u018d\u018e\t\t\2\2\u018e\u0190")
        buf.write("\5T+\2\u018f\u018c\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192S\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0194\u0195\b+\1\2\u0195\u0196\5V,\2\u0196\u019c")
        buf.write("\3\2\2\2\u0197\u0198\f\4\2\2\u0198\u0199\t\n\2\2\u0199")
        buf.write("\u019b\5V,\2\u019a\u0197\3\2\2\2\u019b\u019e\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019dU\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019f\u01a0\7\61\2\2\u01a0\u01a3\5V,\2")
        buf.write("\u01a1\u01a3\5X-\2\u01a2\u019f\3\2\2\2\u01a2\u01a1\3\2")
        buf.write("\2\2\u01a3W\3\2\2\2\u01a4\u01a5\7-\2\2\u01a5\u01a8\5X")
        buf.write("-\2\u01a6\u01a8\5Z.\2\u01a7\u01a4\3\2\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8Y\3\2\2\2\u01a9\u01aa\b.\1\2\u01aa\u01ab")
        buf.write("\5\\/\2\u01ab\u01b3\3\2\2\2\u01ac\u01ad\f\4\2\2\u01ad")
        buf.write("\u01ae\7&\2\2\u01ae\u01af\5L\'\2\u01af\u01b0\7\'\2\2\u01b0")
        buf.write("\u01b2\3\2\2\2\u01b1\u01ac\3\2\2\2\u01b2\u01b5\3\2\2\2")
        buf.write("\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4[\3\2\2")
        buf.write("\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\b/\1\2\u01b7\u01b8")
        buf.write("\5^\60\2\u01b8\u01c5\3\2\2\2\u01b9\u01ba\f\5\2\2\u01ba")
        buf.write("\u01bb\7=\2\2\u01bb\u01c4\5n8\2\u01bc\u01bd\f\4\2\2\u01bd")
        buf.write("\u01be\7=\2\2\u01be\u01bf\5n8\2\u01bf\u01c0\7\"\2\2\u01c0")
        buf.write("\u01c1\5f\64\2\u01c1\u01c2\7#\2\2\u01c2\u01c4\3\2\2\2")
        buf.write("\u01c3\u01b9\3\2\2\2\u01c3\u01bc\3\2\2\2\u01c4\u01c7\3")
        buf.write("\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6]")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9\7@\2\2\u01c9")
        buf.write("\u01ca\7>\2\2\u01ca\u01d4\7?\2\2\u01cb\u01cc\7@\2\2\u01cc")
        buf.write("\u01cd\7>\2\2\u01cd\u01ce\7?\2\2\u01ce\u01cf\7\"\2\2\u01cf")
        buf.write("\u01d0\5f\64\2\u01d0\u01d1\7#\2\2\u01d1\u01d4\3\2\2\2")
        buf.write("\u01d2\u01d4\5`\61\2\u01d3\u01c8\3\2\2\2\u01d3\u01cb\3")
        buf.write("\2\2\2\u01d3\u01d2\3\2\2\2\u01d4_\3\2\2\2\u01d5\u01d6")
        buf.write("\7\30\2\2\u01d6\u01d7\5n8\2\u01d7\u01d8\7\"\2\2\u01d8")
        buf.write("\u01d9\5f\64\2\u01d9\u01da\7#\2\2\u01da\u01db\5`\61\2")
        buf.write("\u01db\u01de\3\2\2\2\u01dc\u01de\5b\62\2\u01dd\u01d5\3")
        buf.write("\2\2\2\u01dd\u01dc\3\2\2\2\u01dea\3\2\2\2\u01df\u01e0")
        buf.write("\7\"\2\2\u01e0\u01e1\5L\'\2\u01e1\u01e2\7#\2\2\u01e2\u01e5")
        buf.write("\3\2\2\2\u01e3\u01e5\5d\63\2\u01e4\u01df\3\2\2\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e5c\3\2\2\2\u01e6\u01ee\5j\66\2\u01e7")
        buf.write("\u01ee\7\6\2\2\u01e8\u01ee\7\7\2\2\u01e9\u01ee\7\b\2\2")
        buf.write("\u01ea\u01ee\5n8\2\u01eb\u01ee\7!\2\2\u01ec\u01ee\5l\67")
        buf.write("\2\u01ed\u01e6\3\2\2\2\u01ed\u01e7\3\2\2\2\u01ed\u01e8")
        buf.write("\3\2\2\2\u01ed\u01e9\3\2\2\2\u01ed\u01ea\3\2\2\2\u01ed")
        buf.write("\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01eee\3\2\2\2\u01ef")
        buf.write("\u01f2\5h\65\2\u01f0\u01f2\3\2\2\2\u01f1\u01ef\3\2\2\2")
        buf.write("\u01f1\u01f0\3\2\2\2\u01f2g\3\2\2\2\u01f3\u01f4\5L\'\2")
        buf.write("\u01f4\u01f5\7)\2\2\u01f5\u01f6\5h\65\2\u01f6\u01f9\3")
        buf.write("\2\2\2\u01f7\u01f9\5L\'\2\u01f8\u01f3\3\2\2\2\u01f8\u01f7")
        buf.write("\3\2\2\2\u01f9i\3\2\2\2\u01fa\u01fb\t\13\2\2\u01fbk\3")
        buf.write("\2\2\2\u01fc\u01fd\7\32\2\2\u01fd\u0207\7\"\2\2\u01fe")
        buf.write("\u0203\5L\'\2\u01ff\u0200\7)\2\2\u0200\u0202\5L\'\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0208\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0206\u0208\3\2\2\2\u0207\u01fe\3\2\2\2\u0207\u0206")
        buf.write("\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a\7#\2\2\u020a")
        buf.write("m\3\2\2\2\u020b\u020c\t\f\2\2\u020co\3\2\2\2)w\u0083\u008a")
        buf.write("\u008e\u0096\u009f\u00a4\u00b4\u00ba\u00d3\u00e2\u00f8")
        buf.write("\u0100\u0106\u0116\u0124\u013c\u0140\u0152\u015e\u016e")
        buf.write("\u0175\u017c\u0186\u0191\u019c\u01a2\u01a7\u01b3\u01c3")
        buf.write("\u01c5\u01d3\u01dd\u01e4\u01ed\u01f1\u01f8\u0203\u0207")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Break'", "'Foreach'", "'Int'", "'Null'", "'Constructor'", 
                     "'Continue'", "'True'", "'Float'", "'Class'", "'Destructor'", 
                     "'If'", "'False'", "'Boolean'", "'Val'", "'New'", "'Elseif'", 
                     "'Array'", "'String'", "'Var'", "'By'", "'Else'", "'In'", 
                     "'Return'", "'Self'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "';'", "','", "':'", "'..'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", 
                     "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", 
                     "'.'", "'::'" ]

    symbolicNames = [ "<INVALID>", "BLOCK_CMT", "INTLIT_GT0", "ZERO", "FLOATLIT", 
                      "BOOLLIT", "STRLIT", "MUDI_ARRLIT", "BREAK", "FOREACH", 
                      "INT", "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", 
                      "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", 
                      "VAL", "NEW", "ELSEIF", "ARRAY", "STRING", "VAR", 
                      "BY", "ELSE", "IN", "RETURN", "SELF", "LP", "RP", 
                      "LCB", "RCB", "LSB", "RSB", "SM", "CM", "CL", "DDT", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                      "EQUAL", "ASSIGN", "NOT_EQUAL", "GT", "GE", "LT", 
                      "LE", "COMPARE_STR", "STR_CONCAT", "INSTANCE_ATTR_ACCESS", 
                      "STATIC_ATTR_ACCESS", "ID_STATIC", "ID_WITHOUT_STATIC", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_decls = 1
    RULE_class_decl = 2
    RULE_superclass = 3
    RULE_memberlists = 4
    RULE_member = 5
    RULE_attribute = 6
    RULE_idlist = 7
    RULE_typename = 8
    RULE_pairList = 9
    RULE_pair = 10
    RULE_arrayType = 11
    RULE_classType = 12
    RULE_primitive_type = 13
    RULE_method = 14
    RULE_paralist = 15
    RULE_para = 16
    RULE_block_stmt = 17
    RULE_stmt_list = 18
    RULE_stmt = 19
    RULE_var_decl_stmt = 20
    RULE_idlist2 = 21
    RULE_pairList2 = 22
    RULE_pair2 = 23
    RULE_assign_stmt = 24
    RULE_lhs = 25
    RULE_if_stmt = 26
    RULE_elseifs_stmt = 27
    RULE_elses_stmt = 28
    RULE_else_stmt = 29
    RULE_for_stmt = 30
    RULE_bys_stmt = 31
    RULE_by_stmt = 32
    RULE_break_stmt = 33
    RULE_continue_stmt = 34
    RULE_return_stmt = 35
    RULE_methodInvo_stmt = 36
    RULE_expr = 37
    RULE_expr1 = 38
    RULE_expr2 = 39
    RULE_expr3 = 40
    RULE_expr4 = 41
    RULE_expr5 = 42
    RULE_expr6 = 43
    RULE_expr7 = 44
    RULE_expr8 = 45
    RULE_expr9 = 46
    RULE_expr10 = 47
    RULE_expr11 = 48
    RULE_operand = 49
    RULE_exprlists = 50
    RULE_exprlist = 51
    RULE_intlit = 52
    RULE_index_arrlit = 53
    RULE_ids = 54

    ruleNames =  [ "program", "class_decls", "class_decl", "superclass", 
                   "memberlists", "member", "attribute", "idlist", "typename", 
                   "pairList", "pair", "arrayType", "classType", "primitive_type", 
                   "method", "paralist", "para", "block_stmt", "stmt_list", 
                   "stmt", "var_decl_stmt", "idlist2", "pairList2", "pair2", 
                   "assign_stmt", "lhs", "if_stmt", "elseifs_stmt", "elses_stmt", 
                   "else_stmt", "for_stmt", "bys_stmt", "by_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "methodInvo_stmt", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "expr11", "operand", 
                   "exprlists", "exprlist", "intlit", "index_arrlit", "ids" ]

    EOF = Token.EOF
    BLOCK_CMT=1
    INTLIT_GT0=2
    ZERO=3
    FLOATLIT=4
    BOOLLIT=5
    STRLIT=6
    MUDI_ARRLIT=7
    BREAK=8
    FOREACH=9
    INT=10
    NULL=11
    CONSTRUCTOR=12
    CONTINUE=13
    TRUE=14
    FLOAT=15
    CLASS=16
    DESTRUCTOR=17
    IF=18
    FALSE=19
    BOOLEAN=20
    VAL=21
    NEW=22
    ELSEIF=23
    ARRAY=24
    STRING=25
    VAR=26
    BY=27
    ELSE=28
    IN=29
    RETURN=30
    SELF=31
    LP=32
    RP=33
    LCB=34
    RCB=35
    LSB=36
    RSB=37
    SM=38
    CM=39
    CL=40
    DDT=41
    ADD=42
    SUB=43
    MUL=44
    DIV=45
    MOD=46
    NOT=47
    AND=48
    OR=49
    EQUAL=50
    ASSIGN=51
    NOT_EQUAL=52
    GT=53
    GE=54
    LT=55
    LE=56
    COMPARE_STR=57
    STR_CONCAT=58
    INSTANCE_ATTR_ACCESS=59
    STATIC_ATTR_ACCESS=60
    ID_STATIC=61
    ID_WITHOUT_STATIC=62
    WS=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decls(self):
            return self.getTypedRuleContext(D96Parser.Class_declsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.class_decls()
            self.state = 111
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(D96Parser.Class_declContext,0)


        def class_decls(self):
            return self.getTypedRuleContext(D96Parser.Class_declsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decls" ):
                return visitor.visitClass_decls(self)
            else:
                return visitor.visitChildren(self)




    def class_decls(self):

        localctx = D96Parser.Class_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decls)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.class_decl()
                self.state = 114
                self.class_decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.class_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def superclass(self):
            return self.getTypedRuleContext(D96Parser.SuperclassContext,0)


        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def memberlists(self):
            return self.getTypedRuleContext(D96Parser.MemberlistsContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(D96Parser.CLASS)
            self.state = 120
            self.match(D96Parser.ID_WITHOUT_STATIC)
            self.state = 121
            self.superclass()
            self.state = 122
            self.match(D96Parser.LCB)
            self.state = 123
            self.memberlists()
            self.state = 124
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_superclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclass" ):
                return visitor.visitSuperclass(self)
            else:
                return visitor.visitChildren(self)




    def superclass(self):

        localctx = D96Parser.SuperclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_superclass)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(D96Parser.CL)
                self.state = 127
                self.match(D96Parser.ID_WITHOUT_STATIC)
                pass
            elif token in [D96Parser.LCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def memberlists(self):
            return self.getTypedRuleContext(D96Parser.MemberlistsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memberlists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlists" ):
                return visitor.visitMemberlists(self)
            else:
                return visitor.visitChildren(self)




    def memberlists(self):

        localctx = D96Parser.MemberlistsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memberlists)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.member()
                self.state = 132
                self.memberlists()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.member()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(D96Parser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.attribute()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def pairList(self):
            return self.getTypedRuleContext(D96Parser.PairListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = D96Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 143
                self.idlist()
                self.state = 144
                self.match(D96Parser.CL)
                self.state = 145
                self.typename()
                pass

            elif la_ == 2:
                self.state = 147
                self.pairList()
                pass


            self.state = 150
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idlist)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.ids()
                self.state = 153
                self.match(D96Parser.CM)
                self.state = 154
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.ids()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def classType(self):
            return self.getTypedRuleContext(D96Parser.ClassTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typename

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypename" ):
                return visitor.visitTypename(self)
            else:
                return visitor.visitChildren(self)




    def typename(self):

        localctx = D96Parser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typename)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.arrayType()
                pass
            elif token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.classType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def pair(self):
            return self.getTypedRuleContext(D96Parser.PairContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_pairList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPairList" ):
                return visitor.visitPairList(self)
            else:
                return visitor.visitChildren(self)




    def pairList(self):

        localctx = D96Parser.PairListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pairList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.ids()
            self.state = 165
            self.pair()
            self.state = 166
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def pair(self):
            return self.getTypedRuleContext(D96Parser.PairContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = D96Parser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pair)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(D96Parser.CM)
                self.state = 169
                self.ids()
                self.state = 170
                self.pair()
                self.state = 171
                self.expr()
                self.state = 172
                self.match(D96Parser.CM)
                pass
            elif token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(D96Parser.CL)
                self.state = 175
                self.typename()
                self.state = 176
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def INTLIT_GT0(self):
            return self.getToken(D96Parser.INTLIT_GT0, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = D96Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(D96Parser.ARRAY)
            self.state = 181
            self.match(D96Parser.LSB)
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 182
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 183
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 186
            self.match(D96Parser.CM)
            self.state = 187
            self.match(D96Parser.INTLIT_GT0)
            self.state = 188
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassType" ):
                return visitor.visitClassType(self)
            else:
                return visitor.visitChildren(self)




    def classType(self):

        localctx = D96Parser.ClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_classType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(D96Parser.NEW)
            self.state = 191
            self.ids()
            self.state = 192
            self.match(D96Parser.LP)
            self.state = 193
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def paralist(self):
            return self.getTypedRuleContext(D96Parser.ParalistContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID_STATIC) | (1 << D96Parser.ID_WITHOUT_STATIC))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 198
            self.match(D96Parser.LP)
            self.state = 199
            self.paralist()
            self.state = 200
            self.match(D96Parser.RP)
            self.state = 201
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(D96Parser.ParaContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def paralist(self):
            return self.getTypedRuleContext(D96Parser.ParalistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = D96Parser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paralist)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.para()
                self.state = 204
                self.match(D96Parser.SM)
                self.state = 205
                self.paralist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.para()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist2(self):
            return self.getTypedRuleContext(D96Parser.Idlist2Context,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = D96Parser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.idlist2()
            self.state = 212
            self.match(D96Parser.CL)
            self.state = 213
            self.typename()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Stmt_listContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(D96Parser.LCB)
            self.state = 216
            self.stmt_list()
            self.state = 217
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Stmt_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = D96Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt_list)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.stmt()
                self.state = 220
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_stmt(self):
            return self.getTypedRuleContext(D96Parser.Var_decl_stmtContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def methodInvo_stmt(self):
            return self.getTypedRuleContext(D96Parser.MethodInvo_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.var_decl_stmt()
                self.state = 227
                self.match(D96Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.assign_stmt()
                self.state = 230
                self.match(D96Parser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.break_stmt()
                self.state = 235
                self.match(D96Parser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 237
                self.continue_stmt()
                self.state = 238
                self.match(D96Parser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 240
                self.return_stmt()
                self.state = 241
                self.match(D96Parser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 243
                self.methodInvo_stmt()
                self.state = 244
                self.match(D96Parser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def idlist2(self):
            return self.getTypedRuleContext(D96Parser.Idlist2Context,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def pairList2(self):
            return self.getTypedRuleContext(D96Parser.PairList2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stmt" ):
                return visitor.visitVar_decl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stmt(self):

        localctx = D96Parser.Var_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_decl_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 249
                self.idlist2()
                self.state = 250
                self.match(D96Parser.CL)
                self.state = 251
                self.typename()
                pass

            elif la_ == 2:
                self.state = 253
                self.pairList2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idlist2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def idlist2(self):
            return self.getTypedRuleContext(D96Parser.Idlist2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idlist2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist2" ):
                return visitor.visitIdlist2(self)
            else:
                return visitor.visitChildren(self)




    def idlist2(self):

        localctx = D96Parser.Idlist2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_idlist2)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(D96Parser.ID_WITHOUT_STATIC)
                self.state = 257
                self.match(D96Parser.CM)
                self.state = 258
                self.idlist2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(D96Parser.ID_WITHOUT_STATIC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairList2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def pair2(self):
            return self.getTypedRuleContext(D96Parser.Pair2Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_pairList2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPairList2" ):
                return visitor.visitPairList2(self)
            else:
                return visitor.visitChildren(self)




    def pairList2(self):

        localctx = D96Parser.PairList2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_pairList2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(D96Parser.ID_WITHOUT_STATIC)
            self.state = 263
            self.pair2()
            self.state = 264
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def pair2(self):
            return self.getTypedRuleContext(D96Parser.Pair2Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_pair2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair2" ):
                return visitor.visitPair2(self)
            else:
                return visitor.visitChildren(self)




    def pair2(self):

        localctx = D96Parser.Pair2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_pair2)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.CM)
                self.state = 267
                self.match(D96Parser.ID_WITHOUT_STATIC)
                self.state = 268
                self.pair2()
                self.state = 269
                self.expr()
                self.state = 270
                self.match(D96Parser.CM)
                pass
            elif token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(D96Parser.CL)
                self.state = 273
                self.typename()
                self.state = 274
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.lhs()
            self.state = 279
            self.match(D96Parser.ASSIGN)
            self.state = 280
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def INSTANCE_ATTR_ACCESS(self):
            return self.getToken(D96Parser.INSTANCE_ATTR_ACCESS, 0)

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def STATIC_ATTR_ACCESS(self):
            return self.getToken(D96Parser.STATIC_ATTR_ACCESS, 0)

        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.expr()
                self.state = 284
                self.match(D96Parser.INSTANCE_ATTR_ACCESS)
                self.state = 285
                self.match(D96Parser.ID_WITHOUT_STATIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID_WITHOUT_STATIC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 288
                self.match(D96Parser.STATIC_ATTR_ACCESS)
                self.state = 289
                self.match(D96Parser.ID_STATIC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def elseifs_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseifs_stmtContext,0)


        def elses_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elses_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(D96Parser.IF)
            self.state = 293
            self.match(D96Parser.LP)
            self.state = 294
            self.expr()
            self.state = 295
            self.match(D96Parser.RP)
            self.state = 296
            self.block_stmt()
            self.state = 297
            self.elseifs_stmt()
            self.state = 298
            self.elses_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseifs_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def elseifs_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseifs_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseifs_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifs_stmt" ):
                return visitor.visitElseifs_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseifs_stmt(self):

        localctx = D96Parser.Elseifs_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elseifs_stmt)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(D96Parser.ELSEIF)
                self.state = 301
                self.match(D96Parser.LP)
                self.state = 302
                self.expr()
                self.state = 303
                self.match(D96Parser.RP)
                self.state = 304
                self.block_stmt()
                self.state = 305
                self.elseifs_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(D96Parser.ELSEIF)
                self.state = 308
                self.match(D96Parser.LP)
                self.state = 309
                self.expr()
                self.state = 310
                self.match(D96Parser.RP)
                self.state = 311
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elses_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elses_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElses_stmt" ):
                return visitor.visitElses_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elses_stmt(self):

        localctx = D96Parser.Elses_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elses_stmt)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.else_stmt()
                pass
            elif token in [D96Parser.INTLIT_GT0, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.BREAK, D96Parser.FOREACH, D96Parser.CONTINUE, D96Parser.IF, D96Parser.VAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.VAR, D96Parser.RETURN, D96Parser.SELF, D96Parser.LP, D96Parser.RCB, D96Parser.SUB, D96Parser.NOT, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(D96Parser.ELSE)
            self.state = 321
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DDT(self):
            return self.getToken(D96Parser.DDT, 0)

        def bys_stmt(self):
            return self.getTypedRuleContext(D96Parser.Bys_stmtContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = D96Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(D96Parser.FOREACH)
            self.state = 324
            self.match(D96Parser.LP)
            self.state = 325
            self.ids()
            self.state = 326
            self.match(D96Parser.IN)
            self.state = 327
            self.expr()
            self.state = 328
            self.match(D96Parser.DDT)
            self.state = 329
            self.expr()
            self.state = 330
            self.bys_stmt()
            self.state = 331
            self.match(D96Parser.RP)
            self.state = 332
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bys_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def by_stmt(self):
            return self.getTypedRuleContext(D96Parser.By_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bys_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBys_stmt" ):
                return visitor.visitBys_stmt(self)
            else:
                return visitor.visitChildren(self)




    def bys_stmt(self):

        localctx = D96Parser.Bys_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_bys_stmt)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.by_stmt()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class By_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_by_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBy_stmt" ):
                return visitor.visitBy_stmt(self)
            else:
                return visitor.visitChildren(self)




    def by_stmt(self):

        localctx = D96Parser.By_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_by_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(D96Parser.BY)
            self.state = 339
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(D96Parser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(D96Parser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(D96Parser.RETURN)
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_GT0, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LP, D96Parser.SUB, D96Parser.NOT, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.state = 346
                self.expr()
                pass
            elif token in [D96Parser.SM]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvo_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def INSTANCE_ATTR_ACCESS(self):
            return self.getToken(D96Parser.INSTANCE_ATTR_ACCESS, 0)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exprlists(self):
            return self.getTypedRuleContext(D96Parser.ExprlistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def STATIC_ATTR_ACCESS(self):
            return self.getToken(D96Parser.STATIC_ATTR_ACCESS, 0)

        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodInvo_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvo_stmt" ):
                return visitor.visitMethodInvo_stmt(self)
            else:
                return visitor.visitChildren(self)




    def methodInvo_stmt(self):

        localctx = D96Parser.MethodInvo_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_methodInvo_stmt)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.expr()
                self.state = 351
                self.match(D96Parser.INSTANCE_ATTR_ACCESS)
                self.state = 352
                self.ids()
                self.state = 353
                self.match(D96Parser.LP)
                self.state = 354
                self.exprlists()
                self.state = 355
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(D96Parser.ID_WITHOUT_STATIC)
                self.state = 358
                self.match(D96Parser.STATIC_ATTR_ACCESS)
                self.state = 359
                self.match(D96Parser.ID_STATIC)
                self.state = 360
                self.match(D96Parser.LP)
                self.state = 361
                self.exprlists()
                self.state = 362
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def STR_CONCAT(self):
            return self.getToken(D96Parser.STR_CONCAT, 0)

        def COMPARE_STR(self):
            return self.getToken(D96Parser.COMPARE_STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.expr1()
                self.state = 367
                _la = self._input.LA(1)
                if not(_la==D96Parser.COMPARE_STR or _la==D96Parser.STR_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 368
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def GE(self):
            return self.getToken(D96Parser.GE, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def LE(self):
            return self.getToken(D96Parser.LE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.expr2(0)
                self.state = 374
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.GT) | (1 << D96Parser.GE) | (1 << D96Parser.LT) | (1 << D96Parser.LE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 375
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 385
                    self.expr3(0) 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 394
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 395
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 396
                    self.expr4(0) 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 405
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 406
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 407
                    self.expr5() 
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr5)
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(D96Parser.NOT)
                self.state = 414
                self.expr5()
                pass
            elif token in [D96Parser.INTLIT_GT0, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LP, D96Parser.SUB, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr6)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(D96Parser.SUB)
                self.state = 419
                self.expr6()
                pass
            elif token in [D96Parser.INTLIT_GT0, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LP, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 426
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427
                    self.match(D96Parser.LSB)
                    self.state = 428
                    self.expr()
                    self.state = 429
                    self.match(D96Parser.RSB) 
                self.state = 435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def INSTANCE_ATTR_ACCESS(self):
            return self.getToken(D96Parser.INSTANCE_ATTR_ACCESS, 0)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exprlists(self):
            return self.getTypedRuleContext(D96Parser.ExprlistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 449
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 439
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 440
                        self.match(D96Parser.INSTANCE_ATTR_ACCESS)
                        self.state = 441
                        self.ids()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 442
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 443
                        self.match(D96Parser.INSTANCE_ATTR_ACCESS)
                        self.state = 444
                        self.ids()
                        self.state = 445
                        self.match(D96Parser.LP)
                        self.state = 446
                        self.exprlists()
                        self.state = 447
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def STATIC_ATTR_ACCESS(self):
            return self.getToken(D96Parser.STATIC_ATTR_ACCESS, 0)

        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exprlists(self):
            return self.getTypedRuleContext(D96Parser.ExprlistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr9)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(D96Parser.ID_WITHOUT_STATIC)
                self.state = 455
                self.match(D96Parser.STATIC_ATTR_ACCESS)
                self.state = 456
                self.match(D96Parser.ID_STATIC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(D96Parser.ID_WITHOUT_STATIC)
                self.state = 458
                self.match(D96Parser.STATIC_ATTR_ACCESS)
                self.state = 459
                self.match(D96Parser.ID_STATIC)
                self.state = 460
                self.match(D96Parser.LP)
                self.state = 461
                self.exprlists()
                self.state = 462
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exprlists(self):
            return self.getTypedRuleContext(D96Parser.ExprlistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr10)
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(D96Parser.NEW)
                self.state = 468
                self.ids()
                self.state = 469
                self.match(D96Parser.LP)
                self.state = 470
                self.exprlists()
                self.state = 471
                self.match(D96Parser.RP)
                self.state = 472
                self.expr10()
                pass
            elif token in [D96Parser.INTLIT_GT0, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LP, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr11)
        try:
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(D96Parser.LP)
                self.state = 478
                self.expr()
                self.state = 479
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.INTLIT_GT0, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intlit(self):
            return self.getTypedRuleContext(D96Parser.IntlitContext,0)


        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def STRLIT(self):
            return self.getToken(D96Parser.STRLIT, 0)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def index_arrlit(self):
            return self.getTypedRuleContext(D96Parser.Index_arrlitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_operand)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_GT0, D96Parser.ZERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.intlit()
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 486
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 487
                self.match(D96Parser.STRLIT)
                pass
            elif token in [D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.enterOuterAlt(localctx, 5)
                self.state = 488
                self.ids()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 6)
                self.state = 489
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 490
                self.index_arrlit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exprlists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlists" ):
                return visitor.visitExprlists(self)
            else:
                return visitor.visitChildren(self)




    def exprlists(self):

        localctx = D96Parser.ExprlistsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_exprlists)
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_GT0, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LP, D96Parser.SUB, D96Parser.NOT, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.exprlist()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = D96Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_exprlist)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.expr()
                self.state = 498
                self.match(D96Parser.CM)
                self.state = 499
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

        def INTLIT_GT0(self):
            return self.getToken(D96Parser.INTLIT_GT0, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_intlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntlit" ):
                return visitor.visitIntlit(self)
            else:
                return visitor.visitChildren(self)




    def intlit(self):

        localctx = D96Parser.IntlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_intlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            _la = self._input.LA(1)
            if not(_la==D96Parser.INTLIT_GT0 or _la==D96Parser.ZERO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_arrlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_index_arrlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arrlit" ):
                return visitor.visitIndex_arrlit(self)
            else:
                return visitor.visitChildren(self)




    def index_arrlit(self):

        localctx = D96Parser.Index_arrlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_index_arrlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(D96Parser.ARRAY)
            self.state = 507
            self.match(D96Parser.LP)
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_GT0, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LP, D96Parser.SUB, D96Parser.NOT, D96Parser.ID_STATIC, D96Parser.ID_WITHOUT_STATIC]:
                self.state = 508
                self.expr()
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 509
                    self.match(D96Parser.CM)
                    self.state = 510
                    self.expr()
                    self.state = 515
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 519
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_WITHOUT_STATIC(self):
            return self.getToken(D96Parser.ID_WITHOUT_STATIC, 0)

        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = D96Parser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID_STATIC or _la==D96Parser.ID_WITHOUT_STATIC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[39] = self.expr2_sempred
        self._predicates[40] = self.expr3_sempred
        self._predicates[41] = self.expr4_sempred
        self._predicates[44] = self.expr7_sempred
        self._predicates[45] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




