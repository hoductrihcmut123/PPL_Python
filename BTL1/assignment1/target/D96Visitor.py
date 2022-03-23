# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decls.
    def visitClass_decls(self, ctx:D96Parser.Class_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#superclass.
    def visitSuperclass(self, ctx:D96Parser.SuperclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberlists.
    def visitMemberlists(self, ctx:D96Parser.MemberlistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typename.
    def visitTypename(self, ctx:D96Parser.TypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pairList.
    def visitPairList(self, ctx:D96Parser.PairListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair.
    def visitPair(self, ctx:D96Parser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayType.
    def visitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classType.
    def visitClassType(self, ctx:D96Parser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paralist.
    def visitParalist(self, ctx:D96Parser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para.
    def visitPara(self, ctx:D96Parser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_list.
    def visitStmt_list(self, ctx:D96Parser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_decl_stmt.
    def visitVar_decl_stmt(self, ctx:D96Parser.Var_decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist2.
    def visitIdlist2(self, ctx:D96Parser.Idlist2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pairList2.
    def visitPairList2(self, ctx:D96Parser.PairList2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair2.
    def visitPair2(self, ctx:D96Parser.Pair2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseifs_stmt.
    def visitElseifs_stmt(self, ctx:D96Parser.Elseifs_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elses_stmt.
    def visitElses_stmt(self, ctx:D96Parser.Elses_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_stmt.
    def visitElse_stmt(self, ctx:D96Parser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_stmt.
    def visitFor_stmt(self, ctx:D96Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bys_stmt.
    def visitBys_stmt(self, ctx:D96Parser.Bys_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#by_stmt.
    def visitBy_stmt(self, ctx:D96Parser.By_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodInvo_stmt.
    def visitMethodInvo_stmt(self, ctx:D96Parser.MethodInvo_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr11.
    def visitExpr11(self, ctx:D96Parser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprlists.
    def visitExprlists(self, ctx:D96Parser.ExprlistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprlist.
    def visitExprlist(self, ctx:D96Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#intlit.
    def visitIntlit(self, ctx:D96Parser.IntlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arrlit.
    def visitIndex_arrlit(self, ctx:D96Parser.Index_arrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ids.
    def visitIds(self, ctx:D96Parser.IdsContext):
        return self.visitChildren(ctx)



del D96Parser