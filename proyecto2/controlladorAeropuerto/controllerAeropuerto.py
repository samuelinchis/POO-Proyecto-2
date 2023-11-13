import json
import requests
from viewAeropuerto.menuView import Menu
from modeloAeropuerto.aeropuerto import Aeropuerto
from modeloAeropuerto.avion import Avion
from modeloAeropuerto.jet import Jet
from modeloAeropuerto.vuelo import Vuelo
from modeloAeropuerto.tripulante import Tripulante
from modeloAeropuerto.embarque import Embarque
from modeloAeropuerto.helicoptero import Helicoptero
from modeloAeropuerto.pasajero import Pasajero
from modeloAeropuerto.torrecontrol import TorreControl
from modeloAeropuerto.aerolinea import Aerolinea
import streamlit as st


class Controller:
    """Constructor de la clase controlador del aeropuerto"""
    def __init__(self):
        if 'aeropuerto' not in st.session_state:
            st.session_state.aeropuerto = Aeropuerto()
        if 'torre' not in st.session_state:
            st.session_state.torre = TorreControl()
        if 'click' not in st.session_state:
            st.session_state.click = False
        self.view = Menu()

    def click_button(self):
        st.session_state.click = True

    """Organiza el menu en un sidebar, dependiendo de la eleccion del usuario en el menú llama las funciones
    correspondientes"""
    def menu_opciones(self):
        with st.sidebar:
            opciones_menu = ("Información Aeropuerto", "Crear objetos", "Información general", "Reservar vuelo", "Mostrar estados", "Informacion de los países", "Asignar vuelos", "Asignar puertas", "Despegar")
            st.title("Menu de principal")
            st.divider()
            option = st.selectbox("Seleccionar area del menú:", opciones_menu)
            st.divider()

        if option == "Información Aeropuerto":
            self.view.info_aeropuerto()
        if option == "Crear objetos":
            eleccion = self.view.crearOBJ_view()
            self.Seleccionar_OBJ_crear(eleccion)
        if option == "Información general":
            self.mostrarAerolineas()
            self.mostrarVuelos()
            self.mostrarAeronaves()
            self.mostrarPuertas()
            self.mostrarPasajeros()
            self.mostrarTripulantes()
        if option == "Reservar vuelo":
            self.comprarVuelos()
        if option == "Mostrar estados":
           self.cambiarEstados()
        if option == "Informacion de los países":
            pais = self.view.requestpais()
            if pais:
                self.getPaises(pais)

        if option == "Asignar vuelos":
            self.consignarVuelos()

        if option == "Asignar puertas":
            self.asignarPuertas()
        if option == "Despegar":
            self.simularVuelo()

    """Se encarga de llamar a varias funciones que en conjunto se encargan de verificar si una aeronave existente puede
    o no realizar un cambio en su estado"""
    def cambiarEstados(self):
        datos = self.view.mostrar_disponibilidad(st.session_state.aeropuerto.get_aeronaves())
        if datos is not None:
            idAeronave = st.number_input("Digite el id", min_value=0)
            aeropuerto = st.session_state.aeropuerto
            flag = st.session_state.torre.validar_cambio(idAeronave, aeropuerto)
            if not flag:
                st.warning("La aeronave ha sido totalmente asignada")
            else:
                choice = self.view.cambiar_dispo_mante()
                st.session_state.torre.cambiar_estado(choice, idAeronave, st.session_state['aeropuerto'])

    def newAeronave(self):
        st.title("Sistema de Creación de Aeronaves")
        opciones = ['Avion', 'Helicoptero', 'Jet']
        tipo_aeronave = st.selectbox('Selecciona una opción', opciones)
        st.write('Has seleccionado:', tipo_aeronave)
        if tipo_aeronave == 'Avion':
            datos = self.view.crearAvion()
            if datos is not None:
                avion = Avion(datos["marca"], datos["modelo"], datos["capacidad"],
                              datos["velocidad"], datos["autonomia"], datos["fabricacion"], datos["estado"],0, [],
                              datos["altitud"], 2, datos["categoria"])
                st.session_state.aeropuerto.add_aeronave(avion)
                st.success("Creación confirmada", icon='✅')
        if tipo_aeronave == 'Helicoptero':
            datos1 = self.view.crearHelicoptero()
            if datos1 is not None:
                helicoptero = Helicoptero(datos1["marca"], datos1["modelo"], datos1["capacidad"],
                                          datos1["velocidad"], datos1["autonomia"], datos1["fabricacion"], 0, [], datos1["estado"], datos1["uso"], datos1["elevacion"])
                st.session_state.aeropuerto.add_aeronave(helicoptero)
                st.success("Creación confirmada", icon='✅')
        if tipo_aeronave == 'Jet':
            datos2 = self.view.crearJet()
            if datos2 is not None:
                jet = Jet(datos2["marca"], datos2["modelo"], datos2["capacidad"],
                          datos2["velocidad"], datos2["autonomia"], datos2["fabricacion"], datos2["estado"], [], datos2["propietario"], datos2["destinos"], datos2["servicios"])
                st.session_state.aeropuerto.add_aeronave(jet)
                st.success("Creación confirmada", icon='✅')

    def newTripulante(self):
        datos = self.view.crearTripulante()
        if datos is not None:
            tripulante = Tripulante(datos["nombre"], datos["cedula"], datos["genero"], datos["apellido"], datos["fecha"]
                                    , "Desconocida", datos["telefono"], "Desconocido", datos["puesto"], 0, datos["horas"])
            st.session_state.aeropuerto.add_tripulante(tripulante)
            st.success("Creación confirmada", icon='✅')

    def newPasajero(self):
        datos = self.view.crearPasajero()
        if datos is not None:
            pasajero = Pasajero(datos["nombre"],datos["cedula"], datos["genero"], datos["apellido"], datos["fecha"], datos["direccion"], datos["telefono"], datos["correo"], datos["nacionalidad"]
                                , datos["maletas"], datos["medica"])
            st.session_state.aeropuerto.add_pasajero(pasajero)
            st.success("Creación confirmada", icon='✅')


    def newAerolinea(self):
        st.title("Sistema de creación de aerolineas")
        nombre = self.view.crearAerolinea()
        if nombre is not None:
            aerolinea = Aerolinea(nombre)
            st.session_state.aeropuerto.add_aerolinea(aerolinea)
            st.success("Creación confirmada", icon='✅')

    def newVuelo(self):
        st.title("Sistema de creación de vuelos")
        aerolineas = st.session_state.aeropuerto.get_aerolinea()
        if not aerolineas:
            st.warning("Es necesario tener al menos una aerolinea para crear los vuelos!!")
        else:
            datos = self.view.crearVuelo(st.session_state.aeropuerto.get_nombresaeros())
            if datos is not None:
                vuelo = Vuelo(datos["identificacion"], datos["fecha"], datos["origen"], datos["destino"], datos["sillas"], datos["aerolinea"],[])
                st.session_state.torre.new_vuelo(vuelo)
                st.success("Creación confirmada", icon='✅')

    def newEmbarque(self):
        st.title("Sistema de creación de puertas de embarque")
        datos = self.view.crearEmbarque()
        if datos is not None:
            embarque = Embarque(datos["identificacion"], datos["ubicacion"], "Libre", datos["hora"])
            st.session_state.aeropuerto.add_puerta_emb(embarque)
            st.success("Creación confirmada", icon='✅')

    def mostrarAeronaves(self):
        self.view.mostrar_aeronaves(st.session_state.aeropuerto.get_aeronaves())

    def mostrarPuertas(self):
        self.view.mostrar_puertas(st.session_state.aeropuerto.get_puertas_emb())

    def mostrarVuelos(self):
        self.view.mostrar_vuelos(st.session_state.torre.get_vuelo())

    def mostrarAerolineas(self):
        self.view.mostrar_aerolineas(st.session_state.aeropuerto.get_aerolinea())

    def mostrarPasajeros(self):
        self.view.mostrar_pasajeros(st.session_state.aeropuerto.get_pasajeros())

    def mostrarTripulantes(self):
        self.view.mostrar_tripulantes(st.session_state.aeropuerto.get_tripulantes())

    """Recibe una eleccion de un submenu que aparece cuando el usuario esta intentando crear un objeto dentro del 
    sistema. Dependiendo de la eleccion del usuario la logica ejecuta la funcion correspondiente"""
    def Seleccionar_OBJ_crear(self, seleccion):
        if seleccion == "Aeronaves":
            self.newAeronave()
        elif seleccion == "Aerolineas":
            self.newAerolinea()
        elif seleccion == "Vuelos":
            self.newVuelo()
        elif seleccion == "Tripulacion":
            self.newTripulante()
        elif seleccion == "Puertas de embarque":
            self.newEmbarque()



    def comprarVuelos(self):
        st.title("Sistema de reservas de vuelos")

        if not st.session_state.torre.get_vuelo():
            st.info("No hay vuelos creados por el momento", icon="ℹ️")
        else:
            aerolineas = st.session_state.aeropuerto.get_nombresaeros()
            aero = st.session_state.aeropuerto.get_aerolinea()[0]
            aerolinea = st.selectbox('Selecciona una opción', aerolineas)
            st.write('Has seleccionado:', aerolinea)
            codigos = st.session_state.torre.codigosVuelosaero(aerolinea)
            vuelos = st.session_state.torre.get_vuelo()
            if aerolinea is not None:
                code = self.view.compraVuelos(vuelos, codigos, aerolinea)
                st.subheader("Debes crear un pasajero para reservar el vuelo")
                self.newPasajero()
                if not st.session_state.aeropuerto.get_pasajeros():
                    st.warning("Esperar a crear pasajero", icon="👌")
                else:
                    pasajero = st.session_state.aeropuerto.get_pasajeros()[-1]
                    if code is not None:
                        aero.reservar_vuelo(pasajero, code, vuelos)

    def simularVuelo(self):
        st.title("Sistema de simulación de vuelos")
        aeronaves = st.session_state.aeropuerto.get_aeronaves()
        if not aeronaves:
            st.warning("Es necesario crear aeronaves")
        else:
            modelos = st.session_state.aeropuerto.modelos_aeronaves()
            vuelos = st.session_state.torre.get_vuelo()
            if not vuelos:
                st.warning("Es necesario crear vuelos")
            else:
                codigos = st.session_state.torre.codigosVuelo()
                data = self.view.simular_vuelo(aeronaves, modelos, vuelos, codigos)
                if data is not None:
                    aeronave = data[0]
                    vuelo = data[1]
                    abordaje = st.selectbox("Iniciar proceso de abordaje:", ("_", "Iniciar"))
                    if abordaje != "_":
                        aeronave.set_estado("En puerta de embarque")
                        pista = st.selectbox("Permitir paso a la pista", ("_", "Permitir"))
                        if pista != "_":
                            aeronave.set_estado("En pista")
                            volar = st.selectbox("Volar", ("-", "Despegar"))
                            if volar != "_":
                                aeronave.set_estado("Volando")
                                st.success("La aeronave ha sido liberada correctamente", icon='✅')
                                vuelo.get_puerta().set_disponibilidad("Disponible")
                                vuelo.set_puerta(None)




    """concatena un mensaje a la url y hace un request, verfica si el request es exitoso, si lo es entonces el imprime la 
    informacion acerca del pais"""
    def getPaises(self, pais):
        url = "https://restcountries.com/v3.1/name/" + pais

        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = json.loads(respuesta.text)
            moneda = datos[0]["currencies"]
            st.write("Nombre: ", datos[0]["name"]["common"])
            st.table(moneda)
            st.write("Ciudad Capital: ", datos[0]["capital"][0])
            st.write("Region donde se ubica: ", datos[0]["region"])
            st.write("Poblacion: ", datos[0]["population"])
            st.image(datos[0]["flags"]["png"])
        else:
            st.warning("No se pudo encontrar el pais")


    def consignarVuelos(self):
        st.title("Sistema de asignación de vuelos a las aeronaves")
        aeronaves = st.session_state.aeropuerto.get_aeronaves()
        if not aeronaves:
            st.warning("Es necesario crear aeronaves")
        else:
            marcas = st.session_state.aeropuerto.modelos_aeronaves()
            vuelos = st.session_state.torre.get_vuelo()
            if not vuelos:
                st.warning("Es necesario crear vuelos")
            else:
                codigos = st.session_state.torre.codigosVuelo()
                resultado = self.view.consignar_vuelos(marcas, aeronaves, vuelos, codigos)
                if resultado is not None:
                    codigo = resultado[0]
                    aeronave = resultado[1]
                    st.session_state.torre.asignarVuelos(codigo, aeronave)


    def asignarPuertas(self):
        st.title("Sistema de asignación de puertas")
        puertas = st.session_state.aeropuerto.get_puertas_emb()
        ids = st.session_state.aeropuerto.id_puertas()
        vuelos = st.session_state.torre.get_vuelo()
        codigos = st.session_state.torre.codigosVuelo()
        result = self.view.asignar_embarque(puertas, ids, codigos, vuelos)
        if result is not None:
            codigo = result[0]
            puerta = result[1]
            vuelo = vuelos[codigo]
            puerta.set_disponibilidad("Asignada")
            vuelo.set_puerta(puerta)


