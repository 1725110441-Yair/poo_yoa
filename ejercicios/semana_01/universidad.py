class Universidad:
    def __init__(self, logo, oferta_educativa, localidad, sistema_informatico, modalidad, servicios, ubicacion, talleres, cantidad_salones, rector):
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.sistema_informatico = sistema_informatico
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.talleres = talleres
        self.cantidad_salones = cantidad_salones
        self.rector = rector
        print(f"Logo de la Universidad: {self.logo}")
        print(f"Oferta educativa: {self.oferta_educativa}")
        print(f"Localidad: {self.localidad}")
        print(f"Sistema educativo: {self.sistema_informatico}")
        print(f"Modalidad: {self.modalidad}")
        print(f"Servicios: {self.servicios}")
        print(f"Ubicacion: {self.ubicacion}")
        print(f"Talleres: {self.talleres}")
        print(f"Cantidad de salones: {self.cantidad_salones}")
        print(f"Rector: {self.rector}")
unideh = Universidad("logo.jpg","Ingenieria en Software, Turismo, etc.","San Miguel","CADU","Virtual","Biblioteca Digital","Santa Catarina",None,None,"Octavio Castillo")