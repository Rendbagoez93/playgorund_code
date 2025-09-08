# Main Script

# Define two 3x3 matrices
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Matrix Addition
def add_matrices(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Matrix Subtraction
def subtract_matrices(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Matrix Multiplication
def multiply_matrices(X, Y):
    result = []
    for i in range(len(X)):
        row = []
        for j in range(len(Y[0])):
            total = sum(X[i][k] * Y[k][j] for k in range(len(Y)))
            row.append(total)
        result.append(row)
    return result

# Display neatly
def print_matrix(name, M):
    print(f"\n{name}:")
    for row in M:
        print("  ", row)

# Run operations
add_result = add_matrices(A, B)
sub_result = subtract_matrices(A, B)
mul_result = multiply_matrices(A, B)

print_matrix("A + B", add_result)
print_matrix("A - B", sub_result)
print_matrix("A x B", mul_result)
# ============= 2 ==============

# New matrices for the second part
import os

# 3x4 keypad grid (with operators)
grid = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['+', '0', '-'],
    ['*', '=', '/'],
    ['C', ' ', 'Q']
]

rows, cols = len(grid), len(grid[0])
cursor_x, cursor_y = 0, 0
expression = ""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display():
    clear_screen()
    print("=== Simple Calculator ===")
    print(f"Expression: {expression or ' '}")
    print()

    for y in range(rows):
        row = ""
        for x in range(cols):
            cell = grid[y][x]
            if x == cursor_x and y == cursor_y:
                row += f"[{cell:^3}]"
            else:
                row += f" {cell:^3} "
        print(row)
    print("\nUse W/A/S/D to move, E to select key.\n")

while True:
    display()
    command = input("Command (W/A/S/D/E): ").lower()

    if command == 'w' and cursor_y > 0:
        cursor_y -= 1
    elif command == 's' and cursor_y < rows - 1:
        cursor_y += 1
    elif command == 'a' and cursor_x > 0:
        cursor_x -= 1
    elif command == 'd' and cursor_x < cols - 1:
        cursor_x += 1
    elif command == 'e':
        selected = grid[cursor_y][cursor_x]
        if selected == '=':
            try:
                expression = str(eval(expression))
            except:
                expression = "Error"
        elif selected == 'C':
            expression = ""
        elif selected == 'Q':
            print("Goodbye!")
            break
        elif selected.strip():
            expression += selected