file1 = open('input.txt', 'r')
lines = file1.readlines()

class Monkey():
    def __init__(self, num):
        self.num = num
        self.starting_items = []
        self.operation = []
        self.test = []
        self.throws = []
        self.count = 0

def parse_monkeys():
    monkeys = []
    lcm = 1
    line_count = 0
    current_monkey = None
    worry = 0
    for line in lines:
        if 'Monkey' in line:
            line_count = 0
            num = line.split(' ')[1].split(':')[0]
            current_monkey = Monkey(num)
            monkeys.append(current_monkey)
        if line_count == 1:
            current_monkey.starting_items = [int(s) for s in line.replace(',', '').split() if s.isdigit()]
        if line_count == 2:
            current_monkey.operation = line.split()[-2:]
        if line_count == 3:
            current_monkey.test = [int(s) for s in line.replace(',', '').split() if s.isdigit()][0]
            lcm *= current_monkey.test
        if line_count == 4 or line_count == 5:
            current_monkey.throws.append([int(s) for s in line.replace(',', '').split() if s.isdigit()][0])
        line_count += 1
    return monkeys, lcm

def play_round(monkeys, n):
    for _ in range(n):
        for monkey in monkeys:
            for item in monkey.starting_items:
                item = calculate_worry(monkey.operation.copy(), item) // 3
                monkey.count += 1
                if (item % int(monkey.test) == 0):
                    get_monkey(int(monkey.throws[0]), monkeys).starting_items.append(item)
                else:
                    get_monkey(int(monkey.throws[1]), monkeys).starting_items.append(item)
            monkey.starting_items = []

def play_round2(monkeys, n, lcm):
    for _ in range(n):
        for monkey in monkeys:
            for item in monkey.starting_items:
                item = calculate_worry(monkey.operation.copy(), item) % lcm
                monkey.count += 1
                if (item % int(monkey.test) == 0):
                    get_monkey(int(monkey.throws[0]), monkeys).starting_items.append(item)
                else:
                    get_monkey(int(monkey.throws[1]), monkeys).starting_items.append(item)
            monkey.starting_items = []

def calculate_worry(op, item):
    current_worry = item
    if op[1] == 'old':
        op[1] = item
    if op[0] == '*':
        current_worry = int(item) * int(op[1])
    else:
        current_worry = int(item) + int(op[1])
    return current_worry

def get_monkey(n, monkeys):
    for monkey in monkeys:
        if int(monkey.num) == n:
            return monkey

def part1():
    monkeys, _ = parse_monkeys()
    play_round(monkeys, 20)
    counts = []
    for m in monkeys:
        counts.append(m.count)
    counts.sort()
    return counts[-1] * counts[-2]

def part2():
    monkeys, lcm = parse_monkeys()
    play_round2(monkeys, 10000, lcm)
    counts = []
    for m in monkeys:
        counts.append(m.count)
    counts.sort()
    return counts[-1] * counts[-2]

print(part1(), part2())