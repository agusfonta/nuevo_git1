

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