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

- Utiliza el algoritmo A* para encontrar la ruta más corta desde inicio (`S`) hasta meta (`G`) en un laberinto representado como matriz  
- Laberinto incluye obstáculos estáticos (`1`) y obstáculos dinámicos que se mueven aleatoriamente en cada paso  
- El agente percibe las celdas libres vecinas y replantea la ruta cuando los obstáculos bloquean el camino actual  
- Animación paso a paso en la terminal mostrando el movimiento del agente (`A`)  
- Limita el número máximo de pasos para evitar bucles infinitos  
- Parámetros del laberinto y obstáculos configurables para pruebas variadas

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

Este agente:

- Percibe continuamente su entorno, incluyendo obstáculos móviles  
- Usa búsqueda heurística (A*) para planificar dinámicamente la ruta más corta  
- Actúa moviéndose paso a paso, replanteando la ruta cuando el entorno cambia  
- Demuestra autonomía y racionalidad adaptando sus decisiones en lugar de seguir reglas fijas

---

## 🆚 Difference from a normal program / Diferencia con un programa tradicional

- Traditional programs execute predetermined sequences without adapting  
- This agent evaluates the maze state at each step and replans paths accordingly, showing adaptive behavior

- Los programas tradicionales ejecutan secuencias predefinidas sin adaptarse  
- Este agente evalúa el estado del laberinto en cada paso y replantea rutas, mostrando comportamiento adaptativo

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
