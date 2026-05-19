class Mesa:
    def __init__(self, color, material, largo, ancho, alto, textura):
        self.color = color
        self.material = material
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.textura = textura

        print(f"Color: {self.color}")
        print(f"Material: {self.material}")
        print(f"Largo: {self.largo}")
        print(f"Ancho: {self.ancho}")
        print(f"Alto: {self.alto}")
        print(f"Textura: {self.textura}")

mesa1 = Mesa("Marrón", "Madera", 1.5, 0.8, 0.75, "Liso")