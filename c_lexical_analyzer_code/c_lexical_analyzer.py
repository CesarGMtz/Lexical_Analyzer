import ply.lex as lex

# Para KEYWORD
keywords = [
  'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
  'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
  'inline', 'int', 'long', 'register', 'restrict', 'return', 'short',
  'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union',
  'unsigned', 'void', 'volatile', 'while', 
  '_Bool', '_Complex', '_Imaginary'
]

# Para PUNCTUATOR
punctuators = [
  '[', ']', '(', ')', '{', '}', '.', '->', '++', '--', '&', '*', '+', '-',
  '~', '!', '/', '%', '<<', '>>', '<', '>', '<=', '>=', '==', '!=', '^',
  '|', '&&', '||', '?', ':', ';', '...', '=', '*=', '/=', '%=', '+=',
  '-=', '<<=', '>>=', '&=', '^=', '|=', ',', '#', '##', '<:', ':>', '<%',
  '%>', '%:', '%:%:'
]

# Falta Universl character names
tokens = [
  'KEYWORD',
  'ID',
  'INT',
  'FLOAT',
  'CHAR',
  'STR',
  'PUNCTUATOR',
  'HEADER'
]

def t_CHAR(t):
  r'L?\'[^\'\n]+\''
  return t

def t_STR(t):
  r'L?\"[^\'\n]+\"'
  return t

def t_ID(t): # Y KEYWORD
  r'[_a-zA-Z][\w]*'
  if t.value in keywords:
    t.type = 'KEYWORD' # EL TOKEN DEBE SER "KEYWORD" O LA KEYWORD EN ESPECÍFICO, EX: "AUTO", "_BOOL", ETC.
  return t

def t_FLOAT(t):
  r'(\d+\.\d*|\.\d+)([e|E][+-]?\d+)?|(\d*[e|E][+-]?\d+)|0[xX]([a-fA-F\d]+\.[a-fA-F\d]*|\.[a-fA-F\d]+)[pP][+-]?\d+|0[xX][a-fA-F\d]+[pP][+-]?\d+'
  return t

def t_INT(t):
  r'0[xX][a-fA-F\d]+|[1-9]\d*|0[0-7]*'
  return t

def t_HEADER(t):
  r'\<[^\n\>]+\>'
  return t

def t_PUNCTUATOR(t):
  r'\W+' # PASAR PUNSTUATOR A REGEX ACÁ PARA QUE NO ACEPTE "<<<<"
  return t

t_ignore = ' \t'

def getLexer():
  return lex.lex()
        