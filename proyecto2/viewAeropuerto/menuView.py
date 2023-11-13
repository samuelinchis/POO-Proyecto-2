import streamlit as st
from datetime import datetime

"""Esta clase se encarga de mostrar la intefaz del usuario ademas de recoger la informacion necesaria para la creacion
de objetos y la interaccion del usuario con el sistema"""

class Menu:

    def __init__(self):
        st.title("Aeropuerto Alfonso Bonilla Aragón")

    """Despliega las opciones del menu principal y retorna la eleccion del usuario"""
    def crearOBJ_view(self):
        st.title("Creacion de objetos")
        choice = st.sidebar.selectbox("Seleccione el objeto que desea crear", ["Aeronaves","Aerolineas","Vuelos","Tripulacion","Puertas de embarque"])
        return choice

    """Trabaja juntos con otras dos funciones, mostrar_aeronaves y mostrar_aerolineas que se encargan de mostrar la     
    informacion de las aeronaves disponibles en el sistema y las aerolineas existentes respectivamente"""
    def mostrar_info(self):
        st.title("Visualizacion de la informacion")
        self.mostrar_aeronaves()
        self.show_aerolineasVuelos()

    def mostrar_aeronaves(self, aeronaves):
        st.header("Aeronaves creadas")
        data = []
        for i in range(len(aeronaves)):
            aeronave = aeronaves[i]
            numero = len(aeronave.get_vuelos())
            data.append({
                'Marca': aeronave.get_marca(),
                'Modelo': aeronave.get_modelo(),
                'Capacidad': aeronave.get_capacidad(),
                'Velocidad Maxima': aeronave.get_velmax(),
                'Autonomia': aeronave.get_autonomia(),
                'Año de fabricación': aeronave.get_anofabricacion(),
                'Estado': aeronave.get_estado(),
                'Numero de vuelos': numero})
        if data:
            st.table(data)
        else:
            st.info("No hay aeronaves creadas hasta el momento", icon="ℹ️")

    def mostrar_aerolineas(self, aerolineas):
        st.header("Aerolineas creadas")
        data1 = []
        for i in range(len(aerolineas)):
            aerolinea = aerolineas[i]
            data1.append({
                'Marca': aerolinea.get_nombre()})
        if data1:
            st.table(data1)
        else:
            st.info("No hay aerolineas creadas hasta el momento", icon="ℹ️")

    """Recopila la informacion de los vuelos existentes en el sistema y los organiza en una tabla que es visible al 
    usuario"""
    def mostrar_vuelos(self, vuelos):
        st.header("Vuelos creados")
        data2 = []
        # vuelos.values() arroja todos los valores del diccionario "vuelos"
        for vuelo in vuelos.values():
            if vuelo.get_puerta() is not None:
                puerta = vuelo.get_puerta().get_identificacion()
            else:
                puerta = "No hay puerta asignada"
            data2.append({
                'Id': vuelo.get_identificacion(),
                'Fecha': vuelo.get_fecha(),
                'Ciudad de Origen': vuelo.get_ciudad_origen(),
                'Ciudad de Destino': vuelo.get_ciudad_destino(),
                'Sillas Disponibles': vuelo.get_sillas(),
                'Aerolinea:': vuelo.get_aerolinea(),
                'Id puerta de embarque:': puerta})
        if data2:
            st.table(data2)
        else:
            st.info("No hay vuelos creados hasta el momento para esa aerolinea", icon="ℹ️")

    """Recopila la informacion de una lista de puertas que entra como parametro y la organiza en una tabla que luego es 
    visible para el usuario"""
    def mostrar_puertas(self, puertas):
        st.header("Puertas de embarque creadas")
        data = []
        for i in range(len(puertas)):
            puerta = puertas[i]
            data.append({
                'Id': puerta.get_identificacion(),
                'Ubicacion': puerta.get_ubicacion(),
                'Disponibilidad': puerta.get_disponibilidad(),
                'Hora de embarque': puerta.get_hora_embarque()})
        if data:
            st.table(data)
        else:
            st.info("No hay puertas de embarque creadas hasta el momento", icon="ℹ️")

    """Recopila la informacion de una lista de pasajeros que entra como parametro y la organiza en una tabla que luego es 
    visible para el usuario"""
    def mostrar_pasajeros(self, pasajeros):
        st.header("Pasajeros creados")
        data = []
        for i in range(len(pasajeros)):
            pasajero = pasajeros[i]
            data.append({
                'Nombre': pasajero.obtener_nombre(),
                'Apellido': pasajero.obtener_apellido(),
                'Genero': pasajero.obtener_genero(),
                'Fecha de nacimiento': pasajero.obtener_fecha_nacimiento(),
                'Dirección:': pasajero.obtener_direccion(),
                'Telefono': pasajero.obtener_telefono(),
                'Correo:': pasajero.obtener_correo(),
                'Nacionalidad:': pasajero.get_nacionalidad(),
                'Numero de maletas:': pasajero.get_num_maletas(),
                'Información medica:': pasajero.get_info_medica()})
        if data:
            st.table(data)
        else:
            st.info("No hay pasajeros por el momento", icon="ℹ️")

    """Recopila la informacion de una lista de tripulantes que entra como parametro y la organiza en una tabla que luego es 
    visible para el usuario"""
    def mostrar_tripulantes(self, tripulantes):
        st.header("Tripulantes creados")
        data = []
        for i in range(len(tripulantes)):
            tripulante = tripulantes[i]
            data.append({
                'Nombre': tripulante.obtener_nombre(),
                'Apellido': tripulante.obtener_apellido(),
                'Genero': tripulante.obtener_genero(),
                'Fecha de nacimiento': tripulante.obtener_fecha_nacimiento(),
                'Telefono': tripulante.obtener_telefono(),
                'Puesto': tripulante.obtener_puesto(),
                'Horas de trabajo': tripulante.obtener_horas_trabajo()})
        if data:
            st.table(data)
        else:
            st.info("No hay tripulantes por el momento", icon="ℹ️")

    """muestra un titulo y un subtitulo"""
    def show_aerolineasVuelos(self):
        st.header("Aerolineas creadas")
        st.subheader("Vuelos disponibles")

    """Muestra un formulario que recopila informacion que el usuario ingresa al sistema para crear un avion, retorna
    un diccionario con la informacion ingresada"""
    def crearAvion(self):

        with st.form("mi_formulario"):
            marca = st.selectbox('Selecciona tu marca:', ('Airbus', 'ATR', 'Beechcraft', 'Boeing', 'Dornier'))
            modelo = st.text_input('Modelo', '')
            capacidad = st.selectbox('Selecciona la capacidad:', (50, 75, 100, 150, 200))
            velocidad = st.selectbox('Selecciona la velocidad en km/h:', (750, 800, 825, 850, 890))
            autonomia = st.selectbox('Selecciona la autonomia (Distancia Maxima km):', (14500, 15000, 15500, 15700, 16000))
            fabricacion = st.date_input("Año de fabricación", datetime.now())
            estado = st.selectbox('Selecciona el estado:', ('Mantenimiento', 'Disponible'))
            altitud = st.selectbox('Selecciona la altitud maxima:', (12000, 12500, 12800))
            categoria = st.selectbox('Selecciona la categoria:', ('Comercial', 'Carga'))
            crear = st.form_submit_button("Crear")
            if crear:
                return {"marca": marca, "modelo": modelo, "capacidad": capacidad, "velocidad": velocidad, "autonomia": autonomia, "fabricacion": fabricacion,
                        "estado": estado, "altitud": altitud, "categoria": categoria}

    """Muestra un formulario que recopila informacion que el usuario ingresa al sistema para crear un helicoptero, retorna
        un diccionario con la informacion ingresada"""
    def crearHelicoptero(self):
        with st.form("mi_formulario2"):
            marca = st.selectbox('Selecciona tu marca:', ('Bell', 'Sikorsky', 'Airbus', 'Martin', 'AW'))
            modelo = st.text_input('Modelo', '')
            capacidad = st.selectbox('Selecciona la capacidad:', (1, 2, 3, 4, 6))
            velocidad = st.selectbox('Selecciona la velocidad en km/h:', (150, 200, 225, 250, 275))
            autonomia = st.selectbox('Selecciona la autonomia (Distancia Maxima km):',
                                     (390, 400, 420, 450, 460))
            fabricacion = st.date_input("Año de fabricación", datetime.now())
            estado = st.selectbox('Selecciona el estado:', ('Mantenimiento', 'Disponible'))
            rotores = st.selectbox('Selecciona número de rotores:', (1, 2, 3))
            uso = st.selectbox('Selecciona su uso:', ("Rescate", "Turismo", "Transporte"))
            elevacion = st.selectbox('Capacidad maxima de carga', ("1000kg", "1200kg", "1500kg"))
            crear = st.form_submit_button("Crear")
            if crear:
                return {"marca": marca, "modelo": modelo, "capacidad": capacidad, "velocidad": velocidad, "autonomia": autonomia, "fabricacion": fabricacion,
                        "estado": estado, "rotores": rotores, "uso": uso, "elevacion": elevacion}

    """Muestra un formulario que recopila informacion que el usuario ingresa al sistema para crear un Jet, retorna
        un diccionario con la informacion ingresada"""
    def crearJet(self):
        with st.form("mi_formulario3"):
            marca = st.selectbox('Selecciona tu marca:', ('Cessna', 'Embraer', 'Hawker', 'Dassault', 'Gulfstream'))
            modelo = st.text_input('Modelo', '')
            capacidad = st.selectbox('Selecciona la capacidad:', (10, 15, 12, 13, 20))
            velocidad = st.selectbox('Selecciona la velocidad en km/h:', (800, 850, 900, 975, 1000))
            autonomia = st.selectbox('Selecciona la autonomia (Distancia Maxima km):',
                                     (13000, 13500, 13700, 14000, 14200))
            fabricacion = st.date_input("Año de fabricación", datetime.now())
            estado = st.selectbox('Selecciona el estado:', ('Mantenimiento', 'Disponible'))
            propietario = st.text_input('Nombre del dueño', '')
            destinos = st.multiselect('Selecciona tu lista de destinos:', ('Venezuela', 'Nueva Zelanda', 'Mexico', 'Honduras'))
            servicios = st.multiselect('Selecciona tu lista de servicios',('Wifi', 'Cocteleria', 'Video juegos', 'Masajes', 'Comida'))
            crear = st.form_submit_button("Crear")
            if crear:
                return {"marca": marca, "modelo": modelo, "capacidad": capacidad, "velocidad": velocidad,
                        "autonomia": autonomia, "fabricacion": fabricacion,
                        "estado": estado, "propietario": propietario, "destinos": destinos, "servicios": servicios}

    """Muestra un formulario que recopila informacion que el usuario ingresa al sistema para crear un tripulante, 
    retorna un diccionario con la informacion ingresada"""
    def crearTripulante(self):

        with st.form("mi_formulario4"):
            nombre = st.text_input("Digite su nombre", "")
            apellido = st.text_input("Digite su apellido", "")
            cedula = st.text_input("Digite su cedula", "")
            telefono = st.text_input("Digite su número", "")
            genero = st.selectbox("Cual es su genero", ("Masculino", "Femenino"))
            fecha = st.date_input("Fecha de nacimiento", datetime.now())
            puesto = st.selectbox("Cual es su puesto", ("Mecanico", "Azafat@", "Piloto"))
            horas = st.selectbox("Definir su horario laboral", (5, 6, 8, 10, 11))
            crear = st.form_submit_button("Crear")
            if crear:
                return {"nombre": nombre, "apellido": apellido, "cedula": cedula, "genero": genero,
                         "telefono": telefono, "fecha": fecha, "puesto": puesto, "horas": horas}

    """Muestra un formulario que recopila informacion que el usuario ingresa al sistema para crear un pasajero, retorna
     un diccionario con la informacion ingresada"""
    def crearPasajero(self):

        with st.form("mi_formulario4"):
            nombre = st.text_input("Digite su nombre", "")
            apellido = st.text_input("Digite su apellido", "")
            cedula = st.text_input("Digite su cedula", "")
            direccion = st.text_input("Digite su dirección", "")
            telefono = st.text_input("Digite su número", "")
            genero = st.selectbox("Cual es su genero", ("Masculino", "Femenino"))
            fecha = st.date_input("Fecha de nacimiento", datetime.now())
            correo = st.text_input("Digite su correo electronico", "")
            nacionalidad = st.text_input("Digite su nacionalidad", "")
            maletas = st.selectbox("Cual es su número de maletas", (1, 2, 3, 4))
            medica = st.text_input("Información medica", "")
            crear = st.form_submit_button("Crear")
            if crear:
                return {"nombre": nombre, "apellido": apellido, "cedula": cedula, "genero": genero, "direccion": direccion
                         ,"fecha": fecha, "telefono": telefono, "correo": correo ,"nacionalidad": nacionalidad, "maletas": maletas
                        , "medica": medica}

    """Muestra un formulario que recopila informacion que el usuario ingresa al sistema para crear una aeronlinea,
     retorna el nombre de la aerolinea creada"""
    def crearAerolinea(self):

        with st.form("mi_formulario5"):
            nombre = st.text_input("Digite el nombre de la aerolinea:")
            crear = st.form_submit_button("Crear")

            if crear:
                return nombre

    """Muestra un formulario que recopila informacion que el usuario ingresa al sistema para crear un vuelo, retorna 
    un diccionario con la informacion ingresada"""
    def crearVuelo(self, aerolineas):

        with st.form("mi_formulario6"):
            identificacion = st.number_input("Digita el numero de identificación", value=None, placeholder="Número")
            fecha = st.date_input("Fecha del vuelo:", datetime.now())
            origen = st.selectbox("Selecciona la ciudad de origen del vuelo:", ("Cali", "Bogota", "Pasto", "Cartagena"
                                                                                , "Santa Marta", "Medellin"))
            destino = st.selectbox("Selecciona la ciudad de destino", ("Otawa", "Caracas", "New York", "Monte Video", "Buenos Aires", "Sevilla"))
            sillas = st.selectbox("Selecciona el numero de sillas disponibles:", (50, 60, 70, 80, 100))
            aerolinea = st.selectbox("Selecciona la aerolinea", aerolineas)
            crear = st.form_submit_button("Crear")
            if crear:
                return {"identificacion": identificacion, "fecha": fecha, "origen": origen,
                        "destino": destino, "sillas": sillas, "aerolinea": aerolinea}

    """Muestra un formulario que recopila informacion que el usuario ingresa al sistema para crear una puerta de 
    embarque, retorna un diccionario con la informacion ingresada"""
    def crearEmbarque(self):

        with st.form("mi:formulario7"):
            identificacion = st.number_input("Digita el numero de identificación")
            ubicacion = st.selectbox("Cual es la ubicación de la puerta", ("Zona Sur", "Zona Norte", "Zona Oeste", "Zona Este"))
            hora = st.time_input('Selecciona una hora')
            crear = st.form_submit_button("Crear")
            if crear:
                return {"identificacion": identificacion, "ubicacion": ubicacion, "hora": hora}

    """Recopila la informacion de los vuelos existentes en el sistema y los organiza en una tabla que es visible al 
        usuario. Esta informacion solo se muestra si el vuelo esta asosiado con la aerolinea que entra de parametro"""
    def mostrar_vuelos_aerolinea(self,vuelos, aerolinea):
        st.header("Vuelos creados")
        data2 = []
        for vuelo in vuelos.values():
            if vuelo.get_puerta() is not None:
                puerta = vuelo.get_puerta().get_identificacion()
            else:
                puerta = "No hay puerta asignada"
            if vuelo.get_aerolinea() == aerolinea:
                data2.append({
                    'Id': vuelo.get_identificacion(),
                    'Fecha': vuelo.get_fecha(),
                    'Ciudad de Origen': vuelo.get_ciudad_origen(),
                    'Ciudad de Destino': vuelo.get_ciudad_destino(),
                    'Sillas Disponibles': vuelo.get_sillas(),
                    'Aerolinea:': vuelo.get_aerolinea(),
                    'Id puerta de embarque:': puerta})
        if data2:
            st.table(data2)
        else:
            st.info("No hay vuelos creados hasta el momento para esa aerolinea", icon="ℹ️")

    """Muestra una lista de vuelos ya asosiados a una aerlinea en especifico y recibe un codigo del usuario para comprar
     el vuelo con dicho codigo"""
    def compraVuelos(self, lista, codigos, aerolinea):
        st.header("Escoje el código de vuelo que deseas reservar de la lista:")
        self.mostrar_vuelos_aerolinea(lista, aerolinea)
        with st.form("formulario"):
            codigo = st.selectbox("Código del vuelo a reservar", codigos)
            crear = st.form_submit_button("Reservar")
            if crear:
                return codigo

    """Recibe una lista de aeronaves y muestra el modelo, la marca y el estado de la aeronave al usuario organizada en 
    una tabla"""
    def mostrar_disponibilidad(self,l_aeronaves):
        datos = []
        if len(l_aeronaves) == 0:
            st.warning("No existen aeronaves disponibles")
        else:
            for i in range(len(l_aeronaves)):
                aeronave = l_aeronaves[i]
                datos.append({
                    "id": i,
                    "Modelo":aeronave.get_modelo(),
                    "Marca": aeronave.get_marca(),
                    "Estado": aeronave.get_estado()
                })
            if datos:
                st.table(datos)
            return datos

    """Da la posibilidad de elegir un estado. retorna ese estado"""
    def cambiar_dispo_mante(self):
        return st.selectbox("Seleccione el nuevo estado",["Disponible", "En mantenimiento"], placeholder="Seleccione el estado")


    """Muestra la informacion mas general del aeropuerto ademas de unas imagenes"""
    def info_aeropuerto(self):
        st.title(f"Información del Aeropuerto: Alfonso Bonilla Aragón")

        # Mostrar detalles generales del aeropuerto
        st.header("Detalles Generales")
        st.write(f"- Ciudad: Cali")
        st.write(f"- País: Colombia")
        st.write(f"- Código IATA: CLO")
        st.divider()

        st.subheader("Imagenes")

        # Mostrar imágenes del aeropuerto
        st.header("Imágenes del Aeropuerto")
        imagenes = ["https://www.semana.com/resizer/YQFRKgcGtxlkQO0YUQEkK1COR34=/1280x720/smart/filters:format(jpg):quality(80)/cloudfront-us-east-1.images.arcpublishing.com/semana/PAGU6HGVJZA5DPECRCVNAXKMLI.jpg", "https://www.eltiempo.com/files/article_main/uploads/2017/06/18/59471cae5eb5e.jpeg", "https://i.pinimg.com/564x/06/59/21/0659214670c36ae5e3061df3ce26cd81.jpg"]
        for imagen_url in imagenes:
            st.image(imagen_url, caption="Aeropuerto", use_column_width=True)

    """Muestra la aeronaves disponibles en el sistema, y espera una opcion del usuario para asignar un vuelo a dicha aeronave
     despues muestra una lista de los vuelos disponibles y retorna el codigo del vuelo y la aeronave elegidos, saltan 
     excepciones en caso de que la aeronave tenga 3 vuelos asignados o si la aeronave ya tiene un vuelo con ciudad de 
     origen en cali"""
    def consignar_vuelos(self, marcas, aeronaves, vuelos, codigos):
        self.mostrar_aeronaves(aeronaves)
        marcas.insert(0, "_")
        mark = st.selectbox("Elegir el modelo de aeronave para asignar", marcas)
        if mark != "_":
            aeronave = None
            for i in range(len(aeronaves)):
                if aeronaves[i].get_modelo() == mark:
                    aeronave = aeronaves[i]
            if len(aeronave.get_vuelos()) >= 3:
                st.warning("No es posible asignar más de 3 vuelos por aeronave", icon="❌")
            else:
                self.mostrar_vuelos(vuelos)
                with st.form("formulario_20"):
                    codigo = st.selectbox("Código del vuelo a reservar", codigos)
                    crear = st.form_submit_button("Reservar")
                if crear:
                    flag = True
                    if vuelos[codigo].get_ciudad_origen() == 'Cali':
                        vuelosaero = aeronave.get_vuelos()
                        for i in range(len(vuelosaero)):
                            if vuelosaero[i].get_ciudad_origen() == 'Cali':
                                st.warning("No es posible asignar 2 vuelos que su ciudad de origen sea Cali", icon='❌')
                                flag = False
                    if flag:
                        return codigo, aeronave

    """Muestra las puertas de embarque disponibles en el sistema, da la opcion de elegir una puerta de embarque, si la 
    puerta de embarque elegida ya esta asignada salta un mensaje. El usuario elije una vuelo para asociar con la puerta
    embarque si el vuelo no tiene ciudad de origen en la ciudad de Cali salta un mensaje de error. Si el vuelo ya tiene 
    una puerta asignada salta una advertencia. Si ninguno de los errores anteriormente mencionados es activado entonces 
    la funcion retorna el codigo del vuelo y la puerta de embarque elegidos """
    def asignar_embarque(self, puertas, ids, codigos,vuelos):
        self.mostrar_puertas(puertas)
        ids.insert(0, "_")
        id = st.selectbox("Escoger el ID de la puerta a asignar:", ids)
        if id != "_":
            puerta = None
            for i in range(len(puertas)):
                if puertas[i].get_identificacion() == id:
                    puerta = puertas[i]
            if puerta.get_disponibilidad() == "Asignada":
                st.warning("La puerta ya ha sido asignada a un vuelo")
            else:
                self.mostrar_vuelos(vuelos)
                with st.form("Formu"):
                    codigo = st.selectbox("Escoger a que vuelo asignar la puerta", codigos)
                    confirm = st.form_submit_button("Confirmar")
                    if confirm:
                        vuelo = vuelos[codigo]
                        if vuelo.get_ciudad_origen() != "Cali":
                            st.warning("Solo es posible asignar puerta de embarque a vuelos desde la ciudad de Cali")
                        else:
                            if vuelo.get_puerta() is not None:
                                st.warning("El vuelo ya tiene asignada una puerta")
                            else:
                                return codigo, puerta

    """El usuario elije una aeronave para simular, si la aeronave elegida no tiene vuelos asignados salta una 
    advertencia. luego el usuario elige un vuelo, si este vuelo no tiene una puerta de embarque asignada salta un 
    mensaje de error. Si ninguno de estos mensajes salta la funcion retorna la aeronave y el vuelos elegidos por el 
    usuario"""
    def simular_vuelo(self, aeronaves, modelos, vuelos, codigos):
        self.mostrar_aeronaves(aeronaves)
        modelos.insert(0, "_")
        modelo = st.selectbox("Elegir el modelo de aeronave para asignar", modelos)
        if modelo != "_":
            aeronave = None
            for i in range(len(aeronaves)):
                if aeronaves[i].get_modelo() == modelo:
                    aeronave = aeronaves[i]
            if not aeronave.get_vuelos():
                st.warning("La aeronave no tiene vuelos asignados")
            else:
                self.mostrar_vuelos(vuelos)
                codigos.insert(0, "_")
                codigo = st.selectbox("Escoger a que vuelo asignar la puerta", codigos)
                if codigo != "_":
                    vuelo = vuelos[codigo]
                    if vuelo.get_puerta() is None:
                        st.warning("La puerta no tiene asignada ninguna puerta de embarque", icon='❌')
                    else:
                        return aeronave, vuelo

    """Recibe el nombre de un pais"""
    def requestpais(self):
        pais = st.text_input("Escriba un pais")
        if st.button("confirmar"):
            return pais