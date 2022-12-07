file1 = open('input.txt', 'r')
lines = file1.readlines()

# Part 1

# Since we are dealing with objects in a heirarchical structure, where we want to be able to traverse between layers, a n-ary tree
# is probably the best approach. We can implement this in an OO style as below.

# Static class variable we will use to store all the nodes for iteration.
node_list = []

class Node(object):
    def __init__(self, parent, name, value):
        self.name = name
        self.value = value
        self.parent = parent
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)
        node_list.append(obj)
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
    def update_value(self, added_value):
        self.value += added_value
        if self.parent:
            self.parent.update_value(added_value)

# Define the root of the tree '/' with an initial of 0. Store each node in a list for iteration later.
root = Node(None, '/', 0)
node_list.append(root)
            
def part1():
    cwd = root
    for line in lines:
        # If line is not a command, we get info about the cwd. We can add children to the cwd node.
        # If we read in a file, we can immediately update the value of the cwd.
        if '$' not in line:
            if 'dir' not in line:
                cwd.update_value(int(line.split(' ')[0].strip()))
                cwd.add_child(Node(cwd, line.split(' ')[1].strip(), line.split(' ')[0].strip()))
            else:
                cwd.add_child(Node(cwd, line.split(' ')[1].strip(), 0))
        elif 'cd' in line:
            if '..' in line:
                # Store the parent of each node to facilitate bi-directional traversal.
                cwd = cwd.parent
            elif '/' in line:
                cwd = root
            else:
                cwd = cwd.get_child(line.split(' ')[2].strip())
    
    # Iterate the node list and sum all the directories with value less than or equal to 100,000
    node_sum = 0
    for n in node_list:
        if int(n.value) <= 100000 and len(n.children)> 0:
            node_sum += int(n.value)
    return node_sum

# Part 2
def part2():
    # We need to find the directory with the smallest size.
    required_space = root.value - 40000000
    candidates = []
    for n in node_list:
        if len(n.children)> 0 and n.value >= required_space:
            candidates.append(n)
    
    min_node = candidates[0]
    for n in candidates:
        if (n.value < min_node.value):
            min_node = n
    return min_node.name, min_node.value

print("Part 1:", part1() , "\nPart 2: ",part2())