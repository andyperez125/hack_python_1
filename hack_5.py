"""
text: "fooziman" output => "f00z1m@n"
"""

def reemplazar_letras(palabra):
    reemplazos = {'a': '@', 'i': '1', 'o': '0'}
    nueva_palabra = ""
    for letra in palabra:
        if letra in reemplazos:
            nueva_palabra += reemplazos[letra]
        else:
            nueva_palabra += letra
    return nueva_palabra

# Solicitar al usuario que ingrese una palabra
palabra = "fooziman"
resultado = reemplazar_letras(palabra)
print( resultado)
