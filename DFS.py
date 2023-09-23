def minKnightMoves(start_x, start_y, target_x, target_y):
    # Define possible knight moves
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Create a set to store visited positions
    visited = set()

    # Define a DFS function with depth limit
    def dfs(x, y, steps, depth_limit):
        # Check if we've reached the target square
        if x == target_x and y == target_y:
            return steps

        # Check if this square has already been visited or if we've exceeded the depth limit
        if (x, y) in visited or steps >= depth_limit:
            return float('inf')

        # Mark this square as visited
        visited.add((x, y))

        # Initialize a list to store the number of moves for each possible move
        move_counts = []

        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            move_counts.append(dfs(next_x, next_y, steps + 1, depth_limit))

        # Remove the current square from the visited set after visiting all neighbors
        visited.remove((x, y))

        # Return the minimum number of moves among all possible moves
        return min(move_counts)

    depth_limit = abs(target_x - start_x) + abs(target_y - start_y) + 2  # Adjust depth limit as needed
    return dfs(start_x, start_y, 0, depth_limit)


import time
# Example usage:
start_x, start_y = 0,0
target_x, target_y = 3,3
start_time = time.time()
result = minKnightMoves(start_x, start_y, target_x, target_y)
end_time = time.time()

print("Minimum number of moves:", result)
print("Time taken:", end_time - start_time, "seconds")