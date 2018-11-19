grammar LuLu2Grammar;
program:ft_dcl? ft_def+;
ft_dcl: KEYWORD_DECLARE OPENING_BRACE ( func_dcl | type_dcl | var_def )+ CLOSING_BRACE;
func_dcl: ( OPENING_PARENTHEISIS args CLOSING_PARENTHEISIS SYMBOL_EQUAL )? ID OPENING_PARENTHEISIS ( args | args_var )? CLOSING_PARENTHEISIS SYMBOL_SEMICOLON;
args : type ( OPENING_BRACKET CLOSING_BRACKET )* | args SYMBOL_COMMA type ( OPENING_BRACKET CLOSING_BRACKET )*;
args_var : type ( OPENING_BRACKET CLOSING_BRACKET )* ID | args_var SYMBOL_COMMA type ( OPENING_BRACKET CLOSING_BRACKET )* ID;
type_dcl : ID SYMBOL_SEMICOLON;
var_def : KEYWORD_CONST? type var_val ( SYMBOL_COMMA var_val )* SYMBOL_SEMICOLON;
var_val : ref ( SYMBOL_EQUAL expr)? ;
ft_def : ( type_def | fun_def ) ;
type_def : KEYWORD_TYPE ID ( SYMBOL_COLON ID )? OPENING_BRACE component+ CLOSING_BRACE ;
component : access_modifier ? ( var_def | fun_def );
access_modifier : KEYWORD_PRIVATE | KEYWORD_PUBLIC | KEYWORD_PROTECTED;
fun_def : ( OPENING_PARENTHEISIS args_var CLOSING_PARENTHEISIS SYMBOL_EQUAL )? KEYWORD_FUNCTION ID OPENING_PARENTHEISIS args_var? CLOSING_PARENTHEISIS block;
block: OPENING_BRACE ( var_def | stmt )* CLOSING_BRACE;
stmt :    assign SYMBOL_SEMICOLON
        | func_call SYMBOL_SEMICOLON
        | cond_stmt
        | loop_stmt
        | KEYWORD_RETURN SYMBOL_SEMICOLON
        | KEYWORD_BREAK SYMBOL_SEMICOLON
        | KEYWORD_CONTINUE SYMBOL_SEMICOLON
        | KEYWORD_DESTRUCT ( OPENING_BRACKET CLOSING_BRACKET )* ID SYMBOL_SEMICOLON ;
assign : ( var | OPENING_PARENTHEISIS var ( SYMBOL_COMMA var )*CLOSING_PARENTHEISIS ) SYMBOL_EQUAL expr;
var : ( ( KEYWORD_THIS | KEYWORD_SUPER ) SYMBOL_DOT )? ref ( SYMBOL_DOT ref )*;
ref : ID ( OPENING_BRACKET expr CLOSING_BRACKET )*;
expr : OPENING_PARENTHEISIS expr CLOSING_PARENTHEISIS
        | unary_op expr
        | expr binary_op1 expr
        | expr binary_op2 expr
        | expr binary_op3 expr
        | expr binary_op4 expr
        | expr binary_op5 expr
        | expr binary_op6 expr
        | expr binary_op7 expr
        | expr binary_op8 expr
        | expr binary_op9 expr
        | const_val
        | KEYWORD_ALLOCATE handle_call
        | func_call
        | var
        | list
        | KEYWORD_NIL;
func_call : ( var SYMBOL_DOT )? handle_call | KEYWORD_READ OPENING_PARENTHEISIS var CLOSING_PARENTHEISIS | KEYWORD_WRITE OPENING_PARENTHEISIS var CLOSING_PARENTHEISIS;
list : OPENING_BRACKET ( expr | list ) ( SYMBOL_COMMA ( expr| list ) )* CLOSING_BRACKET;
handle_call : ID OPENING_PARENTHEISIS params? CLOSING_PARENTHEISIS;
params : expr | expr SYMBOL_COMMA params;
cond_stmt : KEYWORD_IF expr block ( KEYWORD_ELSE block )?
        | KEYWORD_SWITCH var OPENING_BRACE ( KEYWORD_CASE INT_CONST SYMBOL_COLON block )* KEYWORD_DEFAULT SYMBOL_COLON block CLOSING_BRACE;
