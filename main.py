from random import *
from sudoku import crear_juego
from mapas import *
from sudoku import *

MAPA = MAPAS[0]
sudoku = crear_juego(MAPA)
def draw_sudoku(sudoku):
    for  i in range(ALTO_TABLERO):
        for j in range(ANCHO_TABLERO):
            print(sudoku[i][j], end = ' ')
        print('\n')
draw_sudoku(sudoku)


'''
#hago random y el numero se lo doy a una variable
p = [randint in range (len(MAPAS))]
mapa[p]
crear_juego(mapa[p])
running = True
While running == True:
    draw_sudoku
    pido input fila, columna y valor
    if fila or columna or valor == exit
        break
    sudoku = insertar valor si valor es cero borrar valor
    
    chequear esta terminado

'''    

