class Transporte:
    def __init__(self, marca, modelo, numero_llantas, numero_puertas, motor, color):
        self.marca = marca
        self.modelo = modelo
        self.numero_llantas = numero_llantas
        self.numero_puertas = numero_puertas
        self.motor = motor
        self.color = color
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Numero de llantas: {self.numero_llantas}")
        print(f"Numero de puertas: {self.numero_puertas}")
        print(f"Motor: {self.motor}")
        print(f"Color: {self.color}")

    def abrirCofre(self):
        print(f"Abriendo cofre del {self.modelo}")

    def moverse(self):
        print(f"El {self.modelo} se mueve")

    def abrirPuertas(self):
        print(f"Abriendo puertas del {self.modelo}")

coche1 = Transporte("Mazda","MX-5",4,2,"2.0L SKYACTIV-G","Rojo")
coche1.abrirCofre()
coche1.moverse()
coche1.abrirPuertas()