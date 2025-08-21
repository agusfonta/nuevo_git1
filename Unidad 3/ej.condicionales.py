print("Actividades Unidad 3 - Condicionales")

#___________ PUNTO 1 ______________
print("______Punto 1______")

edad = int(input("Ingresa tu edad: "))

if edad >= 18: 
    print("Es mayor de edad")
else: 
    print("Es menor de edad")

#___________ PUNTO 2 ______________
print("______Punto 2______")

nota = int(input("Ingresa tu nota: "))

if nota >= 6: 
    print("Aprobado")
else: 
    print("Desaprobado")

#___________ PUNTO 3 ______________
print("______Punto 3______")

num = int(input("Ingresa un numero par: "))

if num % 2 != 0: 
    print("Por favor ingrese un numero par")
    num = int(input("Ingresa un numero par: "))
else: 
    print("Ha ingresado un numero par")

#___________ PUNTO 4 ______________
print("______Punto 4______")

edad = int(input("Ingresa tu edad: "))

if edad <= 12: 
    print("Niño/a")
elif edad > 12 and edad < 18: 
    print("Adolescente")
elif edad >= 18 and edad < 30: 
    print("Adulto/a joven")
else: 
    print("Adulto/a")

#___________ PUNTO 5 ______________
print("______Punto 5 ______")

contraseña = input("Ingresa una contraseña de 8 a 14 caracteres: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Se ha ingresado correctamente")
else:
    contraseña = input("Por favor, ingrese una contraseña entre 8 y 14 caracteres: ")

#___________ PUNTO 6 ______________
print("______Punto 6 ______")

from statistics import mode, median, mean 
import random 

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)

if media>mediana and mediana>moda:
    print("Sesgo positivo")
elif media<mediana and mediana>moda:
    print("Sesgo negativo")
elif mediana == media == moda: 
    print("Sin sesgo")
else:
    "No se pudo realizar el calculo"

#___________ PUNTO 7 ______________
print("______Punto 7 ______")

palabra = input("Ingresa una palabra: ")
ultima_letra = palabra[len(palabra) - 1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{palabra}!")
else:
    print(f"{palabra}")

#___________ PUNTO 8 ______________
print("______Punto 8 ______")

nombre = input("Ingrese su nombre: ")
mayus = nombre.upper()
minus = nombre.lower()
titulo = nombre.title()

opcion = input(f"Elija 1, 2 o 3 segun lo deseado: \n 1. En mayusculas \n 2. En minusculas \n 3. Primera mayuscula, el resto minuscula \n - ")

if opcion == "1":
    print(mayus)
elif opcion == "2":
    print(minus)
else:
    print(titulo)

#___________ PUNTO 9 ______________
print("______Punto 9 ______")

magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3:
    print("Muy leve")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#___________ PUNTO 10 ______________
print("______Punto 10 ______")

hemisferio = input("Ingrese en que hemisferio se encuentra(responda con N o S mayusculas): ")
dia = int(input("Ingrese que dia es: "))
mes = input("Ingrese que mes es (todo minusculas): ")

if (mes=="diciembre" and dia >=21) or mes == "enero" or mes == "febrero" or (mes=="marzo" and dia <=20):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")
if (mes=="marzo" and dia >=21) or mes == "abril" or mes == "mayo" or (mes=="junio" and dia <=20):
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")
if (mes=="junio" and dia >=21) or mes == "julio" or mes == "agosto" or (mes=="septiembre" and dia <=20):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")
if (mes=="septiembre" and dia >=21) or mes == "octubre" or mes == "noviembre" or (mes=="diciembre" and dia <=20):
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")
