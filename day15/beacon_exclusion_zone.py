
# Part 1

def part1(t):
    sensors, beacons, positions = [], [], []

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.replace(':',' ').replace(',',' ').replace('=',' ').split()
        sensors.append([int(x) for x in line if x.isdigit() or x[1:].isdigit()][:2])
        beacons.append([int(x) for x in line if x.isdigit() or x[1:].isdigit()][2:])

    target, count = t, 0
    counted = set()

    for s, b in zip(sensors, beacons):
        if b[1] == target and b[0] not in counted:
            counted.add(b[0])
            count += 1
        for p in calc(s, b, target, False):
            positions.append(p)

    return len(set(positions)) - count

def calc(s, b, target, bounded):
    # Calculates the x coordinates of every grid point hit by the sensor in the target row.
    distance = (abs(s[0] - b[0]) + abs(s[1] - b[1]))
    
    # March to the target row. The remainder is how far we can stretch in both directions.
    # Positive if the target is below, Negative if the target is above.
    march_len = target - s[1]

    # If the sensor cannot reach the target row, there are no intersections.
    if (abs(march_len) > distance):
        return []
    
    elif (distance == abs(march_len)):
            return [s[0], s[0]]
    
    else:
        # The sensor reaches the target row and spreads out.
        steps = distance - abs(march_len)
        ret = []
        if not bounded:
            for i in range(steps + 1):
                ret.append(s[0] + i)
                ret.append(s[0] - i)
            return ret
        else:
            # If we are bounded in part 2, instead of constructing an array, just return a range so we can check the boundary.
            return [max(s[0] - steps, 0), min(s[0] + steps, 4000000)]

def overlap(section1, section2):
    if int(section1[0]) < int(section2[0]):
        if int(section1[-1]) >= int(section2[0]):
            return True
    elif int(section1[0]) > int(section2[0]):
        if int(section2[-1]) >= int(section1[0]):
            return True
    else:
        return True
    return False

def contains(section1, section2):
    sizes = [int(section1[-1]) - int(section1[0]) + 1, int(section2[-1]) - int(section2[0]) + 1]
    if sizes[0] == sizes[1]:
        return False
    if section1[0] <= section2[0]:
        if section1[-1] >= section2[-1]:
            return True
    else:
        if section2[-1] >= section1[-1]:
            return True
    return False

# Part 2
def part2(t):
    sensors, beacons = [], []

    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.replace(':',' ').replace(',',' ').replace('=',' ').split()
        sensors.append([int(x) for x in line if x.isdigit() or x[1:].isdigit()][:2])
        beacons.append([int(x) for x in line if x.isdigit() or x[1:].isdigit()][2:])

    for target in range(0, t):
        ranges = []

        # Calculate the coverage for each row by considering the range in the row each sensor occupies.
        for s, b in zip(sensors, beacons):
            ret = calc(s, b, target, True)
            ranges.append(ret) if ret and ret not in ranges else None
            if (s[1] == target):
                ranges.append([s[1], s[1]]) if [s[1], s[1]] not in ranges else None
    
        # Sort the ranges by starting x-coordinate, makes it easier to compare to find any lack in overlap.
        ranges.sort()

        # If the very first range starts at 1, then the position is at x = 0.
        if (ranges[0][0] > 0):
            return [target, ranges[0][0]]

        # We now need to iterate over the ranges and try to find a gap in the domain. If there is a gap, return the index of the gap, target.
        for i in range(len(ranges) - 1):

            # If the next range is contained in the current range, we want to use the current range for the next comparison.
            if contains(ranges[i], ranges[i+1]):
                ranges[i], ranges[i+1] = ranges[i+1], ranges[i]
                continue

            # If there is not an overlap between adjacent ranges, return the position outside the first range in the comparison.
            if not overlap(ranges[i], ranges[i+1]):
                return target + (ranges[i][1] + 1) * 4000000

        # If the last range ends before 4000000, then the position is at x = 4000000
        if (ranges[-1][1] < t):
            return target + ranges[-1][1] * 4000000
    return -1

# print(part1(10), part2(20))
print(part1(2000000), part2(4000000))