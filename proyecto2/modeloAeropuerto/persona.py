""" Clase persona """


class Persona:
    """Constructor de la clase Pasajero"""
    def __init__(self,  nombre="Desconocido", cedula=0, genero="Desconocido", apellido="Desconocido", fecha="Desconocida", direccion="Desconocida", telefono=0, correo="Desconocido"):
        self._nombre = nombre
        self._cedula = cedula
        self._genero = genero
        self._apellido = apellido
        self._fecha = fecha
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo

    # Getters

    def obtener_nombre(self):
        return self._nombre

    def obtener_cedula(self):
        return self._cedula

    def obtener_genero(self):
        return self._genero

    def obtener_apellido(self):
        return self._apellido

    def obtener_fecha_nacimiento(self):
        return self._fecha

    def obtener_direccion(self):
        return self._direccion

    def obtener_telefono(self):
        return self._telefono

    def obtener_correo(self):
        return self._correo

    # Setters
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_cedula(self, nueva_cedula):
        self._cedula = nueva_cedula

    def set_genero(self, nuevo_genero):
        self._genero = nuevo_genero

    def set_apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    def set_fecha_nacimiento(self, nueva_fecha):
        self._fecha = nueva_fecha

    def set_direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    def set_telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono

    def set_correo(self, nuevo_correo):
        self._correo = nuevo_correo

