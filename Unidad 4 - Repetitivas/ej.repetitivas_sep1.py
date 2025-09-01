""" 
Unidad 4 - Estructuras repetitivas FOR Y WHILE

"""

#EJERCICIO FOR 

corrimiento = int(input("Ingresa el corrimiento: "))
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


for oficial in range(5):

    mensaje = (input(f"Ingresa el mensaje para el oficial {oficial+1}: ")).upper()
    mensaje_encriptado = ""

    for letra in mensaje: 
        if letra == " ": 
            mensaje_encriptado += " "
        else:
            posicion = abecedario.find(letra)
            nva_letra = abecedario[(posicion+corrimiento)%27]
            mensaje_encriptado += nva_letra
    
    print(f"Mensaje para oficial {oficial+1}: {mensaje_encriptado} ")



