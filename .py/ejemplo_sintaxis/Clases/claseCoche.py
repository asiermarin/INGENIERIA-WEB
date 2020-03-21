class Coche:

    anchuraRuedasEstatico = "21 pulgadas"

    def get_anchuraRuedas(self):
        return self.anchuraRuedasEstatico

    def set_anchuraRuedas(self, x):
        self.anchuraRuedasEstatico = x

    # Los atributos se definen en el constructor
    def __init__(self, altura):
        self._color = "un color" # Protectered
        self.__km = 0            # Private
        self.altura = altura
        self.anchura = ""
        self.anchuraRuedas = "No definida"

    # Los métodos funcionan sin tener que hacer una instacia previa
    def Conducir(self, altura):
        return print(f"estas conduciendo un coche con esta altura {altura}")

unCoche = Coche("2.0 metros")
unCoche.Conducir(unCoche.altura)

#Atributo con variable pre-definida
print(unCoche.anchuraRuedasEstatico)

# Uso con seters
unCoche.set_anchuraRuedas("30 pulgadas")
print(unCoche.anchuraRuedasEstatico)
print(unCoche.get_anchuraRuedas())
print(unCoche.anchuraRuedasEstatico)

Coche("").Conducir("2.3 metros")