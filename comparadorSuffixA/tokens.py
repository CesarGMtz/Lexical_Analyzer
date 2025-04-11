keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
    'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]

tokens = [
    'KEYWORD',
    'ID',
    'NUMBER',
    'FLOAT',
    'STRING',
    'PUNCTUATOR',
    'COMMENT',
    'NEWLINE',
    'HEADER'
] + keywords

def t_COMMENT(t):
    r'\#.*'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

def t_HEADER(t):
    r'\#[^\n]*'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords:
        t.type = 'KEYWORD'
    return t

def t_NUMBER(t):
    r'\d+'
    return t

def t_FLOAT(t):
    r'\d+\.\d*([eE][-+]?\d+)?'
    return t

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"|\'([^\\\']|\\.)*\'' 
    return t

def t_PUNCTUATOR(t):
    r'[\+\-\*/\=\%<>\!\&\|\^~\:\,\.\;\(\)\[\]\{\}]'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)