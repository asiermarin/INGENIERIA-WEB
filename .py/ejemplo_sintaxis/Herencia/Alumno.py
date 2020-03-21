from Persona import Persona

class Alumno(Persona):

    def __init__(self, nombre, edad, numeroAsignaturas):
        Persona.__init__(self, nombre, edad) # Mejor opción para herencia múltiple
        self.__NumeroAsignaturas = numeroAsignaturas
        
# -----------------------------------------------------------        
alumno = Alumno("Asier", 18, 5)
print(alumno._Edad)