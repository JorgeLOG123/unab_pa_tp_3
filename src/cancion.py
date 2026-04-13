"""Nivel 3: Clase Cancion
Crear archivo linea.py dentro de src y desarrollar la clase Cancion con los siguientes atributos:
● titulo: una variable String que guarda el título de la canción.
● autor: una variable String que guarda el autor de la canción.
Con los siguientes métodos:
● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la canción
(por este orden).
● get_titulo(): devuelve el título de la canción.
● get_autor(): devuelve el autor de la canción.
● set_titulo(String): establece el título de la canción.
● set_autor(String): establece el autor de la canción"""

# Hola profe! Me tome el tiempo de agregarle cosas que he visto por mi cuenta! :)))




import json
from datetime import datetime
 
 
class Cancion:
 
    contador_canciones = 0
 
    def __init__(self, titulo, autor, duracion):
        Cancion.contador_canciones += 1
        self.num = Cancion.contador_canciones
        self._titulo = titulo
        self._autor = autor
        self._duracion = duracion
        self._fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M")
 
    def mostrardatos(self):
        print(f"""
        Cancion numero : {self.num}
        Titulo         : {self.titulo}
        Autor          : {self.autor}
        Duracion       : {self.duracion}
        Fecha agregada : {self._fecha_creacion}
        """)
 
    def guardar_json(self):
    
        try:
            with open("canciones.json", "r", encoding="utf-8") as archivo: # Sin encoding — puede fallar con tildes
                canciones = json.load(archivo)
        except FileNotFoundError:
            canciones = []
 
        # 2. Arma el diccionario con los datos de esta canción
        nueva_cancion = {
            "num": self.num,
            "titulo": self._titulo,
            "autor": self._autor,
            "duracion": self._duracion,
            "fecha_creacion": self._fecha_creacion
        }
 
        # 3. Agrega la nueva canción a la lista
        canciones.append(nueva_cancion)
 
        # 4. Guarda todo de nuevo en el archivo
        with open("canciones.json", "w", encoding="utf-8") as archivo:
            json.dump(canciones, archivo, indent=4, ensure_ascii=False)
 
        print(f'✅ Cancion "{self._titulo}" guardada en canciones.json')
 
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
    def duracion(self):
        return self._duracion
 
    @duracion.setter
    def duracion(self, duracion):
        if duracion > 0:
            self._duracion = duracion