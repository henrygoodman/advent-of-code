file1 = open('input.txt', 'r')
lines = file1.readlines()

calorie_sum = 0
max_list = [0,0,0]

# This solution tracks the top 3 in order, could be optimized by not caring about order (as we only care about the sum).
# This could be achieved by replacing the min in the array if the sum is greater than min.

for line in lines:
    if (len(line) == 1):
        # If we get a new max, we need to shift down the existing top 3.
        if (calorie_sum >= max_list[0]):
            max_list[2] = max_list[1]
            max_list[1] = max_list[0]
            max_list[0] = calorie_sum
        # If we do not get a new max, check if it larger than the 2nd largest.
        elif (calorie_sum >= max_list[1]):
            max_list[2] = max_list[1]
            max_list[1] = calorie_sum
        # If not larger than 2nd largest, check if larger than 3rd largest.
        elif (calorie_sum >= max_list[2]):
            max_list[2] = calorie_sum

        calorie_sum = 0
    else:
        calorie_sum += int(line)

print("Calories for top 3 elf: " + str(sum(max_list)))