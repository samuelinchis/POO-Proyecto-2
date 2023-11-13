import random
from modeloAeropuerto.torrecontrol import TorreControl
""" Clase Aeronave """



class Aeronave:

    """Constructor de la clase aeronave"""
    def __init__(self, marca="", modelo="", capacidad=0, velmax=0, autonomia=0, ano_fabricacion=0, estado="Disponible", ubicacion=0, vuelos=[]):
        self._marca = marca
        self._modelo = modelo
        self._capacidad = capacidad
        self._velmax = velmax
        self._autonomia = autonomia
        self._ano_fabricacion = ano_fabricacion
        self._estado = estado
        self._ubicacion = ubicacion
        self._vuelos = vuelos
        self._mediador = TorreControl()

    # Getters

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_capacidad(self):
        return self._capacidad

    def get_velmax(self):
        return self._velmax

    def get_autonomia(self):
        return self._autonomia

    def get_anofabricacion(self):
        return self._ano_fabricacion

    def get_estado(self):
        return self._estado

    def get_vuelos(self):
        return self._vuelos

    # Setters

    def set_marca(self, nueva_marca):
        self._marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    def set_capacidad(self, nueva_capacidad):
        self._capacidad = nueva_capacidad

    def set_velmax(self, nueva_velmax):
        self._velmax = nueva_velmax

    def set_autonomia(self, nueva_autonomia):
        self._autonomia = nueva_autonomia

    def set_anofabricacion(self, nuevo_anofabricacion):
        self._ano_fabricacion = nuevo_anofabricacion

    def set_estado(self, nuevo_estado):
        self._estado = nuevo_estado

    # Metodos

    """Añade un vuelo a la lista interna de la aeronave"""
    def addVuelo(self, vuelo):
        self._vuelos.append(vuelo)

    """Muestra los vuelos de la aeronave"""
    def mostrar_vuelos(self):
        size = len(self._vuelos)
        if size == 0:
            print("No hay vuelos por mostrar")
        else:
            for i in range(size):
                print(f"Vuelo ")

    """Esta funcion recibe un mensaje de una aeronave externa"""
    def recibir_mensaje(self, ubi, avion):
        print("Recibiendo el mensaje: ", ubi, "de parte de ", avion.get_modelo())

    """Esta funcion genera una altura random entre 1 y 1000 y manda esta ubicacion a la torre de control"""
    def enviar_ubi(self):
        ubi = random.randint(1, 10000)
        print(self._modelo, " está ubicado a ", ubi, " pies de altura.")
        self._mediador.enviar_mensaje(ubi,self)

    """Esta funcion manda el estado actual de la aeronave a la torre de control"""
    def enviar_estado(self):
        self._mediador.enviar_estado(self)

    """Esta funcion recibe el estado de una aeronave externa"""
    def recibir_estado(self, aeronave):
            print ("La aeronave ", aeronave.get_modelo(), "tiene el estado", aeronave.get_estado())



