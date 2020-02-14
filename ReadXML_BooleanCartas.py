import xml.etree.ElementTree as ET

cartasCargadas = False

## WHILE con BOOLEAN para introducir la ruta de nuestra baraja, hasta que la ruta del fichero no sea valida y exista
## no saldra del WHILE

while not cartasCargadas:
    ruta = input("Ruta de la baraja: ")
    try:
        tree = ET.ElementTree(file=ruta)
        cartasCargadas = True
    except FileNotFoundError:
        print("Fitxer no valid...\n")

## FOR para recorrer las etiquetas de nuestro XML desde la raiz

for child in root:
    print (child.tag, child.attrib)
    for child in child:
        print("\t"+child.tag, child.attrib)
