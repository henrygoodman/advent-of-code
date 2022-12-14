with open('input.txt', 'r') as file:
    lines = file.readlines()

class Cave:
    def __init__(self, w_max, w_min, h, padding):
        self.w_max = w_max
        self.w_offset = w_min - (padding + 1)
        self.cave = [['.'] * (2 * (padding + 1) + w_max - w_min + 1) for _ in range(h+1)]
        self.sand_pos = [0,500]
        self.settled = True
        self.count = - 1

    def set_rock(self, pos):
        self.cave[pos[1]][pos[0] - self.w_offset] = '#'

    def drop_sand(self):
        if self.settled:
            self.count += 1
            self.sand_pos = [0, 500 - self.w_offset]
            self.cave[0][500 - self.w_offset] = 'o'
            self.settled = False
        return self.update_sand()

    def update_sand(self):
        try:
            if self.cave[self.sand_pos[0] + 1][self.sand_pos[1]] not in 'o#':
                self.cave[self.sand_pos[0]][self.sand_pos[1]] = '.'
                self.cave[self.sand_pos[0] + 1][self.sand_pos[1]] = 'o'
                self.sand_pos = [self.sand_pos[0] + 1, self.sand_pos[1]]
            elif self.cave[self.sand_pos[0] + 1][self.sand_pos[1] - 1] not in 'o#':
                self.cave[self.sand_pos[0]][self.sand_pos[1]] = '.'
                self.cave[self.sand_pos[0] + 1][self.sand_pos[1]  - 1] = 'o'
                self.sand_pos = [self.sand_pos[0] + 1, self.sand_pos[1] - 1]
            elif self.cave[self.sand_pos[0] + 1][self.sand_pos[1] + 1] not in 'o#':
                self.cave[self.sand_pos[0]][self.sand_pos[1]] = '.'
                self.cave[self.sand_pos[0] + 1][self.sand_pos[1]  + 1] = 'o'
                self.sand_pos = [self.sand_pos[0] + 1, self.sand_pos[1] + 1]
            else:
                self.settled = True
                if self.sand_pos == [0, 500 - self.w_offset]:
                    return self.count + 1
        except IndexError as e:
            return self.count

    def __repr__(self):
        ret = ''
        for y in range(len(self.cave)):
            for x in range(len(self.cave[0])):
                ret += self.cave[y][x]
            ret += '\n'
        return ret
    
def init_cave(void):
    min_x, max_x, max_y = 500, 0, 0

    # Get the dimensions of the data structure to store the cave.
    for l in lines:
        line = list(map(lambda x: x.split(','), l.strip().split('->')))
        for inst in line:
            if int(inst[0]) < min_x:
                min_x = int(inst[0])
            if int(inst[0]) > max_x:
                max_x = int(inst[0])
            if int(inst[1]) > max_y:
                max_y = int(inst[1])

    # Initialise the 2d list using dimensions.
    cave = Cave(max_x, min_x, 2 + max_y, 2 * max_x + 1)

    # Set the rocks
    for l in lines:
        line = list(map(lambda x: x.strip().split(','), l.strip().split('->')))
        previous_inst = line[0]
        for inst in line[1:]:
            pos_to = [int(inst[0]), int(inst[1])]
            pos_from = [int(previous_inst[0]), int(previous_inst[1])]
            for pos in get_positions_in_line(pos_from, pos_to):
                cave.set_rock(pos)
            previous_inst = inst

    # Set the floor as rock if the void is disabled.
    if not void:
        cave.cave[max_y + 2] = '#' * len(cave.cave[max_y])

    return cave

def get_positions_in_line(pos_from, pos_to):
    ret = []
    if (pos_from[0] == pos_to[0]):
        if (pos_from[1] <= pos_to[1]):
            for i in range(pos_to[1] - pos_from[1] + 1):
                ret.append([pos_from[0], pos_from[1] + i])
        else:
            for i in range(pos_from[1] - pos_to[1]  + 1):
                ret.append([pos_to[0], pos_to[1] + i])
    else:
        if (pos_from[0] <= pos_to[0]):
            for i in range(pos_to[0] - pos_from[0] + 1):
                ret.append([pos_from[0] + i, pos_from[1]])
        else:
            for i in range(pos_from[0] - pos_to[0]  + 1):
                ret.append([pos_to[0] + i, pos_to[1]])
    return ret 

# Part 1
def part1():
    cave = init_cave(1)
    ret = None
    while (ret is None):
        ret = cave.drop_sand()
    return ret

# Part 2
def part2():
    cave = init_cave(0)
    ret = None
    while (ret is None):
        ret = cave.drop_sand()
    return ret

print(part1(), part2())