class Silla:
    def __init__(self, material, forma_respaldo, forma_asiento, color_principal, color_secundario, peso, alto, largo, ancho, precio):
        
        self.material = material
        self.forma_respaldo = forma_respaldo
        self.forma_asiento = forma_asiento
        self.color_principal = color_principal
        self.color_secundario = color_secundario
        self.peso = peso
        self.alto = alto
        self.largo = largo
        self.ancho = ancho
        self.precio = precio

        print(f"Material: {self.material}")
        print(f"Forma del respaldo: {self.forma_respaldo}")
        print(f"Forma del asiento: {self.forma_asiento}")
        print(f"Color principal de la silla: {self.color_principal}")
        print(f"Color secundario de la silla: {self.color_secundario}")
        print(f"Peso: {self.peso} kg")
        print(f"Alto: {self.alto} cm")
        print(f"Largo: {self.largo} cm")
        print(f"Ancho: {self.ancho} cm")
        print(f"Precio: ${self.precio}")

    def sentar(self):
        print("Se sentaron en la silla")

    def levantar(self):
        print("Se levantaron de la silla")

    def mover(self):
        print("Se movio la silla")

    def reclinar(self):
        print("Se reclino la silla")

    def voltear(self):
        print("Se volteo la silla")

silla1 = Silla("Cuero", "Rectangular", "Cuadrada", "Negro", "Rojo", 30, 70, 35, 35, 2500)
silla1.sentar()
silla1.levantar()
silla1.mover()
silla1.reclinar()
silla1.voltear()