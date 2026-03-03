# U2-Practrica1-ReservaHotel_Pilas

#Objetivo
Implementar un sistema de reservas de hotel utilizando pilas para gestionar operaciones de reserva y cancelación, con funcionalidad de deshacer usando el patrón Command y estructuras de datos tipo pila implementadas desde cero.

#Diagrama de Clases UML
┌─────────────────────────────┐
│     SistemaReservasHotel    │
├─────────────────────────────┤
│ - pila_reservas_actuales    │
│ - pila_deshacer            │
│ - habitaciones: List       │
│ - contador_reservas: int   │
├─────────────────────────────┤
│ + __init__()               │
│ + reservar_habitacion()    │
│ + cancelar_reserva()       │
│ + deshacer_cancelacion()   │
│ + mostrar_reservas()       │
│ + buscar_habitacion()      │
└─────────────────────────────┘
                │
                │ 1..*
                ▼
┌─────────────────────────────┐
│         Habitacion          │
├─────────────────────────────┤
│ - numero: int              │
│ - tipo: str                │
│ - precio: float            │
│ - disponible: bool         │
├─────────────────────────────┤
│ + __init__(numero, tipo,   │
│           precio)          │
│ + __str__()                │
│ + __repr__()               │
└─────────────────────────────┘
                ▲
                │
                │ 1
┌─────────────────────────────┐
│          Reserva            │
├─────────────────────────────┤
│ - id_reserva: int          │
│ - habitacion: Habitacion   │
│ - fecha: str               │
│ - cliente: str             │
├─────────────────────────────┤
│ + __init__(id_reserva,     │
│           habitacion,      │
│           fecha, cliente)  │
│ + __str__()                │
│ + __repr__()               │
└─────────────────────────────┘
                ▲
                │
                │ 0..*
┌─────────────────────────────┐
│      PilaPersonalizada      │
├─────────────────────────────┤
│ - elementos: List          │
│ - capacidad_maxima: int    │
├─────────────────────────────┤
│ + __init__(capacidad)      │
│ + push(elemento)           │
│ + pop() -> elemento        │
│ + peek() -> elemento       │
│ + is_empty() -> bool       │
│ + is_full() -> bool        │
│ + size() -> int            │
│ + __str__()                │
└─────────────────────────────┘

Relaciones:
Composición: SistemaReservasHotel ◆—► PilaPersonalizada (2 instancias)
Agregación: SistemaReservasHotel ◇—► Habitacion (1..*)
Asociación: Reserva ——► Habitacion (1)

#Código Fuente Documentado
Características Técnicas Implementadas
Pilas implementadas desde cero - Sin uso de collections
Principios de POO - Encapsulamiento, abstracción, herencia
Clean Code - Nombres descriptivos, métodos pequeños, documentación completa
Manejo de excepciones - Control robusto de errores
Documentación completa - Docstrings en formato estándar de Python
Patrón Command implícito - Para deshacer operaciones

#Comentar Commits
Palabras que se deben usar dependiendo los cambios (seria por ejemplo 
  -feat: Agregar cambios nuevos
    ejemplo-> "feat: Agregar clase Habitacion"
  -fix: Corregir erroes
    ejemplo-> "fix: Corregir calculo de precio total"
  -refactor: Mejoras codigo sin cambiar que hace
    ejemplo-> "refactor: reorganizar logica de reservas"
  -docs: Cuando se cambia la documentacion
    ejemplo-> "docs: actualizar README"
  -style: Cambios de formatos (espacios, identacion o nombres)
    ejemplo-> "style: corregir indentacion en ventana principal"
En descripcion se agrega TODO lo que se agrego en el commit, la clase y metodos descritos de manera general
#NOTA IMPORTATE
  los pullrequest, usan EXACTAMENTE las mismas palabras, la unica diferencia es que en vez de : se usa /
    ejemplo-> "feat/agregue clase habitacion"
  En descripcion agrega que es tooodo lo que se agrega a main, poner "nombre clase", y en descripcion de metodos de manera un poco mas detallada

#Flujo de trabajo
El proyecto estara dividido en 3 faces
  -Modelos
  -Logica
  -UI(parte visual)
#MODELOS
Este contendra 
