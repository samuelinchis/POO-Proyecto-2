""" Clase puerta de embarque """


class Embarque:
    """Constructor de la clase puertas de embarque"""
    def __init__(self, identificacion=0, ubicacion="", disponibilidad="libre", hora_embarque="", historial_vuelos=[]):
        self._identificacion = identificacion
        self._ubicacion = ubicacion
        self._disponibilidad = disponibilidad
        self._hora_embarque = hora_embarque
        self._historial_vuelos = historial_vuelos

    # Getters
    def get_identificacion(self):
        return self._identificacion

    def get_historial_vuelos(self):
        return self._historial_vuelos

    def get_ubicacion(self):
        return self._ubicacion

    def get_hora_embarque(self):
        return self._hora_embarque

    def get_disponibilidad(self):
        return self._disponibilidad

    # Setters

    def set_disponibilidad(self, nueva_disponibilidad):
        self._disponibilidad = nueva_disponibilidad

    def set_hora_embarque(self, nueva_hora_embarque):
        self._hora_embarque = nueva_hora_embarque

    def set_historial_vuelos(self, nuevo_historial_vuelos):
        self._historial_vuelos = nuevo_historial_vuelos

    def set_identificacion(self, nueva_identificacion):
        self._identificacion = nueva_identificacion

    def set_ubicacion(self, nueva_ubicacion):
        self._ubicacion = nueva_ubicacion


