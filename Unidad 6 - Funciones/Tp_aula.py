#______ 1. Funcion "Hola Mundo!"______

#---- funcion ----
def  imprimir_hola_mundo():
    print("Hola Mundo!")

#---- programa principal ----
imprimir_hola_mundo()

#______ 2. Funcion saludar usuario ______

#---- funcion ----
def  saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#---- programa principal ----
nombre = input("Nombre: ")
saludar_usuario(nombre)

#______ 3. Funcion info personal ______

#---- funcion ----
def  informacion_personal(nombre, apellido, edad, recidencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {recidencia}")

#---- programa principal ----
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
recidencia = input("Recidencia: ")
informacion_personal(nombre, apellido, edad, recidencia)

#______ 4. Funcion calcular area circulo ______

#---- funcion ----
def  calcular_area_circulo(radio):
    area = 3,14 * (radio**2)
    print(f"Area: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3,14 * radio
    print(f"Perimetro: {perimetro}")

#---- programa principal ----
radio = float(input("Radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#______ 5. Funcion horas y sec ______

#---- funcion ----
def  segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas.")

#---- programa principal ----
segundos = int(input("Segundos: "))
segundos_a_horas(segundos)


#______ 6. Funcion tabla multiplicar ______

#---- funcion ----
def tabla_multiplicar(numero):
    for i in range(10):
        print(f"{numero}x{i+1} = {numero*(i+1)}")


#---- programa principal ----
numero = int(input("Numero: "))
tabla_multiplicar(numero)

#______ 7. Funcion operaciones basicas ______

#---- funcion ----
def operaciones_basicas(a, b):
    resultados = (a + b, a - b, a * b, a / b)
    return resultados

#---- programa principal ----
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))

suma, resta, multi, divi = operaciones_basicas(a, b)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multi)
print("División:", divi)

#______ 8. Funcion imc ______

#---- funcion ----
def  calcular_imc(peso,altura):
    imc = peso / (altura*2)
    print(f"IMC: {imc}")

#---- programa principal ----
peso = input("Peso en kg: ")
altura = input("Altura en m: ")
calcular_imc(peso,altura)

#______ 9. Funcion temperaturas ______

#---- funcion ----
def  celsius_a_fahrenheit(celsius):
    faren = (celsius * 1.8) + 32
    print(f"{celsius} celsius son {faren} °F")

#---- programa principal ----
celsius = float(input("Grados celsius: "))
calcular_imc(celsius)

#______ 10. Funcion promedio ______

#---- funcion ----
def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    print(f"Promedio: {promedio}")

#---- programa principal ----
num1 = int(input("Ingresa la primer nota: "))
num2 = int(input("Ingresa la segunda nota: "))
num3 = int(input("Ingresa la tercer nota: "))

calcular_promedio(num1, num2, num3)