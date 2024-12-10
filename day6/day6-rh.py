import numpy as np


# part 1

def N(grid, pos, num=1):
    return (pos[0]-num, pos[1])

def E(grid, pos, num=1):
    return (pos[0], pos[1]+num)

def S(grid, pos, num=1):
    return (pos[0]+num, pos[1])

def W(grid, pos, num=1):
    return (pos[0], pos[1]-num)

def test_pos(grid, pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < grid.shape[0] and pos[1] < grid.shape[1]

def simulate(grid, start_pos):
    print(f"Starting at {start_pos}")
    direction_idx = 0
    direction = DIRECTIONS[direction_idx]
    pos = start_pos
    while test_pos(grid, new_pos := direction(grid, pos)):
        # np.savetxt('day6/output.txt', grid, delimiter='', fmt='%s')
        if grid[new_pos] == '#':
            direction_idx = (direction_idx + 1) % len(DIRECTIONS)
            # print(f"Detected '#', changed direction from {direction} to {DIRECTIONS[direction_idx]}")
            direction = DIRECTIONS[direction_idx]
        else:
            if grid[pos[0]][pos[1]]  != 'X':
                grid[pos[0]][pos[1]] = 'X'
            # print(f"Marked {pos} as {grid[pos]}")
            pos = new_pos
            # print(f"Moved to {new_pos}")
    print(f"Finished at {pos}")
    grid[pos[0]][pos[1]] = 'X' # Mark the final position too.
    return grid

DIRECTIONS = [N, E, S, W]

with open('day6/input.txt') as f:
    original_grid = np.stack([np.fromiter(line.strip(), dtype=(str, 1)) for line in f])


start_pos = np.argwhere(original_grid == '^')[0]
grid = original_grid.copy()
grid = simulate(grid, start_pos)

# np.savetxt('day6/output.txt', grid, delimiter='', fmt='%s') # Print the path taken
distinct_positions = np.count_nonzero(grid == 'X')
print(f"Number of distinct positions visited: {distinct_positions}")


# part 2

