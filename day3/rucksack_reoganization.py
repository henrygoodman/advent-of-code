file1 = open('input.txt', 'r')
lines = file1.readlines()

# Part 1

def part1():
    priority_sum = 0
    for line in lines:
        line = line.strip()
        compartments = line[ : int(len(line)/2)], line[int(len(line)/2) :]
        common = [c for c in set(compartments[0]) if c in compartments[1]]
        priority_sum += ord(common[0]) - 38 if str(common).isupper() else ord(common[0]) - 96
    return priority_sum

# Part 2

def get_item(group):
    common = [c for c in set(group[0]) if c in group[1] and c in group[2]]
    priority = ord(common[0]) - 38 if str(common).isupper() else ord(common[0]) - 96
    return priority

def part2():
    group = []
    priority_sum = 0
    for idx, line in enumerate(lines):
        group.append(line.strip())
        if ((idx + 1) % 3 == 0):
            priority_sum += get_item(group)
            group = []

    return priority_sum

print(part1(), part2())