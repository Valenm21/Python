#UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
# franquicia que se insertará en el mercado argentino y en la cual invertirán.
# Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
# Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
# propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos): Se ingresa de cada encuestado:
#● nombre● edad (no menor a 18) ● está empleado (si-no) ● género (Masculino - Femenino - Otro) ● voto (APPLE, DUNKIN, IKEA)
#Se necesita saber: 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
#25 o entre 36 y 49 o que votaron por IKEA.
#2. Nombre y género del encuestado de menor edad que votó por APPLE.
#3. Porcentaje de encuestados de género Femenino que votaron por IKEA con
#edad mayor a 25 años.
#4. Edad promedio de los encuestados que están o no empleados (de cada uno).
#5. Determinar cuál fue la franquicia más votada
empleado=0
desempleado=0
seguir="si"
femenino=0
masculino=0
otro=0
voto_apple=0
voto_dunkin=0
voto_ikea=0
encuestado_masc_edad_votoikea=0
menor_Edad_Apple=0
nombre_menor_edad_apple=0
genero_menor_edad_apple=0
bandera_menor_Edad_Apple=0
votostotal=0
femenino_ikea=0
porcentaje_femenino_ikea=0
acumulador_Edad_empleado=0
acumulador_Edad_desempleado=0

while seguir=="si":
    nombre=input("ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    while edad <18:
        edad=int(input("Debe volver a ingresar, solo puede registrarse siendo mayor a 18 años. "))
    estadolaboral=input("Responder por si, o no, si se encuentra empleado en este momento: ")
    while estadolaboral!="si" and estadolaboral!="no":
        estadolaboral = input("Responda por si o no: ")
    genero=input("Ingrese su genero entre las siguientes opciones: Masculino, femenino, otro: ")
    while genero !="masculino" and genero!="femenino" and genero!="otro":
        genero=input("Por favor, elegir entre las opciones dadas: ")
    voto=input("¿A quien va dirigido su voto entre : APPLE, DUNKIN, IKEA  ")
    while voto!="apple" and voto!="dunkin" and voto!="ikea":
        voto=input("Ninguna opcion es valida, volver a intentar: ")
    else:
        votostotal+=1

    if estadolaboral=="si":
        empleado+=1
        acumulador_Edad_empleado+=edad
        edad_promedio_empleados=acumulador_Edad_empleado//empleado
    else:
        desempleado+=1
        acumulador_Edad_desempleado+=edad
        edad_promedio_desempleado=acumulador_Edad_desempleado//desempleado
    if genero=="femenino":
         femenino +=1
    elif genero=="masculino":
        masculino+=1
    else:
        otro+=1
#Nombre y género del encuestado de menor edad que votó por APPLE.
#4. Edad promedio de los encuestados que están o no empleados (de cada uno).
    if voto=="apple":
        voto_apple+=1
        if bandera_menor_Edad_Apple==0:
            nombre_menor_edad_apple=nombre
            genero_menor_edad_apple=genero
            menor_Edad_Apple=edad
            bandera_menor_Edad_Apple=1
        elif edad<menor_Edad_Apple:
            nombre_menor_edad_apple=nombre
            genero_menor_edad_apple=genero
            menor_Edad_Apple=edad

    elif voto=="dunkin":
        voto_dunkin+=1
    else:
        voto_ikea+=1
    seguir=input("¿Desea seguir?")
#Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA.
    if genero=="masculino":
        if edad>=18 and edad<=25 or edad>=36 and edad<=49 and voto=="ikea":
            encuestado_masc_edad_votoikea+=1
#3. Porcentaje de encuestados de género Femenino que votaron por IKEA con
#edad mayor a 25 años.
    if genero=="femenino":
        if voto=="ikea" and edad>25:
            femenino_ikea+=1
#5. Determinar cuál fue la franquicia más votada
if voto_apple>voto_ikea and voto_apple>voto_dunkin:
   print("La franquicia más votada fue apple")
elif voto_ikea>voto_dunkin:
    print("La franquicia más votada fue dunkin")
else:
    print ("La franquicia más votada fue ikea. ")

porcentaje_femenino_ikea=(femenino_ikea/votostotal)*100



print("la cantidad de encuestados de genero masculino, entre 18 y 25 o 36 y 49 o que votaron ikea es de ", encuestado_masc_edad_votoikea)
print(nombre_menor_edad_apple,"fue la persona con menor edad que votó apple, su genero es", genero_menor_edad_apple)
print("%", porcentaje_femenino_ikea, "es el porcentaje de votos femeninos mayores a 25 que votaron IKEA. ")
print("La edad promedio de empleados es de ", edad_promedio_empleados, "mientras que la edad promedio de desempleados es de ", edad_promedio_desempleado)


    



