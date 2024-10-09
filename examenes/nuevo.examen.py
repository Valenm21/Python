#UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
# franquicia que se insertará en el mercado argentino y en la cual invertirán.
# Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
# Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
# propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos): Se ingresa de cada encuestado:
#● nombre● edad (no menor a 18) ● está empleado (si-no) ● género (Masculino - Femenino - Otro) ● voto (APPLE, DUNKIN, IKEA)
#1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA.
#2. Nombre y género del encuestado de menor edad que votó por APPLE.
#3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años.
#4. Edad promedio de los encuestados que están o no empleados (de cada uno).
#5. Determinar cuál fue la franquicia más votada


seguir="si"
masculino_edad_media_ikea=0
voto_mayor_femenino_ikea=0
voto_apple=0
nombre_menor_apple=0
genero_menor_apple=0
edad_menor_apple=0
bandera_menor_apple=0
voto_dunkin=0
voto_ikea=0
desempleado=0
empleado=0
edad_desempleado=0
edad_empleado=0
contador=0


while seguir=="si":
    nombre_ingresado=input("ingrese su nombre:  ")
    edad_ingresada=int(input("ingrese su edad:  "))

    while edad_ingresada <18:
        edad_ingresada=int(input("REingrese su edad (+18):    "))

    estado_laboral=input("¿Actualmente está empleado?   ")
    while estado_laboral !="si" and estado_laboral!="no":
        estado_laboral=input("REingrese la respuesta por si o no:   ")

    genero_ingresado=input("ingrese su genero entre masculino, femenino u otro:     ")
    while genero_ingresado!="masculino" and genero_ingresado!="femenino" and genero_ingresado!="otro":
        genero_ingresado=input("volver a ingresar su respuesta con las opciones dadas:  ")

    voto_ingresado=input("ingrese a quien dar su voto entre, APPLE, DUNKIN, O IKEA:   ")
    while voto_ingresado!="apple" and voto_ingresado!="dunkin" and voto_ingresado!="ikea":
        voto_ingresado=input("volver a ingresar el voto, con las opciones dadas:    ")

#1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA.  
    match genero_ingresado:
        case "masculino":
            if edad_ingresada>18 and edad_ingresada<25:
                    masculino_edad_media_ikea+=1
            if edad_ingresada>36 and edad_ingresada<49:
                 masculino_edad_media_ikea+=1
            if voto_ingresado=="ikea":
                 masculino_edad_media_ikea+=1

#3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años.
        case "femenino":
              if voto_ingresado=="ikea":
                   if edad_ingresada>25:
                        voto_mayor_femenino_ikea+=1

#2. Nombre y género del encuestado de menor edad que votó por APPLE.
#5. Determinar cuál fue la franquicia más votada   

    match voto_ingresado:
        case "apple":
            if voto_apple==0:
                nombre_menor_apple=nombre_ingresado
                genero_menor_apple=genero_ingresado
                edad_menor_apple=edad_ingresada
                bandera_menor_apple = 1
            elif edad_ingresada<edad_menor_apple:
                nombre_menor_apple= nombre_ingresado
                genero_menor_apple=genero_ingresado
                edad_menor_apple=edad_ingresada
            voto_apple+=1

        case "dunkin":
            voto_dunkin+=1

        case "ikea":
            voto_ikea+=1

#4. Edad promedio de los encuestados que están o no empleados (de cada uno).
    match estado_laboral:
        case "no":
            edad_desempleado+=edad_ingresada
            desempleado+=1
        case _:
            edad_empleado+=edad_ingresada
            empleado+=1
    contador+=1
    seguir=input("¿Desea seguir?")

porcentaje_mayor_femenino_ikea=(voto_mayor_femenino_ikea / contador)*100
promedio_edad_empleados=(edad_empleado/empleado)
promedio_edad_desempleados=(edad_desempleado/desempleado)

print(f"la cantidad de encuestados genero masculino, de entre 18 y 25 o 36 y 49 años fue de {masculino_edad_media_ikea}")
print(f"El nombre de la persona con menor edad que votó apple es {nombre_menor_apple} y su genero es {genero_menor_apple}")
print (f"El porcentaje de encuestados de género Femenino que votaron IKEA con edad mayor a 25 años es de {porcentaje_mayor_femenino_ikea}")
print(f"La edad promedio de las personas que votaron empleadas es de {promedio_edad_empleados}, mientras que la edad promedio de desempleados corresponde a {promedio_edad_desempleados}")
if voto_apple>voto_dunkin and voto_apple>voto_ikea:
    print("La franquicia con más votos es la de apple. ")
if voto_dunkin>voto_ikea:
    print("La franquicia con más votos es la de ikea. ")
else:
    print ("La franquicia con mas votos es la de dunkin. ")
      
