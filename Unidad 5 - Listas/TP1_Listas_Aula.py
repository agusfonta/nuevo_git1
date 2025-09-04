
print(f"\n-Ejercicio 1 \n")
# EJ 1 - lista de numeros del 1 al 100 multiplos de 4

lista = []

for numeros in range(0,101,4):
    if numeros != 0:
        lista.append(numeros)
    else:
        continue

print(lista)

print(f"\n-Ejercicio 2 \n")
# EJ 2 - lista y mostrar penultimo

lista = ["pelota","perro","planta","mate","factura"]

print(lista[3])
print(lista[-2]) #indexin negativo

print(f"\n-Ejercicio 3 \n")
# EJ 3 - lista y agregar con append

lista_vacia = []

lista_vacia.append("hola")
lista_vacia.append("como")
lista_vacia.append("esta")

print(lista_vacia)

print(f"\n-Ejercicio 4 \n")
# EJ 4 -  reemplazar el segundo y último valor por “loro” y “oso”

animales = ["perro", "gato", "conejo", "pez"] 
animales[1] = "loro"
animales[-1] = "oso"

print(animales)

print(f"\n-Ejercicio 5 \n")
#Ej 5 - analizar el programa y explicar lo que realiza

numeros = [8,15,3,22,7]
numeros.remove(max(numeros)) # Lo que hace es eliminar el numero mas grande de la lista
print(numeros)

print(f"\n-Ejercicio 6 \n")
# Ej 6 - lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros. 

lista = []
for numeros in range(10,31,5):
    lista.append(numeros)

print(lista[0],lista[1])

print(f"\n-Ejercicio 7 \n")
# Ej 7 - reemplazar los dos valores centrales por otra cosa

autos = ["sedan", "polo", "suran", "gol"] 
autos[1] = "rojo"
autos[2] = "verde"

print(autos)

print(f"\n-Ejercicio 8 \n")
# Ej 8 - lista vacia llamada "dobles" y agregar el doble de 5, 10 y 15

dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

print(f"\n-Ejercicio 9 \n")
# Ej 9- lista de compras
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan") # o tambien compras[0].pop(0)


print(compras)

print(f"\n-Ejercicio 10 \n")
# Ej 10 - lista anidada

lista_anidada = []
lista_dentro = []

lista_dentro.append(25.5)
lista_dentro.append(57.9)
lista_dentro.append(30.6)

lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append(lista_dentro)
lista_anidada.append(False)

print(lista_anidada)