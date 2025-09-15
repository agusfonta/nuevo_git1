# Caso 2 - Clinica Turnos por especialidad (cupos del día)

lista_esp = []
lista_cupos = []
menu_abierto = True
op_elegida = 0

while menu_abierto == True:

#Menu
    print( "\n------ Menu ------")
    print( "\n 1. Ingresar especialidades y sus cupos" \
    "\n 2. Mostrar agenda (solo especialidades con cupos disponibles)" \
    "\n 3. Consultar cupos de una especialidad" \
    "\n 4. Especialidades sin cupo" \
    "\n 5. Agregar especialidad y sus cupos" \
    "\n 6. Actualizar cupos (reservar/cancelar)" \
    "\n 7. Agenda completa" \
    "\n 8. Salir")

    op_elegida = int(input( "Elije una opcion: "))

#---------Opcion uno ----------
    if op_elegida == 1:
        cantidad = int(input("¿Cuantas especialidades ingresaras?: "))
        for i in range(cantidad):
                especialidad = input("Ingresa una especialidad: ").lower()
                while especialidad in lista_esp:
                    print("Especialidad ya ingresada.")
                    especialidad = input("Ingresa nuevamente la especialidad: ").lower()
                else: 
                    lista_esp.append(especialidad)
                    cupo = int(input("Ingresa su cupo: "))
                    lista_cupos.append(cupo)

#-------Opcion dos---------
    if op_elegida == 2:
        for i in range(len(lista_esp)):
            if not int(lista_cupos[i]) <= 0:
                print(f"{lista_esp[i]}: {lista_cupos[i]}")
            if all in lista_cupos <= 0:
                print("Ninguna especialidad con cupos disponibles")
    

#---------- Opcion tres -----------
    if op_elegida == 3:
        consulta = input("Especialidad que quiere consultar: ").lower()
        # ------ validando -----------
        while not consulta in lista_esp: 
            print("No encontrado en nuestra lista de especialidades")
            otra_vez = input("Desea ingresar otra especialidad? s/n: ").lower()
            
            if otra_vez == "s":
                consulta = input("Ingrese nuevamente: ").lower()
            else:
                break
        else:
            pos= lista_esp.index(consulta)
            print(f"\n Cupos de {consulta}: {lista_cupos[pos]}")

#---------- opcion cuatro ------------------
    if op_elegida == 4:
        for i in range(len(lista_esp)):
            if int(lista_cupos[i]) <= 0:
                print(f"{lista_esp[i]} - Cupos Agotados")

#---------opcion cinco------------
    if op_elegida == 5:
        nueva_esp = input("Especialidad que quiere agregar: ").lower()
        while nueva_esp in lista_esp: 
            print("Especialidad ya en lista.")
            otra_vez = input("Desea ingresar otra especialidad? s/n: ").lower()
            if otra_vez == "s":
                nueva_esp = input("Ingrese nuevamente: ").lower()
            else:
                break

        lista_esp.append(nueva_esp)
        nuevo_cupo = int(input("Cupos: "))
        lista_cupos.append(nuevo_cupo)

#---------------opcion seis---------------
    if op_elegida == 6:
        accion = input("Quiere reservar o cancelar? r/c: ").lower()
        
        if accion == "r": 
            esp = input("Que especialidad quiere reservar?: ").lower()
            # buscar si esta en la lista
            while not esp in lista_esp: 
                print("Especialidad no disponible.")
                otra_vez = input("Desea ingresar otra especialidad? s/n: ").lower()
                if otra_vez == "s":
                    nueva_esp = input("Ingrese nuevamente: ").lower()
                else:
                    break
            else:
            # si esta reservarla y restarle a los cupos
                pos= lista_esp.index(esp)
                lista_cupos[pos] -= 1
                print(f"\n Cupos acualizados de {esp}: {lista_cupos[pos]}")

        
        elif accion == "c": 
            esp = input("Que especialidad quiere cancelar?: ").lower()
            # buscar si esta en la lista
            while not esp in lista_esp: 
                print("Especialidad no disponible.")
                otra_vez = input("Desea ingresar otra especialidad? s/n: ").lower()
                if otra_vez == "s":
                    nueva_esp = input("Ingrese nuevamente: ").lower()
                else:
                    break
            else:
            # si esta reservarla y restarle a los cupos
                pos = lista_esp.index(esp)
                lista_cupos[pos] += 1
                print(f"\n Cupos acualizados de {esp}: {lista_cupos[pos]}")

        else:
            print("Ingrese los datos nuevamente por favor.")

# ------------siete-------------
    if op_elegida == 7:
        print("AGENDA COMPLETA:")
        for i in range(len(lista_esp)):
                print(f"{lista_esp[i]}: {lista_cupos[i]}")

#----------ocho----------------
    if op_elegida == 8:
        print("Saliendo...")
        menu_abierto = False
        break