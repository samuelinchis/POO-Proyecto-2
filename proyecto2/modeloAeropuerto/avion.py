from modeloAeropuerto.aeronave import Aeronave

""" Clase Avion """


class Avion(Aeronave):
    """Constructor de la clase Avion. Hereda atributos de la clase Aeronave"""
    def __init__(self, marca="", modelo="", capacidad=0, velmax=0, autonomia=0, ano_fabricacion="", estado="", ubicacion=0, vuelos=[], altitudmax=0, num_motores=2, categoria="Indefinida"):
        super().__init__(marca, modelo, capacidad, velmax, autonomia, ano_fabricacion, estado, ubicacion, vuelos)
        self._altitudmax = altitudmax
        self._num_motores = num_motores
        self._categoria = categoria

    # Setters

    def set_altitud(self, altitudmax):
        self._altitudmax = altitudmax

    def set_nummotores(self, num_motores):
        self._num_motores = num_motores

    def set_categoria(self, categoria):
        self._categoria = categoria

    # Getters

    def get_altitudmax(self):
        return self._altitudmax

    def get_num_motores(self):
        return self._num_motores

    def get_categoria(self):
        return self._categoria

