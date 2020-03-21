lista1 = [12, 56, 89, 45 ,14, 5 ,7]
lista2 = [56, 45, 95, 75, 32, 42, 1, 5, 6]

listaNumerosCoincidentes = []

for numero in lista1:
    for otroNumero in lista2:
        if(numero == otroNumero):
            listaNumerosCoincidentes.append(numero)


print(listaNumerosCoincidentes)