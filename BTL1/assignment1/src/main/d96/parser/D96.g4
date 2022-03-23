// 1912288
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


/*********************PARSER**********************/
program: class_decls EOF;
class_decls: class_decl class_decls | class_decl;
class_decl: CLASS ID_WITHOUT_STATIC superclass LCB memberlists RCB ;
superclass: CL ID_WITHOUT_STATIC | ;
memberlists: member memberlists | member | ;
member: attribute | method;

attribute: (VAL | VAR) (idlist CL typename | pairList) SM;
idlist: ids CM idlist | ids ;
typename: primitive_type | arrayType | classType;
pairList: ids pair expr;
pair: CM ids pair expr CM | CL typename ASSIGN;
/************* Type ************/
arrayType: ARRAY LSB (primitive_type | arrayType) CM INTLIT_GT0 RSB;
classType: NEW ids LP RP;
primitive_type: INT | FLOAT | BOOLEAN | STRING;
/******************************/

method: (ID_STATIC | ID_WITHOUT_STATIC | CONSTRUCTOR | DESTRUCTOR) LP paralist RP block_stmt;
paralist: para SM paralist | para | ;
para: idlist2 CL typename;

block_stmt: LCB stmt_list RCB;
stmt_list: stmt stmt_list | stmt | ;
stmt: var_decl_stmt SM| assign_stmt SM| if_stmt | for_stmt | break_stmt SM| continue_stmt SM| return_stmt SM
    | methodInvo_stmt SM;

var_decl_stmt: (VAL | VAR) (idlist2 CL typename | pairList2);
idlist2: ID_WITHOUT_STATIC CM idlist2 | ID_WITHOUT_STATIC;
pairList2: ID_WITHOUT_STATIC pair2 expr;
pair2: CM ID_WITHOUT_STATIC pair2 expr CM | CL typename ASSIGN;

assign_stmt: lhs ASSIGN expr;
lhs: ids
    | expr INSTANCE_ATTR_ACCESS ID_WITHOUT_STATIC 
    | (ID_WITHOUT_STATIC|SELF) STATIC_ATTR_ACCESS ID_STATIC;

if_stmt: IF LP expr RP block_stmt elseifs_stmt elses_stmt ;
elseifs_stmt: ELSEIF LP expr RP block_stmt elseifs_stmt | ELSEIF LP expr RP block_stmt | ;
elses_stmt: else_stmt | ;
else_stmt: ELSE block_stmt;

for_stmt: FOREACH LP ids IN expr DDT expr bys_stmt RP block_stmt;
bys_stmt: by_stmt | ;
by_stmt: BY expr;

break_stmt: BREAK;
continue_stmt: CONTINUE;
return_stmt: RETURN (expr | );

methodInvo_stmt: expr INSTANCE_ATTR_ACCESS ids LP exprlists RP
                | ID_WITHOUT_STATIC STATIC_ATTR_ACCESS ID_STATIC LP exprlists RP; 

expr: expr1 (STR_CONCAT | COMPARE_STR) expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL | GT | GE | LT | LE) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: expr7 LSB expr RSB | expr8;
expr8: expr8 INSTANCE_ATTR_ACCESS ids 
    | expr8 INSTANCE_ATTR_ACCESS ids LP exprlists RP 
    | expr9;
expr9: ID_WITHOUT_STATIC STATIC_ATTR_ACCESS ID_STATIC 
    | ID_WITHOUT_STATIC STATIC_ATTR_ACCESS ID_STATIC LP exprlists RP 
    | expr10;    
expr10: NEW ids LP exprlists RP expr10 | expr11;
expr11: LP expr RP | operand;
operand: intlit | FLOATLIT | BOOLLIT | STRLIT | ids | SELF | index_arrlit;

exprlists: exprlist | ;
exprlist: expr CM exprlist | expr;


/********************** COMMENT ***********************/
BLOCK_CMT: DoubleHastag .*? DoubleHastag -> skip;

/********************* FRAGMENTS **********************/
fragment DoubleHastag: '##';
fragment Letter: [A-Za-z];
fragment Underscore: '_';
fragment Digit: [0-9];
fragment Dollar: '$';
fragment NonZeroDigit: [1-9];
fragment DoubleQuote: '"';

