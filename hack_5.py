"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    palabra = "fooziman"
    reemplazos = {'a': '@', 'i': '1', 'o': '0'}
    nueva_palabra = ""
    for letra in palabra:
        if letra in reemplazos:
            nueva_palabra += reemplazos[letra]
        else:
            nueva_palabra += letra
    return nueva_palabra
