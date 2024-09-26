import numpy as np
import math

class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.height, self.width = grid.shape
        self.start = start
        self.goal = goal
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def search(self):
        """Perform a search algorithm to find the shortest path from the start to
        the goal.

        This function implements a search algorithm that explores possible paths
        in a grid to find the shortest route from a starting point to a goal
        point. It uses a set to keep track of open nodes, calculates scores for
        each node based on distance and heuristic, and reconstructs the path
        once the goal is reached. The function continues until it either finds
        the goal or exhausts all possibilities.

        Returns:
            list: The reconstructed path from start to goal if found, otherwise None.
        """

        open_set = set()
        open_set.add(self.start)
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}

        while open_set:
            current = min(open_set, key=lambda node: f_score.get(node, float('inf')))
            if current == self.goal:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)

            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if not self.is_valid(neighbor) or self.grid[neighbor] == 1:
                    continue
                tentative_g_score = g_score[current] + self.distance(current, neighbor)

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, self.goal)
                    open_set.add(neighbor)

        return None

    def heuristic(self, current, goal):
        return ((goal[0] - current[0]) ** 2 + (goal[1] - current[1]) ** 2) ** 0.5
        
    def distance(self, a, b):
        return math.hypot(b[0] - a[0], b[1] - a[1])

    def is_valid(self, pos):
        return 0 <= pos[0] < self.height and 0 <= pos[1] < self.width

    def reconstruct_path(self, came_from, current):
        """Reconstruct a path from the given mapping of nodes.

        This function takes a dictionary that maps each node to its predecessor
        and reconstructs the path from the starting node to the current node. It
        iteratively follows the predecessors until it reaches the starting node,
        collecting the nodes along the way. The resulting path is returned in
        the correct order from start to end.

        Args:
            came_from (dict): A dictionary mapping each node to its predecessor.
            current: The current node from which to reconstruct the path.

        Returns:
            list: A list representing the reconstructed path from the start node to the
                current node.
        """

        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(self.start)
        return path[::-1]

