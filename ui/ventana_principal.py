import tkinter as tk
from tkinter import ttk


class InterfazHotel:

    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema

        self.root.title("Sistema de Reservas del Hotel")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        titulo = ttk.Label(root, text="Sistema de Reservas", font=("Arial", 18))
        titulo.pack(pady=10)

        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Reservar habitación", command=self.ventana_reserva).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Cancelar reserva", command=self.cancelar).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botones, text="Deshacer cancelación", command=self.deshacer).grid(row=0, column=2, padx=5)

        ttk.Button(frame_botones, text="Mostrar habitaciones", command=self.mostrar_habitaciones).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(frame_botones, text="Mostrar reservas", command=self.mostrar_reservas).grid(row=1, column=1, padx=5, pady=5)

        self.texto = tk.Text(root, height=12, width=70)
        self.texto.pack(pady=10)

    def validar_numero(self, valor):
        if valor == "":
            return True
        return valor.isdigit()

    def ventana_reserva(self):

        ventana = tk.Toplevel(self.root)
        ventana.title("Nueva reserva")
        ventana.geometry("320x260")

        vcmd = (ventana.register(self.validar_numero), "%P")

        ttk.Label(ventana, text="Número habitación").pack()

        num = tk.Spinbox(
            ventana,
            from_=1,
            to=999,
            validate="key",
            validatecommand=vcmd
        )
        num.pack()

        ttk.Label(ventana, text="Fecha").pack(pady=(10, 0))

        frame_fecha = ttk.Frame(ventana)
        frame_fecha.pack()

        ttk.Label(frame_fecha, text="Día").grid(row=0, column=0)
        ttk.Label(frame_fecha, text="Mes").grid(row=0, column=1)
        ttk.Label(frame_fecha, text="Año").grid(row=0, column=2)

        dia = tk.Spinbox(frame_fecha, from_=1, to=31, width=5, validate="key", validatecommand=vcmd)
        dia.grid(row=1, column=0)

        mes = tk.Spinbox(frame_fecha, from_=1, to=12, width=5, validate="key", validatecommand=vcmd)
        mes.grid(row=1, column=1)

        anio = tk.Spinbox(frame_fecha, from_=2026, to=2035, width=7, validate="key", validatecommand=vcmd)
        anio.grid(row=1, column=2)

        ttk.Label(ventana, text="Cliente").pack(pady=(10, 0))
        cliente = ttk.Entry(ventana)
        cliente.pack()

        def confirmar():

            numero = num.get().strip()
            nombre = cliente.get().strip()

            if not numero.isdigit():
                self.texto.insert(tk.END, "\nNúmero de habitación inválido\n")
                return

            if nombre == "":
                self.texto.insert(tk.END, "\nEl nombre del cliente no puede estar vacío\n")
                return

            if not nombre.replace(" ", "").isalpha():
                self.texto.insert(tk.END, "\nEl nombre solo debe tener letras\n")
                return

            fecha = f"{dia.get()}/{mes.get()}/{anio.get()}"

            exito = self.sistema.reservar_habitacion(
                int(numero),
                fecha,
                nombre
            )

            if exito:
                self.texto.insert(tk.END, f"\nReserva realizada para {nombre} el {fecha}\n")
            else:
                self.texto.insert(tk.END, "\nNo se pudo realizar la reserva\n")

            ventana.destroy()

        ttk.Button(ventana, text="Confirmar", command=confirmar).pack(pady=10)

    def cancelar(self):

        if self.sistema.cancelar_reserva():
            self.texto.insert(tk.END, "\nReserva cancelada\n")
        else:
            self.texto.insert(tk.END, "\nNo hay reservas para cancelar\n")

    def deshacer(self):

        if self.sistema.deshacer_cancelacion():
            self.texto.insert(tk.END, "\nCancelación deshecha\n")
        else:
            self.texto.insert(tk.END, "\nNo se pudo deshacer\n")

    def mostrar_habitaciones(self):

        self.texto.delete(1.0, tk.END)

        for h in self.sistema.habitaciones:
            estado = "Disponible" if h.disponibilidad else "Ocupada"
            self.texto.insert(tk.END, f"Habitación {h.numero} - {h.tipo} - {estado}\n")

    def mostrar_reservas(self):

        self.texto.delete(1.0, tk.END)

        if self.sistema.pila_reservas_actuales.is_empty():
            self.texto.insert(tk.END, "No hay reservas\n")
            return

        for r in self.sistema.pila_reservas_actuales.elementos:
            self.texto.insert(tk.END, f"{r}\n")
