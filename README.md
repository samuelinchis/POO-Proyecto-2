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

### Explicacion tecnica del programa
El programa esta implementado con python, al estar escrito con el patron de diseño MVC los archivos estan repartidos en tres carpetas las cuales son controlladorAeropuerto, viewAeropuerto y modeloAeropuerto
el unico archivo por fuera de estas carpetas es el main.py que es el que se compila.

Esta version del proyecto cuenta con 14 clases las cuales son
+ Menu
+ Controller
+ Aerolinea
+ Aeropuerto
+ Aeronave
+ Avion
+ Jet
+ Helicoptero
+ Embarque
+ Vuelo
+ Persona
+ Tripulante
+ Pasajero
+ TorreControl

El programa utiliza un framework llamado streamlit por eso en muchos de los archivos se puede ver que en las cabezeras se hace un ´import streamlit as st´
En la opcion de consultar informacion sobre los paises se hace el uso de una API y se ultilizan librerias como json y request para conectarse al servidos en linea

### Como compilarlo
El programa utiliza un framework llamado streamlit que debe estar instalado en la maquina del usuario para poder 
ejecutar el programa. Para compilar el programa tendra que:

+ Abrir la terminal de su maquina y navegar hasta la carpeta donde se encuentra ubicado el codigo
+ Escribir lo siguiente `streamlit run main.py` y presionar la tecla enter

Esto deberia cargar un host local en su maquina y usted deberia ser capaz de ver el programa funcionando.

### Imagenes 
## Inicio 
![Inicio](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/35f0dde9-235e-4e7b-8c42-cd8e56fffda8)

## Menu principal
![Menú](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/5b6a1817-9074-423d-bfa4-3799719aa105)

## Creacion de objetos
![Creacion de diferentes objetos](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/64b5f3a7-c9e1-4c76-b2a3-30e3575e732e)
![Creacion de un avión](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/0d249c76-5262-47b9-b9ec-da4199d54a1e)

## Informacion general
![La informacion de los objetos en el sistema](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/3e354522-5911-4e5c-a948-1ba1f2e8b49f)


## Reserva de un vuelo 
![y creacion de un pasajero](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/25cf6576-11b0-4294-bb1b-dc5ed79904d4)

## Mostrar estados
![visualiza y cambia los estados de las aeronaves](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/633bc98a-aff6-4079-b9c1-4d184aa1f7f9)

## Informacion de los paises
![consulta informacion de cualquier pais](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/523d4b3b-0160-43d7-a80b-bfffa769a022)

## Asignar vuelos
![Asigna un vuelo a una aeronave](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/bce67d57-90e7-4349-b720-278acb39092c)

## Asignar puertas 
![Asigna una puerta a una aeronave](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/28eda124-368a-49de-a22c-d094e263ab42)

## Despegar
![Simulador de despegue](https://github.com/samuelinchis/POO-Proyecto-2/assets/110745715/2952f6df-f5a5-48e7-8061-34ae387fc991)

***Gracias por haber leido el readme. Esperamos que este manual tecnico haya sido de ayuda***
:+1:

