// Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammer.g4 by ANTLR 4.7
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LuLu2GrammerLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ID=1, KEYWORD=2, INT_CONST=3, REAL_CONST=4, STRING_CONST=5;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"ID", "KEYWORD", "INT_CONST", "REAL_CONST", "STRING_CONST"
	};

	private static final String[] _LITERAL_NAMES = {
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "ID", "KEYWORD", "INT_CONST", "REAL_CONST", "STRING_CONST"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public LuLu2GrammerLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "LuLu2Grammer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7\u00f6\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\5\2\17\n\2\3\2\7\2\22\n\2\f\2\16"+
		"\2\25\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00b9\n\3\3\4\3\4\3\4\3\4\5\4\u00bf\n"+
		"\4\3\4\6\4\u00c2\n\4\r\4\16\4\u00c3\3\4\6\4\u00c7\n\4\r\4\16\4\u00c8\5"+
		"\4\u00cb\n\4\3\5\5\5\u00ce\n\5\3\5\3\5\6\5\u00d2\n\5\r\5\16\5\u00d3\3"+
		"\5\3\5\3\5\5\5\u00d9\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00ee\n\6\f\6\16\6\u00f1\13\6\3\6\3"+
		"\6\3\6\3\6\3\u00ef\2\7\3\3\5\4\7\5\t\6\13\7\3\2\6\6\2%%C\\aac|\7\2%%\62"+
		";C\\aac|\5\2\62;CHch\3\2\62;\2\u0122\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2"+
		"\2\2\t\3\2\2\2\2\13\3\2\2\2\3\16\3\2\2\2\5\u00b8\3\2\2\2\7\u00ca\3\2\2"+
		"\2\t\u00d8\3\2\2\2\13\u00da\3\2\2\2\r\17\t\2\2\2\16\r\3\2\2\2\17\23\3"+
		"\2\2\2\20\22\t\3\2\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3"+
		"\2\2\2\24\4\3\2\2\2\25\23\3\2\2\2\26\27\7c\2\2\27\30\7n\2\2\30\31\7n\2"+
		"\2\31\32\7q\2\2\32\33\7e\2\2\33\34\7c\2\2\34\35\7v\2\2\35\u00b9\7g\2\2"+
		"\36\37\7d\2\2\37 \7q\2\2 !\7q\2\2!\u00b9\7n\2\2\"#\7d\2\2#$\7t\2\2$%\7"+
		"g\2\2%&\7c\2\2&\u00b9\7m\2\2\'(\7e\2\2()\7c\2\2)*\7u\2\2*\u00b9\7g\2\2"+
		"+,\7e\2\2,-\7q\2\2-.\7p\2\2./\7u\2\2/\u00b9\7v\2\2\60\61\7e\2\2\61\62"+
		"\7q\2\2\62\63\7p\2\2\63\64\7v\2\2\64\65\7k\2\2\65\66\7p\2\2\66\67\7w\2"+
		"\2\67\u00b9\7g\2\289\7f\2\29:\7g\2\2:;\7e\2\2;<\7n\2\2<=\7c\2\2=>\7t\2"+
		"\2>\u00b9\7g\2\2?@\7f\2\2@A\7g\2\2AB\7h\2\2BC\7c\2\2CD\7w\2\2DE\7n\2\2"+
		"E\u00b9\7v\2\2FG\7f\2\2GH\7g\2\2HI\7u\2\2IJ\7v\2\2JK\7t\2\2KL\7w\2\2L"+
		"M\7e\2\2M\u00b9\7v\2\2NO\7g\2\2OP\7n\2\2PQ\7u\2\2Q\u00b9\7g\2\2RS\7h\2"+
		"\2ST\7c\2\2TU\7n\2\2UV\7u\2\2V\u00b9\7g\2\2WX\7h\2\2XY\7w\2\2YZ\7p\2\2"+
		"Z[\7e\2\2[\\\7v\2\2\\]\7k\2\2]^\7q\2\2^\u00b9\7p\2\2_`\7h\2\2`a\7n\2\2"+
		"ab\7q\2\2bc\7c\2\2c\u00b9\7v\2\2de\7h\2\2ef\7q\2\2f\u00b9\7t\2\2gh\7k"+
		"\2\2h\u00b9\7h\2\2ij\7k\2\2jk\7p\2\2k\u00b9\7v\2\2lm\7p\2\2mn\7k\2\2n"+
		"\u00b9\7n\2\2op\7q\2\2p\u00b9\7h\2\2qr\7r\2\2rs\7t\2\2st\7k\2\2tu\7x\2"+
		"\2uv\7c\2\2vw\7v\2\2w\u00b9\7g\2\2xy\7r\2\2yz\7t\2\2z{\7q\2\2{|\7v\2\2"+
		"|}\7g\2\2}~\7e\2\2~\177\7v\2\2\177\u0080\7g\2\2\u0080\u00b9\7f\2\2\u0081"+
		"\u0082\7r\2\2\u0082\u0083\7w\2\2\u0083\u0084\7d\2\2\u0084\u0085\7n\2\2"+
		"\u0085\u0086\7k\2\2\u0086\u00b9\7e\2\2\u0087\u0088\7t\2\2\u0088\u0089"+
		"\7g\2\2\u0089\u008a\7c\2\2\u008a\u00b9\7f\2\2\u008b\u008c\7t\2\2\u008c"+
		"\u008d\7g\2\2\u008d\u008e\7v\2\2\u008e\u008f\7w\2\2\u008f\u0090\7t\2\2"+
		"\u0090\u00b9\7p\2\2\u0091\u0092\7u\2\2\u0092\u0093\7v\2\2\u0093\u0094"+
		"\7t\2\2\u0094\u0095\7k\2\2\u0095\u0096\7p\2\2\u0096\u00b9\7i\2\2\u0097"+
		"\u0098\7u\2\2\u0098\u0099\7w\2\2\u0099\u009a\7r\2\2\u009a\u009b\7g\2\2"+
		"\u009b\u00b9\7t\2\2\u009c\u009d\7u\2\2\u009d\u009e\7y\2\2\u009e\u009f"+
		"\7k\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1\7e\2\2\u00a1\u00b9\7j\2\2\u00a2"+
		"\u00a3\7v\2\2\u00a3\u00a4\7j\2\2\u00a4\u00a5\7k\2\2\u00a5\u00b9\7u\2\2"+
		"\u00a6\u00a7\7v\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7w\2\2\u00a9\u00b9"+
		"\7g\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7{\2\2\u00ac\u00ad\7r\2\2\u00ad"+
		"\u00b9\7g\2\2\u00ae\u00af\7y\2\2\u00af\u00b0\7j\2\2\u00b0\u00b1\7k\2\2"+
		"\u00b1\u00b2\7n\2\2\u00b2\u00b9\7g\2\2\u00b3\u00b4\7y\2\2\u00b4\u00b5"+
		"\7t\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b9\7g\2\2\u00b8"+
		"\26\3\2\2\2\u00b8\36\3\2\2\2\u00b8\"\3\2\2\2\u00b8\'\3\2\2\2\u00b8+\3"+
		"\2\2\2\u00b8\60\3\2\2\2\u00b88\3\2\2\2\u00b8?\3\2\2\2\u00b8F\3\2\2\2\u00b8"+
		"N\3\2\2\2\u00b8R\3\2\2\2\u00b8W\3\2\2\2\u00b8_\3\2\2\2\u00b8d\3\2\2\2"+
		"\u00b8g\3\2\2\2\u00b8i\3\2\2\2\u00b8l\3\2\2\2\u00b8o\3\2\2\2\u00b8q\3"+
		"\2\2\2\u00b8x\3\2\2\2\u00b8\u0081\3\2\2\2\u00b8\u0087\3\2\2\2\u00b8\u008b"+
		"\3\2\2\2\u00b8\u0091\3\2\2\2\u00b8\u0097\3\2\2\2\u00b8\u009c\3\2\2\2\u00b8"+
		"\u00a2\3\2\2\2\u00b8\u00a6\3\2\2\2\u00b8\u00aa\3\2\2\2\u00b8\u00ae\3\2"+
		"\2\2\u00b8\u00b3\3\2\2\2\u00b9\6\3\2\2\2\u00ba\u00bb\7\62\2\2\u00bb\u00bf"+
		"\7Z\2\2\u00bc\u00bd\7\62\2\2\u00bd\u00bf\7z\2\2\u00be\u00ba\3\2\2\2\u00be"+
		"\u00bc\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00c2\t\4\2\2\u00c1\u00c0\3\2"+
		"\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4"+
		"\u00cb\3\2\2\2\u00c5\u00c7\t\5\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00c8\3\2"+
		"\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca"+
		"\u00be\3\2\2\2\u00ca\u00c6\3\2\2\2\u00cb\b\3\2\2\2\u00cc\u00ce\5\7\4\2"+
		"\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1"+
		"\7\60\2\2\u00d0\u00d2\t\5\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2"+
		"\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d9\3\2\2\2\u00d5\u00d6"+
		"\5\7\4\2\u00d6\u00d7\7\60\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00cd\3\2\2\2"+
		"\u00d8\u00d5\3\2\2\2\u00d9\n\3\2\2\2\u00da\u00db\7\u00e4\2\2\u00db\u00dc"+
		"\7\u20ae\2\2\u00dc\u00dd\7\u02de\2\2\u00dd\u00ef\3\2\2\2\u00de\u00ee\3"+
		"\2\2\2\u00df\u00e0\7^\2\2\u00e0\u00ee\7p\2\2\u00e1\u00e2\7^\2\2\u00e2"+
		"\u00ee\7t\2\2\u00e3\u00e4\7^\2\2\u00e4\u00ee\7^\2\2\u00e5\u00e6\7^\2\2"+
		"\u00e6\u00ee\7v\2\2\u00e7\u00e8\7^\2\2\u00e8\u00ee\7\62\2\2\u00e9\u00ea"+
		"\7^\2\2\u00ea\u00eb\7\u00e4\2\2\u00eb\u00ec\7\u20ae\2\2\u00ec\u00ee\7"+
		"\u2124\2\2\u00ed\u00de\3\2\2\2\u00ed\u00df\3\2\2\2\u00ed\u00e1\3\2\2\2"+
		"\u00ed\u00e3\3\2\2\2\u00ed\u00e5\3\2\2\2\u00ed\u00e7\3\2\2\2\u00ed\u00e9"+
		"\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0"+
		"\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7\u00e4\2\2\u00f3\u00f4"+
		"\7\u20ae\2\2\u00f4\u00f5\7\u2124\2\2\u00f5\f\3\2\2\2\20\2\16\21\23\u00b8"+
		"\u00be\u00c3\u00c8\u00ca\u00cd\u00d3\u00d8\u00ed\u00ef\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}