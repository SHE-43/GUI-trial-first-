import tkinter as tk

root = tk.Tk()

tk.Label(root,
            text = "Red text in times font",
            fg = 'red',
            font = 'Times'
).pack()

tk.Label(root,
            text = "Green text in Helvetica font",
            fg = 'light green',
            bg = 'dark green',
            font = 'Helvetica 16 bold italic'
).pack()

tk.Label(root,
            text = "Blue text in Verdana bold",
            fg = 'blue',
            font = 'Verdana 10 bold'
).pack()


root.mainloop()