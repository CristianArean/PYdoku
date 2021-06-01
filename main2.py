from random import randint
from mapas import *
from sudoku import *
MAPA = MAPAS[randint(0, 49)]
sudoku = crear_juego(MAPA)
def draw_sudoku(sudoku):
    print('A', '      B', '      C', '      D', '      E', '      F', '      G', '      H', '      I', '    FILA')
    for  i in range(ALTO_TABLERO):
        for j in range(ANCHO_TABLERO):
            print(sudoku[i][j], end='\t')
        print(i+1)
        print('', end = '\n')

def agregar_variables(): #tiene los if despues de cada variable para que sea mas facil saber que numero estuvo mal
    valor = int(input('ingrese el valor a insertar[entre 0 y 9]: '))
    if not valor in range(0,10):
        return False
    fila = int(input('indique en la fila que se va a inserta[entre 0 y 8]: '))
    if not fila in range(1,11):
        return False
    if fila == 1:
         fila = 0
    if fila == 2:
         fila = 1
    if fila == 3:
         fila = 2
    if fila == 4:
         fila = 3
    if fila == 5:
         fila = 4
    if fila == 6:
         fila = 5
    if fila == 7:
         fila = 6 
    if fila == 8:
         fila = 7
    if fila == 9:
         fila = 8 
    if fila == 10:
         fila = 9    
    columna = input('Indique en la columna que se va a insertar el valor: ').lower()
    if columna == 'a':
         columna = 0
    if columna == 'b':
         columna = 1
    if columna == 'c':
         columna = 2
    if columna == 'c':
         columna = 3
    if columna == 'd':
         columna = 4
    if columna == 'e':
         columna = 5
    if columna == 'f':
         columna = 6 
    if columna == 'g':
         columna = 7
    if columna == 'h':
         columna = 8 
    if columna == 'i':
         columna = 9  
    else:
        return False  
    return valor, fila, columna

def borrador():
    fila = int(input('indique en la fila que se va a borrar: '))
    if not fila in range(1,11):
        return False
    if fila == 1:
         fila = 0
    if fila == 2:
         fila = 1
    if fila == 3:
         fila = 2
    if fila == 4:
         fila = 3
    if fila == 5:
         fila = 4
    if fila == 6:
         fila = 5
    if fila == 7:
         fila = 6 
    if fila == 8:
         fila = 7
    if fila == 9:
         fila = 8 
    if fila == 10:
         fila = 9
    else:
        return False    
    columna = input('Indique en la columna que se va a borrar el valor: ').lower()
    if columna == 'a':
         columna = 0
    if columna == 'b':
         columna = 1
    if columna == 'c':
         columna = 2
    if columna == 'c':
         columna = 3
    if columna == 'd':
         columna = 4
    if columna == 'e':
         columna = 5
    if columna == 'f':
         columna = 6 
    if columna == 'g':
         columna = 7
    if columna == 'h':
         columna = 8 
    if columna == 'i':
         columna = 9  
    else:
        return False  
    return valor, fila, columna

def main():
    print('Bienvendio a sudoku')
    while not esta_terminado(sudoku) == True:
        draw_sudoku(sudoku)
        print('Que deseas hacer?')
        seleccionador = input('si desea borrar escriba ''borrar'' si desea agregar valor inserte ''agregar'': ').lower()
        while not seleccionador == 'borrador' or seleccionador == 'agregar':         
            if seleccionador == 'agregar':
                if hay_movimientos_posibles(sudoku) == True:
                    agregar_variables()
                    insertar_valor(sudoku, fila, columna, valor)
                print('no hay movimientos posibles')
            if seleccionador == 'borrar':
                #while valor, fila, columna:             
                borrador()
                    #break
                borrar_valor(sudoku, fila, columna)
                
               

    print('GANASTE')
main()