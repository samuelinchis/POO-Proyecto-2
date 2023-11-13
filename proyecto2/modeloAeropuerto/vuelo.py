""" Clase Vuelo """


class Vuelo:
    """Constructor de la clase Vuelo"""
    def __init__(self, identificacion=0, fecha="", ciudad_origen="", ciudad_destino="", sillas_dispo=0,  aerolinea="", tripulantes=None):
        if tripulantes is None:
            tripulantes = []
        self._identificacion = identificacion
        self._fecha = fecha
        self._ciudad_origen = ciudad_origen
        self._ciudad_destino = ciudad_destino
        self._tripulantes = tripulantes
        self._sillas_dispo = sillas_dispo
        self._puerta_embarque = None
        self._aerolinea = aerolinea

    # Getters
    def get_identificacion(self):
        return self._identificacion

    def get_fecha(self):
        return self._fecha

    def get_ciudad_origen(self):
        return self._ciudad_origen

    def get_ciudad_destino(self):
        return self._ciudad_destino

    def get_puerta(self):
        return self._puerta_embarque

    def get_tripulantes(self):
        return self._tripulantes

    def get_sillas(self):
        return self._sillas_dispo

    def get_aerolinea(self):
        return self._aerolinea

    # Setters

    def set_identificacion(self, identificacion):
        self._identificacion = identificacion

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_ciudad_origen(self, ciudad_origen):
        self._ciudad_origen = ciudad_origen

    def set_ciudad_destino(self, ciudad_destino):
        self._ciudad_destino = ciudad_destino

    def set_puerta(self, puerta_embarque):
        self._puerta_embarque = puerta_embarque

    def set_sillas(self, sillas_dispo):
        self._sillas_dispo = sillas_dispo

    def set_aerolinea(self, aerolinea):
        self._aerolinea = aerolinea

    # Métodos

    """Añade un tripulante al vuelo"""
    def asignar_tripulacion(self, tripulante):
        self._tripulantes.append(tripulante)

    """Elimina un tripulante al vuelo"""
    def eliminar_tripulante(self, cedula):
        for i in range(len(self._tripulantes)):
            if self._tripulantes[i].obtener_cedula() == cedula:
                del (self._tripulantes[i])
