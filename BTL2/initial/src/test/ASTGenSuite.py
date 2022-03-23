import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test2(self):
        input = """        
        Class Shape {
            Val $numOfShape: Int = 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test3(self):
        input = """
        Class Shape {
            Val immutableAttribute: Int = 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test4(self):
        input = """
        Class Shape {
            Var length, width: Int = 0, 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(width),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test5(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int = 0, 0;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(width),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test6(self):
        input = """
        Class Shape {
            getNumOfShape() {
                Return numOfShape;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(getNumOfShape),Instance,[],Block([Return(Id(numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,306))
        
    def test7(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Return numOfShape;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id(numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,307))
        
    def test8(self):
        input = """
        Class Shape {
            getNumOfShape() {
                Return $numOfShape;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(getNumOfShape),Instance,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test9(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Return $numOfShape;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,309))
        
    def test10(self):
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,310))
        
    def test11(self):
        input = """
        Class Shape {
            Var length, width: Int;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,311))
        
    def test12(self):
        input = """
        Class Program {
            main() {
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,312))
        
    def test13(self):
        input = """
        Class Program {
            main(x: Float) {
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(x),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,313))
        
    def test14(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([ConstDecl(x,IntType,IntLit(1)),ConstDecl(y,IntType,IntLit(2)),Return(BinaryOp(*,Id(x),Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,314))
        
    def test15(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Return Self.length * Self.width;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,315))
        
    def test16(self):
        input = """
        Class Shape {
            Constructor(x, y: Int ){
                Self.x = x;
                Self.y = y;
                Return Self.x * Self.y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x)),AssignStmt(FieldAccess(Self(),Id(y)),Id(y)),Return(BinaryOp(*,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(y))))]))])])"
        self.assertTrue(TestAST.test(input,expect,316))
        
    def test17(self):
        input = """
            Class Test{
                Var x, y: Float = 0, 0;
                
                compare(x, y: Float){
                    Return (Self.x == x) && (Self.y == y);
                }
                }"""
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(x),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,IntLit(0))),MethodDecl(Id(compare),Instance,[param(Id(x),FloatType),param(Id(y),FloatType)],Block([Return(BinaryOp(&&,BinaryOp(==,FieldAccess(Self(),Id(x)),Id(x)),BinaryOp(==,FieldAccess(Self(),Id(y)),Id(y))))]))])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test18(self):
        input = """
                ##
            Constructor with Return
        ##
        Class Shape {
            Constructor(x, y: Int ){
                Self.x = x;
                Self.y = y;
                Return Self.x * Self.y;
            }
            $getNumOfShape() {
                Val x: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x)),AssignStmt(FieldAccess(Self(),Id(y)),Id(y)),Return(BinaryOp(*,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(y))))])),MethodDecl(Id($getNumOfShape),Static,[],Block([ConstDecl(x,IntType,IntLit(1)),ConstDecl(y,IntType,IntLit(2)),Return(BinaryOp(*,Id(x),Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test19(self):
        input = """
        Class Shape {
            Destructor(x, y: Int){
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Destructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test20(self):
        input = """
        Class Shape {
            Constructor(x, y: Int ){
                Self.x = x;
                Self.y = y;
            }
            Destructor(x, y: Int){

            }
            $getNumOfShape() {
                Val x: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x)),AssignStmt(FieldAccess(Self(),Id(y)),Id(y))])),MethodDecl(Id(Destructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([])),MethodDecl(Id($getNumOfShape),Static,[],Block([ConstDecl(x,IntType,IntLit(1)),ConstDecl(y,IntType,IntLit(2)),Return(BinaryOp(*,Id(x),Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test21(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 5] = Array(1, 2, 3);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([VarDecl(a,ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3)])]))])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test22(self):
        input = """
        Class Calculatior {
            $calSum(){
                Break;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([Break]))])])"
        self.assertTrue(TestAST.test(input,expect,322))

    def test23(self):
        input = """
        Class Calculatior {
            $calSum(){
                Continue;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([Continue]))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test24(self):
        input = """
        Class main{}"""
        expect = "Program([ClassDecl(Id(main),[])])"
        self.assertTrue(TestAST.test(input,expect,324))

    def test25(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,325))

    def test26(self):
        input = """Class main_{}"""
        expect = "Program([ClassDecl(Id(main_),[])])"
        self.assertTrue(TestAST.test(input,expect,326))

    def test27(self):
        input = """
        Class Calculatior {
            $calSum(){
                Break ;Continue;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([Break,Continue]))])])"
        self.assertTrue(TestAST.test(input,expect,327))

    def test28(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = "abc";
                Val y: Int = 2;
                Return x*y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([ConstDecl(x,IntType,StringLit(abc)),ConstDecl(y,IntType,IntLit(2)),Return(BinaryOp(*,Id(x),Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,328))

    def test29(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    x = 5;
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    y = 8;
                }
                Else{
                    z = 0;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Triangle),[MethodDecl(Id(checkTriangle),Instance,[param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([If(BinaryOp(&&,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(x),IntLit(5))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(x),Id(z))),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(y),IntLit(8))]),Block([AssignStmt(Id(z),IntLit(0))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,329))

    def test30(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    x = 5;
                }
                Else{
                    z = 0;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Triangle),[MethodDecl(Id(checkTriangle),Instance,[param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([If(BinaryOp(&&,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(x),IntLit(5))]),Block([AssignStmt(Id(z),IntLit(0))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,330))

    def test31(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    x = 5;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Triangle),[MethodDecl(Id(checkTriangle),Instance,[param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([If(BinaryOp(&&,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(x),IntLit(5))]),None)]))])])"
        self.assertTrue(TestAST.test(input,expect,331))

    def test32(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    x = 5;
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    y = 8;
                }
                Elseif ((a == b) || (c == d) || (a == d)){
                    z = 9;
                }
                Else{
                    z = 0;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Triangle),[MethodDecl(Id(checkTriangle),Instance,[param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([If(BinaryOp(&&,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(x),IntLit(5))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(x),Id(z))),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(y),IntLit(8))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(==,Id(c),Id(d))),BinaryOp(==,Id(a),Id(d))),Block([AssignStmt(Id(z),IntLit(9))]),Block([AssignStmt(Id(z),IntLit(0))]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,332))

    def test33(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    x = 5;
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    y = 8;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Triangle),[MethodDecl(Id(checkTriangle),Instance,[param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([If(BinaryOp(&&,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(x),IntLit(5))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(x),Id(z))),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(y),IntLit(8))]),None))]))])])"
        self.assertTrue(TestAST.test(input,expect,333))

    def test34(self):
        input = """Class main : parent{}"""
        expect = "Program([ClassDecl(Id(main),Id(parent),[])])"
        self.assertTrue(TestAST.test(input,expect,334))

    def test35(self):
        input = """
        Class main{
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input,expect,335))

    def test36(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In (3+1) .. (5+4) By 1){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return sum;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(sum,FloatType,IntLit(0)),For(Id(counter),BinaryOp(+,IntLit(3),IntLit(1)),BinaryOp(+,IntLit(5),IntLit(4)),IntLit(1),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(i))),Break,Continue])]),Return(Id(sum))]))])])"
        self.assertTrue(TestAST.test(input,expect,336))

    def test37(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In 4 .. (5+4) By 1){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return sum;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(sum,FloatType,IntLit(0)),For(Id(counter),IntLit(4),BinaryOp(+,IntLit(5),IntLit(4)),IntLit(1),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(i))),Break,Continue])]),Return(Id(sum))]))])])"
        self.assertTrue(TestAST.test(input,expect,337))

    def test38(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In 4 .. 20 By 1){
                    sum = sum + i;
                    Break;
                    Continue;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(sum,FloatType,IntLit(0)),For(Id(counter),IntLit(4),IntLit(20),IntLit(1),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(i))),Break,Continue])])]))])])"
        self.assertTrue(TestAST.test(input,expect,338))

    def test39(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In (4*10) .. (50+4)){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return sum;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(sum,FloatType,IntLit(0)),For(Id(counter),BinaryOp(*,IntLit(4),IntLit(10)),BinaryOp(+,IntLit(50),IntLit(4)),IntLit(1),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(i))),Break,Continue])]),Return(Id(sum))]))])])"
        self.assertTrue(TestAST.test(input,expect,339))

    def test40(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In (4*10) .. (50+4)){
                    Foreach (counter In (3*5) .. (5+4)){
                        Continue;
                    }
                    Break;
                }
                Return sum;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(sum,FloatType,IntLit(0)),For(Id(counter),BinaryOp(*,IntLit(4),IntLit(10)),BinaryOp(+,IntLit(50),IntLit(4)),IntLit(1),Block([For(Id(counter),BinaryOp(*,IntLit(3),IntLit(5)),BinaryOp(+,IntLit(5),IntLit(4)),IntLit(1),Block([Continue])]),Break])]),Return(Id(sum))]))])])"
        self.assertTrue(TestAST.test(input,expect,340))

    def test41(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In a.b .. f By 1){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return sum;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(sum,FloatType,IntLit(0)),For(Id(counter),FieldAccess(Id(a),Id(b)),Id(f),IntLit(1),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(i))),Break,Continue])]),Return(Id(sum))]))])])"
        self.assertTrue(TestAST.test(input,expect,341))

    def test42(self):
        input = """
        Class Calculatior {
            $calSum(){
                Shape :: $getNumofShape();
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([Call(Id(Shape),Id($getNumofShape),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,342))

    def test43(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a, b: Int;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)]))])])"
        self.assertTrue(TestAST.test(input,expect,343))

    def test44(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a, b: Array[Int,5];
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType))]))])])"
        self.assertTrue(TestAST.test(input,expect,344))

    def test45(self):
        input = """
        Class Calculatior {
            $calSum(){
                Foreach(x In 5 .. 2){
                    Out.printInt(arr[x]);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,345))

    def test46(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var r, s: Int;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType)]))])])"
        self.assertTrue(TestAST.test(input,expect,346))

    def test47(self):
        input = """
        Class Calculatior {
            $calSum(){
                r = 2.0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([AssignStmt(Id(r),FloatLit(2.0))]))])])"
        self.assertTrue(TestAST.test(input,expect,347))

    def test48(self):
        input = """
        Class Calculatior {
            $calSum(){
                s = r * r * Self.myPI;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI))))]))])])"
        self.assertTrue(TestAST.test(input,expect,348))

    def test49(self):
        input = """
        Class Calculatior {
            $calSum(){
                r = a[5];
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([AssignStmt(Id(r),ArrayCell(Id(a),[IntLit(5)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,349))

    def test50(self):
        input = """
        Class Calculatior {
            $calSum(){
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,350))

    def test51(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 012;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(10))]))])])"
        self.assertTrue(TestAST.test(input,expect,351))

    def test52(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 072;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(58))]))])])"
        self.assertTrue(TestAST.test(input,expect,352))

    def test53(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 02;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(2))]))])])"
        self.assertTrue(TestAST.test(input,expect,353))

    def test54(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0xAF;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(175))]))])])"
        self.assertTrue(TestAST.test(input,expect,354))

    def test55(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0X2B;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(43))]))])])"
        self.assertTrue(TestAST.test(input,expect,355))

    def test56(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0b1010001101;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(653))]))])])"
        self.assertTrue(TestAST.test(input,expect,356))

    def test57(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0B1011;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(11))]))])])"
        self.assertTrue(TestAST.test(input,expect,357))

    def test58(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 00;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,358))

    def test59(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0x0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,359))

    def test60(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0X0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,360))

    def test61(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0b0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,361))

    def test62(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0B0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,362))

    def test63(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var a : Int = 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([VarDecl(a,IntType,IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,363))

    def test64(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,364))

    def test65(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Square: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,365))

    def test66(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        CLass Square: Rectangle {
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,366))

    def test67(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,367))

    def test68(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        CLass Square: Rectangle {
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,368))

    def test69(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        CLass Parallelogram: Rectangle {
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,369))

    def test70(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        CLass Parallelogram: Rectangle {
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        CLass Equilateral: Triangle {
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,370))

    def test71(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        CLass Parallelogram: Rectangle {
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        CLass IsoscelesRight: Triangle {
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,371))

    def test72(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        CLass Parallelogram: Rectangle {
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        CLass ObtuseIsosceles: Triangle {
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,372))

    def test73(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        CLass Parallelogram: Rectangle {
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        CLass AcuteIsosceles: Triangle {
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,373))

    def test74(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        CLass RightScalene : Triangle {
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,374))

    def test75(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        CLass ObtuseScalene : Triangle {
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,375))

    def test76(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Var length, width, height: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Triangle: Shape {
            getArea() {
                Return Self.width * Self.height / 2;
            }
        }
        CLass AcuteScalene  : Triangle {
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,376))

    def test77(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Var length, width, height: Int;
            Var radius: Float;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        CLass Circle: Shape {
            getArea() {
                Return 3.14 * Self.radius * Self.radius;
            }
        }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(radius),FloatType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,377))

    def test78(self):
        input = """
        Class Program {}
        """
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,378))

    def test79(self):
        input = """
        Class Rectangle : Shape {}
        """
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,379))

    def test80(self):
        input = """
        Class Rectangle {
            Var length: Int;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,380))

    def test81(self):
        input = """
        Class Rectangle {
            Val $x: Int = 10;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input,expect,381))

    def test82(self):
        input = """
        Class Program {
            main(x: Float) {
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(x),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,382))
        
    def test83(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([ConstDecl(x,IntType,IntLit(1)),ConstDecl(y,IntType,IntLit(2)),Return(BinaryOp(*,Id(x),Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,383))
        
    def test84(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Return Self.length * Self.width;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,384))
        
    def test85(self):
        input = """
        Class Shape {
            Constructor(x, y: Int ){
                Self.x = x;
                Self.y = y;
                Return Self.x * Self.y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x)),AssignStmt(FieldAccess(Self(),Id(y)),Id(y)),Return(BinaryOp(*,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(y))))]))])])"
        self.assertTrue(TestAST.test(input,expect,385))
        
    def test86(self):
        input = """
            Class Test{
                Var x, y: Float = 0, 0;
                
                compare(x, y: Float){
                    Return (Self.x == x) && (Self.y == y);
                }
                }"""
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(x),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,IntLit(0))),MethodDecl(Id(compare),Instance,[param(Id(x),FloatType),param(Id(y),FloatType)],Block([Return(BinaryOp(&&,BinaryOp(==,FieldAccess(Self(),Id(x)),Id(x)),BinaryOp(==,FieldAccess(Self(),Id(y)),Id(y))))]))])])"
        self.assertTrue(TestAST.test(input,expect,386))

    def test87(self):
        input = """
                ##
            Constructor with Return
        ##
        Class Shape {
            Constructor(x, y: Int ){
                Self.x = x;
                Self.y = y;
                Return Self.x * Self.y;
            }
            $getNumOfShape() {
                Val x: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x)),AssignStmt(FieldAccess(Self(),Id(y)),Id(y)),Return(BinaryOp(*,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(y))))])),MethodDecl(Id($getNumOfShape),Static,[],Block([ConstDecl(x,IntType,IntLit(1)),ConstDecl(y,IntType,IntLit(2)),Return(BinaryOp(*,Id(x),Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,387))

    def test88(self):
        input = """
        Class Shape {
            Destructor(x, y: Int){
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Destructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,388))

    def test89(self):
        input = """
        Class Shape {
            Constructor(x, y: Int ){
                Self.x = x;
                Self.y = y;
            }
            Destructor(x, y: Int){

            }
            $getNumOfShape() {
                Val x: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x)),AssignStmt(FieldAccess(Self(),Id(y)),Id(y))])),MethodDecl(Id(Destructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([])),MethodDecl(Id($getNumOfShape),Static,[],Block([ConstDecl(x,IntType,IntLit(1)),ConstDecl(y,IntType,IntLit(2)),Return(BinaryOp(*,Id(x),Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,389))

    def test90(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 5] = Array(1, 2, 3);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([VarDecl(a,ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3)])]))])])"
        self.assertTrue(TestAST.test(input,expect,390))

    def test91(self):
        input = """
        Class Calculatior {
            $calSum(){
                Break;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([Break]))])])"
        self.assertTrue(TestAST.test(input,expect,391))

    def test92(self):
        input = """
        Class Calculatior {
            $calSum(){
                Continue;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([Continue]))])])"
        self.assertTrue(TestAST.test(input,expect,392))

    def test93(self):
        input = """
        Class main{}"""
        expect = "Program([ClassDecl(Id(main),[])])"
        self.assertTrue(TestAST.test(input,expect,393))

    def test94(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,394))

    def test95(self):
        input = """Class main_{}"""
        expect = "Program([ClassDecl(Id(main_),[])])"
        self.assertTrue(TestAST.test(input,expect,395))

    def test96(self):
        input = """
        Class Calculatior {
            $calSum(){
                Break ;Continue;
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculatior),[MethodDecl(Id($calSum),Static,[],Block([Break,Continue]))])])"
        self.assertTrue(TestAST.test(input,expect,396))

    def test97(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = "abc";
                Val y: Int = 2;
                Return x*y;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([ConstDecl(x,IntType,StringLit(abc)),ConstDecl(y,IntType,IntLit(2)),Return(BinaryOp(*,Id(x),Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,397))

    def test98(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    x = 5;
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    y = 8;
                }
                Else{
                    z = 0;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Triangle),[MethodDecl(Id(checkTriangle),Instance,[param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([If(BinaryOp(&&,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(x),IntLit(5))]),If(BinaryOp(||,BinaryOp(||,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(x),Id(z))),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(y),IntLit(8))]),Block([AssignStmt(Id(z),IntLit(0))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,398))

    def test99(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    x = 5;
                }
                Else{
                    z = 0;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Triangle),[MethodDecl(Id(checkTriangle),Instance,[param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([If(BinaryOp(&&,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(x),IntLit(5))]),Block([AssignStmt(Id(z),IntLit(0))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,399))

    def test100(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    x = 5;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Triangle),[MethodDecl(Id(checkTriangle),Instance,[param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType)],Block([If(BinaryOp(&&,BinaryOp(==,Id(x),Id(y)),BinaryOp(==,Id(y),Id(z))),Block([AssignStmt(Id(x),IntLit(5))]),None)]))])])"
        self.assertTrue(TestAST.test(input,expect,400))


   