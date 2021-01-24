"""
Copyright (C) 2021 Adrian Szarapow - All Rights Reserved
I retain all rights to the source code and no one may reproduce, distribute, or create derivative works from this work.
"""

import pprint
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def import_file():
    global photo
    global image
    filename = filedialog.askopenfilename(title = 'Select nonogram image',filetypes = (('file_type','*.png, *.PNG'),('all files','*.*')))
    image = Image.open(filename)
    size = image.size[0]
    photo = PhotoImage(file=filename)
    multiplier = 15
    photo = photo.zoom(multiplier, multiplier)
    canvas = Canvas(width=size*multiplier, height=size*multiplier)
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.pack()
    return filename

def convert_to_json():
    pix = image.load()
    sizeX = image.size[0]
    sizeY = image.size[1]

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
    global preJSON
    preJSON = chunks(m, sizeY)

def save_to_file():
    OUTPUT_DIR = filedialog.askdirectory()
    f = open(os.path.join(OUTPUT_DIR, 'output.txt'), 'w')
    pprint.pprint(list(preJSON), f)
    f.close()


window = Tk()
window.title('Nonogram JSON Generator')
window.config(background="black")

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Select nonogram image", command=import_file)
button2 = Button(topFrame, text="Convert to JSON", command=convert_to_json)
button3 = Button(bottomFrame, text="Save JSON", command=save_to_file)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=BOTTOM)

window.mainloop()

