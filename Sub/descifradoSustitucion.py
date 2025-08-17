#Creamos un diccionario para mapear cada letra a su correspondiente caracter desencriptado
desencriptar = {
    'P': 'a', 'Q': 'b', 'R': 'c', 'S': 'd', 'T': 'e', 'U': 'f', 'V': 'g', 'W': 'h',
    'X': 'i', 'Y': 'j', 'Z': 'k', 'A': 'l', 'B': 'm', 'C': 'n', 'D': 'o', 'E': 'p', 'F': 'q',
    'G': 'r', 'H': 's', 'I': 't', 'J': 'u', 'K': 'v', 'L': 'w', 'M': 'x', 'N': 'y', 'O': 'z',
}

input_text = input("Ingrese el texto a desencriptar: ")
output_text = ""

#Recorremos cada caracter del texto de entrada
for i in input_text:

    #Concatenamos el caracter desencriptado al texto de salida
    if i.upper() in desencriptar:
        output_text += desencriptar[i]

    #En caso de que el caracter no este en el diccionario mandamos un mensaje de error
    else:
        print(f"Ingrese caracteres validos")
        exit()

#Mostramos el texto desencriptado
print("Texto desencriptado:", output_text)