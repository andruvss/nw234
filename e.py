#ser el mejor programador del mundo 
import os, csv, time 
from funciones import *

list = []

#menu

while True:
    os.system('cls')
    print("1. Registrar nueva venta")
    print("2. Reporte de ventas historico")
    print("3. Reporte de ventas por producto")
    print("4. Reporte de formas de pago")
    print("5. Salir")
    opc = int(input("Ingrese una opcion: "))
    os.system('cls')

    if opc ==1:
        funcion_opc1()
    elif opc ==2:
        pass
    elif opc ==3:
        pass
    elif opc ==4:
        pass
    else:
        print("ADIOS!")
        time.sleep(3)



