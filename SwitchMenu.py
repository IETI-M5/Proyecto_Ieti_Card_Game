import xml.etree.ElementTree as ET

cartasCargadas = False
cartasEnemigo = False
dentroMenu = True

def cargarCartas():

    # Carga el mazo "myBaraja.xml", el fichero debe estar en la raiz del programa y obligatoriamente tiene que llamarse asi, si
    # no es valido o no esta nos avisara y volvera al menu principal

    # Una vez cargado el mazo activara el booleano "cartasCargadas" para habilitar las nuevas opciones del menu

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

def cargarEnemigo():

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

def menuMazo():

    ## Menu para crear mazo, depende de los booleanos "cartasCargadas" o "cartasEnemigo" para activarse y funcionar, si uno no esta
    ## activados a la hora de introducir "3" en el menu saldra "Opcion no valida..."

    ## En este menu te da la opcion de crear mazos Ofensivos, Defensivos, Equilibrados o Aleatorios, una vez escogida la opcion te pide
    ## si sera para el jugador o el enemigo.

    global usarEnemigo
    preguntaMazo = False
    global cartasCargadas
    global cartasEnemigo

    if cartasCargadas | cartasEnemigo:
       print("----------- CREAR MAZO -----------")
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

def menuLucha():

    ## Menu para luchar, este tendra las opciones de luchar contra bots y luchar contra bots en modo liga,
    ## para poder luchar contra otro jugador (Enemigo.xml) antes debe haberse cargado las cartas del Enemigo

    ## Antes de acceder al menu, el boolean "cartasCargadas" ha de estar habilitado, de el depende ya que sin las
    ## cartas del jugador no podria ni luchar contra el bot ni contra otro jugador, si esta deshabilitado saldra el
    ## error "Opcion no valida...", porque habra introducido una opcion que aun no estaba habilitada ni se mostraba por
    ## pantalla.

    global cartasCargadas
    global cartasEnemigo

    if cartasCargadas:
        print("------------- LUCHAR -------------")
        print(" 1. Jugador VS Bot")
        print(" 2. Jugador VS Bot (Liga)")
        if cartasEnemigo:
            print(" 3. Jugador VS Jugador")
        print("----------------------------------")
        menuInput = input("Introduce una opción: ")
        print("----------------------------------")
    else:
        print("Opcion no valida...\n")
def menuSelect(menuInput):

    ## Funcion para el SWITCH del MENU PRINCIPAL, segun el valor introducido en "menuInput" accedera a la funcion asignada
    ## en el SWITCH.

    switcher = {
        1: cargarCartas,
        2: cargarEnemigo,
        3: menuMazo,
        4: menuLucha,
    }
    return switcher.get(menuInput, "Opcion no valida...\n")

    func = switcher.get(menuInput, "default")
    func()

while dentroMenu:

    ## MENU PRINCIPAL ##

    ## Muestra por pantalla las opciones del menu principal del juego, al principio solo 2 opciones estaran habilitadas,
    ## (Cargar cartas / Cargar cartas Enemigo), el usuario habra de acceder a una de las 2 para empezar y estas haran sus
    ## operaciones correponientes. Cuando las cartas esten cargadas correctamente, tanto las del usuario o las del enemigo
    ## habilitara el boolean "cargarCartas" o "cargarEnemigo".

    ## Para habilitar la opcion 3, uno de los boolean ha de estar habilitado, asi el juego nos permite ya crear mazos con
    ## solo haber cargado una baraja, esta accedera a un submenu.

    ## Para habilitar la opcion 4, con solo tener el boolean "cargarCartas" habilitado nos dejara acceder al submenu de lucha
    ## pero si el boolean "cargarEnemigo" no esta habilitado solo estaran habilitadas unas opciones
    ## en concreto del submenu lucha <--- // POR IMPLEMENTAR

    ## El menu comprobara si el valor introducido es un numero con "menuInput.isnumeric()", en caso de que no lo sea
    ## imprimira por pantalla "Opcion no valida..."

    print("--------- MENU DEL JUEGO ---------")
    print(" 1.- Cargar cartas")
    print(" 2.- Cargar cartas Enemigo")
    if cartasCargadas | cartasEnemigo:
        print(" 3.- Crear mazo")
    if cartasCargadas:
        print(" 4.- Luchar Jugador VS Jugador")
    print("----------------------------------")
    menuInput = input("Introduce una opción: ")
    if menuInput.isnumeric():
        menuSelect(int(menuInput))
    else:
        print("Opcion no valida...\n")
