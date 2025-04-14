from tokenizer import tokenizar_lineas

def analizarCode(source):
    return tokenizar_lineas(source)

f1 = open("examples/example3_1.py", 'r')
source1 = f1.read()
tokens1 = analizarCode(source1)

f2 = open("examples/example3_2.py", 'r')
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
    #print(f"La similitud es de: {similitud:.2f}%")
    return max_lcp, similitud

max_lcp = lcp_all(suffix_array(charL1), suffix_array(charL2), charL1, charL2)
similitud = max_lcp[1]

def commSubs(text1, text2, min_length=1):
    separator = chr(0)
    combined = text1 + separator + text2
    sa = suffix_array(combined)
    lcp = lcp_array(combined, sa, build_rank(sa, len(combined)))
    
    common_substrings = set()
    
    for i in range(1, len(lcp)):
        if lcp[i] >= min_length:
            if (sa[i] < len(text1) and sa[i+1] > len(text1)) or \
               (sa[i] > len(text1)) and sa[i+1] < len(text1):
                substring = combined[sa[i]:sa[i]+lcp[i]]
                is_substring = False
                for existing in list(common_substrings):
                    if substring in existing:
                        is_substring = True
                        break
                    if existing in substring:
                        common_substrings.remove(existing)
                if not is_substring:
                    common_substrings.add(substring)
    
    return sorted(common_substrings, key=len, reverse=True)

def calculateSimil(text1, text2):
    common_substrings = commSubs(text1, text2, min_length=3)
    positions_covered = set()
    total_common = 0
    
    for substr in common_substrings:
        for text in [text1, text2]:
            start = 0
            while True:
                pos = text.find(substr, start)
                if pos == -1:
                    break
                for i in range(pos, pos + len(substr)):
                    if i not in positions_covered:
                        positions_covered.add(i)
                        total_common += 1
                start = pos + 1
    
    min_len = min(len(text1), len(text2))
    similitud = (total_common / min_len) * 100 if min_len > 0 else 0
    
    return min(similitud, 100)


def guardarArchivo(source1, source2, output_file, charL1, charL2, similTokens):
    
    plainSimil = calculateSimil(source1, source2)
    
    strL1 = ''.join(charL1)
    strL2 = ''.join(charL2)
    
    common_plain = commSubs(source1, source2, min_length=10)
    common_tokens = commSubs(strL1, strL2, min_length=3)
    
    with open(output_file, 'w') as f:
        f.write(f"=== RESUMEN DE SIMILITUD ===\n")
        f.write(f"Similitud en texto plano: {plainSimil:.2f}%\n")
        f.write(f"Similitud en tokens procesados: {similTokens:.2f}%\n\n")
        
        f.write("=== Fragmentos comunes en texto plano ===\n")
        for fragment in common_plain:
            f.write(f"\n--- Longitud: {len(fragment)} caracteres ---\n")
            f.write(fragment + "\n")
        
        f.write("\n\n=== Fragmentos comunes en tokens procesados ===\n")
        for fragment in common_tokens:
            f.write(f"\n--- Longitud: {len(fragment)} tokens ---\n")
            original_tokens = []
            for i in range(len(fragment)):
                pos = strL1.find(fragment) if fragment in strL1 else strL2.find(fragment)
                if pos != -1 and pos + i < len(tokens1):
                    original_tokens.append(tokens1[pos + i])
            f.write(' '.join(original_tokens) + "\n")


    print(f"\nResumen de similitud guardado en {output_file}:")
    print(f"- Texto plano: {plainSimil:.2f}%")
    print(f"- Texto preprocesado: {similTokens:.2f}%")

guardarArchivo(source1, source2, "resultadoSA.txt", charL1, charL2, similitud)
