class HolaMundo:
    
    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Metodo Uno")

    def metodoDos(self, variable_uno: int, variable_dos: int)->int:
        """
        Este método recibe dos variables enteras, las suma y devuelve el resultado de la suma.

        Args: 

        variable_uno : int - Primer numero entero
        variable_dos : int - Segundo numero entero

        Return:
        
        suma : int - Suma de los numeros enteros
        """
        suma = variable_uno + variable_dos
        return int(suma)

    def metoddoTres(self, variable_tres: str)->None:
        print(f"Número de caracteres: {len(variable_tres)}")

nombre_objeto = HolaMundo()
nombre_objeto.metodoUno()
