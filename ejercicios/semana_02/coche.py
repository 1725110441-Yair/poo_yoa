class Coche:
    def __init__(self, marca, modelo, numero_llantas, numero_puertas, motor, color_principal, color_secundario, precio, peso, caballos_fuerza):
        
        self.marca = marca
        self.modelo = modelo
        self.numero_llantas = numero_llantas
        self.numero_puertas = numero_puertas
        self.motor = motor
        self.color_principal = color_principal
        self.color_secundario = color_secundario
        self.precio = precio
        self.peso = peso
        self.caballos_fuerza = caballos_fuerza

        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Numero de llantas: {self.numero_llantas}")
        print(f"Numero de puertas: {self.numero_puertas}")
        print(f"Motor: {self.motor}")
        print(f"Color principal: {self.color_principal}")
        print(f"Color secundario: {self.color_secundario}")
        print(f"Precio: ${self.precio}")
        print(f"Peso: {self.peso} kg")
        print(f"Caballos de fuerza: {self.caballos_fuerza} hp")

    def abrirCofre(self):
        print(f"Abriendo cofre del {self.modelo}")

    def moverse(self):
        print(f"El {self.modelo} se mueve")

    def abrirPuertas(self):
        print(f"Abriendo puertas del {self.modelo}")

    def retroceder(self):
        print(f"El {self.modelo} se movio hacia atras")
    
    def prenderDireccional(self):
        print(f"Se prendio la direccional del {self.modelo}")

coche1 = Coche("Mazda","MX-5",4,2,"2.0L SKYACTIV-G","Rojo", "Negro", 1000000, 950, 540)
coche1.abrirCofre()
coche1.moverse()
coche1.abrirPuertas()
coche1.retroceder()
coche1.prenderDireccional()