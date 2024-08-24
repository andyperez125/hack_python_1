"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def convertir_mayusculas(palabra):
    return palabra.upper()

def reemplazar_letras(palabra):
    palabra = palabra.replace('O', '0')
    palabra = palabra.replace('I', '1')
    palabra = palabra.replace('A', '@')
    return palabra

def convertir_a_lista(palabra):
    return list(palabra)

# Palabra inicial
palabra = "fooziman"

# Convertir a mayúsculas
palabra_mayus = convertir_mayusculas(palabra)

# Reemplazar letras
palabra_modificada = reemplazar_letras(palabra_mayus)

# Convertir la palabra modificada en una lista de caracteres
lista_resultado = convertir_a_lista(palabra_modificada)

# Imprimir la lista resultante
print(lista_resultado)
