file1 = open('input.txt', 'r')
lines = file1.readlines()
import math
# Part 1

# We need to track the total amount of squares visited by the tail.
# To track the squares, we should use a dictionary using co-ordinates as keys, set to visited when we pass over.
# This way, whenever we visit a square, we avoid doubling up on squares we have already visited.

def distance(head, tail):
    val = (head[0] - tail[0])**2 + (head[1] - tail[1])**2
    return math.sqrt(abs(val))

def calculate_tail_visits(tail_length):
    visited_squares = {}
    head_pos = [0,0]
    tail_pos = [head_pos.copy() for _ in range(tail_length)]
    visited_squares[tuple(tail_pos[-1])] = True
    for line in lines:
        dir, n = line.split(' ')

        for _ in range(int(n)):     
            # Store current head pos
            temp_head = head_pos.copy()

            # Update head position.
            if dir == 'U':
                head_pos[0] += 1
            if dir == 'D':
                head_pos[0] -= 1
            if dir == 'R':
                head_pos[1] += 1
            if dir == 'L':
                head_pos[1] -= 1

            # Store OLD position of tail in another temp
            temp_tail = tail_pos[0].copy()

            # Update the first tail link if the head is too far away.
            if distance(tail_pos[0], head_pos) > math.sqrt(2):
                tail_pos[0] = temp_head

            # For each subsequent link, update it to the position of the previous link if the distance > sqrt2.
            for i in range(0, len(tail_pos)-1):
                if distance(tail_pos[i], tail_pos[i+1]) > math.sqrt(2):
                    
                    # Store the current position of the next tail link.
                    _temp2 = tail_pos[i+1].copy()

                    # Update the tail (i+1) if the 'head' (i) moves diagonally. 2 cases, head is a knights move away from the tail, head is 2 units directly away from tail.
                    if distance(tail_pos[i], tail_pos[i+1]) == math.sqrt(5) or distance(tail_pos[i], tail_pos[i+1]) == math.sqrt(4):
                        # This logic just ensures if the head moves diagonally, it snaps behind it instead of taking its previous position.
                        if abs(tail_pos[i][0] - tail_pos[i+1][0]) == 2:
                            tail_pos[i+1][0] = int((tail_pos[i][0] + tail_pos[i+1][0])/2)
                            tail_pos[i+1][1] = tail_pos[i][1]
                        else:
                            tail_pos[i+1][1] = int((tail_pos[i][1] + tail_pos[i+1][1])/2)
                            tail_pos[i+1][0] = tail_pos[i][0]

                    # Set the next link to the old position of the previous link.
                    else:
                        tail_pos[i+1] = temp_tail.copy()

                    temp_tail = _temp2.copy()

            # Count the current tail position if it has not been visited, and visit it.
            if tuple(tail_pos[-1]) not in visited_squares:
                visited_squares[tuple(tail_pos[-1])] = True
    return len(visited_squares)

def part1():
    return calculate_tail_visits(1)

# Part 2

# We have 10 links instead of 2.
# The main difference here is that the tail links can move diagonally each step, whereas before the head could only move in cardinal directions.
def part2():
    return calculate_tail_visits(9)

print(part1(), part2())