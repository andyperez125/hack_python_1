"""
loop: while [] output => [5,4,3,2,1,0]
"""

def cuenta_regresiva():
    numero = 5
    while numero > 0:
        print(numero)
        numero -= 1

# Llamar a la función
cuenta_regresiva()
