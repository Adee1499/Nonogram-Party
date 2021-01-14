from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def import_file():
    global photo
    filename = filedialog.askopenfilename(title = 'Select nonogram image',filetypes = (('file_type','*.png, *.PNG'),('all files','*.*')))
    im = Image.open(filename)
    size = im.size[0]
    photo = PhotoImage(file=filename)
    multiplier = 15
    photo = photo.zoom(multiplier, multiplier)
    canvas = Canvas(width=size*multiplier, height=size*multiplier)
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.pack()

window = Tk()
window.title('Nonogram JSON Generator')
window.config(background="black")

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Select nonogram image", command=import_file)
button2 = Button(topFrame, text="Convert to JSON")
button3 = Button(bottomFrame, text="Save JSON")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=BOTTOM)

window.mainloop()