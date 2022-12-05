file1 = open('input.txt', 'r')
lines = file1.readlines()

# Part 1

def contains(section1, section2):
    sizes = [int(section1[1]) - int(section1[0]) + 1, int(section2[1]) - int(section2[0]) + 1]
    if sizes[0] == sizes[1]:
        return False
    if section1[0] <= section2[0]:
        if section1[1] >= section2[1]:
            return True
    else:
        if section2[1] >= section1[1]:
            return True
    return False


def part1():
    count = 0
    for line in lines:
        sections = line.strip().split(',')
        section1 = sections[0].split('-')
        section2 = sections[1].split('-')
        if contains(section1, section2):
            count += 1
    return count

# Part 2

def overlap(section1, section2):
    if int(section1[0]) < int(section2[0]):
        if int(section1[1]) >= int(section2[0]):
            return True
    elif int(section1[0]) > int(section2[0]):
        if int(section2[1]) >= int(section1[0]):
            return True
    else:
        return True
    return False

def part2():
    count = 0
    for line in lines:
        sections = line.strip().split(',')
        section1 = sections[0].split('-')
        section2 = sections[1].split('-')
        if overlap(section1, section2):
            count += 1
    return count

print(part1(), part2())