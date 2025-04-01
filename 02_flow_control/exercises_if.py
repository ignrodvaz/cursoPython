###
# EJERCICIOS
###
import os
os.system('clear')
# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1 = input("Introduce un numero:")
num2 = input("Introduce otro numero:")

if num1>num2:
    print("El primer numero es mayor")
elif num1<num2:
    print("El segundo numero es mayor")
else:
    print("Los numeros son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num3 = input("Introduce un numero:")
num4 = input("Introduce otro numero:")
operacion = input("Introduce la operacion (+, -, *, /):")

if operacion == "+":
    print(int(num3)+int(num4))
elif operacion == "-":
    print(int(num3)-int(num4))
elif operacion == "*":
    print(int(num3)*int(num4))
elif operacion == "/":
    if num4 == 0:
        print("No se puede dividir entre 0")
    else:
        print(int(num3)/int(num4))
else:
    print("Operacion no valida")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = input("Introduce un año:")

if(int(year)%4 == 0):
    if(int(year)%100 == 0):
        if(int(year)%400 == 0):
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad =int(input("Introduce una edad:"))

if(edad>=0 and edad<=2):
    print("Bebé")
elif(edad>=3 and edad<=12):
    print("Niño")
elif(edad>=13 and edad<=17):
    print("Adolescente")
elif(edad>=18 and edad<=64):
    print("Adulto")
else:
    print("Adulto mayor")