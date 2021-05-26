from random import randint
from mapas import *
from sudoku import *

MAPA = MAPAS[0]
sudoku = crear_juego(MAPA)
def draw_sudoku(sudoku):
    for  i in range(ALTO_TABLERO):
        for j in range(ANCHO_TABLERO):
            print(sudoku[i][j], end = ' ')
        print('\n')

def pedir_variables(): #tiene los if despues de cada variable para que sea mas facil saber que numero estuvo mal
        while True:
            valor = int(input('ingrese el valor a insertar[entre 0 y 9]: '))
            if not valor in range(0,10):
                return False
            fila = int(input('indique en la fila que se va a inserta[entre 0 y 9]: '))
            if not fila in range(0,10):
                return False
            columna = int(input('Indique en la columna que se va a insertar el valor[entre 0 y 9]: '))
            if not columna in range(0,10):
                return False
            return True
        return valor, fila, columna

def main():
    draw_sudoku(sudoku)
    while not esta_terminado(sudoku) == True:
        if hay_movimientos_posibles(sudoku):
            pedir_variables()
        insertar_valor(sudoku, fila, columna, valor):

print(main())





def pedir_variables(): #tiene los if despues de cada variable para que sea mas facil saber que numero estuvo mal
        while True:
            valor = int(input('ingrese el valor a insertar[entre 0 y 9]: '))
            if not valor in range(0,10):
                return False
            fila = int(input('indique en la fila que se va a inserta[entre 0 y 9]: '))
            if not fila in range(0,10):
                return False
            columna = int(input('Indique en la columna que se va a insertar el valor[entre 0 y 9]: '))
            if not columna in range(0,10):
                return False
            return True
        return valor, fila, columna

def main():
    while not esta_terminado(sudoku) == True:
        draw_sudoku(sudoku)
        if hay_movimientos_posibles(sudoku):
            pedir_variables()
        insertar_valor(sudoku, fila, columna, valor)

print(main())






'''
while esta_terminado != True:
    draw_sudoku(sudoku)
pass
'''
'''
while esta_terminado != True:
    draw_sudoku(sudoku)
pass
'''
'''
#hago random y el numero se lo doy a una variable
p = [randint in range (len(MAPAS))]
mapa[p]
crear_juego(mapa[p])
running = True
While running == True:
    draw_sudoku
    pido input fila, columna y valor
    chekear si es movimiento valido
        si lo es insertar valor
        si no borrar valor
    if fila or columna or valor == exit
        break
    sudoku = insertar valor si valor es cero borrar valor

    chequear esta terminado

'''