fragment StringChar
    : ~[\b\t\f\r\n"\\]
    | '\''DoubleQuote ;
	
fragment IllegalString
    : '\\' ~[bfrnt'\\]
    | '\\' ;

fragment IntegerPart: (Digit | NonZeroDigit Digit* (Underscore Digit+)*);
fragment DecimalPart: ('.' Digit*);
fragment ExponentPart: (('e' | 'E') ('+' | '-')? (Digit | NonZeroDigit Digit*));


/********************* LITERALS ***********************/
INTLIT_GT0: 
	'0' ([1-7] [0-7]* (Underscore [0-7]+)*) {self.text = self.text.replace("_", "")} //Octal
	| ('0x' | '0X') ([1-9A-F] [0-9A-F]* (Underscore [0-9A-F]+)*) {self.text = self.text.replace("_", "")} //Hexadecimal
	| ('0b' | '0B') ('1' [0-1]* (Underscore [0-1]+)*) {self.text = self.text.replace("_", "")} //Binary
	| (NonZeroDigit Digit* (Underscore Digit+)*) {self.text = self.text.replace("_", "")}; //Decimal

ZERO: '0' [0]   //Octal
    | ('0x' | '0X') '0'    //Hexadecimal
    | ('0b' | '0B') '0'    //Binary
    | '0' ;     //Decimal

intlit: ZERO | INTLIT_GT0;

FLOATLIT:
	IntegerPart DecimalPart {self.text = self.text.replace("_", "")}
	| IntegerPart ExponentPart {self.text = self.text.replace("_", "")}
	| DecimalPart ExponentPart {self.text = self.text.replace("_", "")}
	| IntegerPart DecimalPart ExponentPart {self.text = self.text.replace("_", "")};

BOOLLIT: TRUE | FALSE;

STRLIT: DoubleQuote (StringChar)* DoubleQuote
    {
        result = str(self.text)
        self.text = result[1:-1]
    };

index_arrlit: ARRAY '(' (expr (',' expr)* | ) ')';

MUDI_ARRLIT: ARRAY '(' (ARRAY (',' ARRAY)* | ) ')';

/********************* KEY WORDS **********************/
BREAK: 'Break';
FOREACH: 'Foreach';
INT: 'Int';
NULL: 'Null';
CONSTRUCTOR: 'Constructor';
CONTINUE: 'Continue';
TRUE: 'True';
FLOAT: 'Float';
CLASS: 'Class';
DESTRUCTOR: 'Destructor';
IF: 'If';
FALSE: 'False';
BOOLEAN: 'Boolean';
VAL: 'Val';
NEW: 'New';
ELSEIF: 'Elseif';
ARRAY: 'Array';
STRING: 'String';
VAR: 'Var';
BY: 'By';
ELSE: 'Else';
IN: 'In';
RETURN: 'Return';
SELF: 'Self';

/******************** SEPARATORS **********************/
LP: '(';
RP: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
SM: ';';
CM: ',';
//DT: '.';
CL: ':';
DDT: '..';

/********************* OPERATORS **********************/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
NOT_EQUAL: '!=';
GT: '>';
GE: '>=';
LT: '<';
LE: '<=';
COMPARE_STR: '==.';
STR_CONCAT: '+.';
INSTANCE_ATTR_ACCESS: '.';
STATIC_ATTR_ACCESS: '::';
//OBJ_CREATION: 'New';


/******************** IDENTIFIERS *********************/
ID_STATIC: Dollar (Letter | Underscore | Digit)+;

ID_WITHOUT_STATIC: (Letter | Underscore) (Letter | Underscore | Digit)*;

ids: ID_WITHOUT_STATIC | ID_STATIC;


/*********************** SKIP *************************/

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR:
	. {
        raise ErrorToken(self.text)
    	};

UNCLOSE_STRING
    : DoubleQuote StringChar* ([\b\t\f\n\r"\\] | EOF)
    {
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
    };

ILLEGAL_ESCAPE
    : DoubleQuote StringChar* IllegalString
    {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    };