#Creamos un diccionario para mapear cada letra a su correspondiente caracter encriptado
encriptar = {
    'a': 'P', 'b': 'Q', 'c': 'R', 'd': 'S', 'e': 'T', 'f': 'U', 'g': 'V', 'h': 'W',
    'i': 'X', 'j': 'Y', 'k': 'Z', 'l': 'A', 'm': 'B', 'n': 'C', 'o': 'D', 'p': 'E', 'q': 'F',
    'r': 'G', 's': 'H', 't': 'I', 'u': 'J', 'v': 'K', 'w': 'L', 'x': 'M', 'y': 'N', 'z': 'O',
}

input_text = input("Ingrese el texto a encriptar: ")
output_text = ""

#Recorremos cada caracter del texto de entrada
for i in input_text:

    #Concatenamos el caracter encriptado al texto de salida
    if i.lower() in encriptar:
        output_text += encriptar[i]

    #En caso de que el caracter no este en el diccionario mandamos un mensaje de error
    else:
        print(f"Ingrese caracteres validos")
        exit()

#Mostramos el texto encriptado
print("Texto encriptado:", output_text)