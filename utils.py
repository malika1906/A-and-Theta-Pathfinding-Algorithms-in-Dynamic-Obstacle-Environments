import matplotlib.pyplot as plt

def plot_path(path, grid, title="Path Visualization"):
    """Visualize the path on the grid with a title indicating the algorithm.

    This function takes a path and a grid as input and visualizes the path
    on the grid using a green line. The grid is displayed as an image, and a
    title can be provided to indicate the context of the visualization. If a
    path is provided, it will be plotted over the grid.

    Args:
        path (list): A list of tuples representing the coordinates of the path to be
            visualized.
        grid (2D array): A 2D array representing the grid on which the path is plotted.
        title (str?): The title for the plot. Defaults to "Path Visualization".

    Returns:
        None: This function does not return a value; it displays the plot directly.
    """
    plt.imshow(grid, cmap='gray', origin='lower')
    if path:
        plt.plot([x[1] for x in path], [x[0] for x in path], color='g')  # Green path
    plt.title(title)  # Add title to the plot
    plt.show()

def visualize_obstacles(grid):
    """Visualize the obstacle positions in the grid.

    This function takes a 2D grid as input and plots the positions of
    obstacles represented by the value '1'. It creates a visual
    representation using black squares for each obstacle in the grid. The
    plot is displayed with appropriate limits and an optional title.

    Args:
        grid (numpy.ndarray): A 2D array where obstacles are marked with '1'
            and free spaces are marked with '0'.

    Returns:
        None: This function does not return any value; it displays a plot.
    """
    plt.figure(figsize=(6, 6))
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                plt.plot(j, i, 'ks')  # Black squares for obstacles
    plt.xlim(0, grid.shape[1])
    plt.ylim(0, grid.shape[0])
    plt.title('Obstacles Visualization')  # Optional title
    plt.show()



def plot_comparison_paths(path_a_star, path_theta_star, grid, title="Path Comparison"):
    """Visualize both A* and Theta* paths on the same grid.

    This function creates a visual representation of two different
    pathfinding algorithms, A* and Theta*, by plotting their respective
    paths on a given grid. The A* path is displayed in blue, while the
    Theta* path is shown in orange with a dashed line. The grid is rendered
    in grayscale, and the function allows for customization of the plot
    title.

    Args:
        path_a_star (list): A list of tuples representing the coordinates of the A* path.
        path_theta_star (list): A list of tuples representing the coordinates of the Theta* path.
        grid (2D array): A 2D array representing the grid on which the paths are plotted.
        title (str?): The title of the plot. Defaults to "Path Comparison".

    Returns:
        None: This function does not return any value; it displays the plot directly.
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap='gray', origin='lower')

    # Plot A* path in blue
    if path_a_star:
        plt.plot([x[1] for x in path_a_star], [x[0] for x in path_a_star], color='blue', label='A* Path')

    # Plot Theta* path in orange
    if path_theta_star:
        plt.plot([x[1] for x in path_theta_star], [x[0] for x in path_theta_star], color='orange', linestyle='--', label='Theta* Path')

    plt.title(title)
    
    plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    
    plt.show()

