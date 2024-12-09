import numpy as np


def N(grid, pos, num):
    return grid[pos[0]-num, pos[1]] if pos[0]-num >= 0 else ''

def NE(grid, pos, num):
    return grid[pos[0]-num, pos[1]+num] if pos[0]-num >= 0 and pos[1]+num < grid.shape[1] else ''

def E(grid, pos, num):
    return grid[pos[0], pos[1]+num] if pos[1]+num < grid.shape[1] else ''

def SE(grid, pos, num):
    return grid[pos[0]+num, pos[1]+num] if pos[0]+num < grid.shape[0] and pos[1]+num < grid.shape[1] else ''

def S(grid, pos, num):
    return grid[pos[0]+num, pos[1]] if pos[0]+num < grid.shape[0] else ''

def SW(grid, pos, num):
    return grid[pos[0]+num, pos[1]-num] if pos[0]+num < grid.shape[0] and pos[1]-num >= 0 else ''

def W(grid, pos, num):
    return grid[pos[0], pos[1]-num] if pos[1]-num >= 0 else ''

def NW(grid, pos, num):
    return grid[pos[0]-num, pos[1]-num] if pos[0]-num >= 0 and pos[1]-num >= 0 else ''

DIRECTIONS = [N, NE, E, SE, S, SW, W, NW]


# part 1

TARGET = 'XMAS'

with open('day4/input.txt') as f:
    grid = np.stack([np.fromiter(line.strip(), dtype=(str, 1)) for line in f])

count = 0
for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        for direction in DIRECTIONS:
            word = ''
            for i in range(len(TARGET)):
                word += direction(grid, (x, y), i)
            if word == TARGET:
                count += 1

print(f'{TARGET} count: {count}')


# part 2

count = 0
for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        if grid[x, y] != 'A':
            continue

        if (
            ((NW(grid, (x, y), 1) == 'M' and
              SE(grid, (x, y), 1) == 'S') or 
             (NW(grid, (x, y), 1) == 'S' and
              SE(grid, (x, y), 1) == 'M')) and
            ((NE(grid, (x, y), 1) == 'M' and
              SW(grid, (x, y), 1) == 'S') or 
             (NE(grid, (x, y), 1) == 'S' and
              SW(grid, (x, y), 1) == 'M')) 
        ):
            count += 1

print(f'X-MAS count: {count}')