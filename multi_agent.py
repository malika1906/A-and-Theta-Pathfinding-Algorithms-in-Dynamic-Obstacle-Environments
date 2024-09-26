from theta_star import ThetaStar

class MultiAgentThetaStar:
    def __init__(self, grid, agents):
        self.grid = grid
        self.height, self.width = grid.shape
        self.agents = agents  # List of agent (start, goal) tuples

    def search(self):
        """Search for paths for multiple agents in a grid.

        This function iterates through a list of agents, each defined by a start
        and goal position. For each agent, it utilizes the ThetaStar algorithm
        to find a path from the start to the goal. If a path is found, it prints
        a message indicating success; otherwise, it indicates failure.
        """

        for agent in self.agents:
            start, goal = agent
            path = ThetaStar(self.grid, start, goal).search()
            if path:
                print(f"Agent from {start} to {goal} found a path!")
                # Plot the path using your preferred method
            else:
                print(f"Agent from {start} to {goal} could not find a path!")

