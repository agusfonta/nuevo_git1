# 6/10 - Mochila
#------------------------------------------

def mostrar_menu():
    print("----- MENU -----")
    print("1. Guardar objeto")
    print("2. Ver mochila")
    print("3. Salir")

def iniciar_mochila_vacia(mochila, cantidad):
    for i in range(cantidad):
        mochila.append(0)

def pedir_posicion(cantidad):
    while True:
        try:
            pos = int(input(f"Ingrese la posición (1 - {cantidad}): "))
            if pos < 1 or pos > cantidad:
                print("No existe esa posición. Intente nuevamente.")
            else:
                return pos
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def pedir_objeto():
    while True:
        objeto = input("Ingrese el objeto: ").strip()
        if len(objeto) == 0:
            print("Error: No puede dejar el campo vacío.")
        elif not objeto.isalpha():
            print("Error: El nombre solo puede tener letras.")
        else:
            return objeto

def agregar_objeto():
    pos = pedir_posicion(cantidad)
    objeto = pedir_objeto()

    # Si la posición está vacía, lo guarda
    if mochila[pos - 1] == 0:
        mochila[pos - 1] = objeto
        print(f"Objeto '{objeto}' agregado en la posición {pos}.")
    else:
        print(f"Esa posición ya contiene '{mochila[pos - 1]}'. No se puede reemplazar.")

def mostrar_contenido(): 
    print("--- CONTENIDO DE LA MOCHILA ---")
    for i in range(len(mochila)):
        if mochila[i] == 0:
            print(f"Espacio {i + 1}: --- vacío ---")
        else:
            print(f"Espacio {i + 1}: {mochila[i]}")

#-----------------------------------------
#__________ PROGRAMA PRINCIPAL ___________

andando = True
inicio = True

while inicio:
    try:
        print("- MOCHILA -")
        cantidad = int(input("Ingrese cuántos espacios tendrá la mochila: "))
        if cantidad <= 0:
            print("Error: Debe ingresar un número mayor que 0.")
        else:
            mochila = []
            iniciar_mochila_vacia(mochila, cantidad)
            inicio = False
    except ValueError:
        print("Error: Debe ser un número.")
else:
    print("Espacios ingresados correctamente.\n")

while andando:
    try:
        mostrar_menu()
        op = int(input("Ingrese una opción: "))

        match op:
            case 1:
                print("\n___ 1. Agregar objeto ___")
                agregar_objeto()
            case 2:
                print("\n___ 2. Mostrar mochila ___")
                mostrar_contenido()
            case 3:
                print("\n___ 3. Saliendo... ___")
                andando = False
            case _:
                print("No existe esa opción. Elija nuevamente.")
    except ValueError:
        print("Error: Por favor ingrese un número.")
else:
    print("El programa ha finalizado.")
