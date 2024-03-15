from test_f2 import long_value
from test_f4 import move_grid

#On vérifie ici si la grille est pleine ou pas 
def is_grid_full(grid) :
    for ligne in grid :
        if 0 in ligne :
            return False
    return True

def test_is_full():
    assert is_grid_full([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]])==False
    assert is_grid_full([[2,4,4,2], [4, 4, 2, 2], [8, 2, 8, 2], [2, 2, 2, 2]])==True

#On vérifie ici dans quelle direction les mouvements sont-ils possibles.
def move_possible(grid):
    l=[]
    if move_grid(grid,'left')==grid:
        l+=[False]
    else :
        l+=[True]
    if move_grid(grid,'right')==grid:
        l+=[False]
    else : 
        l+=[True]
    if move_grid(grid,'up')==grid:
        l+=[False]
    else :
        l+=[True]
    if move_grid(grid,'down')==grid:
        l+=[False]
    else :
        l+=[True]
    return l

def test_move_possible():
    assert move_possible([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]) == [True,True,True,True]
    assert move_possible([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]) == [False,False,False,False]

#On vérifie ici si la partie et oui ou non terminée i.e qu'on soit dans une configuration ou aucun mouvement n'est possible
def is_game_over(grid):
    if move_possible(grid)==[False,False,False,False]:
        return 'jeu terminé'
    return 'le jeu peut continuer'

def test_is_game_over():
    assert is_game_over([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]) =='jeu terminé'

#On obtient grâce à cette fonction la valeur maximale parmi celles présentes dans la grille 
def get_grid_tile_max(grid):
    M=[]
    for ligne in grid :
        M.append(max(ligne))
    return max(M)

def test_get_grid_tile_max():
    assert get_grid_tile_max([[2, 4, 8, 16], [16, 8, 4, 2], [2048, 4, 8, 16], [16, 8, 4, 2]])==2048

#On vérifie ici si la grille obtenue et oui ou non gagnante.
def gagnant(grid):
    if get_grid_tile_max(grid)>=2048:
        return 'Félicitation'
    return 'Défaite'