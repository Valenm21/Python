def menu ():
    menu = print (
        """Menú Principal: 
•1 Cargar producto/s.
•2 Buscar producto.
•3 Ordenar inventario.
•4 Mostrar producto más caro y más barato.
•5 Mostrar productos con precio mayor a 15000.
•6 Salir """)
inventario = []
def opcion_menu ():
    print = menu()
    opcion = input("elegir una de estas opciones: ")
    while True:
        if opcion == "1":
            cargar_productos(inventario)
        elif opcion == "2":
            buscar_productos(inventario)
        elif opcion == "3":
            ordenar_inventario()
        elif opcion == "4":
            prod_max_min()
        elif opcion == "5":
            prod_mayor ()
        elif opcion == "6":
            False

def cargar_productos (inventario):
    cargar="si"
    while cargar == "si":
        nombre_producto = input ("ingrese el nombre del producto: ")
        precio = float (input ("ingrese el valor de este producto: "))
        cantidad = int (input ("ingrese la cantidad que requiere: "))
        cargar = input ("¿Desea cargar un producto? ")
        inventario.append ([nombre_producto, precio, cantidad])
        producto = {
        'nombre':nombre_producto,
        'precio':precio,
        'cantidad': cantidad
        }
        inventario.append(producto)
  
def buscar_productos (inventario):
    nombre_prod_buscar = input ("ingrese el nombre del producto que desea buscar: ")
    for producto in inventario: 
        if producto [0] == nombre_prod_buscar:
            print (f"""El producto está dentro del inventario
            nombre:{producto['nombre']}
            precio: ${producto['precio']}
            cantidad:{producto['cantidad']} """)
            return
    print ("El producto no se encuentra en el inventario")

def ordenar_inventario (inventario):
    for i in range (len(inventario)):
        for j in range (0, len(inventario)- i -1):
            if inventario[j][i] > inventario [j + 1][1]:
                inventario[j], inventario[j + 1] = inventario [j + 1], inventario [j]

    
opcion_menu()
             
