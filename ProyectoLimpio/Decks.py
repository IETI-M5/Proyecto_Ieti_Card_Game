#<<<<<EN ESTE FICHERO ESTAN LAS FUNCIONES PARA CARGAR BARAJAS Y GENERAR MAZOS>>>>>

import xml.etree.ElementTree as ET


cartasCargadasA = False
cartasCargadasB = False


#--------------------------------------
#---CARGAR CARTAS ALIADAS Y ENEMIGAS---
#--------------------------------------

def cargarCartasA():

    global cartasCargadasA
    global barajaA

    try:
        barajaA = ET.ElementTree(file = ("myBaraja.xml"))
        print("Baraja aliada cargada correctamente!\n")
        cartasCargadasA = True
        return
    except FileNotFoundError:
        print("Fichero no valido... Asegurese de que el fichero se llame (myBaraja.xml) y se encuentre en la carpeta del juego...\n")
    return


def cargarCartasB():

    global cartasCargadasB
    global barajaB

    try:
        barajaB = ET.ElementTree(file="Enemigo.xml")
        print("Baraja enemiga cargada correctamente!\n")
        cartasCargadasB = True
        return
    except FileNotFoundError:
        print("Fichero no valido... Asegurese de que el fichero se llame (Enemigo.xml) y se encuentre en la carpeta del juego...\n")
    return


#---------------------------
#---GENERAR MAZOS ALIADOS---
#---------------------------

def crearMazoAliadoOf():
    print("falta implementar")

def crearMazoAliadoDef():
    print("falta implementar")

def crearMazoAliadoEq():
    print("falta implementar")

def crearMazoAliadoRan():
    print("falta implementar")


#----------------------------
#---GENERAR MAZOS ENEMIGOS---
#----------------------------

def crearMazoEnemigoOf():
    print("falta implementar")

def crearMazoEnemigoDef():
    print("falta implementar")

def crearMazoEnemigoEq():
    print("falta implementar")

def crearMazoEnemigoRan():
    print("falta implementar")