import pytest
import random
import coverage 
from game2048.grid_2048 import create_grid
from pytest import *


def test_create_grid():
    assert create_grid(4) == [[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]

def get_value_new_tile():
    a=random.randint(1,10)
    if a<=9 :
        return 2
    return 4

def grid_add_new_tile_at_position(table,x,y):
    table[x][y]=get_value_new_tile()
    return table

def get_all_tiles(table):
    ls_tiles=[]
    for ligne in table:
        for elt in ligne :
            if elt==' ':
                ls_tiles.append(0)
            else :
                ls_tiles.append(elt)
    return ls_tiles

def test_grid_add_new_tile_at_position():
    game_grid=create_grid(4)
    game_grid=grid_add_new_tile_at_position(game_grid,1,1)
    tiles = get_all_tiles(game_grid)
    assert 2 in tiles or 4 in tiles

def test_get_value_new_tile():
    assert get_value_new_tile() in {2, 4}

def test_get_all_tiles():
    assert get_all_tiles( [[' ',4,8,2], [' ',' ',' ',' '], [' ',512,32,64], [1024,2048,512, ' ']]) == [0,4,8,2,0,0,0,0,0,512,32,64, 1024,2048,512,0]
    assert get_all_tiles([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]]) == [16, 4, 8, 2, 2, 4, 2, 128, 4, 512, 32, 64, 1024, 2048, 512, 2]

def get_empty_tiles_positions(table):
    l=[]
    print(table)
    for i in range (len(table)):
        for j in range (len(table[i])):
            if table[i][j]==0 or table[i][j]==' ':
                l.append((i,j))
    return l 

def test_get_empty_tiles_positions():
    assert get_empty_tiles_positions([[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]])==[(0,0),(0,3),(1,1),(3,3)]
    assert get_empty_tiles_positions([[' ', 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]])==[(0,0),(0,3),(1,1),(3,3)]
    assert get_empty_tiles_positions(create_grid(2))==[(0,0),(0,1),(1,0),(1,1)]
    assert get_empty_tiles_positions([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]])==[]

def get_new_position(table):
    a=random.randint(0,len(get_empty_tiles_positions(table))-1)
    return get_empty_tiles_positions(table)[a]

def grid_get_value(table,x,y):
    return table[x][y]

def test_get_new_position():
    grid = [[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]]
    x,y=get_new_position(grid)
    assert(grid_get_value(grid,x,y)) == 0
    grid = [[' ',4,8,2], [' ',' ',' ',' '], [' ',512,32,64], [1024,2048,512, ' ']]
    x,y=get_new_position(grid)
    assert(grid_get_value(grid,x,y) == 0 or grid_get_value(grid,x,y)==' ')

def grid_add_new_tile(table) :
    x,y=get_new_position(table)
    table[x][y]=get_value_new_tile()
    return table


def test_grid_add_new_tile():
    game_grid=create_grid(4)
    game_grid=grid_add_new_tile(game_grid)
    tiles = get_all_tiles(game_grid)
    assert 2 in tiles or 4 in tiles

def init_game(n):
    grid=create_grid(n)
    x,y=random.randint(0,n-1),random.randint(0,n-1)
    grid=grid_add_new_tile_at_position(grid,x,y)
    return grid_add_new_tile(grid)


def test_init_game():
    grid = init_game(4)
    tiles = get_all_tiles(grid)
    assert 2 in tiles or 4 in tiles
    assert len(get_empty_tiles_positions(grid)) == 14





