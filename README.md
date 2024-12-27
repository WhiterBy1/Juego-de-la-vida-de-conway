"# Juego-de-la-vida-de-conway" 
# Juego de la Vida de Conway

Una implementación del clásico autómata celular "Juego de la Vida" de John Conway, desarrollada en Python utilizando la biblioteca Tkinter para la interfaz gráfica.

![Ejemplo del Juego de la Vida](/img/image.png)

## 🎮 Características

- Tablero interactivo de 40x40 celdas
- Interfaz gráfica intuitiva
- Controles para iniciar, detener y reiniciar la simulación
- Generación aleatoria de patrones
- Interacción mediante clicks para activar/desactivar células

## 🛠️ Requisitos

- Python 3.x
- NumPy
- Tkinter (viene incluido con Python)

```bash
pip install numpy
```

## 🚀 Instalación y Ejecución

1. Clona este repositorio:
```bash
git clone https://github.com/WhiterBy1/Juego-de-la-vida-de-conway.git
cd Juego-de-la-vida-de-conway
```

2. Ejecuta el juego:
```bash
python conway.py
```

## 📖 Cómo Jugar

1. **Iniciar la Simulación**: Presiona el botón "Iniciar"
2. **Pausar**: Usa el botón "Detener"
3. **Limpiar el Tablero**: Presiona "Limpiar"
4. **Patrón Aleatorio**: Click en "Random"
5. **Crear Patrones**: Click izquierdo en las celdas para activarlas/desactivarlas

## 💻 Explicación del Código

### Estructura Principal

El código está organizado en una clase principal `GameOfLife` que maneja toda la lógica del juego:

```python
class GameOfLife:
    def __init__(self, master):
        # Inicialización de variables y configuración básica
```

### Componentes Principales

1. **Inicialización (`__init__`)**
   - Configura el tamaño del tablero (40x40)
   - Inicializa la matriz del juego usando NumPy
   - Establece variables de control
   - Configura la interfaz gráfica

2. **Interfaz Gráfica (`setup_ui`)**
   - Crea el canvas para el tablero
   - Añade botones de control
   - Configura eventos del mouse

3. **Lógica del Juego (`update_grid`)**
   - Implementa las reglas de Conway:
     - Supervivencia: 2-3 vecinos
     - Nacimiento: exactamente 3 vecinos
     - Muerte: <2 o >3 vecinos

4. **Manejo de Eventos**
   - `handle_click`: Gestiona clicks del mouse
   - `start`, `stop`, `clear`: Controlan el flujo del juego
   - `randomize_grid`: Genera patrones aleatorios

### Reglas Implementadas

```python
def update_grid(self):
    new_grid = self.grid.copy()
    for i in range(self.rows):
        for j in range(self.cols):
            neighbors = self.count_neighbors(i, j)
            if self.grid[i][j] == 1:  # Célula viva
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0  # Muerte
            else:  # Célula muerta
                if neighbors == 3:
                    new_grid[i][j] = 1  # Nacimiento
```

## 🔧 Personalización

Puedes modificar varios parámetros del juego editando las variables en la clase `GameOfLife`:

- `self.rows` y `self.cols`: Dimensiones del tablero
- `self.cell_size`: Tamaño de cada célula en píxeles
- `self.speed`: Velocidad de actualización (en milisegundos)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.



## 🔍 Notas Adicionales

- El juego utiliza un tablero toroidal (los bordes se conectan)
- La actualización del tablero se realiza de forma asíncrona usando `master.after()`
- Se implementa un patrón de diseño orientado a objetos para mejor organización