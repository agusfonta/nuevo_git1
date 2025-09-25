# Caso 7 alumnos y asistencias 

l_alumnos = []
l_asist = []
op = 0
menu = True


while menu == True: 

    #Menu
    print("\n------ Menu ------")
    print("\n 1. Ingresar estudiantes " \
    "\n 2. Ingresar asistencias" \
    "\n 3. Mostrar listado" \
    "\n 4. Cosultar asistencia de un estudiante" \
    "\n 5. Mostar listado de estudiantes con 0 asistencia" \
    "\n 6. Actualizar asistencia de un estudiante" \
    "\n 7. Salir")

    op = int(input("\n Ingrese el numero de la opcion que desea realizar: "))
    op_posibles = [1,2,3,4,5,6,7]

    if op in op_posibles:
        if op==1: 
            print("\n--- 1. Ingresar alumnos ---")
            cant_alumnos = input("Ingrese la cantidad de alumnos del curso, en numeros: ")
            if cant_alumnos.isdigit() and int(cant_alumnos)>0 :
                for i in range(int(cant_alumnos)):
                    nombre = input("Ingrese el nombre del estudiante: ")
                    l_alumnos.append(nombre.lower())
                    l_asist.append(int(0))
            else:
                cant_alumnos = input("Dato Invalido. Por favor ingrese la cantidad de alumnos en numeros: ")

        elif op==2: 
            print("\n--- 2. Ingresar asistencias ---")
            for i in range(len(l_alumnos)):
                print(f"Ingrese asistencia de {str(l_alumnos[i]).capitalize()}")
                asistencia = input("-> ")
                if asistencia.isdigit() and int(asistencia)>=0 :
                    l_asist[i] = int(asistencia)
                else: 
                    asistencia = int(input("Dato Invalido. Por favor ingrese la asistencia en numeros: "))
        
        elif op==3:
            print("\n---3. Mostrar lista  ---")
            for i in range(len(l_alumnos)):
                print(f"{str(l_alumnos[i]).capitalize()}: {l_asist[i]} asistencias.")

        elif op==4:
            print("\n--- 4. Cosultar asistencia de un estudiante ---")
            andando = True
            while andando == True:
                estudiante = input("Ingrese el estudiante: ").lower()

                if estudiante in l_alumnos: 
                    pos = l_alumnos.index(estudiante)
                    print(f"{str(estudiante).capitalize()} tiene {l_asist[pos]} asistencias.")

                    pregunta = input("Quiere consultar otro alumno? si/no: ").lower()
                    if pregunta == "si":
                        andando = True
                    elif pregunta == "no":
                        andando = False
                    else: 
                        pregunta = input("Por favor responda con si/no: ").lower()
                else: 
                    print("Estudiante no encontrado en la lista.")

        elif op==5:
            print("\n--- 5. Alumnos sin asistencia ---")
            for i in range(len(l_alumnos)):
                if l_asist[i] == 0:
                    print(f"{str(l_alumnos[i]).capitalize()}: {l_asist[i]} asistencias.")
                else:
                    continue

        elif op==6:
            
            print("\n--- 6. Actualizar asistencia de un estudiante ---")
            andando = True
            while andando == True:
                estudiante = input("Ingrese el estudiante: ").lower()
                if estudiante in l_alumnos: 
                    pos = l_alumnos.index(estudiante)
                    l_asist[pos] = int(l_asist[pos]) + 1

                    print(f"Actualizacion realizada. {str(estudiante).capitalize()} tiene {l_asist[pos]} asistencias.")
                    
                    pregunta = input("Quiere consultar otro alumno? si/no: ").lower()
                    if pregunta == "si":
                        andando = True
                    elif pregunta == "no":
                        andando = False
                    else: 
                        pregunta = input("Por favor responda con si/no: ").lower()
                else: 
                    print("Estudiante no encontrado en la lista.")

        elif op==7:
            print("\n... Saliendo ...")
            print("________________")
            menu = False

    else: 
        op = int(input("Ingrese una opcion valida, en numeros por favor: "))