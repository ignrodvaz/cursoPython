# ###
# # EJERCICIOS (while)
# ###

import os 
os.system("clear")

# # Ejercicio 1: Cuenta atrás
# # Imprime los números del 10 al 1 usando un bucle while.

def diez_primeros_numeros():
    for i in range(10, 0,-1):
        print(i)

diez_primeros_numeros()

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nSegundo ejercicio")
def suma_pares():
    for i in range(2, 21, 2):
        print(i)

suma_pares()

# # Ejercicio 3: Factorial de un número
# # Pide al usuario que introduzca un número entero positivo.
# # Calcula su factorial usando un bucle while.
# # El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# # 5! = 5 x 4 x 3 x 2 x 1 = 120.

num = int(input("Introduce un numero: "))
resultado = 1
def factorial(num, resultado):
    for i in range(num, 0, -1):
        resultado *= i
    print(resultado)

factorial(num, resultado)

# # Ejercicio 4: Validación de contraseña
# # Pide al usuario que introduzca una contraseña.
# # La contraseña debe tener al menos 8 caracteres.
# # Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# # Si la contraseña es válida, imprime "Contraseña válida".

password = input("Introduce una contraseña: ")
contador = 0

def validacion(password, contador):
    for i in range(0, len(password)):
        contador += 1
    if(contador >= 8):
        print("La contrasena tiene", contador, "caracteres.")
    else:
        print("La contrasena tiene", contador, "caracteres.")

validacion(password, contador)

# # Ejercicio 5: Tabla de multiplicar
# # Pide al usuario que introduzca un número.
# # Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

num = int(input("Introduce un numero: "))
multiplicacion = 0
def tabla_multiplicacion(num, multiplicacion):
    for i in range(1, 11):
        multiplicacion = num * i
        print(num, "x", i, "=", multiplicacion)

tabla_multiplicacion(num, multiplicacion)

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

n = int(input("Introduce un numero entero: "))
numero = 2

def numero_primo(n, numero):
    while(numero <= n):
        es_primo = True
        divisor = 2
        while divisor * divisor <= numero:
            if numero % divisor == 0:
                es_primo = False
                break
            divisor += 1
        if es_primo==True:
            print(numero)

        numero += 1

numero_primo(n, numero)