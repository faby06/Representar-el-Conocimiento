# Definici�n de la clase base "Marco" para acciones, situaciones y eventos
class Marco:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}\nDescripci�n: {self.descripcion}"

# Clase "Accion" que hereda de "Marco"
class Accion(Marco):
    def __init__(self, nombre, descripcion, duracion):
        super().__init__(nombre, descripcion)
        self.duracion = duracion

    def __str__(self):
        return f"{super().__str__()}\nDuraci�n: {self.duracion} minutos"

# Clase "Situacion" que hereda de "Marco"
class Situacion(Marco):
    def __init__(self, nombre, descripcion, lugar):
        super().__init__(nombre, descripcion)
        self.lugar = lugar

    def __str__(self):
        return f"{super().__str__()}\nLugar: {self.lugar}"

# Clase "Evento" que hereda de "Marco"
class Evento(Marco):
    def __init__(self, nombre, descripcion, fecha):
        super().__init__(nombre, descripcion)
        self.fecha = fecha

    def __str__(self):
        return f"{super().__str__()}\nFecha: {self.fecha}"

# Crear instancias de Accion, Situacion y Evento
hacer_deporte = Accion("Hacer deporte", "Ejercicio f�sico", 60)
reunion = Situacion("Reuni�n", "Discusi�n de proyectos", "Sala de conferencias")
conferencia = Evento("Conferencia", "Conferencia sobre IA", "2023-10-30")

# Mostrar informaci�n de las instancias
print(hacer_deporte)
print("\n" + str(reunion))
print("\n" + str(conferencia))
