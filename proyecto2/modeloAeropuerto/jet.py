from modeloAeropuerto.aeronave import Aeronave

""" Clase Jet """


class Jet(Aeronave):
    """Constructor de la clase Jet. Hereda atributos de la clase Aeronave"""
    def __init__(self, marca, modelo, capacidad, velmax, autonomia, ano_fabricacion, estado, ubicacion, vuelos, propietario="Desconocido", lista_servicios=[], lista_destinos=[]):
        super().__init__(marca, modelo, capacidad, velmax, autonomia, ano_fabricacion, estado, ubicacion, vuelos)
        self._propietario = propietario
        self._lista_destinos = lista_destinos
        self._lista_servicios = lista_servicios

    # Setters
    def set_propietario(self, propietario):
        self._propietario = propietario

    def anadir_servicio(self, servicio):
        self._lista_servicios.append(servicio)

    def anadir_destino(self, destino):
        self._lista_destinos.append(destino)

    # Getters
    def get_propietario(self):
        return self._propietario

    def get_servicios(self):
        return self._lista_servicios

    def get_destinos(self):
        return self._lista_destinos

