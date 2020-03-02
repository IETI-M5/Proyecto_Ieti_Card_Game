#<<<<<EN ESTE FICHERO ESTAN LOS MENUS Y LAS LLAMADAS A LAS FUNCIONES DE OTROS FICHEROS>>>>>

import Decks
import Fight
dentroMenu = True

#Switcher para todas las opciones del menu
def menuSelect(menuInput):

    switcher = {
        1: Decks.cargarCartasA,
        2: Decks.cargarCartasB,
        3: menuCrearMazoA,
        4: menuCrearMazoB,
        5: menuLucha,
        11: Decks.crearMazoAliadoOf,
        12: Decks.crearMazoAliadoDef,
        13: Decks.crearMazoAliadoEq,
        14: Decks.crearMazoAliadoRan,
        21: Decks.crearMazoEnemigoOf,
        22: Decks.crearMazoEnemigoDef,
        23: Decks.crearMazoEnemigoEq,
        24: Decks.crearMazoEnemigoRan,
        31: Fight.arcade,
        32: Fight.liga,
        33: Fight.pvp
    }

    func = switcher.get(menuInput, "default")
    func()


#---------------------------
#----------SUBMENUS---------
#---------------------------
# (estos se desbloquean cuando cargamos barajas, creamos mazos..)


def menuCrearMazoA():

    print("-------- CREAR MAZO ALIADO --------")
    print(" 1. Crear mazo Ofensivo")
    print(" 2. Crear mazo Defensivo")
    print(" 3. Crear mazo Equilibrado")
    print(" 4. Crear mazo Aleatorio")
    print(" 5. Atras")
    print("----------------------------------")
    menuInput = int(input("Introduce una opción: "))
    if (menuInput==5):
        return
    #Le sumo 10 para poder seguir usando el mismo switcher con diferentes menus, asi no me coincide con las opciones anteriores.
    menuInput = menuInput+10
    menuSelect(menuInput)
    print("----------------------------------")


def menuCrearMazoB():

    print("-------- CREAR MAZO ENEMIGO --------")
    print(" 1. Crear mazo Ofensivo")
    print(" 2. Crear mazo Defensivo")
    print(" 3. Crear mazo Equilibrado")
    print(" 4. Crear mazo Aleatorio")
    print(" 5. Atras")
    print("----------------------------------")
    menuInput = int(input("Introduce una opción: "))
    if (menuInput==5):
        return
    #Le sumo 20 para poder seguir usando el mismo switcher con diferentes menus, asi no me coincide con las opciones anteriores.
    menuInput = menuInput+20
    menuSelect(menuInput)
    print("----------------------------------")


def menuLucha():
    print("------------- LUCHAR -------------")
    print(" 1. Jugador VS Bot")
    print(" 2. Jugador VS Bot (Liga)")
    if Decks.cartasCargadasB:
        print(" 3. Jugador VS Jugador")
    print(" 4. Atras")
    print("----------------------------------")
    menuInput = int(input("Introduce una opción: "))
    if (menuInput==4):
        return
    #Le sumo 30 para poder seguir usando el mismo switcher con diferentes menus, asi no me coincide con las opciones anteriores.
    menuInput = menuInput+30
    menuSelect(menuInput)
    print("----------------------------------")


#---------------------------
#------------MAIN-----------
#---------------------------
while dentroMenu:

    print("\n--------- MENU DEL JUEGO ---------")
    print(" 1.- Cargar cartas aliadas")
    print(" 2.- Cargar cartas enemigas")
    if Decks.cartasCargadasA:
        print(" 3.- Crear mazo aliado")
    if Decks.cartasCargadasB:
        print(" 4.- Crear mazo enemigo")
    if Decks.cartasCargadasA:
        print(" 5.- Luchar")
    print("----------------------------------")
    menuInput = input("Introduce una opción: ")
    if menuInput.isnumeric():
        menuSelect(int(menuInput))
    else:
        print("Opcion no valida...\n")
