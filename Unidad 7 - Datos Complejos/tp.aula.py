#______ 1. Agregar frutas ______

#---- funcion ----
def agregar_frutas(precios):
    precios["Naranja"] = 1200
    precios["Manzana"] = 1500
    precios["Pera"] = 2300
    return precios

#---- programa principal ----
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas = agregar_frutas(precios_frutas)
print("Diccionario con frutas agregadas:", precios_frutas)


#______ 2. Actualizar precios ______

#---- funcion ----
def actualizar_precios(precios):
    precios["Banana"] = 1330
    precios["Manzana"] = 1700
    precios["Melón"] = 2800
    return precios

#---- programa principal ----
precios_frutas = actualizar_precios(precios_frutas)
print("Diccionario con precios actualizados:", precios_frutas)


#______ 3. Lista de frutas ______

lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

#______ 4. Agenda telefonica ______

#---- funcion ----
def crear_agenda():
    agenda = {}
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
        telefono = input(f"Ingrese el número de {nombre}: ")
        agenda[nombre] = telefono
    return agenda

def consultar_agenda(agenda, nombre):
    if nombre in agenda:
        print(f"El número de {nombre} es {agenda[nombre]}")
    else:
        print("Ese contacto no existe en la agenda.")

#---- programa principal ----
agenda = crear_agenda()
nombre_buscar = input("Ingrese el nombre a consultar: ")
consultar_agenda(agenda, nombre_buscar)


#______ 5. Analizar frase ______

#---- funcion ----
def analizar_frase(frase):
    palabras = frase.split()
    palabras_unicas = set(palabras)
    
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return palabras_unicas, contador

#---- programa principal ----
frase = input("Ingrese una frase: ")
unicas, cantidad= analizar_frase(frase)

print("Palabras únicas: ", unicas)
print("Cantidad de palabras: ", cantidad)

#______ 6. Promedio alumnos ______

#---- funcion ----
def cargar_alumnos():
    alumnos = {}
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
            notas.append(nota)
        alumnos[nombre] = tuple(notas)
    return alumnos

def mostrar_promedios(alumnos):
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es {promedio:.2f}")

#---- programa principal ----
alumnos = cargar_alumnos()
mostrar_promedios(alumnos)


#______ 7. Parciales ______

#---- funcion ----
def analizar_parciales(parcial1, parcial2):
    ambos = parcial1 & parcial2
    solo_uno = parcial1 ^ parcial2
    al_menos_uno = parcial1 | parcial2
    
    print("Aprobaron ambos parciales:", ambos)
    print("Aprobaron solo uno:", solo_uno)
    print("Aprobaron al menos uno:", al_menos_uno)

#---- programa principal ----
parcial1 = {9, 2, 5, 7, 5} # ALUMNOS: 2="Juan"| 5="Celeste"| 6="Maria" | 7="Carlos" | 9="Ana" | 10="Bruno"
parcial2 = {7, 5, 6, 10, 8}

analizar_parciales(parcial1, parcial2)


#______ 8. Stock productos ______

#---- funcion ----
def gestionar_stock():
    stock = {"Arroz": 20, "Fideos": 15, "Pan": 10}
    
    producto = input("Ingrese el producto que desea consultar o agregar: ")
    if producto in stock:
        print(f"Stock actual de {producto}: {stock[producto]}")
        agregar = int(input("Ingrese unidades a agregar: "))
        stock[producto] += agregar
        print(f"Nuevo stock de {producto}: {stock[producto]}")
    else:
        unidades = int(input(f"Ingrese stock inicial para {producto}: "))
        stock[producto] = unidades
        print(f"Producto {producto} agregado con stock {unidades}")
    
    return stock

#---- programa principal ----
stock_final = gestionar_stock()
print("Stock final:", stock_final)


#______ 9. Agenda eventos ______

#---- funcion ----
def crear_agenda_eventos():
    agenda = {}
    for i in range(3):
        dia = input("Ingrese el día (ej: Lunes): ")
        hora = input("Ingrese la hora (ej: 10:00): ")
        evento = input("Ingrese el evento: ")
        agenda[(dia, hora)] = evento
    return agenda

def consultar_evento(agenda, dia, hora):
    clave = (dia, hora)
    if clave in agenda:
        print(f"El evento en {dia} a las {hora} es: {agenda[clave]}")
    else:
        print("No hay evento en esa fecha y hora.")

#---- programa principal ----
agenda_eventos = crear_agenda_eventos()
dia = input("Ingrese día a consultar: ")
hora = input("Ingrese hora a consultar: ")
consultar_evento(agenda_eventos, dia, hora)


#______ 10. Invertir diccionario ______

#---- funcion ----
def invertir_diccionario(diccionario):
    nuevo_diccionario = {}
    for pais, capital in diccionario.items():
        nuevo_diccionario[capital] = pais
    return nuevo_diccionario

#---- programa principal ----
paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}
capitales = invertir_diccionario(paises)
print("Diccionario invertido:", capitales)
