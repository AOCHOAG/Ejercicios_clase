import pickle

def store(data, filename):
    pickle.dump(data, open(filename, "wb"))

def retrieve(filename):
    try:
        archivo = open(filename, "rb") #En caso de que el archivo exista pasa a linea 13
    except: #En caso de que el archivo no exista le pido que imprima el fallo
        print("Error al abrir el archivo", filename)
        return None #Se sale de la funcion devolviendo None (Para que no rompa el programa

    content = pickle.load(archivo) #Mete loq ue hay en el archivo en la  variable content
    archivo.close() #Cierra el archivo, para evitar errores
    return content #Devuelve a donde se le ha llamado a la función,
                   #lo que ha cargado del archivo