import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_1(self):
        self.assertTrue(TestLexer.test("""
        abcd
        ""","abcd,<EOF>",101))
    
    def test_2(self):
        self.assertTrue(TestLexer.test("""
        abcd_
        ""","abcd_,<EOF>",102))
    
    def test_3(self):
        self.assertTrue(TestLexer.test("""
        $abcd
        ""","$abcd,<EOF>",103))
    
    def test_4(self):
        self.assertTrue(TestLexer.test("""
        $1234
        ""","$1234,<EOF>",104))
    
    def test_5(self):
        self.assertTrue(TestLexer.test("""
        $___
        ""","$___,<EOF>",105))
    
    def test_6(self):
        self.assertTrue(TestLexer.test("""
        _12325
        ""","_12325,<EOF>",106))
    
    def test_7(self):
        self.assertTrue(TestLexer.test("""
        $_12325
        ""","$_12325,<EOF>",107))
    
    def test_8(self):
        self.assertTrue(TestLexer.test("""
        _abcd
        ""","_abcd,<EOF>",108))
    
    def test_9(self):
        self.assertTrue(TestLexer.test("""
        $.1234567
        ""","Error Token $",109))
    
    def test_10(self):
        self.assertTrue(TestLexer.test("""
        12345
        ""","12345,<EOF>",110))
    
    def test_11(self):
        self.assertTrue(TestLexer.test("""
        055
        ""","055,<EOF>",111))
    
    def test_12(self):
        self.assertTrue(TestLexer.test("""
        0x0
        ""","0x0,<EOF>",112))
    
    def test_13(self):
        self.assertTrue(TestLexer.test("""
        0026
        ""","00,26,<EOF>",113))
    
    def test_14(self):
        self.assertTrue(TestLexer.test("""
        0334
        ""","0334,<EOF>",114))
    
    def test_15(self):
        self.assertTrue(TestLexer.test("""
        0X20
        ""","0X20,<EOF>",115))
    
    def test_16(self):
        self.assertTrue(TestLexer.test("""
        0x00
        ""","0x0,0,<EOF>",116))
    
    def test_17(self):
        self.assertTrue(TestLexer.test("""
        0xb0
        ""","0,xb0,<EOF>",117))
    
    def test_18(self):
        self.assertTrue(TestLexer.test("""
        00
        ""","00,<EOF>",118))
    
    def test_19(self):
        self.assertTrue(TestLexer.test("""
        0b10101
        ""","0b10101,<EOF>",119))
    
    def test_20(self):
        self.assertTrue(TestLexer.test("""
        01643
        ""","01643,<EOF>",120))
    
    def test_21(self):
        self.assertTrue(TestLexer.test("""
        0B20
        ""","0,B20,<EOF>",121))
    
    def test_22(self):
        self.assertTrue(TestLexer.test("""
        5.0
        ""","5.0,<EOF>",122))
    
    def test_23(self):
        self.assertTrue(TestLexer.test("""
        2.
        ""","2.,<EOF>",123))
    
    def test_24(self):
        self.assertTrue(TestLexer.test("""
        1.e10
        ""","1.e10,<EOF>",124))
    
    def test_25(self):
        self.assertTrue(TestLexer.test("""
        12_213_2.231_321
        ""","122132.231,_321,<EOF>",125))
    
    def test_26(self):
        self.assertTrue(TestLexer.test("""
        12_12.e1_2
        ""","1212.e1,_2,<EOF>",126))
    
    def test_27(self):
        self.assertTrue(TestLexer.test("""
        23.454f8
        ""","23.454,f8,<EOF>",127))
    
    def test_28(self):
        self.assertTrue(TestLexer.test("""
        e-10
        ""","e,-,10,<EOF>",128))
    
    def test_29(self):
        self.assertTrue(TestLexer.test("""
        2e
        ""","2,e,<EOF>",129))
    
    def test_30(self):
        self.assertTrue(TestLexer.test("""
        1e-102
        ""","1e-102,<EOF>",130))
    
    def test_31(self):
        self.assertTrue(TestLexer.test("""
        .123
        """,".,123,<EOF>",131))
    
    def test_32(self):
        self.assertTrue(TestLexer.test("""
        (1,2,3)
        ""","(,1,,,2,,,3,),<EOF>",132))
    
    def test_33(self):
        self.assertTrue(TestLexer.test("""
        (1,1.0,0)
        ""","(,1,,,1.0,,,0,),<EOF>",133))
    
    def test_34(self):
        self.assertTrue(TestLexer.test("""
        (\"abc\",\"abc\")
        ""","(,abc,,,abc,),<EOF>",134))
    
    def test_35(self):
        self.assertTrue(TestLexer.test("""
        ((a),(b),(c))
        ""","(,(,a,),,,(,b,),,,(,c,),),<EOF>",135))
    
    def test_36(self):
        self.assertTrue(TestLexer.test("""
        \"ab	\"
        ""","Unclosed String: ab",136))
    
    def test_37(self):
        self.assertTrue(TestLexer.test("""
        \"abc
        \"
        ""","Unclosed String: abc",137))
    
    def test_38(self):
        self.assertTrue(TestLexer.test("""
        \"abc\"\"
        ""","abc,Unclosed String: ",138))
    
    def test_39(self):
        self.assertTrue(TestLexer.test("""
        \"\"abc\"\"
        """,",abc,,<EOF>",139))
    
    def test_40(self):
        self.assertTrue(TestLexer.test("""
        \"'\"'\"'\"
        ""","Unclosed String: '\"'\"'\"",140))
    
    def test_41(self):
        self.assertTrue(TestLexer.test("""
        \"'\"'\"'\\'\"
        ""","Unclosed String: '\"'\"'",141))
    
    def test_42(self):
        self.assertTrue(TestLexer.test("""
        \"\\t\"
        ""","Unclosed String: ",142))
    
    def test_43(self):
        self.assertTrue(TestLexer.test("""
        \"	\"
        ""","Unclosed String: ",143))
    
    def test_44(self):
        self.assertTrue(TestLexer.test("""
        \"abc'\"\"
        ""","abc'\",<EOF>",144))
    
    def test_45(self):
        self.assertTrue(TestLexer.test("""
        \"ab
        \"
        ""","Unclosed String: ab",145))
    
    def test_46(self):
        self.assertTrue(TestLexer.test("""
        \"abc\\h\"
        ""","Illegal Escape In String: abc\\h",146))
    
    def test_47(self):
        self.assertTrue(TestLexer.test("""
        \"abcddd\\n\"
        ""","Unclosed String: abcddd",147))
    
    def test_48(self):
        self.assertTrue(TestLexer.test("""
        \"abc\\\"
        ""","Illegal Escape In String: abc\\\"",148))
    
    def test_49(self):
        self.assertTrue(TestLexer.test("""
        \"\\x
        ""","Illegal Escape In String: \\x",149))
    
    def test_50(self):
        self.assertTrue(TestLexer.test("""
        \"abc,'\"aaa'\"\"
        ""","abc,'\"aaa'\",<EOF>",150))
    
    def test_51(self):
        self.assertTrue(TestLexer.test("""
        \"\"
        """,",<EOF>",151))
    
    def test_52(self):
        self.assertTrue(TestLexer.test("""
        \"\" \"\"
        """,",,<EOF>",152))
    
    def test_53(self):
        self.assertTrue(TestLexer.test("""
        \"Tri\"\"
        ""","Tri,Unclosed String: ",153))
    
    def test_54(self):
        self.assertTrue(TestLexer.test("""
        2==1
        ""","2,==,1,<EOF>",154))
    
    def test_55(self):
        self.assertTrue(TestLexer.test("""
        2>3
        ""","2,>,3,<EOF>",155))
    
    def test_56(self):
        self.assertTrue(TestLexer.test("""
        5<6
        ""","5,<,6,<EOF>",156))
    
    def test_57(self):
        self.assertTrue(TestLexer.test("""
        \"abc\"+.\"xyz\"
        ""","abc,+.,xyz,<EOF>",157))
    
    def test_58(self):
        self.assertTrue(TestLexer.test("""
        2+3*5/4
        ""","2,+,3,*,5,/,4,<EOF>",158))
    
    def test_59(self):
        self.assertTrue(TestLexer.test("""
        return 2*x
        ""","return,2,*,x,<EOF>",159))
    
    def test_60(self):
        self.assertTrue(TestLexer.test("""
        studentX.height
        ""","studentX,.,height,<EOF>",160))
    
    def test_61(self):
        self.assertTrue(TestLexer.test("""
        A.B.C
        ""","A,.,B,.,C,<EOF>",161))
    
    def test_62(self):
        self.assertTrue(TestLexer.test("""
        A::$AAA
        ""","A,::,$AAA,<EOF>",162))
    
    def test_63(self):
        self.assertTrue(TestLexer.test("""
        Y^5
        ""","Y,Error Token ^",163))
    
    def test_64(self):
        self.assertTrue(TestLexer.test("""

        ""","<EOF>",164))
    
    def test_65(self):
        self.assertTrue(TestLexer.test("""
        X=10+2+i
        ""","X,=,10,+,2,+,i,<EOF>",165))
    
    def test_66(self):
        self.assertTrue(TestLexer.test("""
        arr[1][2][3]
        ""","arr,[,1,],[,2,],[,3,],<EOF>",166))
    
    def test_67(self):
        self.assertTrue(TestLexer.test("""
        arr[x+x][y][(2+2)*3]
        ""","arr,[,x,+,x,],[,y,],[,(,2,+,2,),*,3,],<EOF>",167))
    
    def test_68(self):
        self.assertTrue(TestLexer.test("""
        S::arr.x.y.z[1][2]
        ""","S,::,arr,.,x,.,y,.,z,[,1,],[,2,],<EOF>",168))
    
    def test_69(self):
        self.assertTrue(TestLexer.test("""
        a.b.c(2,3,4,New c)
        ""","a,.,b,.,c,(,2,,,3,,,4,,,New,c,),<EOF>",169))
    
    def test_70(self):
        self.assertTrue(TestLexer.test("""
        New A(2,3)
        ""","New,A,(,2,,,3,),<EOF>",170))
    
    def test_71(self):
        self.assertTrue(TestLexer.test("""
        Return 33
        ""","Return,33,<EOF>",171))
    
    def test_72(self):
        self.assertTrue(TestLexer.test("""
        \"abc\" ==. \"abc\"
        ""","abc,==.,abc,<EOF>",172))
    
    def test_73(self):
        self.assertTrue(TestLexer.test("""
        \"\" == \"\"
        """,",==,,<EOF>",173))
    
    def test_74(self):
        self.assertTrue(TestLexer.test("""
        For i in 1..10
        ""","For,i,in,1.,.,10,<EOF>",174))
    
    def test_75(self):
        self.assertTrue(TestLexer.test("""
        For x in 1 .. 10
        ""","For,x,in,1,..,10,<EOF>",175))
    
    def test_76(self):
        self.assertTrue(TestLexer.test("""
        Class main{}
        ""","Class,main,{,},<EOF>",176))
    
    def test_77(self):
        self.assertTrue(TestLexer.test("""
        Var y:Float = 2.0;
        ""","Var,y,:,Float,=,2.0,;,<EOF>",177))
    
    def test_78(self):
        self.assertTrue(TestLexer.test("""
        x,y = y,x
        ""","x,,,y,=,y,,,x,<EOF>",178))
    
    def test_79(self):
        self.assertTrue(TestLexer.test("""
        If (a+b==2) x=x*x;
        ""","If,(,a,+,b,==,2,),x,=,x,*,x,;,<EOF>",179))
    
    def test_80(self):
        self.assertTrue(TestLexer.test("""
        if (a+b==2) x=x*x
        ""","if,(,a,+,b,==,2,),x,=,x,*,x,<EOF>",180))
    
    def test_81(self):
        self.assertTrue(TestLexer.test("""
        Class Program
        ""","Class,Program,<EOF>",181))
    
    def test_82(self):
        self.assertTrue(TestLexer.test("""
        class program
        ""","class,program,<EOF>",182))
    
    def test_83(self):
        self.assertTrue(TestLexer.test("""
        Hello + World
        ""","Hello,+,World,<EOF>",183))
    
    def test_84(self):
        self.assertTrue(TestLexer.test("""
        Self.x[2][2].x
        ""","Self,.,x,[,2,],[,2,],.,x,<EOF>",184))
    
    def test_85(self):
        self.assertTrue(TestLexer.test("""
        Self..x
        ""","Self,..,x,<EOF>",185))
    
    def test_86(self):
        self.assertTrue(TestLexer.test("""
        Self.2.3
        ""","Self,.,2.3,<EOF>",186))
    
    def test_87(self):
        self.assertTrue(TestLexer.test("""
        Self!=This
        ""","Self,!=,This,<EOF>",187))
    
    def test_88(self):
        self.assertTrue(TestLexer.test("""
        !!!!isPrime
        ""","!,!,!,!,isPrime,<EOF>",188))
    
    def test_89(self):
        self.assertTrue(TestLexer.test("""
        c::c:c::c
        ""","c,::,c,:,c,::,c,<EOF>",189))
    
    def test_90(self):
        self.assertTrue(TestLexer.test("""
        (ab.s)[2+x.y+1.e10]
        ""","(,ab,.,s,),[,2,+,x,.,y,+,1.e10,],<EOF>",190))
    
    def test_91(self):
        self.assertTrue(TestLexer.test("""
        (a+b
        ""","(,a,+,b,<EOF>",191))
    
    def test_92(self):
        self.assertTrue(TestLexer.test("""
        (B::$a.c).c.
        ""","(,B,::,$a,.,c,),.,c,.,<EOF>",192))
    
    def test_93(self):
        self.assertTrue(TestLexer.test("""
        ''
        ""","Error Token '",193))
    
    def test_94(self):
        self.assertTrue(TestLexer.test("""
        \"Hello world\" ==. \"Goodbye world\"
        ""","Hello world,==.,Goodbye world,<EOF>",194))
    
    def test_95(self):
        self.assertTrue(TestLexer.test("""
        continue1.25;
        ""","continue1,.,25,;,<EOF>",195))
    
    def test_96(self):
        self.assertTrue(TestLexer.test("""
        Continue1.;
        ""","Continue1,.,;,<EOF>",196))
    
    def test_97(self):
        self.assertTrue(TestLexer.test("""
        .....
        ""","..,..,.,<EOF>",197))
    
    def test_98(self):
        self.assertTrue(TestLexer.test("""
        :::::::.
        ""","::,::,::,:,.,<EOF>",198))
    
    def test_99(self):
        self.assertTrue(TestLexer.test("""
        Continue;
        ""","Continue,;,<EOF>",199))
    
    def test_100(self):
        self.assertTrue(TestLexer.test("""
        .2e-15
        """,".2e-15,<EOF>",200))
    