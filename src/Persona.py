class Persona:

    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre != "":
            self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        if apellido != "":
            self._apellido = apellido

    def __str__(self):
        return f"{self._apellido}, {self._nombre}"
