import streamlit as st
"""" Clase Aerolinea """


class Aerolinea:
    # Constructor de la clase Aerolinea
    def __init__(self, nombre=""):
        self.nombre = nombre

    """revisa si el vuelo tiene sillas disponibles, en caso de que si entonces asigna un pasajero al vuelo y reduce el 
    numero de sillas disponibles"""
    def reservar_vuelo(self, pasajero, codigo, vuelo):
        if vuelo[codigo].get_sillas() == 0:
            st.warning("No hay suficientes sillas disponibles, intenta otro vuelo.", icon='❌')
        else:
            # Realiza la reserva del vuelo
            pasajero.set_vuelo(vuelo[codigo])
            vuelo[codigo].set_sillas(vuelo[codigo].get_sillas() - 1)
            print("El vuelo ha sido adquirido correctamente, preparate para despegar!!\n")

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    # Getters
    def get_nombre(self):
        return self.nombre
