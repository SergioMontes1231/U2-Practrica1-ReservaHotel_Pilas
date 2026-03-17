import unittest
from logica.sistema_reservas_hotel import SistemaReservasHotel


class TestSistemaReservasHotel(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba"""
        self.hotel = SistemaReservasHotel(5)

        self.hotel.agregar_habitacion(101, "Simple", 500)
        self.hotel.agregar_habitacion(102, "Doble", 800)


    def test_buscar_habitacion(self):
        habitacion = self.hotel.buscar_habitacion(101)
        self.assertIsNotNone(habitacion)


    def test_reserva_exitosa(self):
        resultado = self.hotel.reservar_habitacion(101, "2025-12-25", "Juan")
        self.assertTrue(resultado)
        self.assertEqual(self.hotel.pila_reservas_actuales.size(), 1)


    def test_reservar_habitacion_ocupada(self):
        self.hotel.reservar_habitacion(101, "2025-12-25", "Juan")
        resultado = self.hotel.reservar_habitacion(101, "2025-12-26", "Ana")
        self.assertFalse(resultado)


    def test_cancelar_reserva(self):
        self.hotel.reservar_habitacion(101, "2025-12-25", "Juan")
        resultado = self.hotel.cancelar_reserva()
        self.assertTrue(resultado)


    def test_deshacer_cancelacion(self):
        self.hotel.reservar_habitacion(101, "2025-12-25", "Juan")
        self.hotel.cancelar_reserva()

        resultado = self.hotel.deshacer_cancelacion()
        self.assertTrue(resultado)


if __name__ == "__main__":
    unittest.main()