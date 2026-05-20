class Perro:
    def __init__(self, nombre, color, raza, edad, genero, peso, altura, dueño, color_ojos, fecha_nacimiento):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.altura = altura
        self.dueño = dueño
        self.color_ojos = color_ojos
        self.fecha_nacimiento = fecha_nacimiento

        print(f"Nombre: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Genero: {self.genero}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        print(f"Dueño: {self.dueño}")
        print(f"Color de ojos: {self.color_ojos}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")

    def moverse(self):
        print("El perro se movio")

    def acostarse(self):
        print("El perro se acosto")

    def dormirse(self):
        print("El perro se durmio")

    def correr(self):
        print("El perro esta corriendo")

    def sacudirse(self):
        print("El perro se esta sacudiendo")

perro1 = Perro("Balto", "Blanco", "Pastor aleman", "6 años", "Macho", "15 kg", "56 cm", "Juan", "Blancos", "14/02/2020")
perro1.moverse()
perro1.acostarse()
perro1.dormirse()
perro1.correr()
perro1.sacudirse()