import re 

pattern = "Hola"

text = "Hola mundo"

result = re.search(pattern, text)

if(result):
    print("Patron encontrado.")
else:
    print("No se ha encontrado el patron")

# --------------------------------

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

pattern = "midu"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())


# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
import re

files = "file1.txt file2.pdf midu-of.webp secret.txt"

pattern = r"\S+\.txt"  # Busca palabras que terminan en .txt

matches = re.findall(pattern, files) #Encuentra todas las palabras que terminen por el patron

print(matches)


# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
# Elimina el prefijo si está presente
phone = re.sub(r"^\+34\s?", "", phone)

print(phone)


# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
# \b 

pattern = r"\b(man|fan|ban)\b"

matches = re.findall(pattern, text)

print(matches) 