# 🏨 U2 - Práctica 1  
# Sistema de Reservas de Hotel con Pilas

---

## 📌 Descripción del Proyecto

Sistema de gestión de reservas de hotel desarrollado en Python, utilizando estructuras de datos tipo pila implementadas desde cero.

El sistema permite:

- Registrar habitaciones
- Crear reservas
- Cancelar reservas
- Deshacer cancelaciones
- Visualizar reservas activas

Se implementa el patrón **Command implícito** para permitir la funcionalidad de deshacer operaciones mediante el uso de una segunda pila.

---

## 🎯 Objetivo

Aplicar estructuras de datos tipo **Pila (LIFO)** en un caso práctico real, integrando principios de Programación Orientada a Objetos, manejo de excepciones y buenas prácticas de desarrollo.

---

## 🧱 Arquitectura del Proyecto

El proyecto está dividido en 3 fases:

### 1️⃣ Modelos
Contiene las clases base del sistema:

- `Habitacion`
- `Reserva`
- `PilaPersonalizada`

Responsabilidad:
Representar las entidades del sistema sin lógica de negocio compleja.

---

### 2️⃣ Lógica
Contiene la clase principal:

- `SistemaReservasHotel`

Responsabilidad:
Gestionar reservas, cancelaciones y deshacer operaciones utilizando pilas.

---

### 3️⃣ UI (Interfaz)
Interfaz por consola que permite interactuar con el sistema mediante un menú.

---

## 📊 Diagrama UML (Resumen)

Clases principales:

- SistemaReservasHotel
- Habitacion
- Reserva
- PilaPersonalizada

Relaciones:

- Composición: SistemaReservasHotel → PilaPersonalizada (2 instancias)
- Agregación: SistemaReservasHotel → Habitacion
- Asociación: Reserva → Habitacion

---

## 🗂️ Estructura de Clases

### 🔹 Habitacion
Atributos:
- numero
- tipo
- precio
- disponible

---

### 🔹 Reserva
Atributos:
- id_reserva
- habitacion
- fecha
- cliente

---

### 🔹 PilaPersonalizada
Implementada sin usar `collections`.

Métodos:
- push()
- pop()
- peek()
- is_empty()
- is_full()
- size()

Controla:
- Overflow
- Underflow

---

### 🔹 SistemaReservasHotel
Atributos:
- pila_reservas_actuales
- pila_deshacer
- habitaciones
- contador_reservas

Métodos principales:
- reservar_habitacion()
- cancelar_reserva()
- deshacer_cancelacion()
- mostrar_reservas()
- buscar_habitacion()

---

## 🔄 Funcionamiento del Deshacer

Cuando se cancela una reserva:

1. Se hace `pop()` de la pila de reservas activas.
2. Se marca la habitación como disponible.
3. Se guarda la reserva en la pila de deshacer.

Al ejecutar deshacer:

1. Se hace `pop()` de la pila de deshacer.
2. Se vuelve a marcar la habitación como no disponible.
3. Se regresa a la pila de reservas activas.

Este comportamiento simula el patrón **Ctrl + Z**.

---

## 🧠 Conceptos Aplicados

- Estructura de datos tipo Pila (LIFO)
- Programación Orientada a Objetos
- Encapsulamiento
- Abstracción
- Manejo de excepciones
- Clean Code
- Patrón Command (implícito)
- Separación en capas (Modelos, Lógica, UI)

---

## ▶️ Ejecución

1. Ejecutar el archivo principal:

```bash
python main.py
