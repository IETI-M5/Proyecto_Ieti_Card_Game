import xml.etree.ElementTree as ET

print("inicio")
cartasCargadas = False
cartasEnemigo = False
dentroMenu = True


def one():
    ## Carga el mazo "myBaraja.xml", el fichero debe estar en la raiz del programa y obligatoriamente tiene que llamarse asi, si
    ## no es valido o no esta nos avisara y volvera al menu principal

    ## Una vez cargado el mazo activara el booleano "cartasCargadas" para habilitar las nuevas opciones del menu

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

    ## Carga el mazo "Enemigo.xml", el fichero debe estar en la raiz del programa y obligatoriamente tiene que llamarse asi, si
    ## no es valido o no esta nos avisara y volvera al menu principal

    ## Una vez cargado el mazo activara el booleano "cartasEnemigo" para habilitar las nuevas opciones del menu

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

    ## Menu para crear mazo, depende de los booleanos "cartasCargadas" y "cartasEnemigo" para activarse y funcionar, si estos no estan
    ## activados a la hora de introducir "3" en el menu saldra "Opcion no valida..."

    ## En este menu te da la opcion de crear mazos Ofensivos, Defensivos, Equilibrados o Aleatorios, una vez escogida la opcion te pide
    ## si sera para el jugador o el enemigo.

    global usarEnemigo
    preguntaMazo = False
    global cartasCargadas
    global cartasEnemigo

    if cartasCargadas | cartasEnemigo:
       print("--------- CREAR MAZO ---------")
       print(" 1. Crear mazo Ofensivo")
       print(" 2. Crear mazo Defensivo")
       print(" 3. Crear mazo Equilibrado")
       print(" 4. Crear mazo Aleatorio")
       print("----------------------------------")
       menuInput = input("Introduce una opción: ")
       print("----------------------------------")
       while not preguntaMazo:
           randomMazo = input("Quieres usar el mazo Enemigo? ")
           if randomMazo.lower() == 'si':
               usarEnemigo = True
               preguntaMazo = True
           elif randomMazo.lower() == 'no':
               usarEnemigo = False
               preguntaMazo = True
           else:
               print("Opcion no valida...\n")
    else:
       print("Opcion no valida...\n")

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
    print("--------- MENU DEL JUEGO ---------")
    print(" 1.- Cargar cartas")
    print(" 2.- Cargar cartas Enemigo")
    if cartasCargadas | cartasEnemigo:
        print(" 3.- Crear mazo")
    if cartasEnemigo & cartasCargadas:
        print(" 4.- Luchar Jugador VS Jugador")
    print("----------------------------------")
    menuInput = input("Introduce una opción: ")
    if menuInput.isnumeric():
        menuSelect(int(menuInput))
