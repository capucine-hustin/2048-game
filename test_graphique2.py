from tkinter import *
from test_f4 import move_grid
from test_f5 import move_possible

from test_python import grid_add_new_tile, init_game


dic_direction={'left':0, 'right': 1, 'up':2, 'down':3}

dico_couleur={0:"#c2b3a9",2:"#fcefe6",4:"#f2e8cb",8:"#f5b682",16:"#f29446",32:"#ff775c",64:"#e64c2e",128:"#ede291",256:"#fce130",512:"#ffdb4a",1024:"#f0b922",2048:"#fad74d"}
dico_text={0:' ',2:'2',4:'4',8:'8',16:'16',32:'32',64:'64',128:'128',256:'256',512:'512',1024:'1024',2048:'2028'}

root = Tk()
root.title('2048')

dessin=Canvas(root, bg="#a39489",height=400, width=400, highlightbackground="#a39489")
dessin.grid(row=0,column=0,columnspan=2, padx=1, pady=1)

#dessin.create_text((50,50), fill='white', text=str(grid[0][0]), font=('Helvetica','30','bold'))

grid=init_game(4)

for i in range(4):
        for j in range (4):
            dessin.create_polygon((100*i,100*j), (100*i,100+100*j), (100+100*i,100+100*j), (100+100*i,100*j), fill=dico_couleur[grid[i][j]],outline="#a39489")
            dessin.create_text((50+100*i,50+100*j), fill='white', text=dico_text[grid[i][j]], font=('Helvetica','30','bold'))

def move_up(e):
    global grid
    if move_possible(grid)[dic_direction['left']] :
        new_grid1=move_grid(grid,'left')
        new_grid=grid_add_new_tile(new_grid1)
        #c'est inversé jsp pourquoi
        for i in range(4):
            for j in range (4):
                if new_grid[i][j]!=grid[i][j]:
                    dessin.create_polygon((100*i,100*j), (100*i,100+100*j), (100+100*i,100+100*j), (100+100*i,100*j), fill=dico_couleur[new_grid[i][j]],outline="#a39489")
                    dessin.create_text((50+100*i,50+100*j), fill='white', text=dico_text[new_grid[i][j]], font=('Helvetica','30','bold'))
        grid=new_grid

def move_down(e):
    global grid
    if move_possible(grid)[dic_direction['right']] :
        new_grid1=move_grid(grid,'right')
        new_grid=grid_add_new_tile(new_grid1)
        #c'est inversé jsp pourquoi
        for i in range(4):
            for j in range (4):
                if new_grid[i][j]!=grid[i][j]:
                    dessin.create_polygon((100*i,100*j), (100*i,100+100*j), (100+100*i,100+100*j), (100+100*i,100*j), fill=dico_couleur[new_grid[i][j]],outline="#a39489")
                    dessin.create_text((50+100*i,50+100*j), fill='white', text=dico_text[new_grid[i][j]], font=('Helvetica','30','bold'))
        grid=new_grid

def move_left(e):
    global grid
    if move_possible(grid)[dic_direction['up']] :
        new_grid1=move_grid(grid,'up')
        new_grid=grid_add_new_tile(new_grid1)
        #c'est inversé jsp pourquoi
        for i in range(4):
            for j in range (4):
                if new_grid[i][j]!=grid[i][j]:
                    dessin.create_polygon((100*i,100*j), (100*i,100+100*j), (100+100*i,100+100*j), (100+100*i,100*j), fill=dico_couleur[new_grid[i][j]],outline="#a39489")
                    dessin.create_text((50+100*i,50+100*j), fill='white', text=dico_text[new_grid[i][j]], font=('Helvetica','30','bold'))
        grid=new_grid

def move_right(e):
    global grid
    if move_possible(grid)[dic_direction['down']] :
        new_grid1=move_grid(grid,'down')
        new_grid=grid_add_new_tile(new_grid1)
        #c'est inversé jsp pourquoi
        for i in range(4):
            for j in range (4):
                if new_grid[i][j]!=grid[i][j]:
                    dessin.create_polygon((100*i,100*j), (100*i,100+100*j), (100+100*i,100+100*j), (100+100*i,100*j), fill=dico_couleur[new_grid[i][j]],outline="#a39489")
                    dessin.create_text((50+100*i,50+100*j), fill='white', text=dico_text[new_grid[i][j]], font=('Helvetica','30','bold'))
        grid=new_grid


root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
#dessin.bind('<KP_Left>',grid=move_grid(grid,'left'))
#Canvas.move(tagOrId, dx, dy)
root.mainloop()