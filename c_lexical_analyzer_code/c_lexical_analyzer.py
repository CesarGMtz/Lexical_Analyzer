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
  'ID',
  'UCN', # Universal-Character-Names
  'INT',
  'FLOAT',
  'CHAR',
  'STR',
  'PUNCTUATOR',
  'HEADER'
]

def t_COMMENT(t):
  r'(//.*)|(/\*(.|\n)*?\*/)'
  pass

def t_UCN(t):
  r'\\(u[\dA-Fa-f]{4}|U[\dA-Fa-f]{8})'
  return t

def t_CHAR(t):
  r"L?'(\\([abfnrtv\\'\"?]|x[\dA-Fa-f]+|[0-7]{1,3}|u[\dA-Fa-f]{4}|U[\dA-Fa-f]{8})|[^\\'\n])*'"
  return t

def t_STR(t):
  r'L?"(\\([abfnrtv\\\'\"?]|x[\dA-Fa-f]+|[0-7]{1,3}|u[\dA-Fa-f]{4}|U[\dA-Fa-f]{8})|[^\\\"\n])*"'
  return t

def t_HEADER(t):
  r'<[^\\n>]+>'
  return t

def t_ID(t): # Y KEYWORD
  r'[_a-zA-Z](\w)*'
  if t.value in keywords:
    t.type = 'KEYWORD'
  return t

def t_FLOAT(t):
  r'((\d+\.\d*|\.\d+)([e|E][+-]?\d+)?|(\d*[e|E][+-]?\d+)|0[xX]([a-fA-F\d]+\.[a-fA-F\d]*|\.[a-fA-F\d]+)[pP][+-]?\d+|0[xX][a-fA-F\d]+[pP][+-]?\d+)[flFL]?'
  return t

def t_INT(t):
  r'(0[xX][a-fA-F\d]+|[1-9]\d*|0[0-7]*)(u|U|l|L|ul|UL|lu|LU|ll|LL|ull|ULL|llu|LLU)?'
  return t

def t_PUNCTUATOR(t):
  r'\[|\]|\(|\)|\{|\}|\.\.\.|\.|->|\+\+|\-\-|&&|&=|&|\*=|\*|\+=|\+|\-=|\-|~|!=|!|/=|/|%=|<%|%>|%:%:|%:|%|<<=|>>=|<<|>>|<=|>=|<:|:>|<|>|==|=|\^=|\^|\|\||\|=|\||\?|:|;|,|\#\#|\#'
  return t

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print(f"Caractér ilegal '{t.value[0]}' en linea {t.lineno}")
  t.lexer.skip(1)
  
if __name__ == '__main__':
  f = open("example.c", 'r')
  data = f.read()

  lexer = lex.lex()
  lexer.input(data)

  tokens_list = []
  while True:
    tok = lexer.token()
    if not tok:
      break
    tokens_list.append((tok.type, tok.value, tok.lineno, tok.lexpos))
  
  for token in tokens_list:
      print(token)

