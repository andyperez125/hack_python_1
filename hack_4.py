"""
text: "fooziman" output => "foozimaN"
"""
def ultima_letra_mayuscula(palabra):
    if len(palabra) == 0:
        return palabra
    return palabra[:-1] + palabra[-1].upper()

# Solicitar al usuario que ingrese una palabra
palabra = "fooziman"
resultado = ultima_letra_mayuscula(palabra)
print(resultado)
