from tkinter import *
from test_f4 import move_grid

from test_python import init_game



dico_couleur={0:"#c2b3a9",2:"#fcefe6",4:"#f2e8cb",8:"#f5b682",16:"#f29446",32:"#ff775c",64:"e64c2e",128:"ede291",256:"fce130",512:"ffdb4a",1024:"f0b922",2048:"fad74d"}

root = Tk()
root.title('2048')


dessin=Canvas(root, bg="#a39489",height=409, width=409, highlightbackground="#a39489")
dessin.grid(row=0,column=0,columnspan=2, padx=1, pady=1)
dessin.create_polygon((0,0), (0,100), (100,100), (100,0), fill="#c2b3a9")
dessin.create_polygon((103,0), (103,100), (203,100), (203,0), fill="#c2b3a9")
dessin.create_polygon((206,0), (206,100), (306,100), (306,0), fill="#c2b3a9")
dessin.create_polygon((309,0), (309,100), (409,100), (409,0), fill="#c2b3a9")
dessin.create_polygon((0,103), (0,203), (100,203), (100,103), fill="#c2b3a9")
dessin.create_polygon((103,103), (103,203), (203,203), (203,103), fill="#c2b3a9")
dessin.create_polygon((206,103), (206,203), (306,203), (306,103), fill="#c2b3a9")
dessin.create_polygon((309,103), (309,203), (409,203), (409,103), fill="#c2b3a9")
dessin.create_polygon((0,206), (0,306), (100,306), (100,206), fill="#c2b3a9")
dessin.create_polygon((103,206), (103,306), (203,306), (203,206), fill="#c2b3a9")
dessin.create_polygon((206,206), (206,306), (306,306), (306,206), fill="#c2b3a9")
dessin.create_polygon((309,206), (309,306), (409,306), (409,206), fill="#c2b3a9")
dessin.create_polygon((0,309), (0,412), (100,412), (100,309), fill="#c2b3a9")
dessin.create_polygon((103,309), (103,412), (203,412), (203,309), fill="#c2b3a9")
dessin.create_polygon((206,309), (206,412), (306,412), (306,309), fill="#c2b3a9")
dessin.create_polygon((309,309), (309,412), (409,412), (409,309), fill="#c2b3a9")
#dessin.create_text((50,50), fill='white', text=str(grid[0][0]), font=('Helvetica','30','bold'))

grid=init_game(4)

for i in range(4):
        for j in range (4):
            dessin.create_text((50+100*i,50+100*j), fill='white', text=str(grid[i][j]), font=('Helvetica','30','bold'))

def move_left(e):
    global grid
    new_grid=move_grid(grid,'left')
    for i in range(3):
        for j in range (3):
            if new_grid[i][j]!=grid[i][j]:
                dessin.create_polygon((100*i,100*j), (100*i,100+100*j), (100+100*i,100+100*j), (100+100*i,100*j), fill=dico_couleur[new_grid[i][j]],bd=3)
                dessin.create_text((50+100*i,50+100*j), fill='white', text=str(new_grid[i][j]), font=('Helvetica','30','bold'))
 
    dessin.create_polygon((0,0), (0,100), (100,100), (100,0), fill="#fcefe6")
    dessin.create_text((50,50), fill='white', text=str(grid[0][0]), font=('Helvetica','30','bold'))
 

root.bind("<space>", move_left)
#dessin.bind('<KP_Left>',grid=move_grid(grid,'left'))
#Canvas.move(tagOrId, dx, dy)
root.mainloop()