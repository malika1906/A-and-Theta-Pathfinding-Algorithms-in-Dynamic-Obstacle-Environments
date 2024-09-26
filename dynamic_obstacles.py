import numpy as np
import random

class Obstacle:
    def __init__(self, grid, size, shape="rectangular"):
        self.grid = grid
        self.size = size
        self.shape = shape
        self.position = self.initialize_position()

    def initialize_position(self):
        """
        Randomly places the obstacle on the grid.
        """
        x = random.randint(0, self.grid.shape[0] - self.size)
        y = random.randint(0, self.grid.shape[1] - self.size)
        self.grid[x:x+self.size, y:y+self.size] = 1
        return (x, y)

    def regenerate(self):
        """
        Randomly repositions the obstacle to create a new configuration.
        """
        x, y = self.position
        self.grid[x:x+self.size, y:y+self.size] = 0  # Clear previous position
        
        # Regenerate a new position
        x = random.randint(0, self.grid.shape[0] - self.size)
        y = random.randint(0, self.grid.shape[1] - self.size)
        self.grid[x:x+self.size, y:y+self.size] = 1
        self.position = (x, y)

def generate_circular_obstacle(grid, radius):
    """
    Generates a circular obstacle in the grid.
    """
    center_x = random.randint(radius, grid.shape[0] - radius)
    center_y = random.randint(radius, grid.shape[1] - radius)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if (i - center_x)**2 + (j - center_y)**2 <= radius**2:
                grid[i, j] = 1
                

                    




