import os

mensaje = input("Ingrese el mensaje a cifrar: ")

clave = os.urandom(len(mensaje))

mensaje_bytes = mensaje.encode()

cifrado = bytes([m ^ k for m, k in zip(mensaje_bytes, clave)])

descifrado = bytes([c ^ k for c, k in zip(cifrado, clave)]).decode()

print("Mensaje original:", mensaje)
print("Clave:", clave)
print("Cifrado:", cifrado)
print("Descifrado:", descifrado)