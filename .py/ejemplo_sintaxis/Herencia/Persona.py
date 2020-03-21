class Persona:

    def __init__(self, nombre, edad):
        self.Nombre = nombre
        self._Edad = edad
        self.Sexo = "Otro"

    def Hablar(self):
        return print("Esta persona está hablando")
