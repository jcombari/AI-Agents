# 🤖 AI Agents Collection / Colección de Agentes de IA

Welcome to my growing collection of intelligent AI agents designed to solve various games and tasks using Python. Each project explores different agent types, from game-playing bots to learning algorithms.

Bienvenido a mi colección en crecimiento de agentes inteligentes de IA diseñados para resolver diversos juegos y tareas usando Python. Cada proyecto explora diferentes tipos de agentes, desde bots para juegos hasta algoritmos de aprendizaje.

---

## 🎮 Tic-Tac-Toe AI Agent / Agente de IA para Tres en Raya

This project implements an intelligent agent that plays the classic Tic-Tac-Toe game using the Minimax algorithm.

Este proyecto implementa un agente inteligente que juega al clásico juego Tres en Raya usando el algoritmo Minimax.

---

### What does this agent do? / ¿Qué hace este agente?

- ✅ Plays optimally and never loses  
- 🎮 Allows human vs AI gameplay  
- 🤖 Supports AI vs AI matches for demonstration

- ✅ Juega de forma óptima y nunca pierde  
- 👤 Permite jugar Humano vs IA  
- 🤖 Soporta partidas IA vs IA para demostración

---

### How to run it / Cómo usarlo

1. Open a terminal and navigate to the project folder:

   ```bash
   cd tictactoe-agent
   ```

2. Make sure you have Python 3 installed:

   ```bash
   python --version
   ```

3. Run the game:

   ```bash
   python main.py
   ```

4. Choose the game mode when prompted:

   ```
   Select game mode:
   1. Human vs AI
   2. AI vs AI
   ```

5. If you select `1`, you will play as `'X'` and the AI will play as `'O'`.

6. Enter the number (0–8) of the cell where you want to place your mark:

   ```
    0 | 1 | 2
   -----------
    3 | 4 | 5
   -----------
    6 | 7 | 8
   ```

---

### Why is this an AI agent? / ¿Por qué esto es un agente de IA?

An AI agent is an entity that:

- Perceives its environment (the current board)  
- Makes decisions (using Minimax to evaluate moves)  
- Acts upon the environment (places its mark)  
- Seeks to maximize performance (win or draw)

Un agente de IA es una entidad que:

- Percibe su entorno (el tablero actual)  
- Toma decisiones (usa Minimax para evaluar jugadas)  
- Actúa en el entorno (coloca su ficha)  
- Busca maximizar su desempeño (ganar o empatar)

This agent is rational and autonomous — it evaluates all possible moves and selects the best one without fixed instructions.

Este agente es racional y autónomo — evalúa todas las jugadas posibles y elige la mejor, sin instrucciones fijas.

---

### Difference from a "normal" program / Diferencia con un programa "normal"

- A traditional program executes fixed steps.  
- An intelligent agent adapts to the environment, predicts future consequences, and makes intelligent decisions to reach a goal.

- Un programa tradicional ejecuta pasos fijos.  
- Un agente inteligente se adapta al entorno, predice consecuencias futuras y toma decisiones inteligentes para alcanzar un objetivo.

---

### Project files / Archivos del proyecto

| File         | Description                        | Descripción                       |
|--------------|------------------------------------|-----------------------------------|
| `main.py`    | Game entry and user interaction    | Inicio del juego e interacción    |
| `agent.py`   | Minimax agent logic                | Lógica del agente con Minimax     |
| `game.py`    | Game rules, moves, and display     | Reglas, movimientos y visualización |
| `README.md`  | This guide                         | Esta guía                         |

---

### Repository link / Enlace al repositorio principal

[https://github.com/jcombari/ai-agents](https://github.com/jcombari/ai-agents)

---

Enjoy playing and learning how intelligent agents think! 🤖🧠  
¡Disfruta jugando y aprendiendo cómo piensan los agentes inteligentes!
