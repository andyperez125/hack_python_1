def convertir_a_mayusculas(palabra):
    return palabra.lower()

def main():
    palabra = "FOOZIMAN"
    palabra_mayusculas = convertir_a_mayusculas(palabra)
    print("La palabra en mayúsculas es:", palabra_mayusculas)

if __name__ == "__main__":
    main()
    