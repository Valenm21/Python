
def menu ():
    lista_pacientes = []
    salir = ""
    while salir != "salir":
        print  ("• 1 Cargar lista_pacientes .")
        print  ("• 2 Buscar paciente.")
        print  ("• 3 Determinar paciente con más/menos días de internación.")
        print  ("• 4 Ordenar pacientes por número de historia clínica")
        print  ("• 5 salir del sistema.")
        respuesta = int (input ("ingrese una opcion entre 1 y 5: "))

        if respuesta == 1:
            cargar_pacientes(lista_pacientes)
        elif respuesta == 2:
            numero = int(input ("ingrese el numero de del paciente que busca: "))
            paciente = buscar_pacientes(lista_pacientes, numero)
            if paciente:
                print (f"Paciente encontrado: {paciente}")
            else: 
                print ("Paciente no encontrado. ")
        elif respuesta == 3:
            max_min_dias_internado (lista_pacientes)
        elif respuesta == 4:
            ordenar_pacientes(lista_pacientes)
        elif respuesta == 5:
            salir = salir
        else:
            print ("Ninguna opcion es validad, volver a intentar")

def cargar_pacientes (pacientes):
        n = int (input("ingrese la cantidad de pacientes que desea ingresar: "))
        for _ in range (n):
            numero = int (input("ingrese el numero de historia clinica: "))
            nombre_paciente = input ("ingrese el nombre del paciente: ")
            edad = int (input("ingrese la edad del paciente: "))
            diagnostico = (input("ingrese el diagnostico: "))
            dias = int (input("ingrese la cantidad de días de internación asignados: "))
            pacientes.append ([numero, nombre_paciente, edad, diagnostico,dias])
        return pacientes

def buscar_pacientes(pacientes, numero):
    for paciente in pacientes:
        if paciente [0] == numero:
            return paciente
    return None

def ordenar_pacientes (pacientes):
    for i in range (len(pacientes)):
        for j in range (0, len(pacientes) - i -1 ):
            if pacientes [j] [0] > pacientes [j+1][0]:
                pacientes [j], pacientes[j+1] = pacientes[j + 1], pacientes[j]
        print ("orden de pacientes, por numero de historial: ")
        for paciente in pacientes :
            print (f"Numero: {pacientes[0]}, Nombre:{pacientes[1]}")
        return pacientes

def max_dias_internado(lista_pacientes):
    if not lista_pacientes:
        print ("no hay pacientes registrados para la operación solicitada")    
        return
    max_dia_internado = lista_pacientes[0]
    for paciente in lista_pacientes:
        if paciente [4] > max_dia_internado [4]:
            max_dia_internado = paciente
    print (f"El maximo de días internados es de {max_dia_internado}")
def min_dias_internados (lista_pacientes):
    if not lista_pacientes:
        print ("La lista está vacia. ")
        return 
    min_dias_internados = lista_pacientes[0]
    for paciente in lista_pacientes:
        if paciente[4] < min_dias_internados [4]:
            min_dias_internados = paciente
        print (f"El minimo de dias internados es de: {min_dias_internados}")

def max_min_dias_internado (lista_pacientes):
    max_dias_internado (lista_pacientes)
    min_dias_internados(lista_pacientes)

def cont_pacientes_mas_cinco_dias (lista_pacientes):
    contador = 0
    for paciente in lista_pacientes:
        if paciente [4] > 5:
            contador += 1
    print (f"La cantidad de pacientes con más de 5 dias de internacion es de:  ")


def calcular_promedio (lista_pacientes):
    if not lista_pacientes:
        print ("La lista está vacia.  ")
        return 
    total_dias = 0 
    for paciente in lista_pacientes:
        total_dias +=paciente[4]
    promedio = total_dias/len(lista_pacientes)
    print (f"El promedio total de los dias de internacion es de: {promedio}")

menu()
