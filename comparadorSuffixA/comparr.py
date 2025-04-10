import ply.lex as lex

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

lexer = lex.lex()

def analizarCode(source):
    lexer.input(source)
    tokens = []
    for token in lexer:
        tokens.append(token.type)
    return tokens

f1 = open("example1.py", 'r')
source1 = f1.read()
tokens1 = analizarCode(source1)

f2 = open("example2.py", 'r')
source2 = f2.read()
tokens2 = analizarCode(source2)

tokenConv = {
    'KEYWORD': 'A',
    'ID': 'B',
    'UCN': 'C',
    'INT': 'D',
    'FLOAT': 'E',
    'CHAR': 'F',
    'STR': 'G',
    'PUNCTUATOR': 'H',
    'HEADER': 'I'
}

charL1 = [tokenConv.get(token_type, 'Nain') for token_type in tokens1]
charL2 = [tokenConv.get(token_type, 'Nain') for token_type in tokens2]

def suffix_array(text):
    return sorted(range(len(text)), key=lambda i: text[i:])

s1 = suffix_array(charL1)
s2 = suffix_array(charL2)

def comparador(s1, s2):
    iguales = 0
    minL = min(len(s1), len(s2))
    
    for i in range(minL):
        if s1[i] == s2[i]:
            iguales += 1
    
    porIg = (iguales / minL) * 100
    return porIg

print(f"Similitud: {comparador(s1, s2):.2f}%")
