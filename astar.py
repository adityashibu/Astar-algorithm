import heapq

# Heuristic function using Manhattan distance
def manhattan_distance(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# A* algorithm with step-by-step fringe (F) and closed (C) list logging
def astar_search(grid, start, goal):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue (min-heap), initialized with start node
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start, goal), 0, start, [start]))

    closed_list = set()  # Closed set to track visited nodes
    step_counter = 1  # Step counter
    
    while open_list:
        print(f"\nStep {step_counter}:")
        step_counter += 1
        
        # Get the node with the smallest f(n)
        f, g, current, path = heapq.heappop(open_list)
        h = f - g  # Calculate h(n) as f(n) - g(n)
        
        print(f"Expanding node {current} with f = {g} + {h} = {f}")
        print(f"Current path: {path}")
        
        if current == goal:
            print("\nGoal Reached!")
            return path, g

        # Add the current node to the closed list
        closed_list.add(current)
        
        # Log the closed set C
        print(f"C = {closed_list}")
        
        # Log the fringe F after expansion
        fringe = []
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # Check if the neighbor is within bounds and not a wall (-1)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != -1:
                tile_weight = grid[neighbor[0]][neighbor[1]]
                new_g = g + tile_weight

                if neighbor not in closed_list:
                    new_f = new_g + manhattan_distance(neighbor, goal)
                    fringe.append((neighbor, new_f, new_g, manhattan_distance(neighbor, goal)))
                    heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
        
        # Log the current state of the fringe F in detail
        print("F = {", end="")
        for node, f_val, g_val, h_val in fringe:
            print(f"({node}, f = {g_val} + {h_val} = {f_val}), ", end="")
        print("}")
    
    # If no path is found, return None
    return None, float('inf')

# Grid initialization
def initialize_grid():
    grid = [
        [1, 1, -1, 2, 1],
        [2, 1, 1, 2, 1],
        [1, 1, -1, 1, 1],
        [2, 1, 2, 1, 2],
        [2, -1, -1, 1, 2],
    ]
    return grid

def main():
    grid = initialize_grid()

    start = (0, 0)
    goal = (4, 3)

    # Run the A* search
    path, cost = astar_search(grid, start, goal)

    if path:
        print("\nPath found:", path)
        print("Cost of the path:", cost)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
