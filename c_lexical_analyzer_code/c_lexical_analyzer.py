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

tokens = [
  'KEYWORD',
  'ID'
]

def t_ID(t): # Y KEYWORD
  r'[_a-zA-Z][_a-zA-Z0-9]*'
  if t.value in keywords:
    t.type = 'KEYWORD' # EL TOKEN DEBE SER "KEYWORD" O LA KEYWORD EN ESPECÍFICO, EX: "AUTO", "_BOOL", ETC.
  return t

t_ignore = ' \t'

def getLexer():
  return lex.lex()
        