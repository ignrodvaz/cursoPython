###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, 10)
lista[0] = 0

print(lista)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
print("Lista A: ", lista_a)
print("Lista B: ", lista_b)
lista_a.extend(lista_b)
print("Extend A y B: ", lista_a)
lista_a.remove(1)
print("Remove 1: ", lista_a)
print(lista_a.pop(3))
print("Pop 3: ", lista_a)
lista_b.clear()
print("Clear B: ", lista_b)


# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
del lista[2:5]
print(lista)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
cantidad_dos = lista.count(2)
esta_el_siete = 7 in lista
print(f"Lista ordenada: {lista}") #Output: Lista ordenada: [1, 2, 2, 4, 5, 8, 9]
print(f"Cantidad de 2: {cantidad_dos}") #Output: Cantidad de 2: 2
print(f"¿Está el 7?: {esta_el_siete}") #Output: ¿Está el 7?: False

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print("Original: ", original)
print("Copia 1: ", copia_1)
print("Copia 2: ", copia_2)
print("Referencia: ", referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

lista = ["Manzana", "pera", "BANANA", "naranja"]

lista = sorted(lista)
print(lista)

lista.sort(key = str.lower)
print(lista)