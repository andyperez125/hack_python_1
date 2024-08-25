"""
text: "fooziman" output => "foozimaN"
"""


def fn_hack_4():
    palabra = "fooziman"
    if len(palabra) == 0:
        return palabra
    return palabra[:-1] + palabra[-1].upper()
