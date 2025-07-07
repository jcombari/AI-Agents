# main.py
from maze import Maze
from astar_agent import astar

maze_layout = [
    ['S', '0', '1', '0', 'G'],
    ['1', '0', '1', '0', '1'],
    ['0', '0', '0', '0', '1'],
    ['0', '1', '1', '0', '0'],
    ['0', '0', '0', '0', '0']
]

maze = Maze(maze_layout)
path = astar(maze)

if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found.")
