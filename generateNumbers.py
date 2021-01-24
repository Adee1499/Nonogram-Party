"""
Copyright (C) 2021 Adrian Szarapow - All Rights Reserved
I retain all rights to the source code and no one may reproduce, distribute, or create derivative works from this work.
"""

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

horizontal = [[] for j in range(height)]
vertical = [[] for j in range(width)]

def generate(a, input):
    rowindex = -1
    for row in input:
        rowindex += 1
        temp = 0
        for element in row:
            if element == 1:
                temp += 1
            elif element == 0:
                if temp != 0:
                    a[rowindex].append(temp)
                temp = 0
        if temp != 0:
            a[rowindex].append(temp)
    return a

rotatedGrid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0])-1,-1,-1)]

pprint.pprint(generate(horizontal, grid))
pprint.pprint(generate(vertical, rotatedGrid))