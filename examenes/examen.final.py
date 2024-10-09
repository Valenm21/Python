#edad(validar entre 1 y 20 años)
#tipo (validar entre gato, perro, hamster)
#peso(mas de 0kg)
#diagnostico (validar problemas digestivos, parasitos, infeccion)
#vacuna antirrabica (validar "si, no")

#cantidad de perros o gatos sin vacuna antirrabica, que pesan entre 10 y 20 kg
#el tipo de mascota más ingresada con parasitos 
#edad y diagnostico de la mascota mas joven que se presento con una infeccion 
#porcentaje de mascotas de cada tipo
#promedio de pesos de mascotas con parasitos 

seguir ="si"
gato_perro_sin_vacuna=0
gato_diagnostico_parasito=0
perro_diagnostico_parasito=0
hamster_diagnostico_parasito=0
contador_infeccion=0
contador_gato=0
contador_perro=0
contador_hamster=0
peso_animales_total=0
contador=0


while seguir == "si":
    edad_ingresada = int (input("ingrese la edad de la mascota :    "))
    while edad_ingresada < 1 and edad_ingresada > 20:
        edad_ingresada = int (input("Vuelva a ingresar la edad teniendo en cuenta el rango de entre (1 y 20 años.)"))
    tipo_ingresado = input("ingrese el tipo de mascota entre gato, perro, hamster:  ")
    while tipo_ingresado!="gato" and tipo_ingresado!="perro" and tipo_ingresado!="hamster":
        tipo_ingresado = input("Vuelva a ingresar respuesta, teniendo en cuenta las opciones: ")
    peso_ingresado = float (input("ingrese el peso en kg:   "))
    while peso_ingresado<0:
        peso_ingresado=float(input("Vuelva a ingresar el peso teniendo en cuenta que no puede ser menos de 0kg: "))
    diagnostico_ingresado = input ("ingrese el diagnostico entre problemas digestivos, parasitos, o infeccion:  ")
    while diagnostico_ingresado!="problemas digestivos" and diagnostico_ingresado!="parasitos" and diagnostico_ingresado!="infeccion":
        diagnostico_ingresado = input ("vuelva a ingresar la respuesta teniendo en cuenta las opciones dadas:   ")
    vacuna_antirrabica = input ("¿La mascota tiene puesta la vacuna antirrabica? Responder por si o no:    ")
    while vacuna_antirrabica !="si" and vacuna_antirrabica != "no":
        vacuna_antirrabica = input("Volver a ingresar respuesta por si o no:    ")

#cantidad de perros o gatos sin vacuna antirrabica, que pesan entre 10 y 20 kg   
#El tipo de mascota más ingresada con parasitos 
    match tipo_ingresado:
        case "gato":
            contador_gato+=1
            peso_animales_total+=peso_ingresado
            if vacuna_antirrabica=="no":
                if peso_ingresado>=10 and peso_ingresado<=20:
                    gato_perro_sin_vacuna+=1
                    if diagnostico_ingresado=="parasitos":
                        gato_diagnostico_parasito+=1
                        
        case "perro":
            contador_perro+=1
            peso_animales_total+=peso_ingresado
            if vacuna_antirrabica=="no":
                if peso_ingresado>=10 and peso_ingresado<=20:
                    gato_perro_sin_vacuna+=1
                    if diagnostico_ingresado=="parasitos":
                        perro_diagnostico_parasito+=1
        case "hamster":
            contador_hamster+=1
            peso_animales_total+=peso_ingresado
            if diagnostico_ingresado=="parasitos":
                hamster_diagnostico_parasito+=1
            
#edad y diagnostico de la mascota mas joven que se presento con una infeccion 
    match diagnostico_ingresado:
        case "infeccion":
            if contador_infeccion==0:
                edad_menor_infeccion = edad_ingresada
                diagnostico_menor_infeccion = diagnostico_ingresado
                bandera_menor_infeccion = 1
            elif edad_ingresada<edad_menor_infeccion:
                edad_menor_infeccion=edad_ingresada
                diagnostico_menor_infeccion=diagnostico_ingresado
    contador+=1
    seguir = (input("¿Desea seguir?   "))

#porcentaje de mascotas de cada tipo
porcentate_perro = (contador_perro/contador)*100
porcentaje_gato = (contador_gato/contador)*100
porcentaje_hamster = (contador_hamster/contador)*100
#promedio de pesos de mascotas con parasitos 
promedio_pesos = (peso_animales_total/contador)

print(f"La cantidad de perros y gatos que sin vacuna antirrabica, que pesan entre 10 y 20 kilos son {gato_perro_sin_vacuna}")
if gato_diagnostico_parasito>perro_diagnostico_parasito and gato_diagnostico_parasito>hamster_diagnostico_parasito:
    print ("El tipo de mascota que más ingresada con parasitos fue el gato.")
elif perro_diagnostico_parasito>hamster_diagnostico_parasito:
    print("El tipo de mascota más ingresado con parasitos fue el perro.")
else:
    print("el tipo de mascota más ingresada con parasitos fue el hamster. ")
print(f"La mascota más joven que se presentó con {diagnostico_menor_infeccion} tenia {edad_menor_infeccion} años.")
print (f"El porcentaje de gatos fue de %{porcentaje_gato} de perros %{porcentate_perro} y de hamster %{porcentaje_hamster}")
print(f"El promedio de pesos es de {promedio_pesos}")