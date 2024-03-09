import tkinter as tk
from tkinter import ttk

root = tk.Tk()


# add logic here
def pressButton():
    quit()


# add widgets here
button = ttk.Button(root, text="Click me", command=pressButton)
button.pack()


# main loop at end
root.mainloop()
