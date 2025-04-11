import ply.lex as lex

from tokens import tokens, keywords, t_COMMENT, t_error, t_FLOAT, t_HEADER, t_ID, t_ignore, t_NEWLINE, t_NUMBER, t_PUNCTUATOR, t_STRING

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
    'NUMBER': 'D',
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


def build_rank(suffix_array, n):

    rank = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    return rank

def lcp_array(text, suffix_array, rank):

    n = len(text)
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]  
            while i + h < n and j + h < n and text[i + h] == text[j + h]:
                h += 1
            lcp[rank[i] - 1] = h
            if h > 0:
                h -= 1
    return lcp

def lcp_all(sa1, sa2, original1, original2):

    n1, n2 = len(original1), len(original2)
    sa1 = suffix_array(original1)
    sa2 = suffix_array(original2)
    
    rank1 = build_rank(sa1, n1)
    rank2 = build_rank(sa2, n2)
    
    lcp1 = lcp_array(original1, sa1, rank1)
    lcp2 = lcp_array(original2, sa2, rank2)
    
    max_lcp = 0
    for i in range(len(lcp1)):
        for j in range(len(lcp2)):
            common = min(lcp1[i], lcp2[j])  
            max_lcp = max(max_lcp, common)
    
    similitud = (2 * max_lcp) / (len(original1) + len(original2)) * 100
    print(f"La similitud es de: {similitud:.2f}%")
    return max_lcp

max_lcp = lcp_all(suffix_array(charL1), suffix_array(charL2), charL1, charL2)
print(f"LCP máximo: {max_lcp}")