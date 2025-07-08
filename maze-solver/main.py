import time
from maze import Maze
from astar_agent import Agent

def main():
    """
    Main program loop:
    - Initialize maze and agent
    - Loop until agent reaches goal or max steps reached
    - Each iteration:
        - Print maze with agent position
        - Agent moves one step toward goal
        - Maze moves dynamic obstacles
        - Wait a bit before next step
    """
    maze = Maze(width=10, height=10, obstacle_prob=0.2)
    agent = Agent(maze)

    steps = 0
    max_steps = 100  # Safety limit to prevent infinite loops

    while agent.position != maze.goal and steps < max_steps:
        maze.print_maze(agent.position)
        print(f"Step: {steps}, Agent position: {agent.position}")
        moved = agent.move_step()
        if not moved:
            print("No path found, agent stuck!")
            break

        maze.move_dynamic_obstacles()  # Move obstacles dynamically

        time.sleep(0.5)  # Pause for readability
        steps += 1

    # Final maze print and status message
    maze.print_maze(agent.position)
    if agent.position == maze.goal:
        print(f"Goal reached in {steps} steps!")
    else:
        print("Failed to reach the goal.")

if __name__ == "__main__":
    main()


