# Generated from D:/Projects/2018/LuLu2Compiler/LuLu2Compiler\LuLu2Grammar.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LuLu2GrammarParser import LuLu2GrammarParser
else:
    from LuLu2GrammarParser import LuLu2GrammarParser

# This class defines a complete generic visitor for a parse tree produced by LuLu2GrammarParser.

class LuLu2GrammarVisitor(ParseTreeVisitor):
    level = 0

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
        defualt_value = "None"
        i = 0
        for var in ctx.var_val():
            print("\t" * self.level,end="")
            print(var.ref().ID(),"=",end="")
            if var.expr() is not None:
                self.visitExpr(var.expr())
            else:
                print(" "+defualt_value,end="")
            print("")


    # Visit a parse tree produced by LuLu2GrammarParser#var_val.
    def visitVar_val(self, ctx:LuLu2GrammarParser.Var_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#ft_def.
    def visitFt_def(self, ctx:LuLu2GrammarParser.Ft_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#type_def.
    def visitType_def(self, ctx:LuLu2GrammarParser.Type_defContext):
        print("\t" * self.level, end="")
        print("class", ctx.ID(0), end="")
        if(len(ctx.ID()) == 2):
            print(" : ", ctx.ID(1), end="")
        print(" : ")
        self.level = self.level + 1
        self.visitChildren(ctx)
        self.level = self.level - 1
        print("")

    # Visit a parse tree produced by LuLu2GrammarParser#component.
    def visitComponent(self, ctx:LuLu2GrammarParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#access_modifier.
    def visitAccess_modifier(self, ctx:LuLu2GrammarParser.Access_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#fun_def.
    def visitFun_def(self, ctx:LuLu2GrammarParser.Fun_defContext):
        print("def",ctx.ID(),end=" ")
        flag = False
        print("(",end="")
        for arg in ctx.args_var():
            if(flag):
                print(", ", end="")
            flag = True
            print(arg.ID(),end="")
        print(")",end="")
        print(" : ",end="")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#block.
    def visitBlock(self, ctx:LuLu2GrammarParser.BlockContext):
        self.level = self.level + 1
        print("")
        tmp = self.visitChildren(ctx)
        self.level = self.level - 1
        print("")
        return tmp


    # Visit a parse tree produced by LuLu2GrammarParser#stmt.
    def visitStmt(self, ctx:LuLu2GrammarParser.StmtContext):
        print("\t" * self.level, end="")
        tmp = self.visitChildren(ctx)
        print("")
        return tmp


    # Visit a parse tree produced by LuLu2GrammarParser#assign.
    def visitAssign(self, ctx:LuLu2GrammarParser.AssignContext):
        flag = False
        for var in ctx.var():
            if(flag):
                print(", ", end="")
            flag = False
            for ref in var.ref():
                if(flag):
                    print(".", end="")
                flag = True
                print(ref.ID(),end="")
            flag = True
        print(" = ", end="")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#var.
    def visitVar(self, ctx:LuLu2GrammarParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#ref.
    def visitRef(self, ctx:LuLu2GrammarParser.RefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#expr.
    def visitExpr(self, ctx:LuLu2GrammarParser.ExprContext):
        if ctx.var() is not None:
            flag = False
            for ref in ctx.var().ref():
                if (flag):
                    print(".", end="")
                flag = True
                print(ref.ID(), end="")
        print(" ", end="")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#func_call.
    def visitFunc_call(self, ctx:LuLu2GrammarParser.Func_callContext):
        return self.visitChildren(ctx)


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
        if ctx.KEYWORD_IF() is not None:
            print("if",end=" ")
            self.visitExpr(ctx.expr())
            print(" :",end=" ")
            self.visitBlock(ctx.block(0))
            if ctx.KEYWORD_ELSE() is not None:
                print("\t" * self.level, end="")
                print("else :",end=" ")
                self.visitBlock(ctx.block(1))




    # Visit a parse tree produced by LuLu2GrammarParser#loop_stmt.
    def visitLoop_stmt(self, ctx:LuLu2GrammarParser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#type_.
    def visitType_(self, ctx:LuLu2GrammarParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#const_val.
    def visitConst_val(self, ctx:LuLu2GrammarParser.Const_valContext):
        str = ctx.start.text
        if str == "true":
            str = "True"
        if str == "false":
            str = "False"
        print(str, end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#unary_op.
    def visitUnary_op(self, ctx:LuLu2GrammarParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op1.
    def visitBinary_op1(self, ctx:LuLu2GrammarParser.Binary_op1Context):
        print(ctx.start.text, end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op2.
    def visitBinary_op2(self, ctx:LuLu2GrammarParser.Binary_op2Context):
        print(ctx.start.text, end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op3.
    def visitBinary_op3(self, ctx:LuLu2GrammarParser.Binary_op3Context):
        print(ctx.start.text,end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op4.
    def visitBinary_op4(self, ctx:LuLu2GrammarParser.Binary_op4Context):
        print(ctx.start.text, end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op5.
    def visitBinary_op5(self, ctx:LuLu2GrammarParser.Binary_op5Context):
        print(ctx.start.text,end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op6.
    def visitBinary_op6(self, ctx:LuLu2GrammarParser.Binary_op6Context):
        print(ctx.start.text,end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op7.
    def visitBinary_op7(self, ctx:LuLu2GrammarParser.Binary_op7Context):
        print(ctx.start.text,end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op8.
    def visitBinary_op8(self, ctx:LuLu2GrammarParser.Binary_op8Context):
        print("and ",end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuLu2GrammarParser#binary_op9.
    def visitBinary_op9(self, ctx:LuLu2GrammarParser.Binary_op9Context):
        print("or ",end=" ")
        return self.visitChildren(ctx)



del LuLu2GrammarParser