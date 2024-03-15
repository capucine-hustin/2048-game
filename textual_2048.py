import random
from test_f2 import grid_to_string_with_size_and_theme

from test_python import init_game

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    if move not in ['g','d','h','b']:
        return input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move

def double():
    x = input("Enter an integer: ")
    return int(x) * 2

def adding():
    x = float(input('Enter the first number'))
    y = float(input('Enter the second number'))
    return x + y

def read_size_grid():
    sizestring = input("Enter the size chosen :")
    size=int(sizestring)
    return init_game(size)

def read_theme_grid():
    theme_choisi = input("Enter number of the theme chosen: ")
    dic=THEMES[theme_choisi]
    grid=read_size_grid()
    n=len(grid)
    return grid_to_string_with_size_and_theme(grid, dic, n)

def move_row_left(ligne):
    l=[]
    for elt in ligne :
        if elt!=0 :
            l.append(elt)
    l+=[0]*(len(ligne)-len(l))


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
