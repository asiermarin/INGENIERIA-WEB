usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },

    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },

    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

print("INTRODUCE USUARIO: ")
nombre = input()
print("INTRODUCE CONTRASENA:")
contrasena = input()

listaUsuario = []
listaUsuario.append(usuarios["iperurena"]["nombre"])
listaUsuario.append(usuarios["fmuguruza"]["nombre"])
listaUsuario.append(usuarios["aolaizola"]["nombre"])

listaContrasenas = []
listaContrasenas.append(usuarios["iperurena"]["password"])
listaContrasenas.append(usuarios["fmuguruza"]["password"])
listaContrasenas.append(usuarios["aolaizola"]["password"])

for usuario in listaUsuario:
    for contrasenaLista in listaContrasenas:
        if(usuario == nombre and contrasenaLista == contrasena):
            print(F"Usuario reconocido con nombre {usuario}")

def Sumar(a, b):
    return a + b

print(Sumar(2, 2))
print(Sumar("2", "2"))