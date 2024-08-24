"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def filtrar_numeros(lista):
    # Filtra los números 3, 5 y 7 de la lista
    numeros_filtrados = [num for num in lista if num in [3, 5, 7]]
    return numeros_filtrados

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = filtrar_numeros(lista_numeros)
print( resultado)
