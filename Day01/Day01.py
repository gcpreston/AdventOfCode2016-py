import math

with open("Day01_Input.txt") as file:
    directions = file.read().split(", ")

# The direction being faced, 0 = North, 1 = East, 2 = South, 3 = West
facing = 0
moves = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
coordinates = [0, 0]
locations = [[0, 0]]
for d in directions:
    if d[0] == "R":
        if facing == 3:
            facing = 0
        else:
            facing += 1
    else:
        if facing == 0:
            facing = 3
        else:
            facing -= 1
            
    for n in range(int(d[1:])):
        coordinates = [x + y for x, y in zip(coordinates, moves[facing])]
        
print(coordinates)
print(int(math.fabs(coordinates[0] + coordinates[1])), "blocks away.")