class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    def impresion(self):
        return f"({self.x}, {self.y})"
    
    def opuesto(self):
        "Devuelvo el punto opuesto"
        factor = -1
        return Punto(self.x * factor, self.y * factor)
    
    def __str__(self):
        return f"({self.x}, {self.y})"