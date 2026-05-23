class PersonajeJuego:
    
    def __init__(self, nombre, juego, edad, habilidad, genero, personalidad, salud, fuerza_ataque, coordenadas, inventario):
        self.nombre = nombre
        self.juego = juego
        self.edad = edad
        self.habilidad = habilidad
        self.genero = genero
        self.personalidad = personalidad
        self.salud = salud
        self.fuerza_ataque = fuerza_ataque
        self.coordenadas = coordenadas
        self.inventario = inventario

        print(f"Nombre del personaje: {self.nombre}")
        print(f"Juego al que pertenece: {self.juego}")
        print(f"Edad: {self.edad}")
        print(f"Habilidad: {self.habilidad}")
        print(f"Genero del personaje: {self.genero}")
        print(f"Personalidad del personaje: {self.personalidad}")
        print(f"Salud: {self.salud}")
        print(f"Fuerza de ataque: {self.fuerza_ataque}")
        print(f"Coordenadas: {self.coordenadas}")
        print(f"Inventario: {self.inventario}")
        
    def moverseAdelante(self):
        print(f"{self.nombre} se movio al frente")

    def moverseAtras(self):
        print(f"{self.nombre} se movio hacia atras")

    def recuperarSalud(self):
        print(f"{self.nombre} recupero salud")

    def saltar(self):
        print(f"{self.nombre} saltó")

    def morir(self):
        print(f"{self.nombre} ha muerto")

link = PersonajeJuego("Link", "The Leyend of Zelda", 27, "Magia", "Masculina", "Valiente", 85, 32, (12,24,67), "Posion, Armadura, Espada")
link.moverseAdelante()
link.moverseAtras()
link.recuperarSalud()
link.saltar()
link.morir()