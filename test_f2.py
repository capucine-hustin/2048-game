from test_python import grid_add_new_tile_at_position, grid_get_value, get_all_tiles


def grid_to_string(table,n):
    string=''
    for i in range(n) :
        string+=' ==='*n
        string+='\n'
        for j in range(n) :
            string+='| '
            string+=str(table[i][j])
            string+=' '
        string+='|\n'
    string+=' ==='*n
    print(string)
    return string 

def long_value(table):
    value=get_all_tiles(table)
    m=max(value)
    a=str(m)
    return len(a)

def grid_to_string_with_size(grid,n):
    
    string=''
    for i in range(n) :
        a=long_value(grid)
        string+=(' =='+'='*a)*n
        string+='\n'
        for j in range(n) :
            string+='| '
            taille=len(str(grid[i][j]))
            string+=str(grid[i][j])
            string+=' '*(a-taille)
            
            string+=' '
        string+='|\n'
    string+=(' =='+'='*a)*n
    return string

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def long_value_with_theme(grid,dic):
    l= get_all_tiles(grid)
    M=[]
    for elt in l :
        M+=[len(dic[elt])]
    return max(M)

def test_long_value_with_theme():
    grid =[[2048, 16, 32, 0], [0, 4, 0, 2], [0, 0, 0, 32], [512, 1024, 0, 2]]
    assert long_value_with_theme(grid,THEMES["0"]) == 4
    assert long_value_with_theme(grid,THEMES["1"]) == 2
    assert long_value_with_theme(grid,THEMES["2"]) == 1
    grid = [[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 4096], [1024, 2048, 512, 2]]
    assert long_value_with_theme(grid,THEMES["0"]) == 4
    assert long_value_with_theme(grid,THEMES["1"]) == 2
    assert long_value_with_theme(grid,THEMES["2"]) == 1

def grid_to_string_with_size_and_theme(grid, dic, n):
        
    string=''
    for i in range(n) :
        a=long_value_with_theme(grid, dic)
        string+=('='+'='*a)*n
        string+='=\n'
        for j in range(n) :
            string+='|'
            taille=len(dic[grid[i][j]])
            string+=dic[grid[i][j]]
            string+=' '*(a-taille)
        
        string+='|\n'
    string+=('='+'='*a)*n
    string+='='
    print(string)
    return string


def test_grid_to_string_with_size_and_theme():
    grid=[[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]
    a="""
=============
|Be|He|Li|H |
=============
|H |He|H |N |
=============
|He|F |B |C |
=============
|Ne|Na|F |H |
=============
"""
    assert grid_to_string_with_size_and_theme(grid,THEMES["1"],4)== a[1:-1]

