# Caso 2 - Clinica Turnos por especialidad (cupos del día)

lista_esp = []
lista_cupos = []
menu_abierto = True
op_elegida = 0

while menu_abierto == True:

    # Menu
    print("\n------ Menu ------")
    print("\n 1. Ingresar especialidades y sus cupos " \
    "\n 2. Mostrar agenda (solo especialidades con cupos disponibles)" \
    "\n 3. Consultar cupos de una especialidad" \
    "\n 4. Especialidades sin cupo" \
    "\n 5. Agregar especialidad y sus cupos" \
    "\n 6. Actualizar cupos (reservar/cancelar)" \
    "\n 7. Agenda completa" \
    "\n 8. Salir")

    try:
        op_elegida = int(input("Elije una opcion: "))
    except ValueError:
        print("Debes ingresar un número.")
        continue

    # --------- Opcion uno ----------
    if op_elegida == 1:
        try:
            cantidad = int(input("¿Cuántas especialidades ingresarás?: "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        for i in range(cantidad):
            especialidad = input("Ingresa una especialidad: ").strip().lower()
            while especialidad == "" or especialidad in lista_esp:
                if especialidad == "":
                    print("No puede estar vacío.")
                else:
                    print("Especialidad ya ingresada.")
                especialidad = input("Ingresa nuevamente la especialidad: ").strip().lower()

            try:
                cupo = int(input("Ingresa su cupo: "))
                while cupo < 0:
                    print(" El cupo no puede ser negativo.")
                    cupo = int(input("Ingresa su cupo: "))
            except ValueError:
                print(" Ingresa un número válido de cupos.")
                continue

            lista_esp.append(especialidad)
            lista_cupos.append(cupo)

    # ------- Opcion dos ---------
    elif op_elegida == 2:
        disponibles = False
        for i in range(len(lista_esp)):
            if lista_cupos[i] > 0:
                print(f"{lista_esp[i]}: {lista_cupos[i]} cupos")
                disponibles = True
        if not disponibles:
            print("No hay especialidades con cupos disponibles.")

    # ---------- Opcion tres -----------
    elif op_elegida == 3:
        consulta = input("Especialidad que quiere consultar: ").lower()
        while consulta not in lista_esp:
            print("No encontrado en nuestra lista de especialidades.")
            otra_vez = input("¿Desea ingresar otra especialidad? s/n: ").lower()
            if otra_vez == "s":
                consulta = input("Ingrese nuevamente: ").lower()
            else:
                consulta = ""
                break
        if consulta != "":
            pos = lista_esp.index(consulta)
            print(f"\nCupos de {consulta}: {lista_cupos[pos]}")

    # ---------- opcion cuatro ------------------
    elif op_elegida == 4:
        sin_cupos = False
        for i in range(len(lista_esp)):
            if lista_cupos[i] == 0:
                print(f"{lista_esp[i]} - Cupos Agotados")
                sin_cupos = True
        if not sin_cupos:
            print("No hay especialidades sin cupos.")

    # --------- opcion cinco ------------
    elif op_elegida == 5:
        nueva_esp = input("Especialidad que quiere agregar: ").strip().lower()
        while nueva_esp == "" or nueva_esp in lista_esp:
            if nueva_esp == "":
                print("No puede estar vacío.")
            else:
                print("Especialidad ya en lista.")
            otra_vez = input("¿Desea ingresar otra especialidad? s/n: ").lower()
            if otra_vez == "s":
                nueva_esp = input("Ingrese nuevamente: ").strip().lower()
            else:
                nueva_esp = ""
                break

        if nueva_esp != "":
            try:
                nuevo_cupo = int(input("Cupos: "))
                while nuevo_cupo < 0:
                    print("El cupo no puede ser negativo.")
                    nuevo_cupo = int(input("Cupos: "))
            except ValueError:
                print("Ingresa un número válido.")
                continue

            lista_esp.append(nueva_esp)
            lista_cupos.append(nuevo_cupo)

    # --------------- opcion seis ---------------
    elif op_elegida == 6:
        accion = input("¿Quiere reservar o cancelar? r/c: ").lower()

        if accion == "r":
            esp = input("Qué especialidad quiere reservar?: ").lower()
            if esp in lista_esp:
                pos = lista_esp.index(esp)
                if lista_cupos[pos] > 0:
                    lista_cupos[pos] -= 1
                    print(f"\nCupo reservado. Cupos actualizados de {esp}: {lista_cupos[pos]}")
                else:
                    print(" No hay cupos disponibles para esa especialidad.")
            else:
                print(" Especialidad no encontrada.")

        elif accion == "c":
            esp = input("Qué especialidad quiere cancelar?: ").lower()
            if esp in lista_esp:
                pos = lista_esp.index(esp)
                lista_cupos[pos] += 1
                print(f"\nReserva cancelada. Cupos actualizados de {esp}: {lista_cupos[pos]}")
            else:
                print(" Especialidad no encontrada.")
        else:
            print(" Ingresa r o c.")

    # ------------ siete -------------
    elif op_elegida == 7:
        print("AGENDA COMPLETA:")
        for i in range(len(lista_esp)):
            print(f"{lista_esp[i]}: {lista_cupos[i]} cupos")

    # ---------- ocho ----------------
    elif op_elegida == 8:
        print("Saliendo...")
        menu_abierto = False

    else:
        print("Opción inválida.")
