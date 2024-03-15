import random
import numpy as np
import argparse

from game2048.grid_2048 import create_grid
from test_f2 import grid_to_string_with_size, grid_to_string_with_size_and_theme
from test_f4 import move_grid
from test_f5 import is_game_over, move_possible
from test_python import grid_add_new_tile, grid_add_new_tile_at_position, init_game
from textual_2048 import read_player_command

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

#Permet de lancer le jeu de manière aléatoire en effectuant des moves aléatoires
def random_play():
    grid=init_game(4)
    grid_affiche=grid_to_string_with_size(grid,4)
    
    print(grid_affiche)
    while is_game_over(grid)!='jeu terminé':
        #gauche, droite, up, down
        l=['left','right','up','down']
        a=random.randint(0,3)
        if move_possible(grid)[a]:
            grid=move_grid(grid,l[a])
            grid=grid_add_new_tile(grid)
            print(grid_to_string_with_size(grid,4))
    print(grid_to_string_with_size(grid,4))

#Permet de renvoyer la taille choisie par l'utilisateur
def ask_and_read_grid_size():
    sizestring = input("Enter the size chosen :")
    size=int(sizestring)
    return size

#Permet de renvoyer le thème choisi par l'utilisateur
def ask_and_read_grid_theme():
    theme_choisi = input("Enter number of the theme chosen: ")
    return THEMES[str(theme_choisi)]

#Permet convertir les directions en chiffres
def conver(d):
    if d=='g':
        return 0
    if d=='d':
        return 1
    if d=='h':
        return 2
    if d=='b':
        return 3

parser = argparse.ArgumentParser(description="Make a person play")
parser.add_argument('taille_de_la_grille', type=int, help='taille voulue pour la grille')
parser.add_argument('theme_de_la_grille', type=int, help='theme voulue pour la grille')
args = parser.parse_args()

#Cette fonction permet de lancer le jeu
def game_play(taille_de_la_grille,theme_de_la_grille):
    #n = ask_and_read_grid_size()
    #dico = ask_and_read_grid_theme()
    n = taille_de_la_grille
    dic = THEMES[str(theme_de_la_grille)]
    grid=init_game(n)
    print(grid_to_string_with_size_and_theme(grid, dic, n))
    while is_game_over(grid)!='jeu terminé':
        l=['left','right','up','down']
        d=read_player_command()
        a=conver(d)
        if move_possible(grid)[a]:
            grid=move_grid(grid,l[a])
            grid=grid_add_new_tile(grid)
            print(grid_to_string_with_size_and_theme(grid,n))
        

if __name__ == '__main__':
    print (game_play(args.taille_de_la_grille,args.theme_de_la_grille))
    #exit(1)
