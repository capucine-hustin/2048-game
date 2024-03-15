from tkinter import *

def graphical_grid_init() :
    root=Tk()
    root.title('2048')
    w = Toplevel(root)
    w.title('2048')
    w.grid(row=0, column=0)

root = Tk()
root.title('2048')

dessin=Canvas(root, bg="#c2b3a9",height=400, width=400, highlightbackground="#a39489")
dessin.grid(row=0,column=0,columnspan=2, padx=1, pady=1)
dessin.create_line(0, 100, 410, 100, fill="#a39489", width=3)
dessin.create_line(0, 200, 410, 200, fill="#a39489", width=3)
dessin.create_line(100, 0, 100, 410, fill="#a39489", width=3)
dessin.create_line(200, 0, 200, 410, fill="#a39489", width=3)
dessin.create_line(300, 0, 300, 410, fill="#a39489", width=3)
dessin.create_line(0, 300, 410, 300, fill="#a39489", width=3)

#Canvas.move(tagOrId, dx, dy)
root.mainloop()