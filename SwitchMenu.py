def one():
    print("Falta implementar")

def two():
    print("Falta implementar")

def three():
    print("Falta implementar")

def four():
    print("Falta implementar")

def five():
    print("Falta implementar")

def six():
    print("Falta implementar")

def seven():
    print("Falta implementar")

def eight():
    print("Falta implementar")

def nine():
    print("Falta implementar")

def ten():
    print("Falta implementar")

def eleven():
    print("Falta implementar")

def twelve():
    print("Falta implementar")

def thirteen():
    print("Falta implementar")


def menuSelect(menuInput):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve,
        13: thirteen
    }

    func = switcher.get(menuInput, "default")

    func()

print ("Seleciona la opción del menu..\n")
menuInput = input()

menuSelect(int(menuInput))
print("despues del menu")

