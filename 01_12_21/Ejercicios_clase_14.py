"""Ejercicio de clase 14"""
lista_numeros = []
while True:
    while True: #Creo un segundo bucle para asegurarme de que todos los datos que introduzco en la lista son enteros

        try:
            numero = int(input("Introduce un número entero: ")) #Cuando el numero que he introducido es un entero,
                                                                #Salgo del bucle
            break
        except:
            print("El dato introducido no es un entero, por fabor introduce un numero entero")

    if numero == -9999:
        break
    lista_numeros.append(numero)
    longitud_lista = len(lista_numeros)

print("Lista numeros sin ordenar: \n", lista_numeros)

for i in range(longitud_lista - 1):
    for j in range (longitud_lista - 1 - i):
        if lista_numeros[j] > lista_numeros[j + 1]:
            aux_variable = lista_numeros[j + 1]
            lista_numeros[j + 1] = lista_numeros[j]
            lista_numeros[j] = aux_variable

print("Lista de numeros ordenada: \n", lista_numeros)



