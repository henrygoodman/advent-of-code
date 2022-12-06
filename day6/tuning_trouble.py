file1 = open('input.txt', 'r')
lines = file1.readlines()

def calc(n, line):
    for i in range(len(line)):
        if len(set([line[i:i+n]])) == n:
            return i + n

# Part 1
def part1():
    return calc(4, lines[0])

# Part 2
def part2():
    return calc(14, lines[0])

print(part1(), part2())