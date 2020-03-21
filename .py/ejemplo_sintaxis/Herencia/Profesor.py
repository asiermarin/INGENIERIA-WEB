from Persona import Persona

class Profesor(Persona):

    def __init__(self, nombre, edad, numeroAlumnos):
        super().__init__(nombre, edad)
        self.__NumeroAlumnos = numeroAlumnos
        
# -----------------------------------------------------------        
profesor = Profesor("Asier", 18, 5)
print(profesor._Edad)