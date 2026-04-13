

class Libro:

    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self._titulo = titulo
        self._autor = autor              # objeto de tipo Persona
        self._isbn = isbn
        self._paginas = paginas
        self._edicion = edicion
        self._editorial = editorial
        self._ciudad = ciudad
        self._pais = pais
        self._fecha_edicion = fecha_edicion

    # --- Getters y Setters ---

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        if titulo != "":
            self._titulo = titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def paginas(self):
        return self._paginas

    @paginas.setter
    def paginas(self, paginas):
        if paginas > 0:
            self._paginas = paginas

    @property
    def edicion(self):
        return self._edicion

    @edicion.setter
    def edicion(self, edicion):
        self._edicion = edicion

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad):
        self._ciudad = ciudad

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self._pais = pais

    @property
    def fecha_edicion(self):
        return self._fecha_edicion

    @fecha_edicion.setter
    def fecha_edicion(self, fecha_edicion):
        self._fecha_edicion = fecha_edicion

    # --- Métodos ---

    def leer_info(self):
        """Devuelve la información del libro como string"""
        return (
            f"Título: {self._titulo} {self._edicion}\n"
            f"Autor: {self._autor}\n"
            f"ISBN: {self._isbn}\n"
            f"{self._editorial}, {self._ciudad} ({self._pais})\n"
            f"{self._fecha_edicion}\n"
            f"{self._paginas} páginas"
        )

    def mostrar_info(self):
        """Imprime la información del libro en pantalla"""
        print(self.leer_info())

    def __str__(self):
        return self.leer_info()


