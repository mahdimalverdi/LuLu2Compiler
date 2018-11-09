// Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammer.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LuLu2GrammerParser}.
 */
public interface LuLu2GrammerListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LuLu2GrammerParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(LuLu2GrammerParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link LuLu2GrammerParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(LuLu2GrammerParser.ProgramContext ctx);
}