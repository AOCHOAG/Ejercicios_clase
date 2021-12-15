"""Contador de palabras que aparecen en una frase"""

PALABRAS = "palabras.txt"
FRASES = "frases.txt"

archivo = open(PALABRAS, "r")

palabras = {}
for linea in archivo:
    palabras[linea.strip()] = []
print("Lista palabras: \n", palabras)

archivo = open(FRASES, "r")
frases = []
for frase in archivo:
    frases.append(frase.strip())
    for palabra in palabras:
        palabras[palabra].append(frase.lower().count(palabra))

archivo.close()
print("Frases: \n", frases)
print("Palabras en frases: \n", palabras)