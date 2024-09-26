import numpy as np
import random

class Obstacle:
    def __init__(self, grid, size, shape="rectangular"):
        self.grid = grid
        self.size = size
        self.shape = shape
        self.position = self.initialize_position()

    def initialize_position(self):
        """Randomly places the obstacle on the grid.

        This method selects a random position on the grid where the obstacle can
        be placed. It ensures that the obstacle fits within the boundaries of
        the grid by checking the dimensions of the grid against the size of the
        obstacle. The selected position is then marked on the grid.

        Returns:
            tuple: A tuple containing the x and y coordinates of the obstacle's position.
        """
        x = random.randint(0, self.grid.shape[0] - self.size)
        y = random.randint(0, self.grid.shape[1] - self.size)
        self.grid[x:x+self.size, y:y+self.size] = 1
        return (x, y)

    def regenerate(self):
        """Randomly reposition the obstacle to create a new configuration.

        This method clears the previous position of the obstacle on the grid and
        generates a new random position within the bounds of the grid. The size
        of the obstacle is taken into account to ensure that it fits within the
        grid dimensions. The new position is then updated in the grid and stored
        as the current position of the obstacle.
        """
        x, y = self.position
        self.grid[x:x+self.size, y:y+self.size] = 0  # Clear previous position
        
        # Regenerate a new position
        x = random.randint(0, self.grid.shape[0] - self.size)
        y = random.randint(0, self.grid.shape[1] - self.size)
        self.grid[x:x+self.size, y:y+self.size] = 1
        self.position = (x, y)

def generate_circular_obstacle(grid, radius):
    """Generate a circular obstacle in the grid.

    This function randomly selects a center point within the grid and
    creates a circular obstacle with a specified radius. The obstacle is
    represented by setting the corresponding grid cells to 1, indicating the
    presence of an obstacle. The center of the circle is chosen such that it
    does not exceed the boundaries of the grid.

    Args:
        grid (numpy.ndarray): A 2D array representing the grid where
            the obstacle will be generated.
        radius (int): The radius of the circular obstacle to be created.

    Returns:
        None: This function modifies the input grid in place.
    """
    center_x = random.randint(radius, grid.shape[0] - radius)
    center_y = random.randint(radius, grid.shape[1] - radius)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if (i - center_x)**2 + (j - center_y)**2 <= radius**2:
                grid[i, j] = 1
                

                    




