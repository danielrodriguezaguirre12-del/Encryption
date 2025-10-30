import random
palabra1, palabra2 = input("Palabra 1: "), input("Palabra 2: ")
texto = palabra1 + " " + palabra2
clave = [random.randint(0, 1) for i in texto]
encriptado = ''.join(chr(ord(c) ^ clave[i]) for i, c in enumerate(texto))
desencriptado = ''.join(chr(ord(c) ^ clave[i]) for i, c in enumerate(encriptado))
print(f"Original: {texto}\nClave: {clave}\nEncriptado: {encriptado}\nDesencriptado: {desencriptado}")            
