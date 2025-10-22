# 1. Factorial de un número 
def factorial(n): 
    if n == 0 or n == 1: 
        return 1 
    else: 
        return n * factorial(n - 1) 

n = input("Ingresa un numero: ")
print(factorial(n))

#2. Serie de Fibonacci 
def fibonacci(n): 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = input("Ingresa un numero: ")
print(fibonacci(n))

# Potencia
def potencia(base, exponente): 
    if exponente == 0: 
        return 1 
    else: 
        return base * potencia(base, exponente - 1) 

b = input("Ingresa la base: ")
e = input("Ingresa el exponente: ")
print(potencia(b, e))

#4) Conversión de decimal a binario 
def decimal_a_binario(n): 
    if n == 0: 
        return "" 
    else: 
        return decimal_a_binario(n // 2) + str(n % 2)
    
n = input("Ingresa un numero: ")
print(decimal_a_binario(n))

#5) Verificar si una palabra es palíndromo 
def es_palindromo(palabra): 
    if len(palabra) <= 1: 
            return True 
    if palabra[0] != palabra[-1]: 
        return False 
    return es_palindromo(palabra[1:-1])

palabra = input("Ingresa una palabra: ")
print(es_palindromo(palabra))

#6) Suma de dígitos de un número 

def suma_digitos(n): 
    if n < 10: 
        return n 
    else: 
        return n % 10 + suma_digitos(n // 10)

n = input("Ingresa un numero: ")
print(suma_digitos(n))


#7) Contar bloques en una pirámide 
def contar_bloques(n): 
    if n == 1: 
        return 1 
    else: 
        return n + contar_bloques(n - 1) 
    
n = input("Ingresa un numero: ")
print(contar_bloques(n))


#8) Contar apariciones de un dígito en un número 
def contar_digito(numero, digito): 
    if numero == 0: 
        return 0 
    else:
        ultimo = numero % 10 
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito) 

n = input("Ingresa un numero: ")
print(contar_digito(n))
