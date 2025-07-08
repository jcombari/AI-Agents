import random
import os
import time

class Maze:
    def __init__(self, width=10, height=10, obstacle_prob=0.2):
        """
        Initialize the maze with given dimensions and obstacle probability.
        'width' and 'height' define maze size.
        'obstacle_prob' is the chance of placing a static obstacle in each cell.
        The start is fixed at top-left (0,0), goal at bottom-right.
        """
        self.width = width
        self.height = height
        self.obstacle_prob = obstacle_prob
        self.grid = []  # 2D list representing the maze grid
        self.start = (0, 0)
        self.goal = (height - 1, width - 1)
        self.dynamic_obstacles = set()  # positions of moving obstacles
        self.generate_maze()  # create maze on init

    def generate_maze(self):
        """
        Generate a new maze grid with start (S), goal (G), free cells (0),
        and static obstacles (1) randomly placed based on obstacle_prob.
        Also add some dynamic obstacles.
        """
        self.grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if (i, j) == self.start:
                    row.append('S')  # Start position
                elif (i, j) == self.goal:
                    row.append('G')  # Goal position
                else:
                    # Place a wall ('1') with probability obstacle_prob, else free path ('0')
                    if random.random() < self.obstacle_prob:
                        row.append('1')
                    else:
                        row.append('0')
            self.grid.append(row)
        self.dynamic_obstacles = set()
        self._add_dynamic_obstacles(5)  # Add 5 dynamic obstacles initially

    def _add_dynamic_obstacles(self, count):
        """
        Place 'count' number of dynamic obstacles randomly on free cells.
        Dynamic obstacles will move later in the simulation.
        """
        added = 0
        while added < count:
            i = random.randint(0, self.height - 1)
            j = random.randint(0, self.width - 1)
            # Ensure dynamic obstacles don't overwrite start, goal or walls
            if self.grid[i][j] == '0' and (i,j) != self.start and (i,j) != self.goal:
                self.grid[i][j] = '1'  # Represent dynamic obstacle as '1' (wall)
                self.dynamic_obstacles.add((i,j))
                added += 1

    def move_dynamic_obstacles(self):
        """
        Move each dynamic obstacle to a random adjacent free cell.
        If no free adjacent cell is available, obstacle stays in place.
        This simulates moving obstacles that the agent must avoid.
        """
        new_positions = set()
        # Clear current positions of dynamic obstacles from grid
        for (i, j) in self.dynamic_obstacles:
            self.grid[i][j] = '0'  # Clear old position

        for (i, j) in self.dynamic_obstacles:
            # Get adjacent positions that are within bounds
            moves = self.get_neighbors((i, j), consider_walls=True)
            # Filter moves to only free cells (no walls, no other dynamic obstacles)
            free_moves = [pos for pos in moves if self.grid[pos[0]][pos[1]] == '0' and pos not in new_positions and pos != self.start and pos != self.goal]
            if free_moves:
                new_pos = random.choice(free_moves)  # Randomly choose a free neighbor
                new_positions.add(new_pos)
            else:
                # No free move possible, remain in current position
                new_positions.add((i, j))

        # Mark new dynamic obstacle positions in the grid
        for (i, j) in new_positions:
            self.grid[i][j] = '1'

        # Update dynamic obstacles set with new positions
        self.dynamic_obstacles = new_positions

        # Uncomment to debug dynamic obstacle movement:
        # print(f"[DEBUG] Dynamic obstacles moved to: {self.dynamic_obstacles}")

    def get_neighbors(self, pos, consider_walls=False):
        """
        Return list of adjacent neighbors (up/down/left/right) of a given position.
        If consider_walls=False, neighbors that are walls ('1') are excluded.
        """
        i, j = pos
        neighbors = []
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.height and 0 <= nj < self.width:
                if consider_walls or self.grid[ni][nj] != '1':
                    neighbors.append((ni, nj))
        return neighbors

    def print_maze(self, agent_pos=None):
        """
        Clear the terminal and print the current maze grid.
        If 'agent_pos' is given, display agent position with 'A'.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.height):
            row_str = ''
            for j in range(self.width):
                if agent_pos == (i,j):
                    row_str += 'A '  # Agent's current position
                else:
                    row_str += self.grid[i][j] + ' '
            print(row_str)
