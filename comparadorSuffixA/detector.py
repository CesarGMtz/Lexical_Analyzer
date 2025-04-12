import difflib
from tokenizer import tokenizar_lineas  

def leer_archivo(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() + '\n' for line in f if line.strip()]

def calcular_similitud(lista1, lista2):
    matcher = difflib.SequenceMatcher(None, lista1, lista2)
    return matcher.ratio() * 100

def fragmentos_similares(lista1, lista2):
    d = difflib.Differ()
    resultado = list(d.compare(lista1, lista2))
    return [line[2:] for line in resultado if line.startswith("  ")]

def fragmentos_similares_con_originales(tokens1, tokens2, originales1, originales2):
    iguales = []
    for i, t1 in enumerate(tokens1):
        for j, t2 in enumerate(tokens2):
            if t1 == t2:
                iguales.append((t1, originales1[i], originales2[j]))
    return iguales

def guardar_resultado(similitud_normal, fragmentos_normal, similitud_tokens, fragmentos_tokens, archivo_salida="resultado.txt"):
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("=== Comparación sin preprocesar (texto llano) ===\n")
        f.write(f"Porcentaje de similitud: {similitud_normal:.2f}%\n\n")
        f.write("Fragmentos similares:\n")
        for linea in fragmentos_normal:
            f.write(f"- {linea.strip()}\n")

        f.write("\n\n=== Comparación con preprocesamiento por tokens ===\n")
        f.write(f"Porcentaje de similitud: {similitud_tokens:.2f}%\n\n")
        f.write("Fragmentos similares:\n")
        for token_line, orig1, orig2 in fragmentos_tokens:
            f.write(f"- {token_line.strip()}\n")
            f.write(f"  ---> Archivo1: {orig1.strip()}\n")
            f.write(f"  ---> Archivo2: {orig2.strip()}\n")

def main():
    archivo1 = "examples/example3_1.py"
    archivo2 = "examples/example3_2.py"

    texto1 = leer_archivo(archivo1)
    texto2 = leer_archivo(archivo2)

    # Comparación texto plano
    similitud_normal = calcular_similitud(texto1, texto2)
    fragmentos_normal = fragmentos_similares(texto1, texto2)

    # Comparación tokenizada (línea por línea)
    tokens1 = tokenizar_lineas(texto1)
    tokens2 = tokenizar_lineas(texto2)
    similitud_tokens = calcular_similitud(tokens1, tokens2)
    fragmentos_tokens = fragmentos_similares_con_originales(tokens1, tokens2, texto1, texto2)

    # Guardar resultado
    guardar_resultado(similitud_normal, fragmentos_normal, similitud_tokens, fragmentos_tokens)

if __name__ == "__main__":
    main()
