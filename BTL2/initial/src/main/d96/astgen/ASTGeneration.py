from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    # program: class_decls EOF
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(self.visit(ctx.class_decls()))
    
    # class_decls: class_decl class_decls | class_decl
    def visitClass_decls(self, ctx: D96Parser.Class_declsContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.class_decl()) + self.visit(ctx.class_decls())
        else:
            return self.visit(ctx.class_decl())
    
    # class_decl: CLASS ID_WITHOUT_STATIC superclass LCB memberlists RCB 
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        classname = Id(ctx.ID_WITHOUT_STATIC().getText())
        memlist = self.visit(ctx.memberlists())
        parentname = self.visit(ctx.superclass())
        return [ClassDecl(classname, memlist, parentname)]
    
    # superclass: CL ID_WITHOUT_STATIC | 
    def visitSuperclass(self, ctx: D96Parser.SuperclassContext):
        if ctx.getChildCount() == 2:
            return Id(ctx.ID_WITHOUT_STATIC().getText())
        else: 
            return 
    
    # memberlists: member memberlists | member | 
    def visitMemberlists(self, ctx: D96Parser.MemberlistsContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.member()) + self.visit(ctx.memberlists())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.member())
        else: 
            return []
    
    # member: attribute | method
    def visitMember(self, ctx: D96Parser.MemberContext):
        if ctx.attribute():
            return self.visit(ctx.attribute())
        else:
            return self.visit(ctx.method())
    
    # attribute: (VAL | VAR) (idlist CL typename | pairList) SM
    def visitAttribute(self, ctx: D96Parser.AttributeContext):
        if ctx.VAL():
            if ctx.idlist():
                res = []
                idlist = self.visit(ctx.idlist())
                for i in idlist:
                    decl = ConstDecl(i, self.visit(ctx.typename()))
                    temp = str(i)
                    if temp[3] == '$':
                        res += [AttributeDecl(Static(), decl)]
                    else: 
                        res += [AttributeDecl(Instance(), decl)]
                return res
            else:
                pairList = self.visit(ctx.pairList())
                res = []
                for i in range(len(pairList)-1):
                    decl = ConstDecl(pairList[i][0], pairList[len(pairList)-1][0], pairList[len(pairList)-i-2][1])
                    temp = str(pairList[i][0])
                    if temp[3] == '$':
                        res += [AttributeDecl(Static(), decl)]
                    else: 
                        res += [AttributeDecl(Instance(), decl)]
                return res 
        else: 
            if ctx.idlist():
                res = []
                idlist = self.visit(ctx.idlist())
                for i in idlist:
                    decl = VarDecl(i, self.visit(ctx.typename()))
                    temp = str(i)
                    if temp[3] == '$':
                        res += [AttributeDecl(Static(), decl)]
                    else: 
                        res += [AttributeDecl(Instance(), decl)]
                return res
            else:
                pairList = self.visit(ctx.pairList())
                res = []
                for i in range(len(pairList)-1):
                    decl = VarDecl(pairList[i][0], pairList[len(pairList)-1][0], pairList[len(pairList)-i-2][1])
                    temp = str(pairList[i][0])
                    if temp[3] == '$':
                        res += [AttributeDecl(Static(), decl)]
                    else: 
                        res += [AttributeDecl(Instance(), decl)]
                return res 
    
    # idlist: ids CM idlist | ids
    def visitIdlist(self, ctx: D96Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.ids())]
        else:
            return [self.visit(ctx.ids())] + self.visit(ctx.idlist())
    
    # typename: primitive_type | arrayType | classType
    def visitTypename(self, ctx: D96Parser.TypenameContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        if ctx.arrayType():
            return self.visit(ctx.arrayType())
        else:
            return self.visit(ctx.classType())
    
    # pairList: ids pair expr
    def visitPairList(self, ctx: D96Parser.PairListContext):
        ids = self.visit(ctx.ids())
        expr = self.visit(ctx.expr())
        return [[ids,expr]] + self.visit(ctx.pair())
    
    # pair: CM ids pair expr CM | CL typename ASSIGN
    def visitPair(self, ctx: D96Parser.PairContext):
        if ctx.getChildCount() == 3:
            return [[self.visit(ctx.typename()),0]]
        else:
            ids = self.visit(ctx.ids())
            expr = self.visit(ctx.expr())
            return [[ids,expr]] + self.visit(ctx.pair())
    
    # arrayType: ARRAY LSB (primitive_type | arrayType) CM INTLIT_GT0 RSB
    def visitArrayType(self, ctx: D96Parser.ArrayTypeContext):
        if ctx.primitive_type():
            return ArrayType(int(ctx.INTLIT_GT0().getText()), self.visit(ctx.primitive_type()))
        else:
            return ArrayType(int(ctx.INTLIT_GT0().getText()), self.visit(ctx.arrayType()))
    
    # classType: NEW ids LP RP
    def visitClassType(self, ctx: D96Parser.ClassTypeContext):
        return ClassType(self.visit(ctx.ids()))
    
    # primitive_type: INT | FLOAT | BOOLEAN | STRING
    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.INT(): return IntType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BoolType()
        if ctx.STRING(): return StringType()
    
    # method: (ID_STATIC | ID_WITHOUT_STATIC | CONSTRUCTOR | DESTRUCTOR) LP paralist RP block_stmt;
    def visitMethod(self, ctx: D96Parser.MethodContext):
        if ctx.ID_STATIC():
            kind = Static()
            name = Id(ctx.ID_STATIC().getText())
            param = self.visit(ctx.paralist())
            body = self.visit(ctx.block_stmt())
            return [MethodDecl(kind, name, param, body)]
        if ctx.ID_WITHOUT_STATIC():
            if ctx.ID_WITHOUT_STATIC().getText() == 'main' and self.visit(ctx.paralist()) == []:
                return [MethodDecl(Static(), Id(ctx.ID_WITHOUT_STATIC().getText()), self.visit(ctx.paralist())
                              , self.visit(ctx.block_stmt()))]
            else:
                return [MethodDecl(Instance(), Id(ctx.ID_WITHOUT_STATIC().getText()), self.visit(ctx.paralist())
                              , self.visit(ctx.block_stmt()))]
        if ctx.CONSTRUCTOR():
            return [MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.paralist())
                              , self.visit(ctx.block_stmt()))]
        else:
            return [MethodDecl(Instance(), Id(ctx.DESTRUCTOR().getText()), self.visit(ctx.paralist())
                              , self.visit(ctx.block_stmt()))]
    
    # paralist: para SM paralist | para | ;
    def visitParalist(self, ctx: D96Parser.ParalistContext):
        if ctx.getChildCount() == 3:
            para = self.visit(ctx.para())
            paralist = self.visit(ctx.paralist())
            return para + paralist
        if ctx.getChildCount() == 1:
            return self.visit(ctx.para())
        else:
            return []
    
    # para: idlist2 CL typename;
    def visitPara(self, ctx: D96Parser.ParaContext):
        ids = self.visit(ctx.idlist2())
        res = []
        for x in ids:
            res += [VarDecl(x, self.visit(ctx.typename()))]
        return res
    
    # block_stmt: LCB stmt_list RCB;
    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        return Block(self.visit(ctx.stmt_list()))
    
    # stmt_list: stmt stmt_list | stmt | ;
    def visitStmt_list(self, ctx: D96Parser.Stmt_listContext):
        if ctx.getChildCount() == 2:
            stmt = self.visit(ctx.stmt())
            stmt_list = self.visit(ctx.stmt_list())
            return stmt + stmt_list
        elif ctx.getChildCount() == 1: return self.visit(ctx.stmt())
        else: return []
            
    # stmt: var_decl_stmt SM| assign_stmt SM| if_stmt | for_stmt | break_stmt SM| continue_stmt SM| return_stmt SM
    #   | methodInvo_stmt SM;
    def visitStmt(self, ctx: D96Parser.StmtContext):
        if ctx.var_decl_stmt():
            return self.visit(ctx.var_decl_stmt())
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        else:
            return self.visit(ctx.methodInvo_stmt())
    
    # var_decl_stmt: (VAL | VAR) (idlist2 CL typename | pairList2);
    # return 1 list
    def visitVar_decl_stmt(self, ctx: D96Parser.Var_decl_stmtContext):
        if ctx.VAL():
            if ctx.idlist2():
                res = []
                idlist2 = self.visit(ctx.idlist2())
                for i in idlist2:
                    res += [ConstDecl(i, self.visit(ctx.typename()))]
                return res 
            if ctx.pairList2():
                pairList2 = self.visit(ctx.pairList2())
                res = []
                for i in range(len(pairList2)-1):
                    res += [ConstDecl(pairList2[i][0], pairList2[len(pairList2)-1][0], pairList2[len(pairList2)-i-2][1])]
                return res 
        if ctx.VAR(): 
            if ctx.idlist2():
                res = []
                idlist2 = self.visit(ctx.idlist2())
                for i in idlist2:
                    res += [VarDecl(i, self.visit(ctx.typename()))]
                return res 
            if ctx.pairList2():
                pairList2 = self.visit(ctx.pairList2())
                res = []
                for i in range(len(pairList2)-1):
                    res += [VarDecl(pairList2[i][0], pairList2[len(pairList2)-1][0], pairList2[len(pairList2)-i-2][1])]
                return res 
    
    # idlist2: ID_WITHOUT_STATIC CM idlist2 | ID_WITHOUT_STATIC; 
    def visitIdlist2(self, ctx: D96Parser.Idlist2Context):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID_WITHOUT_STATIC().getText())]
        else:
            return [Id(ctx.ID_WITHOUT_STATIC().getText())] + self.visit(ctx.idlist2())
    
    # pairList2: ID_WITHOUT_STATIC pair2 expr;
    def visitPairList2(self, ctx: D96Parser.PairList2Context):
        ids = ctx.ID_WITHOUT_STATIC().getText()
        expr = self.visit(ctx.expr())
        return [[ids,expr]] + self.visit(ctx.pair2())
    
    # pair2: CM ID_WITHOUT_STATIC pair2 expr CM | CL typename ASSIGN;
    def visitPair2(self, ctx: D96Parser.Pair2Context):
        if ctx.getChildCount() == 3:
            return [[self.visit(ctx.typename()),0]]
        else:
            ids = ctx.ID_WITHOUT_STATIC().getText()
            expr = self.visit(ctx.expr())
            return [[ids,expr]] + self.visit(ctx.pair2())
    
    # assign_stmt: lhs ASSIGN expr;
    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        return [Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))]
    
    # lhs: ids
    #   | expr INSTANCE_ATTR_ACCESS ID_WITHOUT_STATIC 
    #   | (ID_WITHOUT_STATIC|SELF) STATIC_ATTR_ACCESS ID_STATIC;
    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.ids():
            return self.visit(ctx.ids())
        if ctx.INSTANCE_ATTR_ACCESS():
            return FieldAccess(self.visit(ctx.expr()), Id(ctx.ID_WITHOUT_STATIC().getText()))
        if ctx.SELF():
            return FieldAccess(SelfLiteral(), Id(ctx.ID_STATIC().getText()))
        else:
            return FieldAccess(Id(ctx.ID_WITHOUT_STATIC().getText()), Id(ctx.ID_STATIC().getText()))
    
    # if_stmt: IF LP expr RP block_stmt elseifs_stmt elses_stmt ; 
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.block_stmt())
        elseifs = self.visit(ctx.elseifs_stmt())   
        elses = self.visit(ctx.elses_stmt())
        if elseifs == None:
            return [If(expr, thenStmt, elses)]
        else:
            string = str(elseifs)
            x = string.rfind("nfkjdshkug")
            temp1 = string[0:x]
            temp2 = string[x+10:len(string)]        # 10 is length of random text
            res = temp1 + str(elses) + temp2
            return [If(expr, thenStmt, res)]
    
    # elseifs_stmt: ELSEIF LP expr RP block_stmt elseifs_stmt | ELSEIF LP expr RP block_stmt | 
    def visitElseifs_stmt(self, ctx: D96Parser.Elseifs_stmtContext):
        if ctx.getChildCount() == 6:
            return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt()), self.visit(ctx.elseifs_stmt()))
        if ctx.getChildCount() == 5:
            return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt()), "nfkjdshkug")
        else: 
            return "nfkjdshkug"          # random text use for handle the string above
    
    # elses_stmt: else_stmt | ;
    def visitElses_stmt(self, ctx: D96Parser.Elses_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.else_stmt())
        else: return 
    
    # else_stmt: ELSE block_stmt;
    def visitElse_stmt(self, ctx: D96Parser.Else_stmtContext):
        return self.visit(ctx.block_stmt())
    
    # for_stmt: FOREACH LP ids IN expr DDT expr bys_stmt RP block_stmt;
    def visitFor_stmt(self, ctx: D96Parser.For_stmtContext):
        ids = self.visit(ctx.ids())
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        loop = self.visit(ctx.block_stmt())
        expr3 = self.visit(ctx.bys_stmt())
        return [For(ids, expr1, expr2, loop, expr3)]
    
    # bys_stmt: by_stmt | ;
    def visitBys_stmt(self, ctx: D96Parser.Bys_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.by_stmt())
        else: return IntLiteral(1)
    
    # by_stmt: BY expr;
    def visitBy_stmt(self, ctx: D96Parser.By_stmtContext):
        return self.visit(ctx.expr())
    
    # break_stmt: BREAK;
    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return [Break()]
    
    # continue_stmt: CONTINUE;
    def visitContinue_stmt(self, ctx: D96Parser.Continue_stmtContext):
        return [Continue()]
    
    # return_stmt: RETURN (expr | );
    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        if ctx.expr():
            return [Return(self.visit(ctx.expr()))]
        else: [Return()]
    
    # methodInvo_stmt: expr INSTANCE_ATTR_ACCESS ids LP exprlists RP
    #               | ID_WITHOUT_STATIC STATIC_ATTR_ACCESS ID_STATIC LP exprlists RP;
    def visitMethodInvo_stmt(self, ctx: D96Parser.MethodInvo_stmtContext):
        if ctx.INSTANCE_ATTR_ACCESS():
            return [CallStmt(self.visit(ctx.expr()), self.visit(ctx.ids()), self.visit(ctx.exprlists()))]
        else:
            return [CallStmt(Id(ctx.ID_WITHOUT_STATIC().getText()), Id(ctx.ID_STATIC().getText()), self.visit(ctx.exprlists()))]
    
    # expr: expr1 (STR_CONCAT | COMPARE_STR) expr1 | expr1
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.STR_CONCAT():
            return BinaryOp(ctx.STR_CONCAT().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        elif ctx.COMPARE_STR():
            return BinaryOp(ctx.COMPARE_STR().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        else:
            return self.visit(ctx.expr1(0))
    
    # expr1: expr2 (EQUAL | NOT_EQUAL | GT | GE | LT | LE) expr2 | expr2;
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.NOT_EQUAL():
            return BinaryOp(ctx.NOT_EQUAL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.GT():
            return BinaryOp(ctx.GT().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.GE():
            return BinaryOp(ctx.GE().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.LT():
            return BinaryOp(ctx.LT().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.LE():
            return BinaryOp(ctx.LE().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        else:
            return self.visit(ctx.expr2(0))
    
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())
    
    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())
    
    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())
    
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5()))
        else: return self.visit(ctx.expr6())
    
    # expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.expr6()))
        else: return self.visit(ctx.expr7())
    
    # expr7: expr7 LSB expr RSB | expr8
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.getChildCount() == 4:
            arr = self.visit(ctx.expr7())
            expr = [self.visit(ctx.expr())] 
            return ArrayCell(arr,expr)
        else: return self.visit(ctx.expr8())
    
    # expr8: expr8 INSTANCE_ATTR_ACCESS ids
    # | expr8 INSTANCE_ATTR_ACCESS ids LP exprlists RP
    # | expr9
    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.getChildCount() == 3:
            obj = self.visit(ctx.expr8())
            fieldname = self.visit(ctx.ids())        
            return FieldAccess(obj,fieldname)
        if ctx.getChildCount() == 6:
            obj = self.visit(ctx.expr8())
            method = self.visit(ctx.ids())
            param = self.visit(ctx.exprlists())
            return CallExpr(obj,method,param)
        else: return self.visit(ctx.expr9())
    
    # expr9: ID_WITHOUT_STATIC STATIC_ATTR_ACCESS ID_STATIC 
    # | ID_WITHOUT_STATIC STATIC_ATTR_ACCESS ID_STATIC LP exprlists RP 
    # | expr10
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.getChildCount() == 3:
            obj = Id(ctx.ID_WITHOUT_STATIC().getText())
            fieldname = Id(ctx.ID_STATIC.getText())
            return FieldAccess(obj,fieldname)
        if ctx.getChildCount() == 6:
            obj = Id(ctx.ID_WITHOUT_STATIC().getText())
            method = Id(ctx.ID_STATIC.getText())
            param = self.visit(ctx.exprlists())
            return CallExpr(obj,method,param)
        else: return self.visit(ctx.expr10())
    
    # expr10: NEW ids LP exprlists RP expr10 | expr11;
    #  sẽ ko có testcase về trường hợp này
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.getChildCount() == 6:
            classname = self.visit(ctx.ids())
            param = self.visit(ctx.exprlists())
            return NewExpr(classname, param)     
        else: return self.visit(ctx.expr11())
    
    # expr11: LP expr RP | operand
    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        else: return self.visit(ctx.operand())
    
    # operand: intlit | FLOATLIT | BOOLLIT | STRLIT | ids | SELF | index_arrlit;
    def visitOperand(self, ctx: D96Parser.OperandContext):
        if ctx.intlit():
            return IntLiteral(self.visit(ctx.intlit()))
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == 'TRUE')
        if ctx.STRLIT():
            return StringLiteral(ctx.STRLIT().getText())
        if ctx.ids():
            return self.visit(ctx.ids())
        if ctx.SELF():
            return SelfLiteral()
        else:
            return self.visit(ctx.index_arrlit())
            
    
    # exprlists: exprlist | 
    def visitExprlists(self, ctx: D96Parser.ExprlistsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprlist())
        else: return[]
    
    # exprlist: expr CM exprlist | expr;
    def visitExprlist(self, ctx: D96Parser.ExprlistContext):
        if ctx.getChildCount() == 3:
            expr = [self.visit(ctx.expr())]
            exprlist = self.visit(ctx.exprlist())
            return expr + exprlist
        else: return [self.visit(ctx.expr())]
    
    # intlit: ZERO | INTLIT_GT0;
    def visitIntlit(self, ctx: D96Parser.IntlitContext):
        if ctx.ZERO():
            a = ctx.ZERO().getText()
            if a[0:2] == "0x" or a[0:2] == "0X": 
                return int(ctx.ZERO().getText(),16)
            if a[0:2] == "0b" or a[0:2] == "0B": 
                return int(ctx.ZERO().getText(),2)
            if a[0:2] == "00":   
                temp = ctx.ZERO().getText()
                res = temp[0] + 'o' + temp[1:len(temp)] 
                return int(res,8)
            else:
                return int(ctx.ZERO().getText())
        else :
            b = ctx.INTLIT_GT0().getText()
            if b[0:2] == "0x" or b[0:2] == "0X": 
                return int(ctx.INTLIT_GT0().getText(),16)
            if b[0:2] == "0b" or b[0:2] == "0B": 
                return int(ctx.INTLIT_GT0().getText(),2)
            if b[0:1] == "0": 
                temp = ctx.INTLIT_GT0().getText()
                res = temp[0] + 'o' + temp[1:len(temp)] 
                return int(res,8)
            else:
                return int(ctx.INTLIT_GT0().getText())
        
    # ids: ID_WITHOUT_STATIC | ID_STATIC;
    def visitIds(self, ctx: D96Parser.IdsContext):
        if ctx.ID_WITHOUT_STATIC():
            return Id(ctx.ID_WITHOUT_STATIC().getText())
        else: return Id(ctx.ID_STATIC().getText())
      
    # index_arrlit: ARRAY '(' (expr (',' expr)* | ) ')'  
    def visitIndex_arrlit(self, ctx: D96Parser.Index_arrlitContext):
        exprs = []
        for x in ctx.expr():
            exprs += [self.visit(x)]
        return ArrayLiteral(exprs)