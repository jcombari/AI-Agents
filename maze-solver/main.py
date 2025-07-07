import time

# Laberinto representado como matriz
# S = Start, G = Goal, 0 = camino libre, 1 = pared
maze = [
    ['S', '0', '1', '0', 'G'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '0', '0', '1'],
    ['1', '1', '1', '0', '1']
]

def print_maze(maze, position):
    for i, row in enumerate(maze):
        row_str = ''
        for j, cell in enumerate(row):
            if (i, j) == position:
                row_str += 'A '  # Agente aquí
            else:
                row_str += f'{cell} '
        print(row_str)
    print('\n')

# Simulación de camino encontrado (lista de posiciones)
path = [(0,0), (0,1), (1,1), (2,1), (2,2), (2,3), (3,3), (0,4)]

# Mostrar laberinto paso a paso con pausa
for pos in path:
    print_maze(maze, pos)
    time.sleep(0.7)
