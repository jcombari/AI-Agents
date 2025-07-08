import heapq

class Agent:
    def __init__(self, maze):
        """
        Initialize agent with a reference to the maze.
        Start position is maze start.
        The path list holds the planned path from current position to goal.
        """
        self.maze = maze
        self.position = maze.start
        self.path = []

    def heuristic(self, a, b):
        """
        Heuristic function for A* - Manhattan distance between points a and b.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def perceive(self):
        """
        Agent perception: returns the list of neighbors that are currently free (not walls).
        This simulates limited sensing of the environment.
        """
        neighbors = self.maze.get_neighbors(self.position)
        return neighbors

    def a_star_search(self):
        """
        Perform A* pathfinding from agent's current position to maze goal.
        Returns a list of positions representing the path, or empty list if no path found.
        """
        start = self.position
        goal = self.maze.goal

        open_set = []
        # Heap element: (estimated total cost, cost so far, current position, path list)
        heapq.heappush(open_set, (0 + self.heuristic(start, goal), 0, start, [start]))

        visited = set()

        while open_set:
            est_total_cost, cost_so_far, current, path = heapq.heappop(open_set)

            # Check if reached goal
            if current == goal:
                return path

            if current in visited:
                continue
            visited.add(current)

            for neighbor in self.maze.get_neighbors(current):
                if neighbor in visited:
                    continue
                # Skip neighbors that are walls or dynamic obstacles ('1')
                if self.maze.grid[neighbor[0]][neighbor[1]] == '1':
                    continue
                new_cost = cost_so_far + 1
                est_total = new_cost + self.heuristic(neighbor, goal)
                heapq.heappush(open_set, (est_total, new_cost, neighbor, path + [neighbor]))

        # No path found
        return []

    def move_step(self):
        """
        Move the agent one step along the planned path.
        If no current path or position changed due to dynamic obstacles, replan path.
        Returns True if agent moved, False if stuck or no path.
        """
        # If no path or already at goal, find new path
        if not self.path or self.position == self.maze.goal:
            self.path = self.a_star_search()
            if not self.path:
                return False  # No path found, stuck

        # Move to next position in path if possible
        if len(self.path) > 1:
            self.position = self.path[1]
            self.path = self.path[1:]  # Update path removing current step
            return True
        else:
            return False
