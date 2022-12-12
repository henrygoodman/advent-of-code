file1 = open('input.txt', 'r')
lines = file1.readlines()
import sys
sys.setrecursionlimit(100000)

# Part 1
grid = []
start = []
end = []

def bfs(start, end):
    queue = [[start]]
    visited = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            for c in get_choices(node):
                new_path = list(path)
                new_path.append(c)
                queue.append(new_path)
                if (c == end):
                    print(len(new_path) - 1)
                    return len(new_path) - 1
            visited.append(node)
    print("No path.")
    return 9999999999999
        
def get_choices(pos):
    choices = []
    y, x = pos
    # print(pos, ord(grid[y][x]))
    if pos[1] > 0 and (ord(grid[y][x - 1]) -1 <= ord(grid[y][x])) and (y, x - 1):
        choices.append(tuple([y, x - 1]))
    if pos[1] < len(grid[0]) - 1 and (ord(grid[y][x + 1]) -1 <= ord(grid[y][x])) and (y, x + 1):
        choices.append(tuple([y, x + 1]))
    if pos[0] > 0 and (ord(grid[y - 1][x]) -1 <= ord(grid[y][x])) and (y - 1, x):
        choices.append(tuple([y - 1, x]))
    if pos[0] < len(grid) - 1 and (ord(grid[y + 1][x]) -1 <= ord(grid[y][x])) and (y + 1, x):
        choices.append(tuple([y + 1, x]))
    return choices

def show_grid():
    for line in grid:
        print(line)

# Part 1
def part1():
    global start, end
    for line in lines:
        row = list(line.strip())
        grid.append(row)
        if 'S' in line:
            start = tuple([grid.index(row), line.index('S')])
            grid[start[0]][start[1]] = 'a'
        if 'E' in line:
            end = tuple([grid.index(row), line.index('E')])
            grid[end[0]][end[1]] = 'z'
    return bfs(start, end)

# Part 2
def part2():
    starting_positions = []
    for y in range(len(lines)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'a':
                starting_positions.append(tuple([y, x]))
    min_len = 9999999999
    for idx, s in enumerate(starting_positions[0:]):
        print(s, str(len(starting_positions) - idx) + " remaining.")
        leng = bfs(s, end)
        if leng < min_len:
            min_len = leng
    return min_len

print(part1(), part2())