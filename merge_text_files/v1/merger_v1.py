# Merger v1 - Basic Version
# This script merges all `.txt` files in a given directory into a single output file.
# Features:
# - Prompts the user for the directory path containing the `.txt` files.
# - Verifies the directory and finds all `.txt` files.
# - Merges the files into one, creating an output file in the same directory.

import os

# Solicita al usuario la ruta al directorio de los archivos
directorio = input('Por favor, introduce la ruta del directorio donde están tus archivos de texto: ')

# Verifica si el directorio existe
if not os.path.isdir(directorio):
    print('La ruta proporcionada no es un directorio válido.')
    exit()

# Obtiene una lista de archivos .txt en el directorio
archivos_txt = [f for f in os.listdir(directorio) if f.endswith('.txt')]

# Verifica si hay archivos .txt en el directorio
if not archivos_txt:
    print('No se encontraron archivos .txt en el directorio especificado.')
    exit()

# Ordena los archivos (puedes cambiar el criterio de orden si es necesario)
archivos_txt.sort()

# Crea un nombre lógico para el archivo de salida
# Por ejemplo, 'archivos_unidos_3_archivos.txt' si hay 3 archivos
nombre_archivo_salida = f'archivos_unidos_{len(archivos_txt)}_archivos.txt'

# Ruta completa al archivo de salida (en el mismo directorio que los archivos de origen)
ruta_archivo_salida = os.path.join(directorio, nombre_archivo_salida)

# Abre el archivo de salida en modo escritura
with open(ruta_archivo_salida, 'w', encoding='utf-8') as outfile:
    for archivo in archivos_txt:
        ruta_archivo = os.path.join(directorio, archivo)
        with open(ruta_archivo, 'r', encoding='utf-8') as infile:
            contenido = infile.read()
            outfile.write(contenido)
            outfile.write('\n')  # Agrega un salto de línea entre archivos (opcional)

print(f'Archivos unidos correctamente en: {ruta_archivo_salida}')


