grammar LuLu2Grammar;
program:REAL_CONST*;
ID: ([a-zA-Z]|'#'|'_')([a-zA-Z0-9]|'#'|'_')*;
KEYWORD: 'allocate'| 'bool'| 'break'| 'case'| 'const'| 'continue'| 'declare'| 'default'| 'destruct'| 'else'| 'false'| 'function'| 'float'| 'for'| 'if'| 'int'| 'nil'| 'of'| 'private'| 'protected'| 'public'| 'read'| 'return'| 'string'| 'super'| 'switch'| 'this'| 'true'| 'type'| 'while'| 'write';
INT_CONST: ('0'('X'|'x')[0-9A-Fa-f]+)|([0-9]+);
REAL_CONST: (INT_CONST?('.')([0-9]+))|(INT_CONST('.'));
STRING_CONST: '‘'(|'\\n'|'\\r'|'\\\\'|'\\t'|'\\0'|'\\’')*?'’';