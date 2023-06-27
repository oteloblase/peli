datos_personales=[]
pelicula=["LA TEORIA DEL TODO"]
asiento=[["[.]"]*15 for _ in range (10)]

def mostrar_asiento():
    for fila in asiento:
        print(*fila, sep=" ", end="\n")

def seleccion_asiento():
    cual_asiento=input("seleccione cual asiento desea")
    fila_elegida,columna_elegida=map(int,seleccion_asiento.split(","))
    cual_asiento=[fila_elegida -1][columna_elegida -1]="X"

def registrar_datos():
    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    correo = input("ingrese su correo: ")
    datos_personales.append([nombre, edad, correo])

def menu():
    print("__________________________________________")
    print("[1] ver peliculas en cartelera____________")
    print("[2] ver asientos disponibles______________")
    print("[3] salir_________________________________")

def alumn_duoc():
    alumno=input(
        print("si usted alumno de duoc por favor digite el numero [1] y si no lo es digite el numero [2]")
    )
    if alumno == 1:
        print("se le aplicara un descuento por ser la institucion")
    elif alumno == 2:
        print("se le cobrara la cantidad completa")

       

    opc=int(input("escoga una de las 3 opciones para continuar \n"))
    if opc == 1:
        print("por el momento solo tenemos en cartelera la pelicula: ",(pelicula))
    elif opc == 2:
       print("estos son lo asientos disponibles",(mostrar_asiento))
  