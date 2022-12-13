file1 = open('input.txt', 'r')
lines = file1.readlines()
import json

flag = None
pairs = []

def parse(pair):
    ret = []
    for packet in pair:
        ret.append(json.loads(packet.strip()))
    return ret

def compare(p, q):
    global flag
    for i in range(max(len(p), len(q))):
        if i >= len(p):
            flag = True
            return flag
        if i >= len(q):
            flag = False
            return flag
        if isinstance(p[i], int) and isinstance(q[i], int):
            if (p[i] > q[i]):
                flag = False
                return flag
            elif (p[i] < q[i]):
                flag = True
                return flag
        elif isinstance(p[i], list) and isinstance(q[i], list):
            compare(p[i], q[i])
        else:
            if isinstance(p[i], int):
                new_p = [p[i]]
                new_q = q[i]
            else:
                new_p = p[i]
                new_q = [q[i]]
            compare(new_p, new_q)
        if flag is not None:
            return flag
    return False

# Part 1
def part1():
    global flag
    current_pair = []
    for line in lines:
        if len(line) == 1:
            continue
        current_pair.append(line.strip())
        if len(current_pair) == 2:
            pairs.append(parse(current_pair))
            current_pair = []
    
    count = 0
    for idx, p in enumerate(pairs):
        flag = None
        count += compare(p[0], p[1]) * (idx + 1)
    return count

# Part 2
def part2():
    global flag

    # Store each original list for sorting.
    all_pairs = []
    for pair in pairs:
        for p in pair:
            all_pairs.append(p)

    # Add the markers.
    all_pairs.append([[2]])
    all_pairs.append([[6]])

    # Sort the array using bubble sort, get the final indexes of the markers.
    is_sorted = False
    marker = [-1, -1]
    while not is_sorted:
        is_sorted = True
        for i in range(len(all_pairs) - 1):
            flag = None
            if not compare(all_pairs[i], all_pairs[i+1]):
                all_pairs[i], all_pairs[i+1] = all_pairs[i+1], all_pairs[i]
                is_sorted = False
            if all_pairs[i] == [[2]]:
                marker[0] = i + 1
            if all_pairs[i] == [[6]]:
                marker[1] = i + 1

    # Get the indexes of the markers in the sorted array.
    return (marker[0] * marker[1])

print(part1(), part2())