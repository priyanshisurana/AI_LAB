def is_goal(state):
    return state == [1, 2, 3, 4, 5, 6, 7, 8, 0]

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)  
    row, col = zero_index // 3, zero_index % 3  

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:  
            new_zero_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            neighbors.append(new_state)

    return neighbors

def dfs(start):
    stack = [start]  
    visited = set()
    visited.add(tuple(start))

    while stack:
        current_state = stack.pop()  

        if is_goal(current_state):
            return current_state

        for neighbor in get_neighbors(current_state):
            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))
                stack.append(neighbor)  

    return None  

def get_user_input():
    print("Enter the starting configuration of the 8-puzzle as 9 numbers (0 represents the empty space):")
    input_list = input("Enter numbers separated by spaces (e.g., 1 2 3 4 5 6 0 7 8): ")
    start_state = list(map(int, input_list.split()))  
    if len(start_state) != 9 or sorted(start_state) != list(range(9)):
        print("Invalid input. Please enter exactly 9 numbers between 0 and 8.")
        return get_user_input()  
    return start_state

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

if __name__ == "__main__":
    start_state = get_user_input()  
    solution = dfs(start_state)

    if solution:
        print("Solution found:")
        print_puzzle(solution)
    else:
        print("No solution.")