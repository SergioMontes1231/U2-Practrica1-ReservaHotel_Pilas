# 🏨 U2 - Práctica 1  
# ReservaHotel_Pilas

---

## 📌 Descripción General

Sistema de gestión de reservas de hotel desarrollado en Python utilizando estructuras de datos tipo **Pila (LIFO)** implementadas desde cero.

El sistema permite gestionar reservas, cancelaciones y la funcionalidad de deshacer operaciones mediante el uso implícito del **Patrón Command**.

---

## 🎯 Objetivo

Implementar un sistema de reservas de hotel utilizando pilas para gestionar operaciones de reserva y cancelación, con funcionalidad de deshacer usando el patrón Command y estructuras de datos tipo pila implementadas desde cero.

---

# 🧱 Arquitectura del Proyecto

El proyecto está dividido en 3 fases principales:

## 1️⃣ MODELOS

Contiene las clases base del sistema:

- `Habitacion`
- `Reserva`
- `PilaPersonalizada`

Responsabilidad:
Representar las entidades del sistema sin lógica compleja de negocio.

Incluye:

### 🔹 Habitacion
Atributos:
- numero: int
- tipo: str
- precio: float
- disponible: bool

Métodos:
- __init__()
- __str__()
- __repr__()

---

### 🔹 Reserva
Atributos:
- id_reserva: int
- habitacion: Habitacion
- fecha: str
- cliente: str

Métodos:
- __init__()
- __str__()
- __repr__()

---

### 🔹 PilaPersonalizada

Estructura de datos implementada desde cero sin uso de `collections`.

Atributos:
- elementos: List
- capacidad_maxima: int

Métodos:
- push(elemento)
- pop()
- peek()
- is_empty()
- is_full()
- size()
- __str__()

Controla:
- Overflow (desbordamiento)
- Underflow (subdesbordamiento)

---

## 2️⃣ LOGICA

Clase principal:

### 🔹 SistemaReservasHotel

Responsable de:
- Crear reservas
- Cancelarlas
- Deshacer cancelaciones
- Administrar habitaciones
- Gestionar pilas

Atributos:
- pila_reservas_actuales
- pila_deshacer
- habitaciones
- contador_reservas

Métodos principales:

### reservar_habitacion()
1. Busca la habitación.
2. Verifica disponibilidad.
3. Crea objeto Reserva.
4. Push en pila_reservas_actuales.
5. Marca habitación como no disponible.
6. Incrementa contador.

---

### cancelar_reserva()
1. Pop de pila_reservas_actuales.
2. Marca habitación como disponible.
3. Push en pila_deshacer.

---

### deshacer_cancelacion()
1. Pop de pila_deshacer.
2. Marca habitación como no disponible.
3. Push en pila_reservas_actuales.

---

### mostrar_reservas()
Muestra las reservas activas.

---

### buscar_habitacion()
Retorna objeto Habitacion si existe.

---

## 3️⃣ UI (Parte Visual)

Interfaz por consola que permite:

- Agregar habitaciones
- Reservar
- Cancelar
- Deshacer
- Mostrar estado actual

Responsabilidad:
Interactuar con el usuario y conectar con la lógica del sistema.

---

# 📊 Diagrama UML

Clases:

- SistemaReservasHotel
- Habitacion
- Reserva
- PilaPersonalizada

Relaciones:

- Composición: SistemaReservasHotel ◆—► PilaPersonalizada (2 instancias)
- Agregación: SistemaReservasHotel ◇—► Habitacion (1..*)
- Asociación: Reserva ——► Habitacion (1)

---

# 🔄 Patrón Command Implícito

Cada operación de cancelación se almacena en una pila secundaria.

Esto permite:
- Revertir la última cancelación.
- Simular comportamiento tipo Ctrl + Z.

La pila_deshacer actúa como historial de comandos.

---

# 🧠 Características Técnicas Implementadas

- Pilas implementadas desde cero (sin collections).
- Principios de Programación Orientada a Objetos.
- Encapsulamiento y abstracción.
- Clean Code.
- Manejo robusto de excepciones.
- Documentación con docstrings.
- Separación en capas (Modelos, Lógica, UI).
- Patrón Command implícito.

---

# 🔁 Flujo de Trabajo

El proyecto está dividido en 3 fases:

- Modelos
- Lógica
- UI

---

# 📝 Convención de Commits

Palabras que se deben usar dependiendo el tipo de cambio:

- feat: Agregar cambios nuevos  
  Ejemplo:  
  "feat: Agregar clase Habitacion"

- fix: Corregir errores  
  Ejemplo:  
  "fix: Corregir calculo de precio total"

- refactor: Mejoras internas sin cambiar funcionalidad  
  Ejemplo:  
  "refactor: Reorganizar logica de reservas"

- docs: Cambios en documentación  
  Ejemplo:  
  "docs: Actualizar README"

- style: Cambios de formato (espacios, indentación o nombres)  
  Ejemplo:  
  "style: Corregir indentacion en SistemaReservasHotel"

En la descripción del commit se debe agregar TODO lo que se agregó o modificó, incluyendo clases y métodos de manera general.

---

# 🔀 Pull Requests

Regla importante:

En lugar de ":" se usa "/"

Ejemplo:

feat/agregue clase habitacion

En la descripción del Pull Request se debe:

- Especificar el nombre de la clase agregada.
- Mencionar los métodos agregados.
- Explicar de manera general qué se agregó al main.
- Describir los métodos de forma un poco más detallada.

Ejemplo de descripción:

Se agrega clase SistemaReservasHotel con metodos reservar_habitacion, cancelar_reserva y deshacer_cancelacion.  
Se integra manejo de pilas personalizadas y control de disponibilidad de habitaciones.  
Se conecta la clase al archivo main para permitir ejecución mediante menú interactivo.

---

# ▶️ Ejecución

Ejecutar archivo principal:

python main.py

Usar el menú interactivo para gestionar reservas.

---

# 📌 Conclusión

Este proyecto demuestra la aplicación práctica de estructuras tipo Pila en un sistema real, integrando conceptos teóricos con implementación funcional.

La estructura modular permite escalabilidad, mantenimiento y comprensión clara del flujo del sistema.

Se cumple el objetivo de implementar pilas personalizadas y aplicar el patrón Command para deshacer operaciones.

---