loop_stmt : KEYWORD_FOR ( type? assign )? SYMBOL_SEMICOLON expr SYMBOL_SEMICOLON assign? block | KEYWORD_WHILE expr block;
type : KEYWORD_INT
        | KEYWORD_BOOL
        | KEYWORD_FLOAT
        | KEYWORD_STRING
        | ID;
const_val : INT_CONST
        | REAL_CONST
        | BOOL_CONST
        | STRING_CONST;
unary_op : SYMBOL_DASH
        | SYMBOL_EXCLAMATION
        | SYMBOL_MAD;
binary_op1 : SYMBOL_STAR
        | SYMBOL_SLASH
        | SYMBOL_PERCENT;
binary_op2 : SYMBOL_PLUS
        | SYMBOL_DASH;
binary_op3 : RELATIONAL_OPERATORS;
binary_op4 : EQUAL_OPERATORS;
binary_op5 : SYMBOL_AND;
binary_op6 : SYMBOL_XOR;
binary_op7 : SYMBOL_OR;
binary_op8 : SYMBOL_LOGIC_AND;
binary_op9 : SYMBOL_LOGIC_OR;
OPENING_BRACE:'{';
CLOSING_BRACE:'}';
OPENING_PARENTHEISIS:'(';
CLOSING_PARENTHEISIS:')';
OPENING_BRACKET:'[';
CLOSING_BRACKET:']';
SYMBOL_DOT:'.';
SYMBOL_EQUAL:'=';
SYMBOL_SEMICOLON:';';
SYMBOL_COLON:':';
SYMBOL_COMMA:',';
SYMBOL_DASH: '-';
SYMBOL_PLUS: '+';
SYMBOL_STAR: '*';
SYMBOL_XOR: '^';
SYMBOL_SLASH: '/';
SYMBOL_PERCENT: '%';
SYMBOL_EXCLAMATION:'!';
SYMBOL_LOGIC_AND:'&&';
SYMBOL_LOGIC_OR:'||';
SYMBOL_AND:'&';
SYMBOL_OR:'|';
SYMBOL_MAD:'~';
INT_CONST: ([0][Xx][0-9A-Fa-f]+)|([0-9]+);
EXPONENT: ([eE])(SYMBOL_PLUS|SYMBOL_DASH)?([0-9]+);
REAL_CONST: (INT_CONST?SYMBOL_DOT[0-9]*)EXPONENT?;
STRING_CONST: ['](~'\\'|ESCAPE_CHARACTER)*?['];
ESCAPE_CHARACTER: '\\n'|'\\r'|'\\\\'|'\\t'|'\\0'|'\\’'|('\\'[xX][0-9a-fA-F][0-9a-fA-F]);
BOOL_CONST: KEYWORD_TRUE|KEYWORD_FALSE;
EQUAL_OPERATORS: '=='|'!=';
RELATIONAL_OPERATORS: '<='|'<'|'>'|'>=';
KEYWORD_DECLARE:'declare';
KEYWORD_RETURN: 'return';
KEYWORD_BREAK:'break';
KEYWORD_CONTINUE:'continue';
KEYWORD_DESTRUCT:'destruct';
KEYWORD_THIS:'this';
KEYWORD_SUPER:'super';
KEYWORD_CONST:'const';
KEYWORD_PRIVATE:'private';
KEYWORD_PUBLIC:'public';
KEYWORD_PROTECTED:'protected';
KEYWORD_INT:'int';
KEYWORD_BOOL:'bool';
KEYWORD_FLOAT:'float';
KEYWORD_STRING:'string';
KEYWORD_FUNCTION:'function';
KEYWORD_CASE:'case';
KEYWORD_DEFAULT:'default';
KEYWORD_READ:'read';
KEYWORD_WRITE:'write';
KEYWORD_WHILE:'while';
KEYWORD_ALLOCATE:'allocate';
KEYWORD_TYPE:'type';
KEYWORD_NIL:'nil';
KEYWORD_IF:'if';
KEYWORD_ELSE:'else';
KEYWORD_SWITCH:'switch';
KEYWORD_FOR:'for';
KEYWORD_FALSE:'false';
KEYWORD_TRUE:'true';
KEYWORD_OF:'of';
ID: ([a-zA-Z#_])([a-zA-Z0-9#_])*;
COMMENT:(('%%'(~[\n])*)|('%~'.*?'~%')) -> skip;
WHITESPACE:([ \t\n\r])+ -> skip;

