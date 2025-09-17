# Tarjeta Sube
# 1. Ingresar num de tarjeta -> validar 16 num
# 2. Ingresar saldo
# 3. Mostrar todas las tarj y saldos
# 4. Consultar saldo por numero
# 5. Tarjetas con saldo negativo
# 6. Cargar/debitar saldo
# 7. Salir

sube = []
saldo = []
op = 0
andando = True

while andando == True:

    #Mostrar menu

    print("\n-------- Menu ----------")
    print("\n 1. Ingresar numero de tarjeta " \
    "\n 2. Ingresar saldo" \
    "\n 3. Mostrar todas las tarjetas y saldos" \
    "\n 4. Consultar saldo por numero" \
    "\n 5. Tarjetas con saldo negativo"
    "\n 6. Cargar/debitar saldo" \
    "\n 7. Salir" \
    )

    op = int(input("\n- Ingresa la opcion: "))

    #Opciones
    if op == 1:
        cant = input("Cuantas tarjetas quieres ingresar?: ")
        if cant.isdigit(): 
            for i in range(int(cant)):
                tarjeta = input("Ingresa un numero de tarjeta SUBE: ")
                if len(tarjeta) == 16: 
                    sube.append(tarjeta)
                else:
                    tarjeta = input("Por favor ingresa un numero de tarjeta SUBE que contenga 16 digitos: ")
        else: 
            cant = input("Ingresa un numero, por favor: ")

    if op == 2: 
        for i in range(int(cant)):
            tipo = input("El saldo es negativo o positivo. n/p: ").lower

            if tipo == "p":
                print(f"Ingresa el saldo de la tarjeta {sube[i]}")
                dinero = input("-> $")
                if dinero.isdigit() and int(dinero)> 0:
                    saldo.append(int(dinero))
                else:
                    print(f"Ingresa un saldo valido, por favor")
                    dinero = input("-> $")
            
            elif tipo == "n":
                print(f"Ingresa el saldo de la tarjeta {sube[i]} solo en numeros (sin signo -)")
                dinero = input("-> $- ")
                if dinero.isdigit() and int(dinero)< 0:
                    saldo.append(int(dinero))
                else:
                    print(f"Ingresa un saldo valido, por favor solo numeros")
                    dinero = input("-> $-")
            else: 
                tipo = input("Responda con n o p, por favor: ").lower
    
    if op == 3:
        for i in range(len(sube)):
            print(f"Tarjeta: {sube[i]} -> Saldo: ${saldo[i]}")

    if op == 4: 
        otro = "si"
        while otro == "si":
            tarjeta = input("Ingresa el n° de la SUBE: ")
            if len(tarjeta) == 16 and tarjeta.isdigit():
                pos = sube.index(tarjeta)
                print(f"El saldo de la SUBE - {tarjeta} es de {saldo[pos]}.")
            else:
                print("Ingresa un n° de SUBE valido: ")

            otro = input("¿Quiere consultar otra? si/no: ?").lower()
            
    if op == 5:
        for i in range(len(sube)):
            if saldo[i] <= 0:
                print(f"Tarjeta {sube[i]}: ${saldo[i]}")
            else:
                continue 

    if op == 6:
        accion = input("¿Quiere cargar o debitar saldo? (responda con c/d):").lower()

        if accion == "c":
            tarjeta = input("Ingresa el n° de la SUBE: ")
            if len(tarjeta) == 16 and tarjeta.isdigit():
                cargar = input("¿Cuanto saldo quiere cargar?: ")
                if cargar.isdigit():
                    pos = sube.index(tarjeta)
                    saldo[pos] = int(saldo[pos]) + int(cargar)
                else:
                    cargar = input("Ingrese un saldo valido: ")
            else: 
                tarjeta = input("Ingresa el n° de la SUBE nuevamente. Asegurese de que contenga 16 caracteres: ")

            # quiere cargar otra?

        elif accion == "d":
            tarjeta = int(input("Ingresa el n° de la SUBE: "))
            if len(tarjeta) == 16 and tarjeta.isdigit():
                cargar = input("¿Cuanto saldo quiere debitar?: ")
                if cargar.isdigit():
                    pos = sube.index(tarjeta)
                    saldo[pos] = int(saldo[pos]) - cargar
                else:
                    cargar = input("Ingrese un saldo valido: ")
            else: 
                tarjeta = input("Ingresa el n° de la SUBE nuevamente. Asegurese de que contenga 16 caracteres: ")

        else: 
            accion = input(" Respuesta invalida, por favor responda con ""C"" para cargar o ""D"" para debitar:").lower()

    if op == 7:
        print("...Saliendo...")
        print(" ______________")
        andando = False


