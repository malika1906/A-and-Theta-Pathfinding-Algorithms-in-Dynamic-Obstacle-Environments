from theta_star import ThetaStar

class MultiAgentThetaStar:
    def __init__(self, grid, agents):
        self.grid = grid
        self.height, self.width = grid.shape
        self.agents = agents  # List of agent (start, goal) tuples

    def search(self):
        for agent in self.agents:
            start, goal = agent
            path = ThetaStar(self.grid, start, goal).search()
            if path:
                print(f"Agent from {start} to {goal} found a path!")
                # Plot the path using your preferred method
            else:
                print(f"Agent from {start} to {goal} could not find a path!")

