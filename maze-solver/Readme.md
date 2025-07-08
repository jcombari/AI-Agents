# 🧭 Maze Solver Agent / Agente para Resolver Laberintos

An intelligent agent that navigates dynamic mazes using the A* pathfinding algorithm, adapting to both static and moving obstacles. The agent replans its path dynamically to reach the goal while avoiding collisions with moving obstacles.

Un agente inteligente que navega laberintos dinámicos utilizando el algoritmo de búsqueda A*, adaptándose a obstáculos estáticos y móviles. El agente replantea su ruta de forma dinámica para alcanzar la meta evitando colisiones.

---

## ✅ Features / Características

- Uses A* algorithm to find the shortest path from start (`S`) to goal (`G`) in a maze represented as a matrix  
- Maze includes static obstacles (`1`) and dynamic obstacles that move randomly each step  
- Agent perceives free neighboring cells and replans path whenever obstacles block the current route  
- Step-by-step animation in the terminal showing agent movement (`A`)  
- Limits the maximum number of steps to prevent infinite loops  
- Maze and obstacle parameters (size, density) configurable for flexible testing  
- Supports movement in four directions: up, down, left, and right  
- Handles cases where the agent is trapped by obstacles and no path is available  

- Utiliza el algoritmo A* para encontrar la ruta más corta desde inicio (`S`) hasta meta (`G`) en un laberinto representado como matriz  
- Laberinto incluye obstáculos estáticos (`1`) y obstáculos dinámicos que se mueven aleatoriamente en cada paso  
- El agente percibe las celdas libres vecinas y replantea la ruta cuando los obstáculos bloquean el camino actual  
- Animación paso a paso en la terminal mostrando el movimiento del agente (`A`)  
- Limita el número máximo de pasos para evitar bucles infinitos  
- Parámetros del laberinto y obstáculos configurables para pruebas variadas  
- Permite moverse en cuatro direcciones: arriba, abajo, izquierda y derecha  
- Maneja situaciones donde el agente queda atrapado sin caminos disponibles  

---

## ▶️ How to Run / Cómo usarlo

1. Open a terminal and navigate to the project folder:

       cd maze-solver

2. Verify you have Python 3 installed:

       python --version

3. Run the main program:

       python main.py

4. Watch the agent move step-by-step through the maze adapting to moving obstacles.

5. Customize maze size and obstacle density inside `maze.py` or the start/goal positions as needed.

6. Maze legend:

       S = Start position  
       G = Goal position  
       0 = Free path  
       1 = Wall or obstacle (static or dynamic)

---

## 🤖 Why is this an AI agent? / ¿Por qué es un agente de IA?

This agent:

- Continuously perceives its environment, including moving obstacles  
- Uses heuristic search (A*) to dynamically plan the shortest path  
- Acts by moving one step at a time, replanning when the environment changes  
- Demonstrates autonomy and rationality by adapting its decisions instead of following fixed rules  
- Handles cases when trapped by obstacles by detecting lack of paths and stopping

Este agente:

- Percibe continuamente su entorno, incluyendo obstáculos móviles  
- Usa búsqueda heurística (A*) para planificar dinámicamente la ruta más corta  
- Actúa moviéndose paso a paso, replanteando la ruta cuando el entorno cambia  
- Demuestra autonomía y racionalidad adaptando sus decisiones en lugar de seguir reglas fijas  
- Maneja casos donde queda atrapado sin caminos disponibles detectando la situación y deteniéndose

---

## 🆚 Difference from a normal program / Diferencia con un programa tradicional

- Traditional programs execute predetermined sequences without adapting  
- This agent evaluates the maze state at each step and replans paths accordingly, showing adaptive behavior  
- Detects and handles situations where movement is impossible due to obstacles blocking all neighboring cells

- Los programas tradicionales ejecutan secuencias predefinidas sin adaptarse  
- Este agente evalúa el estado del laberinto en cada paso y replantea rutas, mostrando comportamiento adaptativo  
- Detecta y maneja situaciones donde el movimiento es imposible porque las celdas vecinas están bloqueadas

---

## 🚩 Maze size and movement details / Tamaño del laberinto y detalles de movimiento

- The maze size is configurable; by default, it is 10 rows by 10 columns (10x10)  
- The start position is fixed at the top-left corner `(0,0)` and the goal at the bottom-right corner `(height-1, width-1)`  
- The maze grid contains static obstacles (`1`), free paths (`0`), and dynamic obstacles (`1`) that move randomly  
- The agent can move **up, down, left, and right**, one cell per step, but cannot move diagonally  
- If the agent is at a position (e.g., `(0,0)`) and all accessible neighbors (up, down, left, right) are blocked by walls or obstacles, it detects no available path and stops  
- This prevents the agent from moving into invalid or blocked cells and avoids infinite loops or crashes  

- El tamaño del laberinto es configurable; por defecto es de 10 filas por 10 columnas (10x10)  
- La posición inicial está fija en la esquina superior izquierda `(0,0)` y la meta en la esquina inferior derecha `(altura-1, ancho-1)`  
- La cuadrícula del laberinto contiene obstáculos estáticos (`1`), caminos libres (`0`) y obstáculos dinámicos (`1`) que se mueven aleatoriamente  
- El agente puede moverse **arriba, abajo, izquierda y derecha**, una celda por paso, sin movimientos diagonales  
- Si el agente está en una posición (por ejemplo, `(0,0)`) y todos los vecinos accesibles (arriba, abajo, izquierda, derecha) están bloqueados por paredes u obstáculos, detecta que no hay ruta disponible y se detiene  
- Esto evita que el agente se mueva a celdas inválidas o bloqueadas y previene bucles infinitos o fallos  

---

## 📂 Project files / Archivos del proyecto

| File             | Description                          | Descripción                                |
|------------------|------------------------------------|--------------------------------------------|
| `main.py`        | Maze initialization, agent loop, and visualization | Inicialización del laberinto, ciclo del agente y visualización |
| `astar_agent.py` | A* search algorithm implementation | Implementación del algoritmo de búsqueda A* |
| `maze.py`        | Maze representation, obstacle generation, and movement | Representación del laberinto, generación y movimiento de obstáculos |
| `README.md`      | Project guide                      | Guía del proyecto                          |

---

## 🔗 Repository link / Enlace al repositorio principal

[https://github.com/jcombari/ai-agents](https://github.com/jcombari/ai-agents)

---

Enjoy exploring maze-solving AI techniques with dynamic environments! 🤖🧭  
¡Disfruta explorando técnicas de IA para resolver laberintos con entornos dinámicos!
