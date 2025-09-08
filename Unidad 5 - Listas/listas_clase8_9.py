import random

# --- 1) Generar el cartón ---
carton_numeros = random.sample(range(1, 51), 25)
carton = [carton_numeros[i:i+5] for i in range(0, 25, 5)]

def mostrar_carton(carton):
    for filas in range(5): 
        for columnas in range(5): 
            print(carton[filas][columnas], "|", end=" ") 
        print() 
    print("\n")

def hay_linea(carton):
    for fila in carton:
        if all(n == 0 for n in fila):
            return True
    return False

print("\n ¡Bienvenido al Bingo! \n")
print("Tu cartón es:\n")
mostrar_carton(carton)

# --- 2) Generar lista de números para sortear ---
numeros_sorteo = list(range(1, 51))
random.shuffle(numeros_sorteo)

# --- 3) Jugar ---
for num in numeros_sorteo:
    encontrado = False
    for filas in range(5):
        for columnas in range(5):
            if carton[filas][columnas] == num:
                carton[filas][columnas] = 0
                encontrado = True

    if encontrado:
        print(f"Se sortea el número... {num} -> ¡Lo tenés!")
    else:
        print(f"Se sortea el número... {num} -> No está en tu cartón.")

    mostrar_carton(carton)

    # Línea
    if hay_linea(carton):
        print(" ¡LÍNEA! Una fila completa está en ceros \n")

    # Bingo
    if all(all(n == 0 for n in fila) for fila in carton):
        print(" ¡BINGO! Tu cartón quedó completo \n")
        break

