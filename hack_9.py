"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    lista_numeros = [1, 2, 3]
    resultado = []
    for i in range(len(lista_numeros)):
        resultado.append(lista_numeros[i])
        resultado.append('@')
    return resultado

