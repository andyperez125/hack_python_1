"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

# Lista de números
lista_numeros = [1, 2, 3]

# Inicializar variables
i = 0
resultado = ""

# Usar un ciclo while para recorrer la lista
while i < len(lista_numeros):
    resultado += str(lista_numeros[i])
    if i < len(lista_numeros) - 1:
        resultado += "@"
    i += 1

# Imprimir el resultado
print(resultado)
