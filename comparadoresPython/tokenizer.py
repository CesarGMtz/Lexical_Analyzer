import tokenize
from io import BytesIO
import keyword

# Lista de funciones incorporadas
builtins = {
    'print', 'input', 'len', 'range', 'str', 'int', 'float', 'list', 'dict',
    'set', 'tuple', 'abs', 'max', 'min', 'sum', 'open', 'type', 'isinstance'
}

def tokenizar_lineas(lineas):
    """
    Tokeniza una lista de líneas de código fuente, devolviendo una lista de strings,
    cada uno representando los tokens de una línea.
    """
    all_tokens = []
    codigo = ''.join(lineas)
    g = tokenize.tokenize(BytesIO(codigo.encode('utf-8')).readline)

    current_line = []
    current_lineno = 1
    id_map = {}
    id_counter = 1

    for tok in g:
        if tok.type in (tokenize.ENCODING, tokenize.ENDMARKER):
            continue

        if tok.start[0] != current_lineno:
            if current_line:
                all_tokens.append(' '.join(current_line))
                current_line = []
            current_lineno = tok.start[0]

        if tok.type == tokenize.NAME:
            if tok.string in keyword.kwlist:
                current_line.append(f"KEYWORD({tok.string})")
            elif tok.string in builtins:
                current_line.append(f"BUILTIN({tok.string})")
            else:
                if tok.string not in id_map:
                    id_map[tok.string] = f"ID_{id_counter}"
                    id_counter += 1
                current_line.append(id_map[tok.string])
        elif tok.type == tokenize.STRING:
            current_line.append("STRING")
        elif tok.type == tokenize.NUMBER:
            current_line.append("NUMBER")
        elif tok.type == tokenize.OP:
            current_line.append(tok.string)

    if current_line:
        all_tokens.append(' '.join(current_line))

    return all_tokens
