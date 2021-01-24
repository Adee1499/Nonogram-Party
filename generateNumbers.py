import json;
import pprint;

json_grid = open('1.json')

grid = json.load(json_grid)

#pprint.pprint(grid)

#print(grid)

#print(grid[0])

height = len(grid)
width = len(grid[0])

print("This nonogram is " + str(height) + "X" + str(width))

a = []

for row in grid:
    temp = 0
    print(a)
    for element in row:
        if element == 1:
            temp += 1
        elif element == 0:
            if temp != 0:
                a.append(temp)
            temp = 0
    if temp != 0:
        a.append(temp)

print(a)