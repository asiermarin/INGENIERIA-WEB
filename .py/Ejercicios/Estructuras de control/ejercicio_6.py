# Mostrar el número más alto

print("Bienvenido")
peticiones = 0
numeroMasAlto = 0
entrada = ""

while(peticiones < 6 or entrada != "fin"):
    peticiones += 1
    entrada = input()
    if (entrada != "fin"):
        nuevoNumero = int(entrada)
    else:
        print("La entrada es un string")

    if (nuevoNumero >= numeroMasAlto):
        numeroMasAlto = nuevoNumero
print(numeroMasAlto)

