# POO-Proyecto-2
Aqui se publican todos los archivos relacionados al proyecto final de POO

# Manual técnico del proyecto 2

### Presentación general del proyecto

El proyecto busca simular el aeropuerto Alfonso Bonilla Aragon. Esta diseñado con una interfaz intuitiva para el usuario y 
Tiene manejo de:

+ Aeronaves (aviones, helicopteros y jets)
+ Vuelos
+ Personal y pasajeros
+ Compra de vuelos
+ Embarque y Desembarque
+ Despegue de las aeronaves

### Explicación del programa
El simulador permite crear aeronaves, tripulantes, pasajeros, aerolineas, puertas de embarque y vuelos. Ademas el
sistema permite consultar informacion sobre estos objetos y tiene la funcionalidad de consultar informacion general
sobre paises en los que el usuario este interesado en visitar. Entre las Aeronaves se encuentran tres tipos de 
objetos los cuales son aviones, jets y helicopteros. El sistema fue implementado usando patrones como modelo vista
controlador (MVC), el patrón mediador que se radica en la torre de control del sistema y el patron singleton para 
el aeropuerto y la torre de control. Adicionalmente a esto el sistema permite relacionar aeronaves con vuelos, 
vuelos con aerolineas, puertas de embarque y pasajeros.

### Como compilarlo
El programa utiliza un framework llamado streamlit que debe estar instalado en la maquina del usuario para poder 
ejecutar el programa. Para compilar el programa tendra que:

+ Abrir la terminal de su maquina y navegar hasta la carpeta donde se encuentra ubicado el codigo
+ Escribir lo siguiente `streamlit run main.py` y presionar la tecla enter

Esto deberia cargar un host local en su maquina y usted deberia ser capaz de ver el programa funcionando.

### Imagenes 
#### Menu principal 
![menu](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/35f0dde9-235e-4e7b-8c42-cd8e56fffda8)


***Gracias por haber leido el readme. Esperamos que este manual tecnico haya sido de ayuda***
:+1:

