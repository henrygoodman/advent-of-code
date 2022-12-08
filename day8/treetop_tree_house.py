file1 = open('input.txt', 'r')
lines = file1.readlines()

# Part 1

grid = []

# A point is visible if it is on an edge, or if it is taller than all trees between it and an edge.
def visible(y, x):
    if (x == 0 or x == len(grid[0]) - 1 or y == 0 or y == len(lines) - 1):
        return True

    ret_val = True
    # Negative X direction
    for i in range(0, x):
        if (grid[y][x] <= grid[y][i]):
            ret_val = False
    if ret_val:
        return True

    # Positive X direction
    ret_val = True
    for i in range(x+1, len(grid[0])):
        if (grid[y][x] <= grid[y][i]):
            ret_val = False
    if ret_val:
        return True

    # Positive Y direction
    ret_val = True
    for i in range(0, y):
        if (grid[y][x] <= grid[i][x]):
            ret_val = False
    if ret_val:
        return True

    # Negative Y direction
    ret_val = True
    for i in range(y+1, len(lines)):
        if (grid[y][x] <= grid[i][x]):
            ret_val = False
    if ret_val:
        return True
    return ret_val

# Any tree on an edge has a score of 0. Otherwise, count trees outwards until we reach a tree of greater height.
def get_scenic_score(y, x):
    if (x == 0 or x == len(grid[0]) - 1 or y == 0 or y == len(lines) - 1):
        return 0

    counts = [0,0,0,0]

    # Negative X direction
    for i in range(x - 1, -1, -1):
        counts[0] += 1
        if (grid[y][x] <= grid[y][i]):
            break

    # Positive X direction
    for i in range(x+1, len(grid[0])):
        counts[1] += 1
        if (grid[y][x] <= grid[y][i]):
            break

    # Positive Y direction
    for i in range(y - 1, -1, -1):
        counts[2] += 1
        if (grid[y][x] <= grid[i][x]):
            break

    # Negative Y direction
    for i in range(y+1, len(lines)):
        counts[3] += 1
        if (grid[y][x] <= grid[i][x]):
            break

    return counts[0] * counts[1] * counts[2] * counts[3]

def part1():
    count = 0
    for line in lines:
        grid.append(list(line.strip()))
    
    for x in range(len(grid[0])):
        for y in range(len(lines)):
            count += visible(x, y)
    return count

# Part 2
def part2():
    scenic_scores = []
    for x in range(len(grid[0])):
        for y in range(len(lines)):
            scenic_scores.append(get_scenic_score(x, y))
    return max(scenic_scores)

print(part1(), part2())