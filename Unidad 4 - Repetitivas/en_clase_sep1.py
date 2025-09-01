
#Unidad 4 - Estructuras repetitivas FOR Y WHILE


#EJERCICIO FOR 

corrimiento = int(input("Ingresa el corrimiento: "))
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


for oficial in range(5):

    mensaje = (input(f"Ingresa el mensaje para el oficial {oficial+1}: ")).upper()
    mensaje_encriptado = ""

    for letra in mensaje: 
        if letra in abecedario: 
            posicion = abecedario.find(letra)
            nva_letra = abecedario[(posicion+corrimiento)%27]
            mensaje_encriptado += nva_letra
        else:
            mensaje_encriptado += letra
    
    print(f"Mensaje para oficial {oficial+1}: {mensaje_encriptado} ")



#EJERCICIO WHILE

import random

opciones = ["piedra","papel","tijera"]

estamos_jugando = True

puntos_jugador = 0
puntos_compu = 0


while estamos_jugando:
    jugador = input("Elije: piedra, papel o tijera: ").lower()
    compu = opciones[random.randint(0,2)]

    print(f" Tu: {jugador} \n Compu: {compu}")

    if (jugador == "piedra" and compu == "tijera") or (jugador == "tijera" and compu == "papel") or (jugador == "papel" and compu == "piedra"):
        print(f"Ganaste!")
        puntos_jugador += 1
        sigue = input("Quieres seguir jugando? si/no: ").lower()
        if sigue == "si":
            estamos_jugando =  True
        else:
            estamos_jugando =  False
    elif jugador == compu:
        print("Ha sido un empate, continuen")
    else:
        print(f"Perdiste")
        puntos_compu += 1
        sigue = input("Quieres seguir jugando? si/no: ").lower()
        if sigue == "si":
            estamos_jugando =  True
        else:
            estamos_jugando =  False
        
else: 
    print(f"Marcador: \n Puntos jugador: {puntos_jugador} \n Puntos compu: {puntos_compu}")

