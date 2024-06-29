



preciototal = 0 


import os


def funcion_opc1():
    os.system('cls')
    nombre_del_producto = input("Ingrese el nombre del producto")
    cantidad_de_productos = int(input("Ingrese la cantidad de productos que desea ingresar:"))
    Valor_unitario = int(input("Ingrese el valor unitario del producto: "))
    while True:
            print("1. Efectivo: ")
            print("2. Tarjeta de debito: ")
            print("3. Tarjeta de credito: ")
            print("4. Transeferencia electronica: ")
            mediodepago = int(input("Escoja el medio de pago: "))
            if mediodepago ==1:
                totaldesucompra = Valor_unitario*cantidad_de_productos
                print(f"Su total a pagar es de: ",totaldesucompra)
                dineroefectivo = int(input("Ingrese monto a pagar: "))
                total = dineroefectivo-totaldesucompra
                print(" ")




            
