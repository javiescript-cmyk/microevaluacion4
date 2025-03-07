from src.Geometria2D import Geometria2D

class Cuadrado(Geometria2D):
    def __init__(self, coordenada_x, coordenada_y, lado):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.lado = lado
    
    # Implementación del método abstracto calcular_area
    def calcular_area(self):
        return self.lado * self.lado
    
    # Implementación del método abstracto calcular_perimetro
    def calcular_perimetro(self):
        return 4 * self.lado
