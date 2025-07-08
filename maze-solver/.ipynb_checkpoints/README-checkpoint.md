# 🧭 Maze Solver Agent / Agente para Resolver Laberintos

An intelligent agent that navigates mazes using the A* pathfinding algorithm. Coming soon: reinforcement learning with Q-learning for adaptive maze solving.

Un agente inteligente que navega laberintos utilizando el algoritmo de búsqueda A*. Próximamente: aprendizaje por refuerzo con Q-learning para resolver laberintos de forma adaptativa.

---

## ✅ Features / Características

- Uses A* algorithm to find the shortest path through the maze  
- Maze represented as a simple matrix for easy modification  
- Step-by-step output showing the agent's path  
- Planned: Q-learning agent that learns optimal paths by trial and error

- Utiliza el algoritmo A* para encontrar la ruta más corta en el laberinto  
- Laberinto representado como matriz simple para fácil modificación  
- Salida paso a paso mostrando la ruta del agente  
- Próximamente: agente Q-learning que aprende rutas óptimas por prueba y error

---

## ▶️ How to Run / Cómo usarlo

1. Open a terminal and navigate to the project folder:

        cd maze-solver

2. Verify you have Python 3 installed:

        python --version

3. Run the agent:

        python main.py

4. Observe the output showing the path found by the agent:

        Path found:
        (0, 0)
        (0, 1)
        (1, 1)
        ...

5. Customize the maze layout inside `main.py` to test different mazes. Use the legend:

        S = Start
        G = Goal
        0 = Free path
        1 = Wall

---

## 🤖 Why is this an AI agent? / ¿Por qué es un agente de IA?

This agent:

- Perceives the maze environment  
- Uses A* to evaluate and select optimal paths  
- Acts by moving step-by-step towards the goal  
- Seeks to maximize efficiency by minimizing path length

Este agente:

- Percibe el entorno del laberinto  
- Usa A* para evaluar y seleccionar rutas óptimas  
- Actúa moviéndose paso a paso hacia la meta  
- Busca maximizar la eficiencia minimizando la longitud de la ruta

It is autonomous and rational — planning ahead and adapting its decisions dynamically rather than following a fixed script.

Es autónomo y racional — planea con anticipación y adapta sus decisiones dinámicamente, no sigue un guion fijo.

---

## 🆚 Difference from a normal program / Diferencia con un programa tradicional

- Traditional programs follow predefined sequences  
- This agent dynamically evaluates the environment and plans paths accordingly

- Los programas tradicionales siguen secuencias predefinidas  
- Este agente evalúa dinámicamente el entorno y planifica rutas acorde a ello

---

## 📂 Project files / Archivos del proyecto

| File             | Description                     | Descripción                         |
|------------------|---------------------------------|-----------------------------------|
| `main.py`        | Maze setup and agent execution   | Configuración del laberinto y ejecución del agente |
| `astar_agent.py` | A* pathfinding algorithm         | Algoritmo de búsqueda A*           |
| `maze.py`        | Maze representation and helpers | Representación del laberinto y funciones auxiliares |
| `README.md`      | This guide                      | Esta guía                         |

---

## 🔗 Repository link / Enlace al repositorio principal

[https://github.com/jcombari/ai-agents](https://github.com/jcombari/ai-agents)

---

Enjoy exploring maze-solving AI techniques! 🤖🧭  
¡Disfruta explorando técnicas de IA para resolver laberintos!
