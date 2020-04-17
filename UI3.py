from tkinter import *
from tkinter import ttk
root=Tk()
root.title("可变大小框")
ttk.Sizegrip(root).grid(row=99,column=99,sticky="se")
root.columnconfigure(0,weight=1,minsize=99)
root.rowconfigure(0,weight=1,minsize=99)
root.mainloop()