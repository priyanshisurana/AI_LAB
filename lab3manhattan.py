import heapq

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = [(x, y) for x in range(3) for y in range(3) 
                                   if goal[x][y] == state[i][j]][0]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_neighbors(state):
    neighbors = []
    blank = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x, y = blank

    for dx, dy in possible_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def print_path(path):
    for state in path:
        for row in state:
            print(row)
        print()

def astar_manhattan(start, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start, goal), start, 0, []))  # (f, state, g, path)
    visited = set()

    while open_list:
        f, current, g, path = heapq.heappop(open_list)
        path = path + [current]

        if current == goal:
            print("Solution Found (Manhattan Distance):")
            for state in path:
                distance = manhattan_distance(state, goal)
                print(f"State: {state} | Manhattan Distance: {distance}")
            print_path(path)
            return g  # Return the depth (number of moves)

        current_tuple = tuple(map(tuple, current))
        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                h = manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (g + 1 + h, neighbor, g + 1, path))

    return -1  # No solution found

# Example usage
start = [[5, 4, 0], [6, 1, 8], [7, 3, 2]]
goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
astar_manhattan(start, goal)
