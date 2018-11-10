grammar LuLu2Grammer;
program:KEYWORDS;
ID: ([a-zA-Z]|'#'|'_')([a-zA-Z0-9]|'#'|'_')*;
KEYWORDS: ('allocate'| 'bool'| 'break'| 'case'| 'const'| 'continue'| 'declare'| 'default'| 'destruct'| 'else'| 'false'| 'function'| 'float'| 'for'| 'if'| 'int'| 'nil'| 'of'| 'private'| 'protected'| 'public'| 'read'| 'return'| 'string'| 'super'| 'switch'| 'this'| 'true'| 'type'| 'while'| 'write');
INT_CONST: (('0X'|'0x')[0-9A-Fa-f]+)|([0-9]+);
REAL_CONST: (INT_CONST?('.')([0-9]+))|(INT_CONST('.'));
STRING_CONST: '‘'(~'\\'|ESCAPE_CHARACTER)*?'’';
ESCAPE_CHARACTER: '\\n'|'\\r'|'\\\\'|'\\t'|'\\0'|'\\’'|('\\'('x'|'X')[0-9a-fA-F][0-9a-fA-F]);
BOOL_CONST: 'true'|'false';
COMPARISON_OPERATORS: '=='|'!='|'<='|'<='|'<'|'>'|'>=';
BIT_AND_LOGICAL_OPERATORS: '~'|'|'|'&'|'^'|'!'|'||'|'&&';
MATHEMATICAL_OPERATORS: '-'|'+'|'*'|'/'|'%';
OPERATORS: ('{'.*'}')|('('.*')')|('['.*']')|'.'|','|':'|';';
COMMENT:('%%'(~'\n')*?)|('%~'.*?'~%');
WHITESPACE:(' '|'\t'|'\n'|'\r')* -> skip;

