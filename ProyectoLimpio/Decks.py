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

    import xml.etree.ElementTree as ET

    global barajaA
    root = barajaA.getroot()

    mazoA = []

    class Carta:
        def __init__(self, name, attack, defense, description):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.description = description

    def cardSelect():
        cont = 0
        value = 5
        global p1

        while True:
            if value < 0:
                return
            for child in root.findall('.//deck/'):
                for cardChild in child.getchildren():
                    if cont == 10:
                        return
                    if cardChild.tag == "name":
                        name = cardChild.text
                    if cardChild.tag == "attack":
                        attack = int(cardChild.text)
                    if cardChild.tag == "defense":
                        defense = int(cardChild.text)
                    if cardChild.tag == "description":
                        description = cardChild.text
                if attack == value:
                    mazoA.append(Carta(name, attack, defense, description))
                    cont = cont + 1

            value = value - 1

    cardSelect()

    for i in range(10):
        print(mazoA[i].name + " " + str(mazoA[i].attack) + " " + str(mazoA[i].defense))
        print(str(mazoA[i].description))
        print()



def crearMazoAliadoDef():
    import xml.etree.ElementTree as ET

    global barajaA
    root = barajaA.getroot()

    mazoA = []

    class Carta:
        def __init__(self, name, attack, defense, description):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.description = description

    def cardSelect():
        cont = 0
        value = 5
        global p1

        while True:
            if value < 0:
                return
            for child in root.findall('.//deck/'):
                for cardChild in child.getchildren():
                    if cont == 10:
                        return
                    if cardChild.tag == "name":
                        name = cardChild.text
                    if cardChild.tag == "attack":
                        attack = int(cardChild.text)
                    if cardChild.tag == "defense":
                        defense = int(cardChild.text)
                    if cardChild.tag == "description":
                        description = cardChild.text
                if defense == value:
                    mazoA.append(Carta(name, attack, defense, description))
                    cont = cont + 1

            value = value - 1

    cardSelect()

    for i in range(10):
        print(mazoA[i].name + " " + str(mazoA[i].attack) + " " + str(mazoA[i].defense))
        print(str(mazoA[i].description))
        print()

def crearMazoAliadoEq():

    import xml.etree.ElementTree as ET

    global barajaA
    root = barajaA.getroot()

    ## ordenarXML(root, 'attack')

    mazoA = []

    class Carta:
        def __init__(self, name, attack, defense, description):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.description = description

    def cardSelect():
        cont = 0
        value = 0
        global p1

        while True:
            if value > 5:
                return
            for child in root.findall('.//deck/'):
                for cardChild in child.getchildren():
                    if cont == 10:
                        return
                    if cardChild.tag == "name":
                        name = cardChild.text
                    if cardChild.tag == "attack":
                        attack = int(cardChild.text)
                    if cardChild.tag == "defense":
                        defense = int(cardChild.text)
                    if cardChild.tag == "description":
                        description = cardChild.text
                if abs(attack) - abs(defense) == value:
                    mazoA.append(Carta(name, attack, defense, description))
                    cont = cont + 1

            value = value + 1

    cardSelect()

    for i in range(10):
        print(mazoA[i].name + " " + str(mazoA[i].attack) + " " + str(mazoA[i].defense))
        print(str(mazoA[i].description))
        print()



def crearMazoAliadoRan():
    import xml.etree.ElementTree as ET
    import random

    global barajaA
    root = barajaA.getroot()

    ## Modulo para conseguir array de numeros aleatorios

    def numU(x, L):
        esUnico = True
        for i in range(len(L)):
            if x == L[i]:
                esUnico = False
                break
        return esUnico

    L = []
    j = 0

    while j < 10:
        x = random.randint(1, 20)
        if numU(x, L):
            L.append(x)
            j += 1

    L.sort()

    mazoA = []

    class Carta:
        def __init__(self, name, attack, defense, description):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.description = description

    def cardSelect():
        cont = 0
        value = L[0]
        global p1
        posRandom = 1

        arrayNum = [10]

        while True:
            if posRandom > 20:
                return
            for child in root.findall('.//deck/'):
                for cardChild in child.getchildren():
                    if cont == 10:
                        return
                    if cardChild.tag == "name":
                        name = cardChild.text
                    if cardChild.tag == "attack":
                        attack = int(cardChild.text)
                    if cardChild.tag == "defense":
                        defense = int(cardChild.text)
                    if cardChild.tag == "description":
                        description = cardChild.text
                ## print(cont)
                if posRandom == value:
                    mazoA.append(Carta(name, attack, defense, description))
                    cont = cont + 1
                    if cont != 10:
                        value = L[cont]
                    else:
                        return
                    posRandom = 1
                    break
                posRandom = posRandom + 1
            ##  print(posRandom)

    cardSelect()

    for i in range(10):
        print(mazoA[i].name + " " + str(mazoA[i].attack) + " " + str(mazoA[i].defense))
        print(str(mazoA[i].description))
        print()



