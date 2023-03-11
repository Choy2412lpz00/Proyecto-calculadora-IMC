
print("""
¡Hola! Bienvenido a esta calculadora de IMC
por favor introduce los datos solicitados
""")

#Definición de las variables
nombre = input("Ingresa tu nombre: ")
ApellidoPaterno = input("Ingresa tu apellido paterno: ")
ApellidoMaterno = input("Ingresa tu apellido materno: ")
edad = input("Ingresa tu edad: ")
peso = input("Ingresa tu peso en Kg: ")
estatura = input("Ingresa tu estatura en metros: ")


#Validación de campos vacios de nombre y apellidos
if nombre == "" or ApellidoPaterno == "" or ApellidoMaterno == "":
    print("ERROR - Ingresa tu nombre correctamente")

#Mensaje de error para edad, peso y estatura
try:
    edad = int(edad)
    peso = float(peso)
    estatura = float(estatura)
except ValueError:
    print("Verifica que los datos que ingresaste sean correctos por favor")
else: 
    if edad <= 0 or peso <= 0 or estatura <= 0:
        print("Por favor ingresa cantidades validas")
    else:
        IMC = peso / estatura ** 2


#Impresión de resultados
try:
    (IMC)
except NameError:
    print("""NO ES POSIBLE MOSTRAR TU IMC
    Por favor ingresa TODOS los datos solicitados.""")
else:
    print(f"""¡Hola! {nombre} {ApellidoPaterno} {ApellidoMaterno}
a continuación mostramos tus datos ingresados y el calculo de tu IMC.
Nombre: {nombre}
Apellido paterno: {ApellidoPaterno}
Apellido materno: {ApellidoMaterno}
Edad: {edad}
tu IMC es: {IMC : .2f}""")
    if IMC >= 0 or IMC <= 18.49:
        print("peso bajo")
    elif IMC >= 18.50 or IMC <= 24.99:
        print("peso normal")
    elif IMC >= 25 or IMC <= 34.99:
        print("sobrepeso")
    elif IMC >= 35 or IMC >= 39.99:
        print("obesidad media")
    elif IMC >= 40:
        print("obesidad morbida")

