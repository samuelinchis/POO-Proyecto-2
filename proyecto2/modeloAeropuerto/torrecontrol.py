import streamlit as st
class TorreControl:
    """Instance guarda un solo objeto que se crea de esta clase"""
    _instance = None  # esta es una variable de clase

    """Es esta logica se implementa el singleton de forma que si ya existe una instancia de la torre de control no se 
    llame al constructor sino que simplemente retorna el objeto existente."""
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TorreControl, cls).__new__(cls)
            cls._instance._vuelos = {}
            cls._instance._aeropuerto = None
            cls._chat = []
        return cls._instance

    def asignar_aeropuerto(self,aeropuerto):
        self._aeropuerto = aeropuerto

    def agregar_aeronave(self, aeronave):
        self._chat.append(aeronave)

    """Reenvia un mensaje al chat que existe entre las aeronaves excepto a la nave que originalmente comunicó el mensaje"""
    def enviar_mensaje(self, ubi, avion):
        for destinatario in self._chat:
            if destinatario != avion:
                destinatario.recibir_mensaje(ubi, avion)

    """Reenvia un estado al chat que existe entre las aeronaves excepto a la nave que originalmente comunicó el estado"""
    def enviar_estado(self, aeronave):
        for destinatario in self._chat:
            if destinatario != aeronave:
                destinatario.recibir_estado(aeronave)

    def asignarVuelos(self, idvuelo, aeronave):
        vuelo_a_asignar = self._vuelos[idvuelo]
        aeronave.addVuelo(vuelo_a_asignar)

    # Getters

    def get_aeropuerto(self):
        return self._aeropuerto

    def get_vuelo(self):
        return self._vuelos

    def vuelos_aerolinea(self, aerolinea):
        print(f"Vuelos de la aerolinea {aerolinea}: ")
        for valor in self._vuelos.values():
            if valor.get_aerolinea() == aerolinea:
                valor.info_vuelo()

    def comunicar_todos_estados(self):
        for miembros in self._chat:
            miembros.enviar_estado()

    """Añade un vuelo a diccionario de vuelos de la torre de control"""
    def new_vuelo(self, vuelo):
        self._vuelos[vuelo.get_identificacion()] = vuelo

    """El sistema verfica si la aeronave puede o no cambiar su estado, la unica forma de que una aeronave no pueda 
    cambiar su estado es si ya tiene todos los vuelos posibles asignados. La funcion retorna una excepcion si se le 
    ingresa un id de aeronave que no existe"""
    def validar_cambio(self, id, aeropuerto):
        aeronaves = aeropuerto.get_aeronaves()
        try:
            nave = aeronaves[id]
            if len(nave.get_vuelos()) == 3:
                flag = False
            else:
                flag = True

            return flag
        except IndexError:
            st.warning("El id ingresado no esta en la lista")

    """Cambia el estado de una aeronave"""
    def cambiar_estado(self, estado, id, aeropuerto):
        aeronaves = aeropuerto.get_aeronaves()
        if estado == "Disponible":
            aeronaves[id].set_estado("Disponible")
        if estado == "En mantenimiento":
            aeronaves[id].set_estado("En mantenimiento")


    def codigosVuelo(self):
        lista = []
        for vuelo in self._vuelos.values():
            lista.append(vuelo.get_identificacion())
        return lista

    def codigosVuelosaero(self, aerolinea):
       lista = []
       for vuelo in self._vuelos.values():
           if vuelo.get_aerolinea() == aerolinea:
                lista.append(vuelo.get_identificacion())
       return lista
