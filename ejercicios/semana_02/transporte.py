class Transporte:
    def __init__(self, modelo, tipo, puertas, llantas, potencia, color, asientos, largo, alto, peso):
        
        self.modelo = modelo
        self.tipo = tipo
        self.puertas = puertas
        self.llantas = llantas
        self.potencia = potencia
        self.color = color
        self.asientos = asientos
        self.largo = largo
        self.alto = alto
        self.peso = peso

        print(f"Modelo: {self.modelo}")
        print(f"Tipo de trasnporte: {self.tipo}")
        print(f"Numero de puertas: {self.puertas}")
        print(f"Numero de lantas: {self.llantas}")
        print(f"Potencia del motor: {self.potencia}")
        print(f"Color principal: {self.color}")
        print(f"Cantidad de asientos: {self.asientos}")
        print(f"Largo: {self.largo} m")
        print(f"Alto: {self.alto} m")
        print(f"Peso: {self.peso} kg")

    def moverse(self):
        print(f"Se movio el {self.modelo}")

    def subirPasajeros(self):
        print("Se subieron los pasajeros")

    def bajarPasajeros(self):
        print("Se bajaron los pasajeros")

    def detenerse(self):
        print(f"Se detuvo el {self.modelo}")

    def descomponerse(self):
        print(f"Se descompuso el {self.modelo}")

avion = Transporte("Boeing 737", "Aereo", 4, 6, "117 kN", "Blanco", 146, 34.1, 11.3, 70000)
avion.moverse()
avion.subirPasajeros()
avion.bajarPasajeros()
avion.detenerse()
avion.descomponerse()