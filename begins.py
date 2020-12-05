# Have a window with three buttons that open more windows.
# Fibonacci that gets printed in a separate file or form - figure that out.
            # Generate the sequence in a notepad file that opens immediately after it is made.
            # Or have an expandable space that shows the sequence.
# Factorial that gets the factorial of a number
# Prime numbers before a certain number
# A fake data generator using numpy, pandas and matplotlib - it has limits as well.
# 

import tkinter as tk
import tkinter.font as font
import sys, os
from PIL import ImageTk, Image
path = sys.path[0]
# Or from tkinter import Tk

# Window with title bar
root = tk.Tk()

# root is the parent window
w = tk.Label(root, text = "Hello Tkinter!") 
# This packs the root window around the Label
w.pack() 

# Adding images to Label
"""
image = Image.open(path + '\\' + "dragon_1.gif")
image = image.resize((100,150))#, Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = tk.Label(image=my_img)
my_img.pack()
"""
logo = tk.PhotoImage(file = path + '\\' + 'sample_1.ppm')
logo.zoom(1,2)
w1 = tk.Label(root, image = logo).pack(side="right")

# Image Details
detail = """
This
is
the
left
label
"""

detail_2 = """
This
is
the
right
label
"""

# This font can be can be used for other 
myFont = font.Font(family = "Sans-Serif", size=21, weight='bold') # way 1
myFont = ("Sans-serif", 15, "bold") # way 2

# Label | Justify aligns the text to the left | pad does padding up or down
# Pack | pack puts the widget either left or right
w2 = tk.Label(root, justify = tk.LEFT, padx = 10, pady=10, text = detail, font = myFont, bg = 'dark grey', fg = 'light grey').pack(side="left")
w3 = tk.Label(root, justify = tk.RIGHT, padx = 10, pady=10, text = detail, font = myFont, bg = 'dark grey', fg = 'light grey').pack(side='right')

# Another image.
logo_1 = tk.PhotoImage(file = path + '\\' + 'example.png')
# logo_1.zoom(1,2)
# Compound option will print text as well | Left or right will have them both (photo and label)
w4 = tk.Label(root, compound = tk.CENTER, image = logo_1, text = "Boxes of color", font = ('bold','20'), fg = "white").pack(side="left")


# This is the event loop and this keeps going on till we press X
root.mainloop()



"""

anchor=

expand=

fill=
in=

ipadx=

ipady=

padx=

pady=

side="""


