# maze.py
import numpy as np

class Maze:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.start = tuple(map(int, np.argwhere(self.grid == 'S')[0]))
        self.goal = tuple(map(int, np.argwhere(self.grid == 'G')[0]))
        self.rows, self.cols = self.grid.shape

    def is_valid(self, position):
        x, y = position
        return (0 <= x < self.rows) and (0 <= y < self.cols) and self.grid[x][y] != '1'
    
    def neighbors(self, pos):
        x, y = pos
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            new = (x+dx, y+dy)
            if self.is_valid(new):
                yield new
