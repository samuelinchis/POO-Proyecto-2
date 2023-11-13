from modeloAeropuerto.persona import Persona

""" Clase Pasajero """


class Pasajero(Persona):

    """Constructor de la clase Pasajero. Hereda atributos de la clase persona"""
    def __init__(self, nombre, cedula, genero, apellido, fecha, direccion, telefono, correo, nacionalidad="Desconocida", num_maletas=0, info_medica="Desconocida", vuelo=None):
        super().__init__(nombre, cedula, genero, apellido, fecha, direccion, telefono, correo)
        self._nacionalidad = nacionalidad
        self._num_maletas = num_maletas
        self._info_medica = info_medica
        self._vuelo = vuelo

    # Getters

    def get_nacionalidad(self):
        return self._nacionalidad

    def get_num_maletas(self):
        return self._num_maletas

    def get_info_medica(self):
        return self._num_maletas

    def get_vuelo(self):
        return self._vuelo

    # Setters

    def set_nacionalidad(self, nacionalidad):
        self._nacionalidad = nacionalidad

    def set_num_maletas(self, num_maletas):
        self._num_maletas = num_maletas

    def set_info_medica(self, info_medica):
        self._info_medica = info_medica

    def set_vuelo(self, vuelo):
        self._vuelo = vuelo
