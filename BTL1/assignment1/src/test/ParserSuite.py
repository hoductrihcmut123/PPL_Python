import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))

    def test_1(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int = 0, 0;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        Class Rectangle: Shape {
            getArea() {
                Shape::$getNumOfShape();
                Return Self.length * Self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_2(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Return Self.length * Self.width;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    
    def test_4(self):
      input="""
            Class Test{
               Var ins: Int;
               Var $static: Int;
               
               Test(){
                  Var a: Int= Self::ins;
                  Var b: Int= Self::$static;
               }
            }
      """
      expect = "Error on line 7 col 34: ::"
      self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
        input="""
                Class Test{
                Var x, y: Float = 0, 0;
                
                compare(x, y: Float){
                    Return (Self.x == x) && (Self.y == y);
                }
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    #Constructor with Return;
    def test_6(self):
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
        }
        """
        expect = "successful" 
        self.assertTrue(TestParser.test(input,expect,206))

    #Destructor with parameters;
    def test_7(self):
        input = """
        ##
            Constructor with Return
        ##
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
        }
        """
        expect = "successful" 
        self.assertTrue(TestParser.test(input,expect,207))

    def test_8(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 5] = Array(1, 2, 3);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    
    # Non-static after ::
    def test_9(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
                Return Shape::length * Shape::width;
            }
        }
        """
        expect = "Error on line 4 col 30: length"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_10(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 5 col 25: ("
        self.assertTrue(TestParser.test(input,expect,210))

    def test_11(self):
        input = """
        Class SquareTriagnle {
            getArea() {
                Self.area = (self.x * self.y)/2;
                If (area < 0){
                    print("Nonsense");
                }
                Elseif ((0< area) && (area<=10)){
                    print("Small");
                }
                Elseif ((10 < area) && (area <= 20)){
                    print("Medium");
                }
                Else{
                    print("Large");
                }
            }
        }
        """
        expect = "Error on line 6 col 25: ("
        self.assertTrue(TestParser.test(input,expect,211))

    def test_12(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (Shape.a In (3+1) .. (5+4) By 1){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return sum;
            }
        }
        """
        expect = "Error on line 5 col 30: ."
        self.assertTrue(TestParser.test(input,expect,212))

    def test_13(self):
        input = """
        Class Calculatior {
            $calSum(){
                Break;
            }
        }
        """
        expect = "successful" 
        self.assertTrue(TestParser.test(input,expect,213))

    def test_14(self):
        input = """
        Class Calculatior {
            $calSum(){
                Continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
        
    def test_15(self):
        input = """
        Class main{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        
    def test_16(self):
        input = """
Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
        
    def test_17(self):
        input = """
    Class Shape {
        $getNumOfShape( {
            Return Self.length * Self.width;
        }
    }
"""
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input,expect,217))   
        
    def test_18(self):
        input = """
        Class main_{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
        
    def test_19(self):
        input = """
        class main{}
        """
        expect = "Error on line 2 col 8: class"
        self.assertTrue(TestParser.test(input,expect,219))
        
    def test_20(self):
        input = """
        Class main;{}
        """
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.test(input,expect,220))       
        
    def test_21(self):
        input = """
        Class Calculatior {
            $calSum(){
                Continue;
            }
        }
        """
        expect = "successful" 
        self.assertTrue(TestParser.test(input,expect,221))

    def test_22(self):
        input = """
        Class Calculatior {
            $calSum(){
                Breakkk;
            }
        }
        """
        expect = "Error on line 4 col 23: ;" 
        self.assertTrue(TestParser.test(input,expect,222))

    def test_23(self):
        input = """
        Class Calculatior {
            $calSum(){
                Break ;Continue;
            }
        }
        """
        expect = "successful" 
        self.assertTrue(TestParser.test(input,expect,223))

    def test_24(self):
        input = """
        Class Calculatior {
            $calSum(){
                break;
            }
        }
        """
        expect = "Error on line 4 col 21: ;" 
        self.assertTrue(TestParser.test(input,expect,224))
 
    def test_25(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
                Return Shape::$length * Shape::width;
            }
        }
        """
        expect = "Error on line 4 col 47: width"
        self.assertTrue(TestParser.test(input,expect,225))
        
    def test_26(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
                Return Shape.length * Shape::width;
            }
        }
        """
        expect = "Error on line 4 col 45: width"
        self.assertTrue(TestParser.test(input,expect,226))
        
    def test_27(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
                Return Self::length * Self::width;
            }
        }
        """
        expect = "Error on line 4 col 27: ::"
        self.assertTrue(TestParser.test(input,expect,227))
        
    def test_28(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))   
        
    def test_29(self):
        input = """
        Class Calculatior {
            $calSum(){
                Break;
            
        }
        """
        expect = "Error on line 7 col 8: <EOF>" 
        self.assertTrue(TestParser.test(input,expect,229))
        
    def test_30(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val $x: Int = 1;
                Val $y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "Error on line 4 col 20: $x"
        self.assertTrue(TestParser.test(input,expect,230))
        
    def test_31(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = 1,2;
                Val y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "Error on line 4 col 30: ,"
        self.assertTrue(TestParser.test(input,expect,231))
        
    def test_32(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x,z: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "Error on line 4 col 32: ;"
        self.assertTrue(TestParser.test(input,expect,232))
        
    def test_33(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = "abc";
                Val y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    
    def test_34(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 0] = Array(1, 2, 3);
            }
        }
        """
        expect = "Error on line 4 col 34: 0"
        self.assertTrue(TestParser.test(input,expect,234))
        
    def test_35(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 5] = Array(1, 2, "abc");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
        
    def test_36(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 5] = Array(1, , 3);
            }
        }
        """
        expect = "Error on line 4 col 48: ,"
        self.assertTrue(TestParser.test(input,expect,236))
        
    def test_37(self):
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
        
    def test_38(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    Continue;
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 8 col 25: ("
        self.assertTrue(TestParser.test(input,expect,238))
        
    def test_39(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                Foreach ((x == y) && (y == z)){
                    print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 4 col 25: ("
        self.assertTrue(TestParser.test(input,expect,239))
        
    def test_40(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float, y: Float; z:Float){
                If ((x == y) && (y == z)){
                    print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 3 col 34: ,"
        self.assertTrue(TestParser.test(input,expect,240))
        
    def test_41(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z,k,l,m:Float){
                If ((x == y) && (y == z)){
                    print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 5 col 25: ("
        self.assertTrue(TestParser.test(input,expect,241))
        
    def test_42(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    Self.print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 8 col 25: ("
        self.assertTrue(TestParser.test(input,expect,242))
        
    def test_43(self):
        input = """
        Class main{
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,243))
        
    def test_44(self):
        input = """
        Class _ain{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
        
    def test_45(self):
        input = """
        Class main() {}
        """
        expect = "Error on line 2 col 18: ("
        self.assertTrue(TestParser.test(input,expect,245))
        
    def test_46(self):
        input = """
          Class main () {
            putIntLn(4);
         }
        """
        expect = "Error on line 2 col 21: ("
        self.assertTrue(TestParser.test(input,expect,246))
        
    def test_47(self):
        input = """
       int main( {}
        """
        expect = "Error on line 2 col 7: int"
        self.assertTrue(TestParser.test(input,expect,247))
        
    def test_48(self):
        input = """
  class Main {
  int x = 5;

 main(String[] args) {
    Main myObj1 = new Main();  // Object 1
    Main myObj2 = new Main();  // Object 2
    System.out.println(myObj1.x);
    System.out.println(myObj2.x);
  }
}
        """
        expect = "Error on line 2 col 2: class"
        self.assertTrue(TestParser.test(input,expect,248))
        
    def test_49(self):
        input = """
        Class main : parent{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
        
    def test_50(self):
        input = """
        Class Self{}
        """
        expect = "Error on line 2 col 14: Self"
        self.assertTrue(TestParser.test(input,expect,250))
        
    def test_51(self):
        input = """
     class Person {
    public:
        string firstName;
        string lastName;
        int age;

        void fullname() {
            cout << this->firstName << ' ' << Person::lastName;
        }
};
        """
        expect = "Error on line 2 col 5: class"
        self.assertTrue(TestParser.test(input,expect,251))
        
    def test_52(self):
        input = """
        Class main{
            Destructor ()
        }
        """
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input,expect,252))
        
    def test_53(self):
        input = """
        Class main{
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
        
    def test_54(self):
        input = """
        Class Program {
            main() {
                Out.printInt(Shape::numOfShape);
            }
        }
        """
        expect = "Error on line 4 col 36: numOfShape"
        self.assertTrue(TestParser.test(input,expect,254))
        
    def test_55(self):
        input = """
        Class main{
            Constructor ()
        }
        """
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input,expect,255))
        
    def test_56(self):
        input = """
            ##
            test 56
            ##
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,256))
        
    def test_57(self):
        input = """
        Class main{
            Shape::$getNumOfShape();
        }
        """
        expect = "Error on line 3 col 17: ::"
        self.assertTrue(TestParser.test(input,expect,257))
        
    def test_58(self):
        input = """
        Class main{
            var r, s: Int;
            r = 2.0;
            var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0] = s;
        }
        """
        expect = "Error on line 3 col 16: r"
        self.assertTrue(TestParser.test(input,expect,258))
        
    def test_59(self):
        input = """
        Class main{
            var r, s: Int;
            r = 2.0;
            var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0,1] = s;
        }
        """
        expect = "Error on line 3 col 16: r"
        self.assertTrue(TestParser.test(input,expect,259))
        
    def test_60(self):
        input = """
    Class Shape {
        Va $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
    $getNumOfShape() {
        Return $numOfShape;
    }
        """
        expect = "Error on line 3 col 11: $numOfShape"
        self.assertTrue(TestParser.test(input,expect,260))
        
    def test_61(self):
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        ar length, width: Int;
    $getNumOfShape() {
        Return $numOfShape;
    }
        """
        expect = "Error on line 5 col 11: length"
        self.assertTrue(TestParser.test(input,expect,261))
        
    def test_62(self):
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: int;
    $getNumOfShape() {
        Return $numOfShape;
    }
        """
        expect = "Error on line 5 col 27: int"
        self.assertTrue(TestParser.test(input,expect,262))
        
    def test_63(self):
        input = """
    Class Shape {
        Val $numOfShape Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
    $getNumOfShape() {
        Return $numOfShape;
    }
        """
        expect = "Error on line 3 col 24: Int"
        self.assertTrue(TestParser.test(input,expect,263))
        
    def test_64(self):
        input = """
    Class $Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
    $getNumOfShape() {
        Return $numOfShape;
    }
        """
        expect = "Error on line 2 col 10: $Shape"
        self.assertTrue(TestParser.test(input,expect,264))
        
    def test_65(self):
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, $width: Int;
    $getNumOfShape() {
        Return $numOfShape;
    }
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,265))
        
    def test_66(self):
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
    $getNumOfShape() {
        Return $numOfShape + immutableAttribute * length ;
    }
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,266))
        
    def test_67(self):
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
    $getNumOfShape() {
        Return Self.$numOfShape;
    }
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,267))
        
    def test_68(self):
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
    Self::$getNumOfShape() {
        Return $numOfShape;
    }
        """
        expect = "Error on line 6 col 4: Self"
        self.assertTrue(TestParser.test(input,expect,268))
        
    def test_69(self):
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0, "test69";
        Var length, width: Int;
    $getNumOfShape() {
        Return $numOfShape;
    }
        """
        expect = "Error on line 4 col 39: ,"
        self.assertTrue(TestParser.test(input,expect,269))
        
    def test_70(self):
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
        
    def test_71(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In (3+1) ... (5+4) By 1){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return sum;
            }
        }
        """
        expect = "Error on line 5 col 44: ."
        self.assertTrue(TestParser.test(input,expect,271))
        
    def test_72(self):
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
        
    def test_73(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In (3+1) .. (5+4)){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return sum;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
        
    def test_74(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float =;
                Foreach (counter In (3+1) .. (5+4) By 1){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return sum;
            }
        }
        """
        expect = "Error on line 4 col 32: ;"
        self.assertTrue(TestParser.test(input,expect,274))
        
    def test_75(self):
        input = """
        Class Calculatior {
            $calSum(){
                Var sum: Float = 0;
                Foreach (counter In (3+1) .. (5+4) By 1){
                    sum = sum + i;
                    Break;
                    Continue;
                }
                Return ;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
        
    def test_76(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[int, 5] = Array(1, 2, 3);
            }
        }
        """
        expect = "Error on line 4 col 29: int"
        self.assertTrue(TestParser.test(input,expect,276))
        
    def test_77(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 1] = Array(1, 2, 3);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
        
    def test_78(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array(Int, 5) = Array(1, 2, 3);
            }
        }
        """
        expect = "Error on line 4 col 28: ("
        self.assertTrue(TestParser.test(input,expect,278))
        
    def test_79(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int,] = Array(1, 2, 3);
            }
        }
        """
        expect = "Error on line 4 col 33: ]"
        self.assertTrue(TestParser.test(input,expect,279))
        
    def test_80(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a:  = Array(1, 2, 3);
            }
        }
        """
        expect = "Error on line 4 col 24: ="
        self.assertTrue(TestParser.test(input,expect,280))
        
    def test_81(self):
        input = """
        Class main{
            var r, s:;
            r = 2.0;
            var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0] = s;
        }
        """
        expect = "Error on line 3 col 16: r"
        self.assertTrue(TestParser.test(input,expect,281))
        
    def test_82(self):
        input = """
        Class main{
            var r, s: Int;
            r = 2.0;
            var a, b: Array[Int, 5];
            s = r * r * Self::myPI;
            a[0] = s;
        }
        """
        expect = "Error on line 3 col 16: r"
        self.assertTrue(TestParser.test(input,expect,282))
        
    def test_83(self):
        input = """
        Class main{
            var r, s: Int;
            r = 2.0;
            var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0] = a[1];
        }
        """
        expect = "Error on line 3 col 16: r"
        self.assertTrue(TestParser.test(input,expect,283))
        
    def test_84(self):
        input = """
        Class main{
            var r, s: Int;
            r = 2.0;
            a[0] = s;
        }
        """
        expect = "Error on line 3 col 16: r"
        self.assertTrue(TestParser.test(input,expect,284))
        
    def test_85(self):
        input = """
        Class main{
            m(){
            Var r, s: Int;
            r = 2.0;
            a[0] = s;
             var a, b: Array[Int, 5] = "test85", 10;
             }
        }
        """
        expect = "Error on line 6 col 17: ="
        self.assertTrue(TestParser.test(input,expect,285))
        
    def test_86(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val $x: Int = 1;
                Val $y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "Error on line 4 col 20: $x"
        self.assertTrue(TestParser.test(input,expect,286))
        
    def test_31(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = 1,2;
                Val y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "Error on line 4 col 30: ,"
        self.assertTrue(TestParser.test(input,expect,231))
        
    def test_87(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x,z: Int = 1;
                Val y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "Error on line 4 col 32: ;"
        self.assertTrue(TestParser.test(input,expect,287))
        
    def test_88(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Val x: Int = "abc";
                Val y: Int = 2;
                Return x*y;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    
    def test_89(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 0] = Array(1, 2, 3);
            }
        }
        """
        expect = "Error on line 4 col 34: 0"
        self.assertTrue(TestParser.test(input,expect,289))
        
    def test_90(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 5] = Array(1, 2, "abc");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
        
    def test_91(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                Var a: Array[Int, 5] = Array(1, , 3);
            }
        }
        """
        expect = "Error on line 4 col 48: ,"
        self.assertTrue(TestParser.test(input,expect,291))
        
    def test_92(self):
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
        
    def test_93(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    Continue;
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 8 col 25: ("
        self.assertTrue(TestParser.test(input,expect,293))
        
    def test_94(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                Foreach ((x == y) && (y == z)){
                    print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 4 col 25: ("
        self.assertTrue(TestParser.test(input,expect,294))
        
    def test_95(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float, y: Float; z:Float){
                If ((x == y) && (y == z)){
                    print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 3 col 34: ,"
        self.assertTrue(TestParser.test(input,expect,295))
        
    def test_96(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z,k,l,m:Float){
                If ((x == y) && (y == z)){
                    print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 5 col 25: ("
        self.assertTrue(TestParser.test(input,expect,296))
        
    def test_97(self):
        input = """
        Class Triangle {
            checkTriangle(x: Float; y: Float; z:Float){
                If ((x == y) && (y == z)){
                    Self.print("equilateral triangle");
                }
                Elseif ((x == y) || (x == z) || (y == z)){
                    print("isosceles triangle");
                }
                Else{
                    print("Triagle");
                }
            }
        }
        """
        expect = "Error on line 8 col 25: ("
        self.assertTrue(TestParser.test(input,expect,297))
        
    def test_98(self):
        input = """
        Class main{
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,298))
        
    def test_99(self):
        input = """
        Class _ain{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
        
    def test_100(self):
        input = """
        Class main() {}
        """
        expect = "Error on line 2 col 18: ("
        self.assertTrue(TestParser.test(input,expect,300))
        