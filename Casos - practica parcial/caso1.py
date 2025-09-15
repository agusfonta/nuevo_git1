# Caso 1 - Biblioteca escolar
estamos_en_menu = True
titulos = []
ejemplares = []

while estamos_en_menu:
    print("\n- Opciones del Menu -")
    print(" 1. Ingresar nuevos títulos y ejemplares")
    print(" 2. Ingresar ejemplares de todos los títulos")
    print(" 3. Mostrar catálogo con stock")
    print(" 4. Consultar disponibilidad de un título específico")
    print(" 5. Consultar agotados")
    print(" 6. Actualizar ejemplares (préstamo/devolución)")
    print(" 7. Ver catálogo completo")
    print(" 8. Salir")

    op_menu = input("Ingresa el número de la opción: ")

    if op_menu == "1":
        cantidad = int(input("¿Cuántos libros quieres agregar?: "))
        for _ in range(cantidad):
            titulo_nuevo = input("Introduce el título del libro: ").lower()

            while titulo_nuevo in titulos:
                titulo_nuevo = input("Ese título ya existe. Ingresa uno diferente: ").lower()

            ejemplares_nuevo = int(input("Introduce la cantidad de ejemplares: "))

            titulos.append(titulo_nuevo)
            ejemplares.append(ejemplares_nuevo)
    
    elif op_menu == "2":
        for i in range(len(titulos)):
            print(F"Libro {i}: {titulos[i]}")
            ejemplares_nuevo = int(input("Introduce la cantidad de ejemplares: "))
            ejemplares[i] = ejemplares_nuevo

    elif op_menu == "3":
        print("\nTítulos con stock:")
        for i in range(len(titulos)):
            if ejemplares[i] > 0:
                print(f" {titulos[i]} -> {ejemplares[i]} ejemplares")

    elif op_menu == "4":
        consultar = "s"
        while consultar == "s":
            titulo_a_consultar = input("Ingresa el título: ").lower()
            if titulo_a_consultar in titulos:
                posicion = titulos.index(titulo_a_consultar)
                if ejemplares[posicion] > 0:
                    print(f"El título '{titulo_a_consultar}' está disponible ({ejemplares[posicion]} ejemplares).")
                else:
                    print(f"'{titulo_a_consultar}' está en catálogo pero sin ejemplares.")
            else:
                print("Este título no está en la biblioteca.")
            consultar = input("¿Quieres consultar otro título? s/n: ").lower()

    elif op_menu == "5":
        print("\nTítulos agotados:")
        agotados = False
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(f" {titulos[i]} -> agotado")
                agotados = True
        if not agotados:
            print("No hay títulos agotados.")

    elif op_menu == "6":
        titulo = input("¿Qué título quieres actualizar?: ").lower()
        if titulo in titulos:
            posicion = titulos.index(titulo)
            accion = input("¿Devolución o préstamo? (d/p): ").lower()
            if accion == "d":
                cant = int(input("¿Cuántos ejemplares devolviste?: "))
                ejemplares[posicion] += cant
            elif accion == "p":
                cant = int(input("¿Cuántos ejemplares pediste?: "))
                if ejemplares[posicion] >= cant:
                    ejemplares[posicion] -= cant
                else:
                    print("No hay suficientes ejemplares para prestar.")
            print(f"Actualización: {titulos[posicion]} -> {ejemplares[posicion]} ejemplares")
        else:
            print("Ese título no está en el catálogo.")

    elif op_menu == "7":
        print("\nCatálogo completo:")
        for i in range(len(titulos)):
            print(f" {titulos[i]} -> {ejemplares[i]} ejemplares")

    elif op_menu == "8":
        print("Saliendo del menú...")
        estamos_en_menu = False

    else:
        print("Opción inválida. Intenta de nuevo.")
