#Bingo 8 de septiembre

import random

# Generar el cartón 5x5 con números únicos entre 1 y 50
numeros = random.sample(range(1, 51), 25)
carton = [numeros[i:i+5] for i in range(0, 25, 5)]

print("Bienvenido al Bingo")
print("Tu carton es: ")



#Sorteo

for filas in range(5):
    for columnas in range(5):
        print(carton[filas][columnas], end=" ")
    print()


num=random.randint(1,51)

for filas in range(5):
    for columnas in range(5):
        if num == carton[filas][columnas]:
            carton[filas][columnas] = 0
            print(f"Se sortea el numero {num}. Lo tenes!")
else:
    print(f"Se sortea el numero {num}. No esta en tu carton")
print()








