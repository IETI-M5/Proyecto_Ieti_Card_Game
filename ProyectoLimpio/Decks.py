#<<<<<EN ESTE FICHERO ESTAN LAS FUNCIONES PARA CARGAR BARAJAS Y GENERAR MAZOS>>>>>

import xml.etree.ElementTree as ET
import random


cartasCargadasA = False
cartasCargadasB = False

mazoA = []
mazoB = []

class Carta:
    def __init__(self, summonPoints, typeClass, name, attack, defense):
        self.summonPoints = summonPoints
        self.typeClass = typeClass
        self.name = name
        self.attack = attack
        self.defense = defense


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

    global barajaA
    root = barajaA.getroot()
    cont = 0

    print("\n-----------------------------\nMazo ofensivo generado:\n-----------------------------")
    for value in range (5, 0, -1):
        for card in root.findall('deck/card[attack="'+str(value)+'"]'):
            summonPoints = int(card.attrib['summonPoints'])
            typeClass = card.attrib['type']
            name = card.find("name").text
            attack = card.find("attack").text
            defense = card.find("defense").text

            print (name, attack+"/"+defense)
            mazoA.append(Carta(summonPoints, typeClass, name, attack, defense))
            cont = cont+1
            if cont == 10:
                return
        

def crearMazoAliadoDef():
    global barajaA
    root = barajaA.getroot()
    cont = 0

    print("\n-----------------------------\nMazo defensivo generado:\n-----------------------------")
    for value in range (5, 0, -1):
        for card in root.findall('deck/card[defense="'+str(value)+'"]'):
            summonPoints = int(card.attrib['summonPoints'])
            typeClass = card.attrib['type']
            name = card.find("name").text
            attack = card.find("attack").text
            defense = card.find("defense").text

            print (name, attack+"/"+defense)
            mazoA.append(Carta(summonPoints, typeClass, name, attack, defense))
            cont = cont+1
            if cont == 10:
                return

def crearMazoAliadoEq():

    global barajaA
    root = barajaA.getroot()
    cont = 0

    print("\n-----------------------------\nMazo equilibrado generado:\n-----------------------------")
    for value in range (0, 5, 1):
        for card in root.findall('deck/card'):
            #Si el valor absoluto de la diferencia entre ataque y defensa es igual al valor que utilizamos en el for guardamos la carta, empezando desde 0 hasta llegar a 5.
            if abs( int(card.find("attack").text) - int(card.find("defense").text)) == value:
                summonPoints = int(card.attrib['summonPoints'])
                typeClass = card.attrib['type']
                name = card.find("name").text
                attack = card.find("attack").text
                defense = card.find("defense").text

                print (name, attack+"/"+defense)
                mazoA.append(Carta(summonPoints, typeClass, name, attack, defense))
                cont = cont+1
                if cont == 10:
                    return


def crearMazoAliadoRan():

    global barajaA
    root = barajaA.getroot()

    cont = 0

    #variable i como iterador que va contando por cada carta que pasa, y variable j para la posicion de la array aleatoria
    #Si coincide la variable i, con en contenido de la array en la posicion j, guardara la carta.
    i = 1
    j = 0

    #genera una array de 10 posiciones con numeros aleatorios entre el 1 y el 20 y la ordena.
    randChoices = (random.sample(range(1, 21),10))
    randChoices.sort()

    print("\n-----------------------------\nMazo aleatorio generado:\n-----------------------------")
    for card in root.findall('deck/card'):
        if i == randChoices[j]:
            summonPoints = int(card.attrib['summonPoints'])
            typeClass = card.attrib['type']
            name = card.find("name").text
            attack = card.find("attack").text
            defense = card.find("defense").text

            print (name, attack+"/"+defense)
            mazoA.append(Carta(summonPoints, typeClass, name, attack, defense))
            cont = cont+1
            j = j+1
            if cont == 10 or j==10:
                return
        i=i+1



#----------------------------
#---GENERAR MAZOS ENEMIGOS---
#----------------------------

def crearMazoEnemigoOf():

    global barajaB
    root = barajaB.getroot()
    cont = 0

    print("\n-----------------------------\nMazo ofensivo generado:\n-----------------------------")
    for value in range (5, 0, -1):
        for card in root.findall('deck/card[attack="'+str(value)+'"]'):
            summonPoints = int(card.attrib['summonPoints'])
            typeClass = card.attrib['type']
            name = card.find("name").text
            attack = card.find("attack").text
            defense = card.find("defense").text

            print (name, attack+"/"+defense)
            mazoB.append(Carta(summonPoints, typeClass, name, attack, defense))
            cont = cont+1
            if cont == 10:
                return

def crearMazoEnemigoDef():

    global barajaB
    root = barajaB.getroot()
    cont = 0

    print("\n-----------------------------\nMazo defensivo generado:\n-----------------------------")
    for value in range (5, 0, -1):
        for card in root.findall('deck/card[defense="'+str(value)+'"]'):
            summonPoints = int(card.attrib['summonPoints'])
            typeClass = card.attrib['type']
            name = card.find("name").text
            attack = card.find("attack").text
            defense = card.find("defense").text

            print (name, attack+"/"+defense)
            mazoB.append(Carta(summonPoints, typeClass, name, attack, defense))
            cont = cont+1
            if cont == 10:
                return


def crearMazoEnemigoEq():

    global barajaB
    root = barajaB.getroot()

    cont = 0

    print("\n-----------------------------\nMazo equilibrado generado:\n-----------------------------")
    for value in range (0, 5, 1):
        for card in root.findall('deck/card'):
            #Si el valor absoluto de la diferencia entre ataque y defensa es igual al valor que utilizamos en el for guardamos la carta, empezando desde 0 hasta llegar a 5.
            if abs( int(card.find("attack").text) - int(card.find("defense").text)) == value:
                summonPoints = int(card.attrib['summonPoints'])
                typeClass = card.attrib['type']
                name = card.find("name").text
                attack = card.find("attack").text
                defense = card.find("defense").text

                print (name, attack+"/"+defense)
                mazoB.append(Carta(summonPoints, typeClass, name, attack, defense))
                cont = cont+1
                if cont == 10:
                    return


def crearMazoEnemigoRan():

    global barajaB
    root = barajaB.getroot()

    cont = 0

    #variable i como iterador que va contando por cada carta que pasa, y variable j para la posicion de la array aleatoria
    #Si coincide la variable i, con en contenido de la array en la posicion j, guardara la carta.
    i = 1
    j = 0

    #genera una array de 10 posiciones con numeros aleatorios entre el 1 y el 20 y la ordena.
    randChoices = (random.sample(range(1, 21),10))
    randChoices.sort()

    print("\n-----------------------------\nMazo aleatorio generado:\n-----------------------------")
    for card in root.findall('deck/card'):
        if i == randChoices[j]:
            summonPoints = int(card.attrib['summonPoints'])
            typeClass = card.attrib['type']
            name = card.find("name").text
            attack = card.find("attack").text
            defense = card.find("defense").text

            print (name, attack+"/"+defense)
            mazoB.append(Carta(summonPoints, typeClass, name, attack, defense))
            cont = cont+1
            j = j+1
            if cont == 10 or j==10:
                return
        i=i+1
