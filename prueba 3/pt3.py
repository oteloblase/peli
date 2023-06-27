
lista_asiento = [["[.]"]*15 for _ in range (10)]
lista_pelicula =[ "los increibles"]
valor_entrada = 2500
def asientos():
    for fila in lista_asiento:
        print(*fila, sep=" ", end="\n")
    seleccionar_asiento = input("seleccione el asiento que desea")
    fila_elegida,columna_elegida=map(int,seleccionar_asiento.split(","))
    lista_asiento[fila_elegida -1][columna_elegida -1]= "X"

def menu():
    print("__________________________________________")
    print("[1] ver peliculas en cartelera____________")
    print("[2] ver asientos disponibles______________")
    print("[3] salir_________________________________")
menu()
opc=input("seleccione una opcion")

if opc == 1:
        print("por el mmento solo tenemos disponible: ",(lista_pelicula))
elif opc == 2:
    asientos()
