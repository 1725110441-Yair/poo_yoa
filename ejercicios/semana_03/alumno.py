class Alumno:
    def __init__(self, nombre, apellido_paterno, apellido_materno, edad, matricula, grupo, carrera, grado, genero, tipo_sangre):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
        self.matricula = matricula
        self.grupo = grupo
        self.carrera = carrera
        self.grado = grado
        self.genero = genero
        self.tipo_sangre = tipo_sangre

        print(f"Nombre: {self.nombre}")
        print(f"Apellido paterno: {self.apellido_paterno}")
        print(f"Apellido materno: {self.apellido_materno}")
        print(f"Edad: {self.edad}")
        print(f"Matricula: {self.matricula}")
        print(f"Grupo: {self.grupo}")
        print(f"Carrera: {self.carrera}")
        print(f"Grado: {self.grado}")
        print(f"Genero: {self.genero}")
        print(f"Tipo de sangre: {self.tipo_sangre}")

    def inscribirse(self):
        print(f"El alumno {self.nombre} se ha inscrito")

    def aprobar(self):
        print(f"El alumno {self.nombre} aprobo")

    def reprobar(self):
        print(f"El alumno {self.nombre} ha reprobado")

    def estudiar(self):
        print(f"{self.nombre} esta estudiando")

    def haciendoTarea(self):
        print(f"El alumno {self.nombre} esta haciendo tarea")

alumno1 = Alumno("Juan", "Perez", "Rodriguez", 19, 17263822, 12, "Programacion", 1, "Masculino", "O+")
alumno1.inscribirse()
alumno1.aprobar()
alumno1.reprobar()
alumno1.estudiar()
alumno1.haciendoTarea()