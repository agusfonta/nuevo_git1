# Ahorcado 29/9 

#____________ FUNCIONES _____________

import random

# 1) Función para elegir palabra al azar
def elegir_palabra(lista, usadas):
    # Devuelve una palabra que no haya sido usada antes
    disponibles = [p for p in lista if p not in usadas]
    if not disponibles:
        return None  # Si no quedan palabras
    return random.choice(disponibles)

# 2) Función para mostrar el estado actual de la palabra
def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()

# 3) Función para pedir una letra al jugador
def pedir_letra():
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Por favor, ingresa solo una letra válida.")

# 4) Función principal de una partida
def jugar_una_partida(palabras_secretas, usadas):
    palabra = elegir_palabra(palabras_secretas, usadas)
    if not palabra:
        print("Ya jugaste con todas las palabras disponibles. ¡Fin del juego!")
        return False  # termina el bucle principal

    usadas.add(palabra)
    intentos = 6
    letras_adivinadas = []

    print("\n *** Nueva partida del Ahorcado *** ")
    print(" Adivina la palabra secreta. ¡Tienes 6 intentos!\n")

    while intentos >= 0:
        print(ahorcado[intentos])  # Mostrar dibujo del ahorcado
        print("Palabra:", mostrar_progreso(palabra, letras_adivinadas))
        print("Intentos restantes:", intentos)
        print("Letras ya intentadas:", ", ".join(sorted(letras_adivinadas)) if letras_adivinadas else "Ninguna")

        # Condición de victoria
        if all(l in letras_adivinadas for l in palabra):
            print("¡Felicidades! Adivinaste la palabra:", palabra)
            break

        if intentos == 0:
            print("Te quedaste sin intentos. La palabra era:", palabra)
            break

        letra = pedir_letra()

        if letra in letras_adivinadas:
            print("Ya habías probado esa letra, intenta con otra.\n")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print(" ¡Bien! Adivinaste una letra.\n")
        else:
            intentos -= 1
            print("\n-Letra incorrecta.\n")

    # Preguntar si quiere jugar otra
    seguir = input("¿Quieres jugar otra partida? (s/n): ").lower()
    return seguir == "s"


# _____________ PRINCIPAL _____________________

palabras_secretas = ["perro", "gato", "hormiga", "zorro", "canguro", "tortuga", "lobo", "elefante", "jirafa", "pulpo", "rinoceronte"]

# Etapas del ahorcado (7 estados: 6 → 0 intentos)
ahorcado = [
    """
    -----
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    ===
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  / 
    |
    ===
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  
    |
    ===
    """,
    """
    -----
    |   |
    |   O
    |  /|
    |  
    |
    ===
    """,
    """
    -----
    |   |
    |   O
    |   |
    |  
    |
    ===
    """,
    """
    -----
    |   |
    |   O
    |   
    |  
    |
    ===
    """,
    """
    -----
    |   |
    |   
    |   
    |  
    |
    ===
    """
]

print(" *** Bienvenido al juego del Ahorcado de ANIMALES *** ")

usadas = set()
while True:
    if not jugar_una_partida(palabras_secretas, usadas):
        print("Gracias por jugar. ¡Hasta la próxima!")
        break