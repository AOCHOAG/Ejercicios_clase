"""Ejercicio 9"""
import persistencia_pickle as pp
import car_class
import random as rd
ARCHIVO = "coches_obj.txt" #Archivo al ser constante se pone con mayusculas para identificarlo mas rapido
lista_coches = pp.retrieve(ARCHIVO)
if lista_coches == None: #Si el archivo no existe todavía, se crea la lista vacia
    lista_coches = []
while True:
    marca = input("Marca: ")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    ancho = input("Ancho de la rueda (en mm): ")
    rodadura = input("Rodadura (% del ancho): ")
    diametro = input("Diametro de la llanta (en pulgadas): ")

    wheel = car_class.Wheel(ancho, rodadura, diametro)
    coche = car_class.Car(marca, modelo, combustible, cilindrada, wheel)  #Le llamo marca, igual que le he llamado en el input
                                                                   #de arriba. Esto se va a asociar a la variable marca
                                                                   #coche, puesto que sigue el orden que he marcado en
                                                                   #car_class al definir el objeto.
    lista_coches.append(coche)
    print("Presión por defecto de las ruedas: ", wheel.presion)

    coche.wheel.set_pressure(input("Dime que presión quieres en las ruedas: "))
    coche.move_to(rd.random()*100, rd.random()*600) #A pos_x y pos_y le doy un valor aleatorio
    print("Posición: ", coche.get_pos()) #Le pido que me devuelva los valores de x e y
    coche.move_incr(rd.random()*10,rd.random()*60) #Incrementa los valores de pos_x y pos_y en 10 y 60 respectivamente
    print("Posición: ", coche.get_pos()) #Escribe el nuevo valor de x e y
    del (coche) #Borra el objeto. La variable deja de existir. Ya esta la informacion de coche en la lista.
    del (wheel) #Se hace para evitar futuros problemas.

n = len(lista_coches)
for i in range(n-1):
    for j in range(n-1-i):
        if lista_coches[j].marca > lista_coches[j+1].marca:
            aux=lista_coches[j]
            lista_coches[j] =lista_coches[j+1]


pp.store(lista_coches, ARCHIVO)
lista_coches = []
print(lista_coches)
lista_coches = pp.retrieve(ARCHIVO)
for car in lista_coches: #Por cada objeto en la lista
    # Le doy una indicación de lo que se va a imprimir a continuación
    print("Marca, Modelo, Combustible, Cilindrada ==>",
          car.marca, car.modelo, car.combustible, car.cilindrada) #Cada coche escribo su marca, modelo, combuustible,
                                                        #y cilindrada. Como estan definidos en clase Car(car_class)
    print(car.wheel.print_info())
    #print("Info rueda: ancho, rodadura, diametro, presión => ", car.wheel.print_info())
    print("Posición: ", car.get_pos(), "\n") #Le pido la posición x e y que habia obtenido previamente de cada
                                             #Objeto correspondiente a cada coche
