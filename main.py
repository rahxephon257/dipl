from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

editor = Text(wrap="none")
editor.grid(column=0, row=0, sticky=NSEW)

ys = ttk.Scrollbar(orient="vertical", command=editor.yview)
ys.grid(column=1, row=0, sticky=NS)
xs = ttk.Scrollbar(orient="horizontal", command=editor.xview)
xs.grid(column=0, row=1, sticky=EW)

editor["yscrollcommand"] = ys.set
editor["xscrollcommand"] = xs.set

root.mainloop()