### A* and Theta* Pathfinding Algorithms in Dynamic Obstacle Environments

## Project Overview
This project implements and compares two pathfinding algorithms, A* and Theta*, within a dynamic grid environment containing both static and regenerating obstacles. The main objective is to analyze the efficiency and performance of these algorithms when navigating through a changing obstacle field. 

## Algorithms Implemented
1. **A* Algorithm**: A heuristic-based pathfinding algorithm that finds the shortest path by exploring nodes on a grid. It ensures optimal paths but can be computationally intensive in complex environments.
2. **Theta* Algorithm**: An extension of A* that allows for diagonal shortcuts (line-of-sight) between nodes. It attempts to find more direct paths compared to A*, potentially improving pathfinding time. This implementation includes a version without line-of-sight for comparison.

## Features
- **Dynamic Obstacles**: The grid environment contains randomly generated obstacles that change (regenerate) over time, simulating a dynamic, real-world scenario.
- **Performance Metrics**: The algorithms are evaluated on two main metrics: computational time and path length.
- **Visualization**: 
  - Graphical representation of paths taken by both algorithms at each time step.
  - Time comparison plots showing the performance of A* vs. Theta* over multiple time steps.
- **Comparison**: Provides insights into the trade-offs between the traditional grid-based A* and the more flexible Theta* algorithm in different environmental complexities.

## Key Observations
*Theta Consistency*: Theta* demonstrates a more stable and consistent time performance across different time steps. Its flexibility in taking diagonal shortcuts (line-of-sight) allows it to adapt to changing obstacle configurations more efficiently. This approach minimizes the number of nodes it needs to explore, maintaining a relatively constant computation time.
*A Variability*: A* shows significant fluctuation in its computational time. The spikes and dips indicate that A* is more sensitive to changes in obstacle density and layout. When obstacles force complex, grid-constrained paths, A* requires more extensive node evaluations, resulting in longer computation times.

## Result Analysis
*Theta’s Advantage*: The consistency in Theta*'s performance suggests it handles dynamic environments better by finding more direct paths when possible. It performs well in most scenarios, even when obstacles regenerate.
*A Sensitivity*: A* performs efficiently in less complex scenarios where the obstacles do not impede its grid-based traversal. However, its strict adherence to grid paths results in fluctuating performance, especially when faced with denser obstacle configurations.
