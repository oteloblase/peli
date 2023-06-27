datos_personales=[]
pelicula=["LA TEORIA DEL TODO"]
asientos=[["[.]"]*15 for _ in range (10)]
def mostrar_asiento():
    for fila in asientos:
        print(*fila, sep=" ", end="\n")
def seleccion_asiento():
    asiento=input("seleccione cual asiento desea")
    fila_elegida,columna_elegida=map(int,asiento.split(","))
    asiento[fila_elegida -1][columna_elegida -1]="X"
def alumn_duoc():
    alumno=input(
        print("si usted alumno de duoc por favor digite el numero [1] y si no lo es digite el numero [2]")
    )
    if alumno == 1:
        print("se le aplicara un descuento por ser la institucion")
    elif alumno == 2:
        print("se le cobrara la cantidad completa")

  
    def menu():
    
        print("__________________________________________")
        print("[1] ver peliculas en cartelera____________")
        print("[2] ver asientos disponibles______________")
        print("[3] salir_________________________________")
    menu()
    opc=input("seleccione una opcion")

    if opc == 1:
        print("por el mmento solo tenemos disponible: ",(pelicula))
    elif opc == 2:
        mostrar_asiento()
        seleccion=input("desea comprar un asiento? [1] si [2] no")
        if seleccion == 1:
            seleccion_asiento()
            alumn_duoc()
        elif seleccion == 2:
            menu()
    elif opc == 3:
        exit()



