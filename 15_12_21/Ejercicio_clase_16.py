"""Contador de palabras que aparecen en una frase"""

PALABRAS = "palabras.txt" #Llamo a los archivos que quiero abrir como variables (constantes)
FRASES = "frases.txt"

archivo = open(PALABRAS, "r") #Archivo es la varibale que contiene palabras a modo de lectura ("r")

palabras = {} #Creo un diccionario vacio llamado palabras
for linea in archivo: #Le digo que por cada caracter (linea) de archivo (palabras.txt)
    palabras[linea.strip()] = [] #Le digo que por cada palabra dentro de archivo lo meta en una lista y además
                                 #que emplee el protocolo strip
                                 #para quitar los caracteres especiales de cada palabra, para poder identificarla mejor
                                 #cuando sea descubierta dentro de una frase.

print("Lista palabras: \n", palabras) #Le digo que imprima la lista que he ido llenando con las distintas palabras

archivo = open(FRASES, "r") #dentro de la misma variable archivo, le pido que abra FRASES a modo de lectura ("r")
frases = [] #Creo una lista vacia llamada frases
for frase in archivo: #Para cada string del archivo
    frases.append(frase.strip()) #Al diccioanrio frases, le añado frase empleando ademas
                                 # strip() para quitarle los caracteres especiales

    for palabra in palabras: #Para cada string de la lista palabras
        palabras[palabra].append(frase.lower().count(palabra)) #Por cada palabra dentro del diccionario palabras,
                                                               #Añado al diccionario un contador de las veces que
                                                               #aparece cada palabra en una frase, esto lo meto en una
                                                               #lista con el numero de veces que aparece esa palabra en
                                                               #cada una de las frases que yo tengo. (Para ello se crea
                                                               #anteriormente la lista dentro del diccionario, para
                                                               #meter ahi el recuento de veces que se repite cada palabra

archivo.close() #Dejo de usar el archivo, por lo que lo cierro
print("Frases: \n", frases) #Imprimo las distintas frases que tengo
print("Palabras en frases: \n", palabras) #Imprimo las palabras de mi lista con el contador del numero de veces que se
                                          #repite cada palabra en cada frase.

