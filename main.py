import tkinter as tk

from logica.sistema_reservas_hotel import SistemaReservasHotel
from ui.ventana_principal import InterfazHotel


sistema = SistemaReservasHotel(10)

#Habitacione
sistema.agregar_habitacion(101, "Simple", 500)
sistema.agregar_habitacion(102, "Simple", 500)
sistema.agregar_habitacion(103, "Simple", 500)
sistema.agregar_habitacion(104, "Simple", 500)
sistema.agregar_habitacion(105, "Doble", 800)
sistema.agregar_habitacion(106, "Doble", 800)
sistema.agregar_habitacion(107, "Doble", 800)
sistema.agregar_habitacion(108, "Suite", 1200)
sistema.agregar_habitacion(109, "Suite", 1200)
sistema.agregar_habitacion(110, "Suite", 1200)


root = tk.Tk()
app = InterfazHotel(root, sistema)
root.mainloop()
