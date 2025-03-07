import tkinter as tk
from src.Cuadrado import Cuadrado

# Crear una clase de ventana con Tkinter
class VentanaCuadrado(tk.Tk):
    def __init__(self, cuadrado):
        super().__init__()
        
        self.title("Cuadrado Visual")
        self.geometry("400x400")
        
        # Crear un Canvas para dibujar el cuadrado
        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack()

        # Dibujar el cuadrado en el canvas
        self.dibujar_cuadrado(cuadrado)

    def dibujar_cuadrado(self, cuadrado):
        # Usar las coordenadas y el lado del cuadrado para dibujar el rectángulo
        self.canvas.create_rectangle(
            cuadrado.coordenada_x, cuadrado.coordenada_y,
            cuadrado.coordenada_x + cuadrado.lado, cuadrado.coordenada_y + cuadrado.lado,
            outline="black", fill="blue", width=2
        )

# Crear una instancia de Cuadrado
cuadrado = Cuadrado(50, 50, 100)

# Crear la ventana y dibujar el cuadrado
ventana = VentanaCuadrado(cuadrado)
ventana.mainloop()

