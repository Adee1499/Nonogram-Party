from PIL import Image
import pprint
import json
from tkinter import *

im = Image.open('kid.png')
pix = im.load()
sizeX = im.size[0]
sizeY = im.size[1]

m = []

for y in range(sizeX):
    for x in range(sizeY):
        if 0 in pix[x, y]:
            m.append(1)
        else:
            m.append(0)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

pprint.pprint(list(chunks(m, sizeY)))

preJSON = chunks(m, sizeY)

textfile = open('kid.json', 'w')

pprint.pprint(list(preJSON), textfile)
