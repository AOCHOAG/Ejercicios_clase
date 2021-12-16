class Modelos:
    def __init__(self, archivo):
        a = open(archivo, "r")
        self.fabricantes = {} #Creamos un atributo fabricantes, un diccionario vacio

        for linea in a: #Ejecuto una vez por cada linea del archivo
            modelo, fabricante = linea.strip().split(" ") #Le digo que primero lee modelo y despues fabricante
                                                          #El contenido de cada linea lo mete en la variable linea
                                                          #Strip se utiliza para hacer un \n por cada linea en el archivo
                                                          #Split separa las dos partes de cada linea separadas por un espacio
                                                          #Cada modelo (a1) pasa a formar parte de modelo y
                                                          #fabricante (audi) pasa a formar parte de fabricante

            if fabricante in self.fabricantes: #Le pregunto si audi esta dentro de fabricantes (al principio no está en
                                               #la lista, la cual he creado vacia {}
                self.fabricantes[fabricante].append(modelo)

            else: #En caso de que audi no este dentro de fabricantes
                self.fabricantes[fabricante] = [] #Creo una lista audi, ya que no existe todavia
                self.fabricantes[fabricante].append(modelo) #Añado a1 a la lista audi que he creado