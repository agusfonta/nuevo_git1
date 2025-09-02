# Tp 1 Estructuras repetitivas - AULA VIRTUAL
"""
#--------------- EJERCICIO 1 ---------------------
print("---------------EJERCICIO 1 ---------------")

for num in range(0,101,1):
    print(num)


#--------------- EJERCICIO 2 ---------------------
print("---------------EJERCICIO 2 ---------------")

num = input("Ingrese un numero entero: ")
digitos = 0

for i in range(len(num)):
    digitos += 1

print(f"Tiene {digitos} digitos")

#--------------- EJERCICIO 3 ---------------------
print("---------------EJERCICIO 3 ---------------")

valor1 = int(input("Ingresa el primer valor: "))
valor2 = int(input("Ingresa el segundo valor: "))

suma = 0

for i in range(valor1+1, valor2, 1):
    suma += i
else:
    print(f"La suma entre los numeros desde {valor1} a {valor2} sin incluirlos es {suma}")

#--------------- EJERCICIO 4 -----------------
print("---------------EJERCICIO 4---------------")

suma = 0
num_entero = 1

while num_entero != 0:
    num_entero = int(input("Ingrese un numero: "))
    suma += num_entero
else: 
    print(f"La suma es de {suma}")

    

#--------------- EJERCICIO 5 -----------------
print("---------------EJERCICIO 5 --------------")

import random 

aleatorio = random.randint(0,9)
intentos = 1
jugador = int(input("Adivina el numero entre 0 y 9: "))

if aleatorio == jugador:
    print(f"Ganaste al primer intento! Era {aleatorio}")
else: 
    while aleatorio != jugador:
        jugador = int(input("No acertaste. Adivina el numero entre 0 y 9: "))
        intentos += 1
    else: 
        print(f"Adivinaste, era el numero {aleatorio}. Usaste {intentos} intentos")


#--------------- EJERCICIO 6 -----------------
print("---------------EJERCICIO 6 --------------")

for num in range(100,-1,-1):
    print(num)



#--------------- EJERCICIO 7 -----------------
print("---------------EJERCICIO 7 --------------")

num = int(input("Ingresa un numero entero positivo: "))
suma = 0

for i in range(0, num+1, 1):
    suma += i
else:
    print(f"La suma entre todos los numeros desde 0 hasta {num} es {suma}")


#--------------- EJERCICIO 8 -----------------
print("---------------EJERCICIO 8 --------------")

lista_100 = [] 
pares = 0
impares = 0
negativos = 0
positivos = 0
rango = 100

for i in range(rango):
    numero= int(input("Ingresa un numero: "))
    lista_100.append(numero)
    if numero % 2 == 0:
        pares +=1
    else:
        impares +=1

    if numero > 0:
        positivos +=1
    else:
        negativos +=1


print(f"Numeros: \n{lista_100}")
print(f"Hay {pares} pares, {impares} impares, {positivos} positivos y {negativos} negativos.")


#--------------- EJERCICIO 9 -----------------
print("---------------EJERCICIO 9 --------------")

suma = 0
rango = 100

for i in range(rango):
    numero = int(input(f"Ingresá el número {i+1}: "))
    suma += numero

media = suma / rango

print("\n--- Resultado ---")
print(f"La media de los {rango} números es: {media}")

"""

#--------------- EJERCICIO 10 -----------------
print("---------------EJERCICIO 10 --------------")

num = input("Ingresa un número con al menos dos dígitos: ")
cant_caracteres = len(num)
invertido = ""

for i in range(len(num)):
    invertido += num[cant_caracteres - 1]
    cant_caracteres -= 1

print("Número invertido:", invertido)

    
