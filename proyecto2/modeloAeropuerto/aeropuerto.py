""" Clase Aeropuerto """
import streamlit as st


class Aeropuerto:

    """Constructor de la clase aeropuerto"""
    def __init__(self, puertas_embarque=[], tripulantes=[]):
        self._aeronaves = []
        self._puertas_embarque = puertas_embarque
        self._tripulantes = tripulantes
        self._aerolineas = []
        self._pasajeros = []

    # Getters

    def get_aeronaves(self):
        return self._aeronaves

    def get_puertas_emb(self):
        return self._puertas_embarque

    def get_tripulantes(self):
        return self._tripulantes

    def get_aerolinea(self):
        return self._aerolineas

    def get_pasajeros(self):
        return self._pasajeros


    # Metodos

    """Esta funcion recibe una aeronave y la añade a lista de aeronaves del aeropuerto"""
    def add_aeronave(self, aeronave):
        self._aeronaves.append(aeronave)
        st.session_state['aeronaves'] = self._aeronaves

    """Esta funcion recibe una puerta de embarque y la añade a lista de puertas de embarque del aeropuerto"""
    def add_puerta_emb(self, puerta_emb):
        self._puertas_embarque.append(puerta_emb)

    """Esta funcion esta creada para eliminar una aeronave de la lista de aeronaves del aeropuerto"""
    def delete_aeronave(self, modelo):
        for i in range(len(self._aeronaves)):
            if self._aeronaves[i].get_modelo() == modelo:
                del (self._aeronaves[i])

    """Esta funcion esta creada para eliminar una puerta de embarque de la lista de puertas de embarque del 
    aeropuerto"""
    def delete_puerta(self, identificacion):
        for i in range(len(self._puertas_embarque)):
            if self._puertas_embarque[i].get_identificacion() == identificacion:
                del (self._puertas_embarque[i])

    """Añade un tripulante a la lista de tripulantes del aeropuerto"""
    def add_tripulante(self, tripulante):
        self._tripulantes.append(tripulante)

    """Elimina un tripulante de la lista de tripulantes del aeropuerto"""
    def delete_tripulante(self, nombre):
        for i in range(len(self._tripulantes)):
            if self._tripulantes[i].obtener_nombre() == nombre:
                del (self._tripulantes[i])

    """Añade una aerolinea a la lista de aerolineas del aeropuerto"""
    def add_aerolinea(self, aerolinea):
        self._aerolineas.append(aerolinea)

    """Elimina una aerolinea de la lista de aerolineas del aeropuerto"""
    def delete_aerolinea(self, nombre):
        for i in range(len(self._aerolineas)):
            if self._aerolineas[i].get_nombre() == nombre:
                del (self._aerolineas[i])

    """Esta funcion extrae los nombres de las aerolineas que pertenecen al aeropuerto en un lista, finalmente retorna
    la lista con los nombres"""
    def get_nombresaeros(self):
        lista = []
        for i in range(len(self._aerolineas)):
            lista.append(self._aerolineas[i].get_nombre())
        return lista

    """Esta funcion añade un pasajero a la lista de pasajeros del aeropuerto"""
    def add_pasajero(self, pasajero):
        self._pasajeros.append(pasajero)

    """Esta funcion extrae los modelos de las aeronaves que pertenecen al aeropuerto en un lista, finalmente retorna
    la lista con los modelos"""
    def modelos_aeronaves(self):
        lista = []
        for i in range(len(self._aeronaves)):
            lista.append(self._aeronaves[i].get_modelo())
        return lista

    """Esta funcion extrae los ids de las puertas de embarque que pertenecen al aeropuerto en un lista, finalmente 
    retorna la lista con los ids"""
    def id_puertas(self):
        lista = []
        for i in range(len(self._puertas_embarque)):
            lista.append(self._puertas_embarque[i].get_identificacion())
        return lista