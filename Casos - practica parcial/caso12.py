# Turismo y excursiones

#Menu 1.ingresar excursiones
#   2. ingresar cupos
#   3. Mostrar oferta/cupos
#   4. Consultar cupo por excursion
#   5. Mostrar excursiones sin cupo
#   6. Actualizar cupos de una excursion
#   7. Ver todo
#   8. Salir

andando= True
op=0

excursiones = []
cupos = []

while andando: 

    print("\n_____ MENU ______"\
    "\n 1. Ingresar excursiones "\
    "\n 2. Ingresar cupos"\
    "\n 3. Mostrar todo (oferta/cupos)"\
    "\n 4. Consultar cupo por excursion"\
    "\n 5. Mostrar excursiones sin cupo"\
    "\n 6. Actualizar cupos de una excursion"\
    "\n 7. Salir"\
    )

    
    op = input("Ingresa una opcion: ")

    if not op.isnumeric():
        print("Opcion incorrecta")
        continue

    match op:

        case "1" : 
            print("--- 1. Agregar excursiones --- ")
            cant = input("¿Cuantas quieres ingresar? Responde con numeros: ")
            while not (cant.isdigit()):
                cant = input("Ingresa un numero por favor: ")
            else:
                for i in range(int(cant)):
                    excursion = input("Ingresa la excursion: ").lower()
                    excursiones.append(excursion)
                    cupos.append(0)
                else: 
                    break

        case "2":
            print("--- 2. Agregar cupos --- ")
            if len(excursiones) > 0:
                for i in range(len(excursiones)):
                    print(f"Ingresa los cupos de {str(excursiones[i]).capitalize()}",end= " ")
                    cupo = input("-> ")
                    if cupo.isdigit():
                        cupos[i] = int(cupo)
                    else:
                        print(f"Cupos invalidos. Ingresa neuvamente los cupos de {str(excursiones[i]).capitalize()}",end= " ")
                        cupo = input("-> ")
                        cupos[i] = int(cupo)
                else:
                    break
            else: 
                print("No hay excursiones ingresadas.")
        
        case "3":
            print("--- 3. Listado de excursiones y cupos --- ")

            if len(excursiones)>0:
                for i in range(len(excursiones)):
                    print(f"{str(excursiones[i]).capitalize()} tiene {cupos[i]} cupos.")
                else: 
                    break
            else:
                print("No hay excursiones ingresadas todavia. Elije la opcion 1 para ingresarlas.")
        
        case "4":
            print("--- 4. Consultar cupo de excursion --- ")

            if len(excursiones)>0:
                consulta = "s"
                while consulta == "s":
                    excu = input("Excursion que deseas consultar: ").lower()

                    if excu in excursiones:
                        pos = excursiones.index(excu)
                        print(f"{str(excu).capitalize()} tiene {cupos[pos]} cupos.")
                    else: 
                        excu = input("Excursion no disponible. Ingresa nuevamente: ").lower()
                        pos = excursiones.index(excu)
                        print(f"{str(excu).capitalize()} tiene {cupos[pos]} cupos.")

                    consulta = input("Quieres consultar otro? s/n: ").lower()

                    if not (consulta == "s" or consulta == "n"):
                        consulta = input("Responde con s o n por favor: ").lower()
                else: 
                    break

            else:
                print("No hay excursiones ingresadas todavia. Elije la opcion 1 para ingresarlas.")

        case "5":
            print("--- 5. Excursiones sin cupo --- ")
            if len(excursiones)>0:
                    impr = 0
                    for i in range(len(excursiones)):
                        if cupos[i] == 0:
                            print(f"{str(excursiones[i]).capitalize()} tiene {cupos[i]} cupos.")
                            impr = impr + 1
                    else:
                        if impr == 0:
                            print("No hay excursiones sin cupo.")
                            break
                        else:
                            break
                
            else:
                print("No hay excursiones ingresadas todavia. Elije la opcion 1 para ingresarlas.")
                break

        case "6":
            print("--- 6. Actualizar cupo de excursion --- ")
            andando = True

            if len(excursiones)>0:
                if andando == True:
                    excu = input("Excursion que deseas actualizar: ").lower()
                    pos = excursiones.index(excu)
                    accion = input("¿Quiere sumar o restar cupos? s o r:").lower()

                    if accion == "s":
                        cant = input("Ingrese el numero (sin signos): ")
                        if cant.isdigit():
                            cupos[pos] = int(cupos[pos]) + int(cant)
                            print("Actualizacion realizada correctamente.")
                        else: 
                            cant = input("Por favor ingrese el numero sin signos: ")

                    elif accion == "r":
                        cant = input("Ingrese el numero (sin signos): ")
                        if cant.isdigit():
                            cupos[pos] = int(cupos[pos]) - int(cant)
                            print("Actualizacion realizada correctamente.")
                        else: 
                            cant = input("Por favor ingrese el numero sin signos: ")

            else:
                print("No hay excursiones ingresadas todavia. Elije la opcion 1 para ingresarlas.")
                break
        
        case "7":
            print("---7. Salir --- ")
            print(" Saliendo... ")
            andando = False
            break 

        case _:
            print("Opcion mal ingresaba")
            continue


            






