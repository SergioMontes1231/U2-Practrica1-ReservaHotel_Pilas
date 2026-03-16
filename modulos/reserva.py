from modulos.habitacion import Habitacion 


class Reserva:
    """
    Representa una reserva en un hotel
    Atributos:
        -id_reserva(int): el numero de la reserva
        -habitacion(Habitacion): la habiacion a la que se le ubica la reserva
        -fecha(str): dia de la reserva
        -cliente(str): nombre del cliente al que se le adjudica la reserva
    """


    def __init__(self, id_reserva: int, habitacion: Habitacion, 
        fecha: str, cliente: str)->None:
        """
        Inicializador de clase reserva
        Parametros:
            -id_reserva(int): el numero de la reserva
            -habitacion(Habitacion): la habiacion a la que se le ubica la reserva
            -fecha(str): dia de la reserva
            -cliente(str): nombre del cliente al que se le adjudica la reserva

        """

        self.id_reserva = id_reserva
        self.habitacion = habitacion
        self.fecha = fecha
        self.cliente = cliente


    def __str__(self)->str:
        """
        Representacion en texto sobre los atributos de la clase para usuarios
            return:
                str: Informacion de los atributos
        """
        return (
            f"Numero de reserva: {self.id_reserva}\n"
            f"Habitacion: {self.habitacion}\n"
            f"Fecha de reserva: {self.fecha}\n"
            f"Reserva a nombre de: {self.cliente}"
            )


    def __repr__(self)->str:
        """
        Representacion en texto sobre lo que contienen los atributos de la clase
            return:
                str: Contenido de los atributos
        """
        return (
            f"Id_reserva = {self.id_reserva}\n"
            f"Habitacion = {self.habitacion}\n"
            f"Fecha = {self.fecha}\n"
            f"Cliente = {self.cliente}"

            )
