import numpy as np 
#On réalise ici une fonction pour décaler tous les zéros à droite
def decalegauche(ligne):
    l=[]
    for elt in ligne :
        if elt!=0 :
            l.append(elt)
    l+=[0]*(len(ligne)-len(l))
    return l

#Cette fonction quant-à-elle définit le mouvement à gauche en 2048
def move_row_left(ligne):
    l=decalegauche(ligne)
    for i in range (len(l)-1):
        if l[i]==l[i+1]:
            l[i]=l[i]*2
            l[i+1]=0

    return decalegauche(l)

def test_move_row_left():
    
    assert move_row_left([0, 0, 0, 2]) == [2, 0, 0, 0]
    assert move_row_left([0, 2, 0, 4]) == [2, 4, 0, 0]
    assert move_row_left([2, 2, 0, 4]) == [4, 4, 0, 0]
    assert move_row_left([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert move_row_left([4, 2, 0, 2]) == [4, 4, 0, 0]
    assert move_row_left([2, 0, 0, 2]) == [4, 0, 0, 0]
    assert move_row_left([2, 4, 2, 2]) == [2, 4, 4, 0]
    assert move_row_left([2, 4, 4, 0]) == [2, 8, 0, 0]
    assert move_row_left([4, 8, 16, 32]) == [4, 8, 16, 32]

#On réalise ici une fonction pour décaler tous les zéros à gauche
def decaledroite(ligne):
    l=[]
    for elt in ligne :
        if elt!=0 :
            l.append(elt)
    l=[0]*(len(ligne)-len(l))+l
    return l

#Cette fonction quant-à-elle définit le mouvement à droite en 2048
def move_row_right(ligne):
    l=decaledroite(ligne)
    for i in range (1,len(l)):
        if l[-i]==l[-i-1]:
            l[-i]=l[-i]*2
            l[-i-1]=0
    return decaledroite(l)

def test_move_row_right():
    
    assert move_row_right([2, 0, 0, 0]) == [0, 0, 0, 2]
    assert move_row_right([0, 2, 0, 4]) == [0, 0, 2, 4]
    assert move_row_right([2, 2, 0, 4]) == [0, 0, 4, 4]
    assert move_row_right([2, 2, 2, 2]) == [0, 0, 4, 4]
    assert move_row_right([4, 2, 0, 2]) == [0, 0, 4, 4]
    assert move_row_right([2, 0, 0, 2]) == [0, 0, 0, 4]
    assert move_row_right([2, 4, 2, 2]) == [0, 2, 4, 4]
    assert move_row_right([2, 4, 4, 0]) == [0, 0, 2, 8]
    assert move_row_right([4, 8, 16, 32]) == [4, 8, 16, 32]

#A l'aide des fonctions précédentes, on définit le mouvement d'une grille dans l'une des quatre directions élémentaires connues
def move_grid(grid,d):
    grid_apres=[]
    if d=='left':
        for ligne in grid :
            grid_apres.append(move_row_left(ligne))
        return grid_apres
    elif d=='right':
        for ligne in grid :
            grid_apres.append(move_row_right(ligne))
        return grid_apres
    else :
        grid_nouv=np.transpose(grid)
        if d=='up':
            for ligne in grid_nouv :
                grid_apres.append(move_row_left(ligne))
        if d=='down':
            for ligne in grid_nouv :
                grid_apres.append(move_row_right(ligne))
        return np.transpose(grid_apres).tolist()


def test_move_grid():
    assert move_grid([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]],"left") == [[4,0,0,0], [8, 0, 0, 0], [16, 0, 0, 0], [4, 0, 0, 0]]
    assert move_grid([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]],"right") == [[0,0,0,4], [0, 0, 0, 8], [0, 0, 0, 16], [0, 0, 0, 4]]
    assert move_grid([[2,0,0,2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]],"up") == [[4,8,4,2], [16, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert move_grid([[2,0,0,2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]],"down") == [[0, 0, 0, 0], [0, 0, 0, 0],[4,8,0,0],[16, 2, 4, 2]]
