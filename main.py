import numpy as np
import random
import time
from theta_star import ThetaStar
from a_star import AStar
from dynamic_obstacles import Obstacle, generate_circular_obstacle
from utils import plot_comparison_paths
import matplotlib.pyplot as plt

if __name__ == '__main__':
    grid = np.zeros((100, 100))  # Larger grid for complexity

    # Generate obstacles
    num_obstacles = 40  # Increase the number of obstacles
    max_size = 10  # Larger obstacle size
    obstacles = [Obstacle(grid, size=random.randint(5, max_size)) for _ in range(num_obstacles)]

    # Add circular obstacles
    for _ in range(5):
        generate_circular_obstacle(grid, radius=random.randint(5, 5))

    start = (0, 0)
    goal = (90, 80)

    # Arrays to track performance metrics
    a_star_times = []
    theta_star_times = []

    # Initial pathfinding comparison (before obstacles move)
    print("Initial pathfinding comparison (before obstacles regenerate):")

    # A* search
    a_star = AStar(grid, start, goal)
    start_time = time.time()
    path_a_star = a_star.search()
    a_star_time = time.time() - start_time
    a_star_times.append(a_star_time)

    # Theta* search

    theta_star = ThetaStar(grid, start, goal)
    start_time = time.time()
    path_theta_star = theta_star.search()
    theta_star_time = time.time() - start_time
    theta_star_length = theta_star.calculate_path_length(path_theta_star) if path_theta_star else 0
    theta_star_times.append(theta_star_time)


    # Display initial comparison paths on the same plot
    plot_comparison_paths(path_a_star, path_theta_star, grid, title="Initial Paths: A* vs Theta*")

    # Print initial results
    if path_a_star:
        print(f"A* Path found! Time taken: {a_star_time:.4f} seconds, Path length: {len(path_a_star)}")
    else:
        print("A* Path not found!")

    # Print results
    if path_theta_star:
        print(f"Theta* Path found! Time taken: {theta_star_time:.4f} seconds, Path length: {theta_star_length}")
    else:
        print("Theta* Path not found!")

    # Simulate regenerating obstacles and replan
    print("\nDynamic obstacle comparison (with regenerated obstacles):")
    for time_step in range(10):  # Run for multiple time steps
        print(f"\nTime step: {time_step + 1}")

        # Randomly reposition all obstacles
        for obstacle in obstacles:
            obstacle.regenerate()

        # A* search after obstacles regenerate
        start_time = time.time()
        path_a_star = a_star.search()
        a_star_time = time.time() - start_time
        a_star_times.append(a_star_time)

        # Theta* search after obstacles regenerate
        start_time = time.time()
        path_theta_star = theta_star.search()
        theta_star_time = time.time() - start_time
        theta_star_times.append(theta_star_time)

        # Display comparison paths on the same plot
        plot_comparison_paths(path_a_star, path_theta_star, grid, title=f"Paths at Time Step {time_step + 1}: A* vs Theta*")

        # Print results for this time step
        if path_a_star:
            print(f"A* Path found after regenerating obstacles! Time taken: {a_star_time:.4f} seconds, Path length: {len(path_a_star)}")
        else:
            print("A* Path not found after regenerating obstacles!")

        if path_theta_star:
            print(f"Theta* Path found after regenerating obstacles! Time taken: {theta_star_time:.4f} seconds, Path length: {len(path_theta_star)}")
        else:
            print("Theta* Path not found after regenerating obstacles!")

        time.sleep(1)  # Add delay to visualize steps

    # Now visualize the time comparison metrics
    steps = list(range(1, len(a_star_times) + 1))

    # Plot time taken for both algorithms
    plt.figure(figsize=(10, 5))
    plt.plot(steps, a_star_times, label="A* Time Taken", marker='o')
    plt.plot(steps, theta_star_times, label="Theta* Time Taken", marker='o')
    plt.xlabel('Time Step')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Comparison Between A* and Theta*')
    plt.legend()
    plt.show()

