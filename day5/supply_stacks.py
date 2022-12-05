file1 = open('input.txt', 'r')
lines = file1.readlines()

# Manually store the input data in a 2d list, treat them as queues.
# For some reason Python doesnt like copying lists (like with .copy() or list())
stacks = [  ['N','D','M','Q','B','P','Z'],
            ['C' ,'L' ,'Z' ,'Q' ,'M' ,'D' ,'H' ,'V'],
            ['Q' ,'H' ,'R' ,'D' ,'V' ,'F' ,'Z' ,'G'],
            ['H' ,'G' ,'D' ,'F' ,'N'],
            ['N' ,'F' ,'Q'],
            ['D' ,'Q' ,'V' ,'Z' ,'F' ,'B' ,'T'],
            ['Q' ,'M' ,'T' ,'Z' ,'D' ,'V' ,'S' ,'H'],
            ['M' ,'G' ,'F' ,'P' ,'N' ,'Q'],
            ['B' ,'W' ,'R' ,'M']
            ]

stacks2 = [ ['N','D','M','Q','B','P','Z'],
            ['C' ,'L' ,'Z' ,'Q' ,'M' ,'D' ,'H' ,'V'],
            ['Q' ,'H' ,'R' ,'D' ,'V' ,'F' ,'Z' ,'G'],
            ['H' ,'G' ,'D' ,'F' ,'N'],
            ['N' ,'F' ,'Q'],
            ['D' ,'Q' ,'V' ,'Z' ,'F' ,'B' ,'T'],
            ['Q' ,'M' ,'T' ,'Z' ,'D' ,'V' ,'S' ,'H'],
            ['M' ,'G' ,'F' ,'P' ,'N' ,'Q'],
            ['B' ,'W' ,'R' ,'M']
            ]
# Part 1

def part1():
    for line in lines:
        line = [s for s in line.strip().split() if s.isdigit()]
        number = int(line[0])
        src = int(line[1])
        dst = int(line[2])
        for _ in range(number):
            stacks[dst-1].append(stacks[src-1].pop())
    
    ret = []
    for stack in stacks:
        ret.append(stack[-1])
    return ''.join(ret)

# Part 2
def part2():
    for line in lines:
        line = [s for s in line.strip().split() if s.isdigit()]
        number = int(line[0])
        src = int(line[1])
        dst = int(line[2])
        # To retain order, just pop twice using a temporary stack.
        sub_stack = []
        for _ in range(number):
            sub_stack.append(stacks2[src-1].pop())
        for _ in range(number):
            stacks2[dst-1].append(sub_stack.pop())

    ret = []
    for stack in stacks2:
        ret.append(stack[-1])
    return ''.join(ret)

print(part1(), "\n\n", part2())