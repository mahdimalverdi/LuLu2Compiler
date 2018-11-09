// Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammer.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.AbstractParseTreeVisitor;

/**
 * This class provides an empty implementation of {@link LuLu2GrammerVisitor},
 * which can be extended to create a visitor which only needs to handle a subset
 * of the available methods.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public class LuLu2GrammerBaseVisitor<T> extends AbstractParseTreeVisitor<T> implements LuLu2GrammerVisitor<T> {
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */
	@Override public T visitProgram(LuLu2GrammerParser.ProgramContext ctx) { return visitChildren(ctx); }
}