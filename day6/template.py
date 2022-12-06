file1 = open('input.txt', 'r')
lines = file1.readlines()

# Part 1

def calc(n, line):
    for i in range(len(line)):
        if len(set(list([line[i:i+n]][0]))) == n:
            return i + n

def part1():
    return calc(4, lines[0])

# Part 2
def part2():
    return calc(14, lines[0])

print(part1(), part2())