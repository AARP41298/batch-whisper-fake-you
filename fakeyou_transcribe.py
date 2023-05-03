import os

# Si marca error de que son demasiados para procesar, dividir la carga

# whisper 00000000_8*.wav --language=Spanish -o="S:\aarpfeb23\Descargas\TRASH\audios fh5\extraidos\batch-whisper"
# whisper 00000000_9*.wav --language=Spanish -o="S:\aarpfeb23\Descargas\TRASH\audios fh5\extraidos\batch-whisper"
# whisper 00000000_0*.wav --language=Spanish -o="S:\aarpfeb23\Descargas\TRASH\audios fh5\extraidos\batch-whisper"

# Obtener el directorio actual
directorio_actual = os.getcwd()

# Obtener la lista de archivos en el directorio actual
lista_archivos = os.listdir(directorio_actual)

signos = [".", "!", "?"]

string = ""
# Recorrer la lista de archivos e imprimir el contenido de los que tengan la extensión ".txt"
for archivo in lista_archivos:
    # solo leer los que terminen con .txt y descartar los que empiezan con trans
    if archivo.endswith(".txt") and not archivo.startswith("trans"):
        # Leer el contenido del archivo
        with open(os.path.join(directorio_actual, archivo), "r", encoding="utf-8") as f:
            try:
                contenido = f.read()
            except UnicodeDecodeError:
                print("ocurrio un error con el archivo " + archivo)
                exit(0)

        # cambiar saltos de linea por espacios
        frase = contenido.replace("\n", " ")

        fraseArray = frase.lower().split()

        print(fraseArray)

        if len(fraseArray) == 0:
            continue

        # if fraseArray[0] in ["hola", "bienvenido","bienvenida", "¡bien", "bien,","¡bien,","bien","¡hola","te"]:
        #     continue

        # revisa puntuacion al final

        # limpiar espacios laterales
        clean_frase = frase.strip()

        # descartar frases cortas (minimo 1 para cubrir 'y')
        if len(clean_frase) >= 1:
            # revisar que el ultimo caracter sea un signo, si no, ponerselo
            if clean_frase[-1] not in signos:
                clean_frase += "."

            string += "wavs/" + archivo[:-4] + "| " + clean_frase + "\n"


import codecs

file = codecs.open("transcrito.txt", "w", "utf-8")
file.write(string)
file.close()
