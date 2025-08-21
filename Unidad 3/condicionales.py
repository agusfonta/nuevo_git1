
#___________ PUNTO 10 ______________
print("______Punto 10 ______")

hemisferio = input("Ingrese en que hemisferio se encuentra(N o S): ")
dia = int(input("Ingrese que dia es: "))
mes = input("Ingrese que mes es: ")

if (mes=="diciembre" and dia >=21) or mes == "enero" or mes == "febrero" or (mes=="marzo" and dia <=20):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")
if (mes=="marzo" and dia >=21) or mes == "abril" or mes == "mayo" or (mes=="junio" and dia <=20):
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")
if (mes=="junio" and dia >=21) or mes == "julio" or mes == "agosto" or (mes=="septiembre" and dia <=20):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")
if (mes=="septiembre" and dia >=21) or mes == "octubre" or mes == "noviembre" or (mes=="diciembre" and dia <=20):
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")

