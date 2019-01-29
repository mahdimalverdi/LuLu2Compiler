# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammar.g4 by ANTLR 4.7
from antlr4 import *

from LuLu2.ErrorManager import errorManager
from LuLu2.Scope import Scope, global_scope, convert_to

if __name__ is not None and "." in __name__:
    from .LuLu2GrammarParser import LuLu2GrammarParser
else:
    from LuLu2GrammarParser import LuLu2GrammarParser

# This class defines a complete generic visitor for a parse tree produced by LuLu2GrammarParser.

class LuLu2GrammarVisitorUsage(ParseTreeVisitor):
    __is_need_new_scope__: bool = True

    def __init__(self) -> None:
        super().__init__()
        self.__current_scope__: Scope = global_scope
        self._visited_typed_: list = []

    # Visit a parse tree produced by LuLu2GrammarParser#program.
    def visitProgram(self, ctx:LuLu2GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#ft_dcl.
    def visitFt_dcl(self, ctx:LuLu2GrammarParser.Ft_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#func_dcl.
    def visitFunc_dcl(self, ctx:LuLu2GrammarParser.Func_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#args.
    def visitArgs(self, ctx:LuLu2GrammarParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#args_var.
    def visitArgs_var(self, ctx:LuLu2GrammarParser.Args_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#type_dcl.
    def visitType_dcl(self, ctx:LuLu2GrammarParser.Type_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#var_def.
    def visitVar_def(self, ctx:LuLu2GrammarParser.Var_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#var_val.
    def visitVar_val(self, ctx:LuLu2GrammarParser.Var_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#ft_def.
    def visitFt_def(self, ctx:LuLu2GrammarParser.Ft_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#type_def.
    def visitType_def(self, ctx:LuLu2GrammarParser.Type_defContext):
        tmp_scope = self.__current_scope__
        self.__current_scope__ = global_scope.get_current_scope(ctx.start.line, ctx.start.column)
        self.__is_need_new_scope__ = False
        children = self.visitChildren(ctx)
        self.__current_scope__ = tmp_scope
        return children


    # Visit a parse tree produced by LuLu2GrammarParser#component.
    def visitComponent(self, ctx:LuLu2GrammarParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#access_modifier.
    def visitAccess_modifier(self, ctx:LuLu2GrammarParser.Access_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#fun_def.
    def visitFun_def(self, ctx:LuLu2GrammarParser.Fun_defContext):
        tmp_scope = self.__current_scope__
        self.__current_scope__ = global_scope.get_current_scope(ctx.start.line, ctx.start.column)
        self.__is_need_new_scope__ = False
        children = self.visitChildren(ctx)
        self.__current_scope__ = tmp_scope
        return children


    # Visit a parse tree produced by LuLu2GrammarParser#block.
    def visitBlock(self, ctx:LuLu2GrammarParser.BlockContext):
        tmp_scope = self.__current_scope__
        if self.__is_need_new_scope__ is True:
            self.__current_scope__ = global_scope.get_current_scope(ctx.start.line, ctx.start.column)

        self.__is_need_new_scope__ = True
        children = self.visitChildren(ctx)
        self.__current_scope__ = tmp_scope
        return children


    # Visit a parse tree produced by LuLu2GrammarParser#stmt.
    def visitStmt(self, ctx:LuLu2GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#assign.
    def visitAssign(self, ctx:LuLu2GrammarParser.AssignContext):

        childdren = self.visitChildren(ctx)

        output = self._visited_typed_.pop()

        input_type = None
        if len(ctx.var()) < 2:
            input_type = self._visited_typed_.pop()
        else:
            input_type =[]
            for item in ctx.var():
                t = self._visited_typed_.pop()
                input_type.append(t)

            input_type.reverse()


        convert_to(input_type, output , ctx.start.line, ctx.start.column)
        return childdren

    # Visit a parse tree produced by LuLu2GrammarParser#var.
    def visitVar(self, ctx:LuLu2GrammarParser.VarContext):
        scope = self.__current_scope__
        if ctx.KEYWORD_THIS() is not None:
            v = scope.get_variable("this", ctx.start.line, ctx.start.column)
            if v is not None:
                tmp = scope.get_define_type(v.Type, ctx.start.line, ctx.start.column)
                if tmp is not None:
                    scope = global_scope.get_current_scope(tmp.line, tmp.column)
                else:
                    scope = None
            else:
                scope = None
        elif ctx.KEYWORD_SUPER() is not None:
            v = scope.get_variable("super", ctx.start.line, ctx.start.column)
            if v is not None:
                tmp = scope.get_define_type(v.Type, ctx.start.line, ctx.start.column)
                if tmp is not None:
                    scope = global_scope.get_current_scope(tmp.line, tmp.column)
                else:
                    scope = None
            else:
                scope = None
        if scope is None:
            t1 = "NoneType"
        else:
            if ctx.KEYWORD_THIS() is not None or ctx.KEYWORD_SUPER() is not None:
                v = scope.get_local_variable(ctx.ref(0).ID().getText(), ctx.start.line, ctx.start.column)
            else:
                v = scope.get_variable(ctx.ref(0).ID().getText(), ctx.start.line, ctx.start.column)
            if v is None:
                t1 = "NoneType"
            else:
                tmp = scope.get_define_type(v.Type, ctx.start.line, ctx.start.column)
                if tmp is not None:
                    scope = global_scope.get_current_scope(tmp.line, tmp.column)
                    t1 = tmp.key
                    if scope is not None:
                        for item in ctx.ref()[1:]:
                            v = scope.get_local_variable(item.ID().getText(), item.start.line, item.start.column)
                            if v is None:
                                break
                            tmp_type = scope.get_type(v.Type, item.line, item.column)
                            scope = global_scope.get_current_scope(tmp_type.line, tmp_type.column)
                            if scope is None:
                                break
                        if v is None or scope is None:
                            t1 = "NoneType"
                        else:
                            t1 = v.Type
                else:
                    t1 = "NoneType"
        self._visited_typed_.append(t1)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#ref.
    def visitRef(self, ctx:LuLu2GrammarParser.RefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#expr.
    def visitExpr(self, ctx:LuLu2GrammarParser.ExprContext):
        children = self.visitChildren(ctx)
        op = ""
        t1 = ""
        if ctx.unary_op() is not None:
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            op = ctx.unary_op().getText()
        elif ctx.binary_op1() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op1().getText()
        elif ctx.binary_op2() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op2().getText()
        elif ctx.binary_op3() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op3().getText()
        elif ctx.binary_op4() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op4().getText()

            if t1 == t2:
                self._visited_typed_.append("int")
                return children
        elif ctx.binary_op5() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op5().getText()
        elif ctx.binary_op6() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op6().getText()
        elif ctx.binary_op7() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op7().getText()
        elif ctx.binary_op8() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op8().getText()
        elif ctx.binary_op9() is not None:
            t2 = self._visited_typed_.pop()
            t1 = self._visited_typed_.pop()
            if t1 is None:
                t1 = "NoneType"
            if t2 is None:
                t2 = "NoneType"
            op = ctx.binary_op9().getText()

        if op != "" and t1 != "NoneType" and t2 != "NoneType":
            output = global_scope.get_type(t1, ctx.start.line, ctx.start.column).get_output_type(t1, t2, op, ctx.start.line, ctx.start.column, global_scope)
            self._visited_typed_.append(output)
        elif t1 != "":
            self._visited_typed_.append(t1)

        return children


    # Visit a parse tree produced by LuLu2GrammarParser#func_call.
    def visitFunc_call(self, ctx:LuLu2GrammarParser.Func_callContext):

        children = self.visitChildren(ctx)

        param = ctx.handle_call().params()


        input_type = []
        while param is not None:
            t = self._visited_typed_.pop()
            input_type.append(t)
            param = param.params()
        input_type.reverse()

        if len(input_type) == 1:
            input_type = input_type[0]

        scope = None
        if ctx.var() is not None:
            tmp = global_scope.get_define_type(self._visited_typed_.pop(), ctx.start.line, ctx.start.column, )
            scope = global_scope.get_current_scope(tmp.line, tmp.column)
        else:
            scope = self.__current_scope__

        key = ctx.handle_call().ID().getText()


        fun = scope.get_function(key,input_type,  ctx.start.line, ctx.start.column)
        if fun is not None:
            self._visited_typed_.append(fun.output)
        else:
            self._visited_typed_.append("NoneType")
        return  children


    # Visit a parse tree produced by LuLu2GrammarParser#list_.
    def visitList_(self, ctx:LuLu2GrammarParser.List_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#handle_call.
    def visitHandle_call(self, ctx:LuLu2GrammarParser.Handle_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#params.
    def visitParams(self, ctx:LuLu2GrammarParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#cond_stmt.
    def visitCond_stmt(self, ctx:LuLu2GrammarParser.Cond_stmtContext):
        children = self.visitChildren(ctx)
        if ctx.expr() is not None:
            tmp = global_scope.get_type(self._visited_typed_.pop(),ctx.expr().start.line,ctx.expr().start.column)
            tmp.is_convert_to("bool",ctx.expr().start.line,ctx.expr().start.column)
        elif ctx.var() is not None:
            tmp = global_scope.get_type(self._visited_typed_.pop(),ctx.expr().start.line,ctx.expr().start.column)
            tmp.is_convert_to("int",ctx.expr().start.line,ctx.expr().start.column)
        return children


    # Visit a parse tree produced by LuLu2GrammarParser#loop_stmt.
    def visitLoop_stmt(self, ctx:LuLu2GrammarParser.Loop_stmtContext):
        children = self.visitChildren(ctx)
        if ctx.expr() is not None:
            tmp = global_scope.get_type(self._visited_typed_.pop(),ctx.expr().start.line,ctx.expr().start.column)
            tmp.is_convert_to("bool",ctx.expr().start.line,ctx.expr().start.column)
        return children


    # Visit a parse tree produced by LuLu2GrammarParser#type_.
    def visitType_(self, ctx:LuLu2GrammarParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#const_val.
    def visitConst_val(self, ctx:LuLu2GrammarParser.Const_valContext):
        if ctx.INT_CONST() is not None:
            self._visited_typed_.append("int")
        if ctx.REAL_CONST() is not None:
            self._visited_typed_.append("float")
        if ctx.STRING_CONST() is not None:
            self._visited_typed_.append("string")
        if ctx.BOOL_CONST() is not None:
            self._visited_typed_.append("bool")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#unary_op.
    def visitUnary_op(self, ctx:LuLu2GrammarParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op1.
    def visitBinary_op1(self, ctx:LuLu2GrammarParser.Binary_op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op2.
    def visitBinary_op2(self, ctx:LuLu2GrammarParser.Binary_op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op3.
    def visitBinary_op3(self, ctx:LuLu2GrammarParser.Binary_op3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op4.
    def visitBinary_op4(self, ctx:LuLu2GrammarParser.Binary_op4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op5.
    def visitBinary_op5(self, ctx:LuLu2GrammarParser.Binary_op5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op6.
    def visitBinary_op6(self, ctx:LuLu2GrammarParser.Binary_op6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op7.
    def visitBinary_op7(self, ctx:LuLu2GrammarParser.Binary_op7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op8.
    def visitBinary_op8(self, ctx:LuLu2GrammarParser.Binary_op8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op9.
    def visitBinary_op9(self, ctx:LuLu2GrammarParser.Binary_op9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#array_brackets.
    def visitArray_brackets(self, ctx:LuLu2GrammarParser.Array_bracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#array_brackets_with_size.
    def visitArray_brackets_with_size(self, ctx:LuLu2GrammarParser.Array_brackets_with_sizeContext):
        return self.visitChildren(ctx)



del LuLu2GrammarParser