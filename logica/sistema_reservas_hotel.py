from habitacion import Habitacion
from reserva import Reserva
from pilas_personalizadas import PilaPersonalizada


class SistemaReservasHotel:
    """
    Sistema principal de gestion de reservas de hotel
    Atributos:
        - pila_reservas_actuales(PilaPersonalizada): Almacena las reservas activas
        - pila_deshacer(PilaPersonalizada): Almacena las cancelaciones para deshacer
        - habitaciones(list): Lista de todas las habitaciones del hotel
        - contador_reservas(int): Contador para generar IDs de reserva
    """

    def __init__(self, capacidad_reservas: int) -> None:
        """
        Inicializador de la clase SistemaReservasHotel
        Parametros:
            - capacidad_reservas(int): Capacidad maxima de reservas del sistema
        """
        self.pila_reservas_actuales = PilaPersonalizada(capacidad_reservas)
        self.pila_deshacer = PilaPersonalizada(capacidad_reservas)
        self.habitaciones = []
        self.contador_reservas = 0

    def agregar_habitacion(self, numero: int, tipo: str, precio: float) -> None:
        """
        Agrega una habitacion al sistema
        Parametros:
            - numero(int): Numero de la habitacion
            - tipo(str): Tipo de habitación
            - precio(float): Precio por noche
        """
        habitacion = Habitacion(numero, tipo, precio, True)
        self.habitaciones.append(habitacion)

    def buscar_habitacion(self, numero: int) -> Habitacion | None:
        """
        Busca una habitacion por su numero
        Parametros:
            - numero(int): Numero de la habitacion a buscar
        Return:
            - Habitacion | None: La habitacion encontrada o None si no existe
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return habitacion
        return None

    def reservar_habitacion(self, numero_habitacion: int, fecha: str, cliente: str) -> bool:
        """
        Realiza una reserva de habitacion
        Parametros:
            - numero_habitacion(int): Numero de la habitacion a reservar
            - fecha(str): Fecha de la reserva
            - cliente(str): Nombre del cliente
        Return:
            - bool: True si la reserva fue exitosa, False si no
        """
        """Buscar la habitacion"""
        habitacion = self.buscar_habitacion(numero_habitacion)
        
        """Verificar si la habitacion existe y esta disponible"""
        if not habitacion or not habitacion.disponibilidad:
            return False
        
        """Verificar si hay espacio en la pila de reservas"""
        if self.pila_reservas_actuales.is_full():
            return False
        
        """Crear la reserva"""
        self.contador_reservas += 1
        reserva = Reserva(self.contador_reservas, habitacion, fecha, cliente)
        
        """Agregar a la pila de reservas actuales"""
        self.pila_reservas_actuales.push(reserva)
        
        """Marcar habitacion como no disponible"""
        habitacion.disponibilidad = False
        
        return True

    def cancelar_reserva(self) -> bool:
        """
        Cancela la ultima reserva realizada
        Return:
            - bool: True si la cancelacion fue exitosa, False si no
        """
        """Verificar si hay reservas para cancelar"""
        if self.pila_reservas_actuales.is_empty():
            return False
        
        """Obtener la ultima reserva"""
        reserva_cancelada = self.pila_reservas_actuales.pop()
        
        """Marcar la habitacion como disponible"""
        reserva_cancelada.habitacion.disponibilidad = True
        
        """Agregar a la pila de deshacer"""
        self.pila_deshacer.push(reserva_cancelada)
        
        return True

    def deshacer_cancelacion(self) -> bool:
        """
        Deshace la ultima cancelación realizada
        Return:
            - bool: True si se pudo deshacer la cancelacion, False si no
        """
        """Verificar si hay cancelaciones para deshacer"""
        if self.pila_deshacer.is_empty():
            return False
        
        """Verificar si hay espacio en reservas actuales"""
        if self.pila_reservas_actuales.is_full():
            return False
        
        """Obtener la ultima cancelacion"""
        reserva_recuperada = self.pila_deshacer.pop()
        
        """Verificar si la habitacion sigue disponible"""
        if not reserva_recuperada.habitacion.disponibilidad:
            return False
        
        """Marcar la habitacion como no disponible"""
        reserva_recuperada.habitacion.disponibilidad = False
        
        """Volver a agregar a reservas actuales"""
        self.pila_reservas_actuales.push(reserva_recuperada)
        
        return True

    def mostrar_reservas(self) -> None:
        """
        Muestra todas las reservas activas
        """
        if self.pila_reservas_actuales.is_empty():
            print("No hay reservas activas")
            return
        
        print("\n=== RESERVAS ACTIVAS ===")
        for i, reserva in enumerate(self.pila_reservas_actuales.elementos, 1):
            print(f"\n--- Reserva {i} ---")
            print(reserva)

    def mostrar_habitaciones(self) -> None:
        """
        Muestra todas las habitaciones y su estado
        """
        if not self.habitaciones:
            print("No hay habitaciones registradas")
            return
        
        print("\n=== HABITACIONES ===")
        disponibles = []
        ocupadas = []
        
        for habitacion in self.habitaciones:
            if habitacion.disponibilidad:
                disponibles.append(habitacion)
            else:
                ocupadas.append(habitacion)
        
        print(f"\n- Disponibles ({len(disponibles)}) ---")
        for habitacion in disponibles:
            print(f"Habitacion {habitacion.numero} - {habitacion.tipo} - ${habitacion.precio}")
        
        print(f"\n- Ocupadas ({len(ocupadas)}) ---")
        for habitacion in ocupadas:
            print(f"Habitacion {habitacion.numero} - {habitacion.tipo} - ${habitacion.precio}")

    def mostrar_estado_pilas(self) -> None:
        """
        Muestra el estado actual de las pilas
        """
        print("\n=== ESTADO DEL SISTEMA ===")
        print("\n--- PILA DE RESERVAS ACTUALES ---")
        print(self.pila_reservas_actuales)
        print("\n--- PILA DE DESHACER ---")
        print(self.pila_deshacer)