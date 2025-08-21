
#___________ PUNTO 7 ______________
print("______Punto 7 ______")

palabra = input("Ingresa una palabra: ")
ultima_letra = palabra[len(palabra) - 1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{palabra}!")
else:
    print(f"{palabra}")
