import tkinter as tk
from random import randint
import numpy as np

class GameOfLife:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de la Vida de Conway")
        
        # Dimensiones del tablero
        self.rows = 40
        self.cols = 40
        self.cell_size = 15
        
        # Crear matriz del juego
        self.grid = np.zeros((self.rows, self.cols))
        
        # Variables de control
        self.running = False
        self.speed = 100  # milisegundos entre actualizaciones
        
        self.setup_ui()
        self.randomize_grid()
        
    def setup_ui(self):
        # Canvas para el tablero
        self.canvas = tk.Canvas(
            self.master,
            width=self.cols * self.cell_size,
            height=self.rows * self.cell_size,
            bg='white'
        )
        self.canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Botones de control
        tk.Button(self.master, text="Iniciar", command=self.start).grid(row=1, column=0, padx=5)
        tk.Button(self.master, text="Detener", command=self.stop).grid(row=1, column=1, padx=5)
        tk.Button(self.master, text="Limpiar", command=self.clear).grid(row=1, column=2, padx=5)
        tk.Button(self.master, text="Random", command=self.randomize_grid).grid(row=1, column=3, padx=5)
        
        # Eventos del mouse
        self.canvas.bind("<Button-1>", self.handle_click)
        
    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "black" if self.grid[i][j] else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
    
    def handle_click(self, event):
        # Convertir coordenadas del click a posición en la matriz
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = 1 if self.grid[row][col] == 0 else 0
            self.draw_grid()
    
    def count_neighbors(self, row, col):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                r = (row + i) % self.rows
                c = (col + j) % self.cols
                total += self.grid[r][c]
        return total
    
    def update_grid(self):
        new_grid = self.grid.copy()
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i][j] = 0
                else:
                    if neighbors == 3:
                        new_grid[i][j] = 1
        self.grid = new_grid
        self.draw_grid()
        if self.running:
            self.master.after(self.speed, self.update_grid)
    
    def start(self):
        self.running = True
        self.update_grid()
    
    def stop(self):
        self.running = False
    
    def clear(self):
        self.grid = np.zeros((self.rows, self.cols))
        self.draw_grid()
    
    def randomize_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = randint(0, 1)
        self.draw_grid()

if __name__ == "__main__":
    root = tk.Tk()
    game = GameOfLife(root)
    root.mainloop()