#----------------------------
#---GENERAR MAZOS ENEMIGOS---
#----------------------------

def crearMazoEnemigoOf():

    import xml.etree.ElementTree as ET

    global barajaB
    root = barajaB.getroot()

    mazoB = []

    class Carta:
        def __init__(self, name, attack, defense, description):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.description = description

    def cardSelect():
        cont = 0
        value = 5
        global p1

        while True:
            if value < 0:
                return
            for child in root.findall('.//deck/'):
                for cardChild in child.getchildren():
                    if cont == 10:
                        return
                    if cardChild.tag == "name":
                        name = cardChild.text
                    if cardChild.tag == "attack":
                        attack = int(cardChild.text)
                    if cardChild.tag == "defense":
                        defense = int(cardChild.text)
                    if cardChild.tag == "description":
                        description = cardChild.text
                if attack == value:
                    mazoB.append(Carta(name, attack, defense, description))
                    cont = cont + 1

            value = value - 1

    cardSelect()

    for i in range(10):
        print(mazoB[i].name + " " + str(mazoB[i].attack) + " " + str(mazoB[i].defense))
        print(str(mazoB[i].description))
        print()

def crearMazoEnemigoDef():
    import xml.etree.ElementTree as ET

    global barajaB
    root = barajaB.getroot()

    mazoB = []

    class Carta:
        def __init__(self, name, attack, defense, description):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.description = description

    def cardSelect():
        cont = 0
        value = 5
        global p1

        while True:
            if value < 0:
                return
            for child in root.findall('.//deck/'):
                for cardChild in child.getchildren():
                    if cont == 10:
                        return
                    if cardChild.tag == "name":
                        name = cardChild.text
                    if cardChild.tag == "attack":
                        attack = int(cardChild.text)
                    if cardChild.tag == "defense":
                        defense = int(cardChild.text)
                    if cardChild.tag == "description":
                        description = cardChild.text
                if defense == value:
                    mazoB.append(Carta(name, attack, defense, description))
                    cont = cont + 1

            value = value - 1

    cardSelect()

    for i in range(10):
        print(mazoB[i].name + " " + str(mazoB[i].attack) + " " + str(mazoB[i].defense))
        print(str(mazoB[i].description))
        print()

def crearMazoEnemigoEq():
    import xml.etree.ElementTree as ET

    global barajaB
    root = barajaB.getroot()

    ## ordenarXML(root, 'attack')

    mazoB = []

    class Carta:
        def __init__(self, name, attack, defense, description):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.description = description

    def cardSelect():
        cont = 0
        value = 0
        global p1

        while True:
            if value > 5:
                return
            for child in root.findall('.//deck/'):
                for cardChild in child.getchildren():
                    if cont == 10:
                        return
                    if cardChild.tag == "name":
                        name = cardChild.text
                    if cardChild.tag == "attack":
                        attack = int(cardChild.text)
                    if cardChild.tag == "defense":
                        defense = int(cardChild.text)
                    if cardChild.tag == "description":
                        description = cardChild.text
                if abs(attack) - abs(defense) == value:
                    mazoB.append(Carta(name, attack, defense, description))
                    cont = cont + 1

            value = value + 1

    cardSelect()

    for i in range(10):
        print(mazoB[i].name + " " + str(mazoB[i].attack) + " " + str(mazoB[i].defense))
        print(str(mazoB[i].description))
        print()


def crearMazoEnemigoRan():
    import xml.etree.ElementTree as ET
    import random

    global barajaB
    root = barajaB.getroot()

    ## Modulo para conseguir array de numeros aleatorios

    def numU(x, L):
        esUnico = True
        for i in range(len(L)):
            if x == L[i]:
                esUnico = False
                break
        return esUnico

    L = []
    j = 0

    while j < 10:
        x = random.randint(1, 20)
        if numU(x, L):
            L.append(x)
            j += 1

    L.sort()

    mazoB = []

    class Carta:
        def __init__(self, name, attack, defense, description):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.description = description

    def cardSelect():
        cont = 0
        value = L[0]
        global p1
        posRandom = 1

        arrayNum = [10]

        while True:
            if posRandom > 20:
                return
            for child in root.findall('.//deck/'):
                for cardChild in child.getchildren():
                    if cont == 10:
                        return
                    if cardChild.tag == "name":
                        name = cardChild.text
                    if cardChild.tag == "attack":
                        attack = int(cardChild.text)
                    if cardChild.tag == "defense":
                        defense = int(cardChild.text)
                    if cardChild.tag == "description":
                        description = cardChild.text
                ## print(cont)
                if posRandom == value:
                    mazoB.append(Carta(name, attack, defense, description))
                    cont = cont + 1
                    if cont != 10:
                        value = L[cont]
                    else:
                        return
                    posRandom = 1
                    break
                posRandom = posRandom + 1
            ##  print(posRandom)

    cardSelect()

    for i in range(10):
        print(mazoB[i].name + " " + str(mazoB[i].attack) + " " + str(mazoB[i].defense))
        print(str(mazoB[i].description))
        print()
