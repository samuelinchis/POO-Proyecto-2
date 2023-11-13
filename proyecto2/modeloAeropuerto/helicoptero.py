from modeloAeropuerto.aeronave import Aeronave

""" Clase Helicoptero """


class Helicoptero(Aeronave):
    """Constructor de la clase Helicoptero. Hereda atributos de la clase Aeronave"""
    def __init__(self, marca="", modelo="", capacidad=0, velmax=0, autonomia=0, ano_fabricacion="", ubicacion=0, vuelos=[], estado="", num_rotores=0, cap_elevacion=0, uso="Desconocido"):
        super().__init__(marca, modelo, capacidad, velmax, autonomia, ano_fabricacion, estado, ubicacion, vuelos)
        self._num_rotores = num_rotores
        self._cap_elevacion = cap_elevacion
        self._uso = uso

    # Setters
    def set_num_rotores(self, num_rotores):
        self._num_rotores = num_rotores

    def set_cap_elevacion(self, cap_elevacion):
        self._cap_elevacion = cap_elevacion

    def set_uso(self, uso):
        self._uso = uso

    # Getters
    def get_num_rotores(self):
        return self._num_rotores

    def get_cap_elevacion(self):
        return self._cap_elevacion

    def get_uso(self):
        return self._uso

