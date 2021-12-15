"""Car class"""

class Car: #Defino un nuevo tipo de dato
    def __init__(self, marca_coche, modelo_coche, combustible, cilindrada, wheel): #Defino como van a ser los objetos de
                                                                            #Esta clase
        self.marca = marca_coche #EL objeto va a tener una variable (marca) que va a tomar el valor de marca_coche
        self.modelo = modelo_coche
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.wheel = wheel
        self.pos_x = 0 #Le doy el valor de o a pos_x
        self.pos_y = 0

    def move_to(self, pos_x, pos_y): #Le doy una funcion a esos objetos
        self.pos_x = pos_x #La funcion le da valores a las variables pos x y pos y
        self.pos_y = pos_y


    def move_incr(self, x, y):
        self.pos_x = self.pos_x + x #poner esto
        self.pos_y += y             #Y poner esto, es lo mismo!

    def get_pos(self):
        return self.pos_x, self.pos_y

class Wheel:
    def __init__(self, ancho, rodadura, diametro):
        self.ancho = ancho
        self.rodadura = rodadura
        self.diametro = diametro
        self.presion = 0

    def set_pressure(self, presion):
        self.presion = presion

    def print_info(self):
        print("Dimensiones de la rueda: ", self.ancho, "/",  self.rodadura, "R", self.diametro)
        print("Presión de las ruedas: ", self.presion, "bar")
