class Celular:
    def __init__(self, modelo, sistema_operativo, procesador, ram, almacenamiento, bateria, largo, ancho, grosor, peso):
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.bateria = bateria
        self.largo = largo
        self.ancho = ancho
        self.grosor = grosor
        self.peso = peso

        print(f"Modelo: {self.modelo}")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Bateria: {self.bateria}")
        print(f"Largo: {self.largo}")
        print(f"Ancho: {self.ancho}")
        print(f"Grosor: {self.grosor}")
        print(f"Peso: {self.peso}")
        
s24ultra = Celular("S24-Ultra","One UI 8.0","Snapdragon 8 Gen 3","12 GB","256 GB","5000 mAh","162.3 mm","74 mm","8.6 mm","232 g")