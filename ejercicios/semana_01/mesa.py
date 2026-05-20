class Mesa:
    def __init__(self, color, material, largo, ancho, alto, textura, cantidad_patas, forma_centro, peso, precio):
        self.color = color
        self.material = material
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.textura = textura
        self.cantidad_patas = cantidad_patas
        self.forma_centro = forma_centro
        self.peso = peso
        self.precio = precio

        print(f"Color: {self.color}")
        print(f"Material: {self.material}")
        print(f"Largo: {self.largo}")
        print(f"Ancho: {self.ancho}")
        print(f"Alto: {self.alto}")
        print(f"Textura: {self.textura}")
        print(f"cantidad de patas: {self.cantidad_patas}")
        print(f"Forma del centro: {self.forma_centro}")
        print(f"Peso: {self.peso} kg")
        print(f"Precio: ${self.precio}")

    def mover(self):
        print("Se movio la mesa")

    def voltear(self):
        print("Se volteo la mesa")

    def romper(self):
        print("Se rompio la mesa")

    def ajustarAltura(self):
        print("Se ajusto la altura")

    def usar(self):
        print("se ha usado la mesa para comer")

mesa1 = Mesa("Marrón", "Madera", 1.5, 0.8, 0.75, "Liso", 4, "Rectangular", 10, 14000)
mesa1.mover()
mesa1.voltear()
mesa1.romper()
mesa1.ajustarAltura()
mesa1.usar()