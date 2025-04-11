import difflib

def leer_archivo(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def preprocesar_lineas(lineas):
    # Elimina espacios, líneas vacías y comentarios
    return [line.strip() for line in lineas if line.strip() and not line.strip().startswith("#")]

def calcular_similitud(lineas1, lineas2):
    matcher = difflib.SequenceMatcher(None, lineas1, lineas2)
    return matcher.ratio() * 100  # porcentaje

def obtener_fragmentos_similares(lineas1, lineas2):
    d = difflib.Differ()
    resultado = list(d.compare(lineas1, lineas2))
    similares = [line for line in resultado if line.startswith("  ")]  
    return similares

def guardar_resultado(similitud_normal, fragmentos_normal, similitud_procesado, fragmentos_procesado, archivo_salida="resultado.txt"):
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("=== Comparación sin preprocesar (texto llano) ===\n")
        f.write(f"Porcentaje de similitud: {similitud_normal:.2f}%\n\n")
        f.write("Fragmentos similares:\n")
        for linea in fragmentos_normal:
            f.write(linea)
        
        f.write("\n\n=== Comparación con preprocesamiento ===\n")
        f.write(f"Porcentaje de similitud: {similitud_procesado:.2f}%\n\n")
        f.write("Fragmentos similares:\n")
        for linea in fragmentos_procesado:
            f.write(linea)

def main():
    archivo1 = "archivo1.py"
    archivo2 = "archivo2.py"

    # Texto sin procesar
    lineas1_normales = leer_archivo(archivo1)
    lineas2_normales = leer_archivo(archivo2)
    similitud_normal = calcular_similitud(lineas1_normales, lineas2_normales)
    fragmentos_normal = obtener_fragmentos_similares(lineas1_normales, lineas2_normales)

    # Texto procesado
    lineas1_procesadas = preprocesar_lineas(lineas1_normales)
    lineas2_procesadas = preprocesar_lineas(lineas2_normales)
    similitud_procesado = calcular_similitud(lineas1_procesadas, lineas2_procesadas)
    fragmentos_procesado = obtener_fragmentos_similares(lineas1_procesadas, lineas2_procesadas)

    # Guardar todo en resultado.txt
    guardar_resultado(similitud_normal, fragmentos_normal, similitud_procesado, fragmentos_procesado)

if __name__ == "__main__":
    main()
