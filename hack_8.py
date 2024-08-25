"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    lista_numeros = [1, 3, 5, 7, 9]
    return [num for num in lista_numeros if num in [3, 5, 7]]
