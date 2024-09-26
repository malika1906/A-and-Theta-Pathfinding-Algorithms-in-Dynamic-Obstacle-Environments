import numpy as np
import math


class ThetaStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.height, self.width = grid.shape
        self.start = start
        self.goal = goal
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def search(self):
        """Search for the shortest path from the start node to the goal node.

        This function implements a pathfinding algorithm that explores the grid
        to find the optimal route from a specified starting point to a goal
        point. It utilizes a heuristic to prioritize nodes for exploration and
        maintains scores to track the cost of reaching each node. The function
        continues until it either finds the goal node or exhausts all possible
        paths.

        Returns:
            list: A list of nodes representing the path from the start to the goal if a
                path exists; otherwise, None.
        """

        open_set = set()
        open_set.add(self.start)
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}  # Initialize f_score with heuristic

        while open_set:
            current = self.get_current_node(open_set, f_score)
            open_set.remove(current)

            if current == self.goal:
                return self.reconstruct_path(came_from, current)

            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if not self.is_valid(neighbor) or self.grid[neighbor] == 1:
                    continue

                if current in came_from and self.line_of_sight(came_from[current], neighbor):
                    tentative_g_score = g_score[came_from[current]] + self.distance(came_from[current], neighbor)
                    potential_parent = came_from[current]
                    
                else:
                    tentative_g_score = g_score[current] + self.distance(current, neighbor)
                    potential_parent = current

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = potential_parent
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)
                    open_set.add(neighbor)

        return None

    def get_current_node(self, open_set, f_score):
        return min(open_set, key=lambda node: f_score.get(node, float('inf')))

    def is_valid(self, pos):
        return 0 <= pos[0] < self.height and 0 <= pos[1] < self.width

    def distance(self, a, b):
        return math.hypot(b[0] - a[0], b[1] - a[1])

    def heuristic(self, current, goal):
        return math.hypot(goal[0] - current[0], goal[1] - current[1])

    def reconstruct_path(self, came_from, current):
        """Reconstruct a path from a given starting point to the end point.

        This function takes a dictionary that maps each node to its predecessor
        and a current node, then reconstructs the path from the start node to
        the current node by following the predecessors. The resulting path is
        reversed to present it from the start to the end.

        Args:
            came_from (dict): A dictionary mapping each node to its predecessor.
            current: The current node from which to reconstruct the path.

        Returns:
            list: A list representing the reconstructed path from the start node to the
                current node.
        """

        path = [current]
        
        while current in came_from:
            current = came_from[current]
            path.append(current)
            
        path.reverse()
        
        return path

    def calculate_path_length(self, path):
        """Calculate the total length of a given path.

        This function computes the total length of a path represented as a list
        of points. It iterates through the points in the path, calculating the
        distance between each consecutive pair of points and summing these
        distances to obtain the total path length. If the path is empty or
        contains fewer than two points, the function returns a length of zero.

        Args:
            path (list): A list of points representing the path, where each point is expected to
                be
                in a format compatible with the distance calculation.

        Returns:
            float: The total length of the path. Returns 0 if the path is empty or has
                fewer than two points.
        """

        if not path or len(path) < 2:
            return 0
        total_length = 0
        for i in range(1, len(path)):
            total_length += self.distance(path[i - 1], path[i])
        return total_length

    def line_of_sight(self, point1, point2):
        """Determine if there is a line of sight between two points on a grid.

        This function checks if a clear line of sight exists between two given
        points, `point1` and `point2`, on a grid. It uses Bresenham's line
        algorithm to iterate through the points between the two coordinates,
        verifying that each point is valid and not obstructed by any obstacles.
        The function also restricts the maximum shortcut distance to prevent
        aggressive skipping of potential obstacles.

        Args:
            point1 (tuple): The coordinates of the first point (x0, y0).
            point2 (tuple): The coordinates of the second point (x1, y1).

        Returns:
            bool: True if there is a clear line of sight, False otherwise.
        """

        x0, y0 = point1
        x1, y1 = point2
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        max_shortcut_distance = 20  # Restrict the maximum shortcut distance to prevent aggressive skipping

    # Calculate the Euclidean distance between point1 and point2
        distance = self.distance(point1, point2)
        if distance > max_shortcut_distance:
            return False  # Reject line-of-sight if the shortcut is too long

        while True:
            if not self.is_valid((x0, y0)) or self.grid[x0, y0] == 1:
                return False  # Obstacle or out of bounds
            if (x0, y0) == (x1, y1):
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
        return True


