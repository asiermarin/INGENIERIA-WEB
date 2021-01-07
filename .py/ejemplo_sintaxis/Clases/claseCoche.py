from datetime import datetime

class Coche:

    # Los atributos se definen en el constructor
    def __init__(self):
        self.tipo_de_ruedas = "nexus_componenets"

    def Mensaje_info(self, mensaje):
        current_date = datetime.today()

        return print(f" \033[1;32;48m [{current_date}] INFO {self.tipo_de_ruedas} : {mensaje}")

    def Mensaje_warnning(self, mensaje):
        current_date = datetime.today()

        return print(f" \033[1;33;48m [{current_date}] WARNING {self.tipo_de_ruedas} : {mensaje}")

    def Mensaje_error(self, mensaje):
        current_date = datetime.today()

        return print(f" \033[1;31;48m [{current_date}] ERROR {self.tipo_de_ruedas} : {mensaje}")



coche_pequeño = Coche()
coche_pequeño.tipo_de_ruedas = "nexus_componenex_urls"

# coche.set_tipo_de_ruedas("RUEDAS INVIERNO:")
coche_pequeño.Mensaje_info("No estoy desgastado")
coche_pequeño.Mensaje_warnning("Puede que esté desgastado")
coche_pequeño.Mensaje_error("Si estoy desgastado")


 