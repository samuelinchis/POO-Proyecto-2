from modeloAeropuerto.persona import Persona

""" Clase tripulante """


class Tripulante(Persona):
    """Constructor de la clase Tripulante. Hereda atributos de la clase Persona"""
    def __init__(self, nombre, cedula, genero, apellido, fecha, direccion, telefono, correo, puesto="Desconocido", anos_exp=0, horas_trabajo=0):
        super().__init__(nombre, cedula, genero, apellido, fecha, direccion, telefono, correo)
        self._puesto = puesto
        self._anos_exp = anos_exp
        self._horas_trabajo = horas_trabajo

    # Getters

    def obtener_puesto(self):
        return self._puesto

    def obtener_anos_exp(self):
        return self._anos_exp

    def obtener_horas_trabajo(self):
        return self._horas_trabajo

    # Setters

    def establecer_puesto(self, nuevo_puesto):
        self._puesto = nuevo_puesto

    def establecer_anos_exp(self, nuevos_anos_exp):
        self._anos_exp = nuevos_anos_exp

    def establecer_horas_trabajo(self, nuevas_horas_trabajo):
        self._horas_trabajo = nuevas_horas_trabajo
