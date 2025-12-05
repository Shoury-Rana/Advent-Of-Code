import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    data = f.readlines()
    data = [d.strip('\n') for d in data]

# Part 1
def count_adjacent_at(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "@":
                count += 1
    return count

def count_accessible(grid):
    accessible = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                if count_adjacent_at(grid, r, c) < 4:
                    accessible += 1

    return accessible

print(count_accessible(data))


# Part 2
def count_adjacent(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1

    return count

def total_removable_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    if count_adjacent(grid, r, c) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed

print(total_removable_rolls([list(row) for row in data]))