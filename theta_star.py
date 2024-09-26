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
        path = [current]
        
        while current in came_from:
            current = came_from[current]
            path.append(current)
            
        path.reverse()
        
        return path

    def calculate_path_length(self, path):
        if not path or len(path) < 2:
            return 0
        total_length = 0
        for i in range(1, len(path)):
            total_length += self.distance(path[i - 1], path[i])
        return total_length

    def line_of_sight(self, point1, point2):
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


