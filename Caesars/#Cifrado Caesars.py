#Cifrado Caesars 

texto = input("Ingrese el texto a cifrar: ")

if texto == texto.upper():
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
else:
    abecedario = "abcdefghijklmnopqrstuvwxyz"

cifrado = ""
desplazamiento = -5

for i in texto:
    if i in abecedario:
        cifrado += abecedario[(abecedario.index(i) + desplazamiento) % len(abecedario)]
    else:
        cifrado += i

print("Texto cifrado:", cifrado)
    