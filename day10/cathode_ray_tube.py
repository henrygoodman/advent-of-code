file1 = open('input.txt', 'r')
lines = file1.readlines()

# Part 1

def check_status(status):
    if (status[1] - 20) % 40 == 0:
        print(status)
        return status[0] * status[1]
    return 0

def part1():
    status = [1,0]
    s = 0
    for line in lines:
        if 'noop' in line:
            status[1] += 1
            s += check_status(status)
        else:
            status[1] += 1
            s += check_status(status)
            status[1] += 1
            status[0] += int(line.split(' ')[1])
            s += check_status(status)
        if status[1] >= 220:
            return s
    return s

def check_status2(status):
    if (status[1] % 40 == 0):
        print('')
    if (status[0] == status[1] % 40 or status[0] - 1 == status[1] % 40 or status[0] + 1 == status[1] % 40):
        print("█", end='')
    else:
        print(" ", end='')

# Part 2
def part2():
    status = [1,0]
    check_status2(status)   
    for line in lines:
        if 'noop' in line:
            status[1] += 1
            check_status2(status)
        else:
            status[1] += 1
            check_status2(status)
            status[1] += 1
            status[0] += int(line.split(' ')[1])
            check_status2(status)
    return

print(part1(), part2())