
RUTA = "precios.csv"
import csv

# =============================
# FUNCIONES
# =============================
def menu():
    inicializar_archivo()

    while True:
        print("====== MENÚ DE PRODUCTOS ======")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Salir")
        print("===============================")

        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                mostrar_productos()
            case "2":
                agregar_producto()
            case "3":
                eliminar_producto()
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.\n")

def inicializar_archivo():
    """Crea el archivo CSV con encabezados si no existe."""
    try:
        # Intentamos abrirlo para leer
        with open(RUTA, "r", encoding="utf-8") as archivo:
            pass  # Si existe, no hacemos nada
    except FileNotFoundError:
        # Si no existe, lo creamos
        with open(RUTA, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, delimiter = ";", fieldnames=["nombre", "precio"])
            escritor.writeheader()


def mostrar_productos():
    try:
        with open(RUTA, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter = ";")
            productos = list(lector)

            if not productos:
                print("No hay productos registrados.")
                return

            total = 0
            print("\nProductos registrados:")
            for p in productos:
                try:
                    nombre = p["nombre"]
                    precio = float(p["precio"])
                    total += precio
                    print(f"- {nombre} → ${precio:.2f}")
                except ValueError:
                    print(f" Error al convertir el precio del producto: {p}")

            print(f"Total de precios: ${total:.2f}\n")

    except FileNotFoundError:
        print("Archivo no encontrado. Creando nuevo archivo...")
        inicializar_archivo()

    except ValueError:
        print("Value Error")



def validar_nombre():
    # --- Validar nombre ---
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        break  
    return nombre

def validar_precio():
    # --- Validar precio ---
    while True:
        try:
            precio_str = input("Ingrese el precio: ").strip()
            precio = float(precio_str)
            if precio <= 0:
                raise ValueError("El precio debe ser positivo.")
            break
        except ValueError as e:
            print(f"Error, ingresa un numero")
    
    return precio

def agregar_producto():
    """Agrega un nuevo producto al archivo."""
    nombre = validar_nombre()
    precio = validar_precio()

    with open(RUTA, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"], delimiter=";")
        escritor.writerow({"nombre": nombre, "precio": precio})

    print("Producto agregado correctamente.\n")


def eliminar_producto():
    """Elimina un producto por su nombre."""
    nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()
    encontrado = False

    try:
        with open(RUTA, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter=";")
            productos = list(lector)

        nuevos_productos = [p for p in productos if p["nombre"].lower() != nombre_eliminar.lower()]
        if len(nuevos_productos) < len(productos):
            encontrado = True

        if encontrado:
            with open(RUTA, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"], delimiter=";")
                escritor.writeheader()
                escritor.writerows(nuevos_productos)
            print(f"Producto {nombre_eliminar.capitalize()} eliminado correctamente.\n")
        else:
            print("El producto no existe.\n")

    except FileNotFoundError:
        print("El archivo no existe. No hay productos para eliminar.")
    
# =============================
# EJECUCIÓN
# =============================
if __name__ == "__main__":
    menu()
