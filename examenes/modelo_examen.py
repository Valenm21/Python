productos = []

def cargar_productos ():
    seguir = True
    while seguir:
        seguir = input ("¿Desea cargar un producto? ")
        nombre = (input("ingrese el nombre del producto: "))
        precio = (input("ingrese el valor: "))
        cantidad = (input("ingrese la cantidad de productos que desea cargar: "))
        productos.append({"nombre":nombre, "precio":precio, "cantidad":cantidad})
        seguir = False
cargar_productos()

def buscar_producto (buscar_nombre):
    for producto in productos:
        if producto ["nombre"].lower() == buscar_nombre.lower():
            return producto
        return None

def ordenar_inventario (productos):


def menu ():
    if menu == "1":
        cargar_productos ()
    elif menu == "2":
        buscar_producto ()
    elif menu == "3":
        ordenar_inventario ()
    elif menu == "4":
        pro_mas_caro_mas_barato=()
        
    elif menu == "5":
        prod_precio_mayor_1500=0()
    elif menu =="6":
        salir= ()= 0

