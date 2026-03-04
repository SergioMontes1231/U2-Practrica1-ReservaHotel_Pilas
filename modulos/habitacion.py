class Habitacion:
    """
    Representa una habitacion dentro de un hotel
        atributos:
            numero(int): Numero de la habitacion
            tipo(str): Almecena el tipo de habitacion entre una variedad
            precio(float): Precio de acuerdo a el tipo de habitacion
            disponibilidad(bool): Menciona si esta libre o esta ocupada
    """


    def __init__(self, numero: int, tipo: str, precio: float, disponibilidad: bool)->None:
        """
        Inicializa los atributos de la clase Habitacion
            argumentos:
                numero(int): Numero de la habitacion
                tipo(str): Almecena el tipo de habitacion entre una variedad
                precio(float): Precio de acuerdo a el tipo de habitacion
                disponibilidad(bool): Menciona si esta libre o esta ocupada
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponibilidad = disponibilidad


    def __str__(self)->str:
        """
        Representacion en texto sobre los atributos de la clase para usuarios
            return:
                str: Informacion de los atributos
        """
        return(
            f"Numero de habitacion: {self.numero}\n"
            f"Tipo de habitacion: {self.tipo}\n"
            f"Precio de la habitacion: {self.precio}\n"
            f"Esta disponible: {self.disponibilidad}"
            )


    def __repr__(self)->str:
        """
        Representacion en texto sobre lo que contienen los atributos de la clase
            return:
                string: Contenido de los atributos
        """
        return(
            f"numero = {self.numero}\n"
            f"tipo = {self.tipo}\n"
            f"precio = {self.precio}\n"
            f"disponibilidad = {self.disponibilidad}\n"
            )   
