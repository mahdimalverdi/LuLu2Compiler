# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammar.g4 by ANTLR 4.7
from io import TextIOWrapper

from antlr4 import *

from LuLu2.Scope import Scope, global_scope

if __name__ is not None and "." in __name__:
    from .LuLu2GrammarParser import LuLu2GrammarParser
else:
    from LuLu2GrammarParser import LuLu2GrammarParser


# This class defines a complete generic visitor for a parse tree produced by LuLu2GrammarParser.

class LuLu2GrammarVisitorDeclaration(ParseTreeVisitor):
    __is_need_new_scope__: bool = True

    def __init__(self, outfile: TextIOWrapper) -> None:
        super().__init__()
        self._out_file_ = outfile
        self.__current_scope__: Scope = global_scope

    # Visit a parse tree produced by LuLu2GrammarParser#program.
    def visitProgram(self, ctx: LuLu2GrammarParser.ProgramContext):
        self._out_file_.write("#include <iostream>\n")
        self._out_file_.write("#include <string>\n")
        self._out_file_.write("using namespace std;\n")
        children = self.visitChildren(ctx)
        self._out_file_.write("int main()\n")
        self._out_file_.write("{\n")
        self._out_file_.write("int result = 0;\n")
        self._out_file_.write("start(result);\n")
        self._out_file_.write("\tcout << \"please press Enter.\\n\";\n")
        self._out_file_.write("\tcin >> result;\n")
        self._out_file_.write("\treturn 0;\n")
        self._out_file_.write("}\n")
        return children

    # Visit a parse tree produced by LuLu2GrammarParser#ft_dcl.
    def visitFt_dcl(self, ctx: LuLu2GrammarParser.Ft_dclContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#func_dcl.
    def visitFunc_dcl(self, ctx: LuLu2GrammarParser.Func_dclContext):
        item = ctx.args(0)
        output_type = []
        while item is not None:
            t = item.type_().getText()
            self.__current_scope__.get_type(t, item.type_().start.line, item.type_().start.column)
            output_type.append(t)
            item = item.args()

        output_type.reverse()

        item = ctx.args(1)
        input_type = []
        while item is not None:
            t = item.type_().getText()
            self.__current_scope__.get_type(t, item.type_().start.line, item.type_().start.column)
            input_type.append(t)
            item = item.args()

        item = ctx.args_var()
        while item is not None:
            t = item.type_().getText()
            self.__current_scope__.get_type(t, item.type_().start.line, item.type_().start.column)
            input_type.append(t)
            item = item.args_var()

        input_type.reverse()

        key = ctx.ID().getText()

        if len(input_type) is 1:
            input_type = input_type[0]

        if len(output_type) is 1:
            input_type = output_type[0]

        self.__current_scope__.insert_function(key, ctx.start.line, ctx.start.column, input_type,
                                               output_type, False, 0)

        self.__is_need_new_scope__ = False
        children = self.visitChildren(ctx)

        return children

    # Visit a parse tree produced by LuLu2GrammarParser#args.
    def visitArgs(self, ctx: LuLu2GrammarParser.ArgsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#args_var.
    def visitArgs_var(self, ctx: LuLu2GrammarParser.Args_varContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#type_dcl.
    def visitType_dcl(self, ctx: LuLu2GrammarParser.Type_dclContext):
        self.__current_scope__.insert_type(ctx.ID().getText(), ctx.start.line, ctx.start.column, 0, False, None)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#var_def.
    def visitVar_def(self, ctx: LuLu2GrammarParser.Var_defContext):

        current_type = self.__current_scope__.get_type(ctx.type_().getText(), ctx.start.line, ctx.start.column)

        for item in ctx.var_val():
            sign = "NoneType"
            if current_type is not None:
                sign = ctx.type_().getText()
                for dis in item.ref().array_brackets_with_size():
                    sign += "[]"
                key = item.ref().ID().getText()
                self.__current_scope__.insert_variable(key, item.start.line, item.start.column, sign)
                self._out_file_.write("{0} {1};\n".format(sign, key))

        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#var_val.
    def visitVar_val(self, ctx: LuLu2GrammarParser.Var_valContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#ft_def.
    def visitFt_def(self, ctx: LuLu2GrammarParser.Ft_defContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#type_def.
    def visitType_def(self, ctx: LuLu2GrammarParser.Type_defContext):
        parent = None

        if ctx.ID(1) is not None:
            self.__current_scope__.get_type(ctx.ID(1).getText(), ctx.start.line, ctx.start.column)
        if self.__current_scope__.is_defined_type(ctx.ID(0).getText()) is not True:
            self.__current_scope__.insert_type(ctx.ID(0).getText(), ctx.start.line, ctx.start.column, 0, False, parent)

        tmp_scope = self.__current_scope__
        self.__current_scope__ = self.__current_scope__.insert_scope(ctx.start.line, ctx.start.column)
        self.__current_scope__.insert_variable_without_check("this", ctx.start.line, ctx.start.column,
                                                             ctx.ID(0).getText())
        if ctx.ID(1) is not None:
            p = global_scope.get_type(ctx.ID(1).getText(), ctx.start.line, ctx.start.column)
            self.__current_scope__.insert_variable_without_check("super", ctx.start.line, ctx.start.column,p.key)
        self.__is_need_new_scope__ = False
        children = self.visitChildren(ctx)

        self.__current_scope__.insert_type(ctx.ID(0).getText(), ctx.start.line, ctx.start.column, 0, True, parent)
        self.__current_scope__ = tmp_scope
        return children

    # Visit a parse tree produced by LuLu2GrammarParser#component.
    def visitComponent(self, ctx: LuLu2GrammarParser.ComponentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#access_modifier.
    def visitAccess_modifier(self, ctx: LuLu2GrammarParser.Access_modifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#fun_def.
    def visitFun_def(self, ctx: LuLu2GrammarParser.Fun_defContext):
        self._out_file_.write("void {0}(".format(ctx.ID().getText()))
        item = ctx.args_var(0)
        output_type = []
        w_sim = False
        while item is not None:
            t = item.type_().getText()
            self.__current_scope__.get_type(t, item.type_().start.line, item.type_().start.column)
            output_type.append(t)
            if w_sim is True:
                self._out_file_.write(",")
            w_sim = True
            self._out_file_.write("{0} & {1}".format(t,item.ID().getText()))

            item = item.args_var()

        item = ctx.args_var(1)
        input_type = []
        while item is not None:
            t = item.type_().getText()
            self.__current_scope__.get_type(t, item.type_().start.line, item.type_().start.column)
            input_type.append(t)

            if w_sim is True:
                self._out_file_.write(",")
            w_sim = True
            self._out_file_.write("{0} {1}".format(t,item.ID().getText()))

            item = item.args_var()

        self._out_file_.write(")\n{")
        key = ctx.ID().getText()

        input_type.reverse()

        output_type.reverse()

        if len(input_type) is 1:
            input_type = input_type[0]

        if len(output_type) is 1:
            output_type = output_type[0]

        self.__current_scope__.insert_function(key, ctx.start.line, ctx.start.column, input_type,
                                               output_type, True, 0)

        tmp_scope = self.__current_scope__
        self.__current_scope__ = self.__current_scope__.insert_scope(ctx.start.line, ctx.start.column)

        var = ctx.args_var(0)
        while var is not None:
            t = var.type_().getText()

            self.__current_scope__.get_type(t, var.type_().start.line, var.type_().start.column)

            sign = t
            sign += var.array_brackets().getText()
            key = var.ID().getText()

            self.__current_scope__.insert_variable(key, var.start.line, var.start.column, sign)
            var = var.args_var()

        var = ctx.args_var(1)
        while var is not None:
            t = var.type_().getText()

            self.__current_scope__.get_type(t, var.type_().start.line, var.type_().start.column)

            sign = t
            sign += var.array_brackets().getText()
            key = var.ID().getText()

            self.__current_scope__.insert_variable(key, var.start.line, var.start.column, sign)
            var = var.args_var()

        self.__is_need_new_scope__ = False
        children = self.visitChildren(ctx)

        self.__current_scope__ = tmp_scope

        self._out_file_.write("}\n")
        return children

    # Visit a parse tree produced by LuLu2GrammarParser#block.
    def visitBlock(self, ctx: LuLu2GrammarParser.BlockContext):
        tmp_scope = self.__current_scope__
        if self.__is_need_new_scope__ is True:
            self.__current_scope__ = self.__current_scope__.insert_scope(ctx.start.line, ctx.start.column)

        self.__is_need_new_scope__ = True

        children = self.visitChildren(ctx)

        self.__current_scope__ = tmp_scope
        return children

    # Visit a parse tree produced by LuLu2GrammarParser#stmt.
    def visitStmt(self, ctx: LuLu2GrammarParser.StmtContext):
        children = self.visitChildren(ctx)
        self._out_file_.write(";\n")

    # Visit a parse tree produced by LuLu2GrammarParser#assign.
    def visitAssign(self, ctx: LuLu2GrammarParser.AssignContext):
        self._out_file_.write(ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#var.
    def visitVar(self, ctx: LuLu2GrammarParser.VarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#ref.
    def visitRef(self, ctx: LuLu2GrammarParser.RefContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#expr.
    def visitExpr(self, ctx: LuLu2GrammarParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#func_call.
    def visitFunc_call(self, ctx: LuLu2GrammarParser.Func_callContext):
        ctx.var()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#list_.
    def visitList_(self, ctx: LuLu2GrammarParser.List_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#handle_call.
    def visitHandle_call(self, ctx: LuLu2GrammarParser.Handle_callContext):
        if ctx.ID().getText() == "read" :
            self._out_file_.write("cin")
            param = ctx.params()

            while param is not None:
                self._out_file_.write(">>"+param.expr().getText())
                param = param.params()
        elif ctx.ID().getText() == "write":
            self._out_file_.write("cout")
            param = ctx.params()

            while param is not None:
                self._out_file_.write("<<"+param.expr().getText())
                param = param.params()

        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#params.
    def visitParams(self, ctx: LuLu2GrammarParser.ParamsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#cond_stmt.
    def visitCond_stmt(self, ctx: LuLu2GrammarParser.Cond_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#loop_stmt.
    def visitLoop_stmt(self, ctx: LuLu2GrammarParser.Loop_stmtContext):
        if ctx.type_() is not None:
            item = ctx.assign(0)
            sign = ctx.type_().getText()
            for dis in item.var(0).ref(0).array_brackets_with_size():
                sign += "[]"
            key = item.var(0).ref(0).ID().getText()
            self.__current_scope__.insert_variable(key, item.start.line, item.start.column, sign)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#type_.
    def visitType_(self, ctx: LuLu2GrammarParser.Type_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#const_val.
    def visitConst_val(self, ctx: LuLu2GrammarParser.Const_valContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#unary_op.
    def visitUnary_op(self, ctx: LuLu2GrammarParser.Unary_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op1.
    def visitBinary_op1(self, ctx: LuLu2GrammarParser.Binary_op1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op2.
    def visitBinary_op2(self, ctx: LuLu2GrammarParser.Binary_op2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op3.
    def visitBinary_op3(self, ctx: LuLu2GrammarParser.Binary_op3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op4.
    def visitBinary_op4(self, ctx: LuLu2GrammarParser.Binary_op4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op5.
    def visitBinary_op5(self, ctx: LuLu2GrammarParser.Binary_op5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op6.
    def visitBinary_op6(self, ctx: LuLu2GrammarParser.Binary_op6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op7.
    def visitBinary_op7(self, ctx: LuLu2GrammarParser.Binary_op7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op8.
    def visitBinary_op8(self, ctx: LuLu2GrammarParser.Binary_op8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#binary_op9.
    def visitBinary_op9(self, ctx: LuLu2GrammarParser.Binary_op9Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#array_brackets.
    def visitArray_brackets(self, ctx: LuLu2GrammarParser.Array_bracketsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuLu2GrammarParser#array_brackets_with_size.
    def visitArray_brackets_with_size(self, ctx: LuLu2GrammarParser.Array_brackets_with_sizeContext):
        return self.visitChildren(ctx)


del LuLu2GrammarParser
