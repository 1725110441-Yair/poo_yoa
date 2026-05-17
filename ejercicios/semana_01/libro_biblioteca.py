class LibroBiblioteca:
    def __init__(self, id, nombre, autor, editorial, anio, genero, edicion, idioma, cantidad_disponibles, fecha_adquisicion):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.anio = anio
        self.genero = genero
        self.edicion = edicion
        self.idioma = idioma
        self.cantidad_disponibles = cantidad_disponibles
        self.fecha_adquisicion = fecha_adquisicion
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Año: {self.anio}")
        print(f"Genero: {self.genero}")
        print(f"Edicion: {self.edicion}")
        print(f"Idioma: {self.idioma}")
        print(f"Cantidad disponibles: {self.cantidad_disponibles}")
        print(f"Fecha de adquisicion: {self.fecha_adquisicion}")
libro1 = LibroBiblioteca("12982","Cien años de soledad","Gabriel Garcia Marquez","Sudamericana","1967","Realismo Magico","Primera","Español","3","19/05/2026")