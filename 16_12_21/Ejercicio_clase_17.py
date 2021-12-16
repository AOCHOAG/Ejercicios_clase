"""Modelos_coches.py"""
import modelos
import unidecode
mc = modelos.Modelos("cars.txt")
while True:
    modelo = unidecode.unidecode(input("Modelo: ")).lower() #Unidecode quita los acentos y los caracteres añadidos
                                                            #Lower() convierte el texto a minusculas
    if modelo == "fin":
        break
    encontrado = False
    for f in mc.fabricantes:
        if modelo in mc.fabricantes[f]:
            print("fabricante: ", f )
            encontrado = True
            break
    if encontrado = False:
        print("Modelo no encontrado")
