# ===== IMPORTS ====
from src.punto  import Punto
from src.linea import Linea
from src.cancion import Cancion
from src.Persona import Persona
from src.Libro import Libro

def main():
    p1 = Punto(3,2)
    print(p1.impresion())
    opuesto_p1 = p1.opuesto()
    print(opuesto_p1.impresion())
    
    print("==== PRUEBA CLASE LINEA ====")
    p2 = Punto (5,8)
    linea = Linea(p1,p2)
    print(linea)
    linea.mueve_abajo(3)
    print(linea)
    
    
      # Tarea, implementar las clases Cancion y libro
    
if __name__ == "__main__":
    main()
    
    # CLASE CANCION
    print("---- CLASE CANCION ----")
    
    cancion1 = Cancion("Life in the Fast Lane", "Eagles", "4:46")
    cancion1.mostrardatos()
    cancion1.guardar_json()
 
    cancion2 = Cancion("Hotel California", "Eagles", "6:30")
    cancion2.mostrardatos()
    cancion2.guardar_json()
 
    cancion3 = Cancion("Bohemian Rhapsody", "Queen", "5:55")
    cancion3.mostrardatos()
    cancion3.guardar_json()
 
    print(f"\nTotal de canciones creadas: {Cancion.contador_canciones}")
    # Tarea, implementar las clases Cancion y libro
    
    
    # CLASE PERSONA
    autor1 = Persona("Y. Daniel", "Liang")



    # CLASE LIBRO
    print("---- CLASE LIBRO ----")
    
    libro1 = Libro(
        titulo="Introduction to Java Programming",
        autor=autor1,
        isbn="0-13-031997-X",
        paginas=784,
        edicion="3a. edición",
        editorial="Prentice-Hall",
        ciudad="New Jersey",
        pais="USA",
        fecha_edicion="viernes 16 de noviembre de 2001"
    )

    libro1.mostrar_info()

    print("\n--- Modificando datos ---")
    libro1.paginas = 900
    libro1.edicion = "4a. edición"
    libro1.mostrar_info()