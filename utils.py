import matplotlib.pyplot as plt

def plot_path(path, grid, title="Path Visualization"):
    """
    Visualize the path on the grid with a title indicating the algorithm.
    """
    plt.imshow(grid, cmap='gray', origin='lower')
    if path:
        plt.plot([x[1] for x in path], [x[0] for x in path], color='g')  # Green path
    plt.title(title)  # Add title to the plot
    plt.show()

def visualize_obstacles(grid):
    """
    Visualize the obstacle positions in the grid.
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
    """
    Visualize both A* and Theta* paths on the same grid.
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

