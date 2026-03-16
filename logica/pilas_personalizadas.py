import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modulos.habitacion import Habitacion 
from modulos.reserva import Reserva 


class PilaPersonalizada:
    """
    Almacena las reservas recibidas
    Atributos:
        - elementos(List): almacena las reservas recibidas
        - capacidad_maxima(int): Recibe e indica el número maximo de reservas que puede recibir el sistema
    """

    def __init__(self, capacidad) -> None:
        """
        Inicializador de la clase PilaPersonalizada
        Parametros:
            - capacidad(int): Número máximo de reservas que puede almacenar la pila
        """

        self.elementos = []
        self.capacidad_maxima = capacidad

    def push(self, elemento: Reserva) -> None:
        """
        Permite agregar reservas en la cima de la pila
        """
        if not self.is_full():
            self.elementos.append(elemento)

    def pop(self) -> Reserva | None:
        """
        Muestra la última reserva agregada y la elimina de la pila
        """
        if not self.is_empty():
            return self.elementos.pop()

    def peek(self) -> Reserva | None:
        """
        Muestra la última reserva agregada en la pila sin eliminarla o modificarla
        """
        if not self.is_empty():
            return self.elementos[-1]

    def is_empty(self) -> bool:
        """
        Indica si la lista de reservas está vacia
        """
        return len(self.elementos) == 0

    def is_full(self) -> bool:
        """
        Indica si la lista de reservas está llena
        """
        return len(self.elementos) == self.capacidad_maxima

    def size(self) -> int:
        """
        Muestra el tamaño de la lista de reservas
        """
        return len(self.elementos)

    def __str__(self) -> str:
        """
        Representación en texto de los cambios realizados dentro de la lista de reservas
        """
        return (
            f" Capacidad máxima de reservas: {self.capacidad_maxima}\n"
            f" Número de reservas: {self.size()}\n"
            f" Reservas almacenadas: {self.elementos}\n"
            f" Está llena la lista: {self.is_full()}\n"
            f" Está vacia la lista: {self.is_empty()}")
