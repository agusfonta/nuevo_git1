# EJ COMPLEMENTARIO INSTITUTO DE INGLES 25 de Agosto

fecha_entera = input("Ingrese la fecha en formato dia de la semana, deje un espacio y DD/MM (ej: viernes, 15/04): ")

#Separar la frase en dia de la semana, dia en numero y mes:

fecha_entera = fecha_entera.split(", ")
dia_sem = fecha_entera[0]
dia_barra_mes = fecha_entera[1].split("/")


dia = dia_barra_mes[0]
mes = dia_barra_mes[1]
dia_sem = dia_sem.lower()

if (int(dia) > 31) or (int(mes) > 12) or (dia_sem != "lunes" or dia_sem != "martes" or dia_sem != "miercoles" or dia_sem != "jueves" or dia_sem != "viernes"):
    print("Dato ingresado incorrectamente")
else:
    if dia_sem == "lunes" or dia_sem == "martes" or dia_sem == "miercoles":
        examen = input("Hubo examen ese dia? Responder con si o no: ")
        examen.lower()
        if examen == "si":
            aprobados = int(input("Ingrese la cantidad de aprobados: "))
            desaprobados = int(input("Ingrese la cantidad de desaprobados: "))
            total = aprobados + desaprobados
            porcentaje_aprob = (aprobados * 100) / total
            print(f"El porcentaje de aprobados es de {porcentaje_aprob}")
        else:
            print("Todavia no hubo examen.")

    elif dia_sem == "jueves":
        asistencia = int(input("Ingrese el porcentaje de asistencia a clase solo en numeros: "))
        if asistencia > 50 :
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")

    elif dia_sem == "viernes" and (dia == "01" and mes == "01" or mes == "07"):
        print("Comienzo de nuevo ciclo")
        alumnos_nuevo_ciclo= int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel_por_alumno = int(input("Ingrese el arancel por alumno: "))
        ingreso_total = print(f"El ingreso total es de {alumnos_nuevo_ciclo * arancel_por_alumno}")

