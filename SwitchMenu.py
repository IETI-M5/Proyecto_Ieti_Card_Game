import xml.etree.ElementTree as ET

print("inicio")
cartasCargadas = False
cartasEnemigo = False
dentroMenu = True


def one():
    global cartasCargadas
    cartasCargadas = False
    try:
        baraja = ET.ElementTree(file="myBaraja.xml")
        print("Baraja cargada correctamente!\n")
        cartasCargadas = True
        return baraja
    except FileNotFoundError:
        print("Fichero no valido... Asegurese de que el fichero se llame (myBaraja.xml) y se encuentre en la carpeta del juego...\n")
    return

def two():
    global cartasEnemigo
    cartasEnemigo = False
    try:
        enemigo = ET.ElementTree(file="Enemigo.xml")
        print("Baraja cargada correctamente!\n")
        cartasEnemigo = True
        return enemigo
    except FileNotFoundError:
        print(
            "Fichero no valido... Asegurese de que el fichero se llame (Enemigo.xml) y se encuentre en la carpeta del juego...\n")
    return

def three():
    print("Falta implementar")

def four():
    print("Falta implementar")

def five():
    print("Falta implementar")

def menuSelect(menuInput):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
    }

    func = switcher.get(menuInput, "default")
    func()

#MENU DE SELECCION

while dentroMenu:
    print("----------MENU DEL JUEGO----------")
    print(" 1.- Cargar cartas")
    print(" 2.- Cargar cartas Enemigo")
    if cartasCargadas:
        print(" 3.- Otras Opciones")
        print(" 4.- Muchas otras Opciones")
    if cartasEnemigo:
        print(" 5.- Luchar Jugador VS Jugador")
    print("----------------------------------")
    menuInput = input("Introduce una opción: ")
    menuSelect(int(menuInput))
