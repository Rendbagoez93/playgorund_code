# Main Script

# Map Grid
grid_size = 5
grid = [
    ['[X]', '[X]', '[X]', '[X]', '[X]'],
    ['[X]', '[X]', '[X]', '[X]', '[X]'],
    ['[X]', '[X]', '[X]', '[X]', '[X]'],
    ['[X]', '[X]', '[X]', '[X]', '[X]'],
    ['[X]', '[X]', '[X]', '[X]', '[X]']
] 

# Starting cursor position
cursor_x, cursor_y = 0, 0

def display_grid():
    for y in range(grid_size):
        for x in range(grid_size):
            if x == cursor_x and y == cursor_y:
                print('[O]', end=' ')
            else:
                print(grid[y][x], end=' ')
        print()
    print()

# Movement function
def move_cursor(direction):
    global cursor_x, cursor_y
    if direction == 'w':
        cursor_y = (cursor_y - 1) % grid_size
    elif direction == 's':
        cursor_y = (cursor_y + 1) % grid_size
    elif direction == 'a':
        cursor_x = (cursor_x - 1) % grid_size
    elif direction == 'd':
        cursor_x = (cursor_x + 1) % grid_size

# Game loop
while True:
    display_grid()
    command = input("Move (W/A/S/D), or Q to quit: ").lower()
    if command == 'q':
        print("Exiting...")
        break
    move_cursor(command)
