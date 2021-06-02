from random import randint
from mapas import *
from sudoku import *

def draw_sudoku(sudoku):
    print(' ', 'A', 'B', 'C', '  D', 'E', 'F', '  G', 'H', 'I', '    FI|LA')
    for  i in range(ALTO_TABLERO):
        if i % 3 == 0:
                print('-' * 25) 
        for j in range(ANCHO_TABLERO):
            if j % 3 == 0:
                print('|', end= ' ' )
            print(sudoku[i][j], end=' ')
        print('|    ', i+1)
        print('', ' ')
    print('-'*25)

def agregar_variables(): #tiene los if despues de cada variable para que sea mas facil saber que numero estuvo mal
    valor = int(input('ingrese el valor a insertar[entre 0 y 9]: ')) 
    fila = int(input('indique en la fila que se va a inserta[entre 1 y 9]: ')) - 1
    columna = input('Indique en la columna que se va a insertar el valor: ').lower()
    if columna == 'a':
         columna = 0
    elif columna == 'b':
         columna = 1
    elif columna == 'c':
         columna = 2
    elif columna == 'c':
         columna = 3
    elif columna == 'd':
         columna = 4
    elif columna == 'e':
         columna = 5
    elif columna == 'f':
         columna = 6 
    elif columna == 'g':
         columna = 7
    elif columna == 'h':
         columna = 8 
    elif columna == 'i':
         columna = 9  
    return valor, fila, columna

def borrador():
    fila = int(input('indique en la fila que se va a borrar: ')) - 1
    columna = input('Indique en la columna que se va a borrar el valor: ').lower()
    print(columna)
    if columna == 'a':
         columna = 0
    elif columna == 'b':
         columna = 1
    elif columna == 'c':
         columna = 2
    elif columna == 'c':
         columna = 3
    elif columna == 'd':
         columna = 4
    elif columna == 'e':
         columna = 5
    elif columna == 'f':
         columna = 6 
    elif columna == 'g':
         columna = 7
    elif columna == 'h':
         columna = 8 
    elif columna == 'i':
         columna = 9  
    return fila, columna

def main():
    MAPA = MAPAS[randint(0, 49)]
    sudoku = crear_juego(MAPA)
    print('''\
/$$$$$$$  /$$$$$$ /$$$$$$$$ /$$   /$$ /$$    /$$ /$$$$$$$$ /$$   /$$ /$$$$$$ /$$$$$$$   /$$$$$$ 
| $$__  $$|_  $$_/| $$_____/| $$$ | $$| $$   | $$| $$_____/| $$$ | $$|_  $$_/| $$__  $$ /$$__  $$
| $$  \ $$  | $$  | $$      | $$$$| $$| $$   | $$| $$      | $$$$| $$  | $$  | $$  \ $$| $$  \ $$
| $$$$$$$   | $$  | $$$$$   | $$ $$ $$|  $$ / $$/| $$$$$   | $$ $$ $$  | $$  | $$  | $$| $$  | $$
| $$__  $$  | $$  | $$__/   | $$  $$$$ \  $$ $$/ | $$__/   | $$  $$$$  | $$  | $$  | $$| $$  | $$
| $$  \ $$  | $$  | $$      | $$\  $$$  \  $$$/  | $$      | $$\  $$$  | $$  | $$  | $$| $$  | $$
| $$$$$$$/ /$$$$$$| $$$$$$$$| $$ \  $$   \  $/   | $$$$$$$$| $$ \  $$ /$$$$$$| $$$$$$$/|  $$$$$$/
|_______/ |______/|________/|__/  \__/    \_/    |________/|__/  \__/|______/|_______/  \______/ 
                                                                                                 
                                                                                                
                        release note: Removed Herobraine 


        ''')
    while not esta_terminado(sudoku) == True:
        draw_sudoku(sudoku)
        print('Que deseas hacer?')
        seleccionador = input('si desea borrar escriba ''borrar'' si desea agregar valor inserte ''agregar'': ').lower()
        accion_valida = seleccionador == 'agregar' or seleccionador == 'borrar'
        while accion_valida:         
            if seleccionador == 'agregar':
                if hay_movimientos_posibles(sudoku) == True:
                    valor, fila, columna = agregar_variables()
                    sudoku = insertar_valor(sudoku, fila, columna, valor)
                print('no hay movimientos posibles')
            if seleccionador == 'borrar':                              
                fila, columna = borrador()
                sudoku = borrar_valor(sudoku, fila, columna)
            accion_valida = False        
               

    print('''\

  /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$ /$$
 /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$ /$$__  $$|__  $$__/| $$_____/| $$| $$
| $$  \__/| $$  \ $$| $$$$| $$| $$  \ $$| $$  \__/   | $$   | $$      | $$| $$
| $$ /$$$$| $$$$$$$$| $$ $$ $$| $$$$$$$$|  $$$$$$    | $$   | $$$$$   | $$| $$
| $$|_  $$| $$__  $$| $$  $$$$| $$__  $$ \____  $$   | $$   | $$__/   |__/|__/
| $$  \ $$| $$  | $$| $$\  $$$| $$  | $$ /$$  \ $$   | $$   | $$              
|  $$$$$$/| $$  | $$| $$ \  $$| $$  | $$|  $$$$$$/   | $$   | $$$$$$$$ /$$ /$$
 \______/ |__/  |__/|__/  \__/|__/  |__/ \______/    |__/   |________/|__/|__/
                                                                              

        ''')
    Not_Herobraine = input('')
    if Not_Herobraine == '':
        print('''\

                 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,              
                 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&%              
                 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&&&&              
                 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&              
                 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&              
                 &&&&&&///////////////////////////////////(&&&&&&&              
                 &&&//////////////////*/////////////////(/////&&&&              
                 ////////////////////////*/*///////////////((((((&              
                 ////////////////////////((///////////////////(((&              
                 ///////(////(((/////////(/(///*********,,,//////&              
                 //////            /////////(((         .. //////%              
                 //////            ////////////            (/////%              
                 (((//////////////////##&###///////////////(((###%              
                 #((///////////////##%###%##%##////////////(((###%              
                 ((((((//////########################//////######%              
                 ((#(((//////#####################(((///((/##(####              
                 (((((((#(//////##################//////#((#(####(              
                 ###((#(((((((((#(((((((((((((((#(((##(((((((#####              
                 %########################################(#######              
(((((((((((((((((((((((((((######(/(/((##################(((((((((     ./(((((((
(((((((((((((((((((((((((((######(/((((##################(((((((((((((((((((((((
((((((((((((((((((((((((((((((######((((((###(((######((((((((((((((((((((((((((
(((((((((((((((((((((((((((((((((######(((((/######(((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((((((############((((((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
(((((((((((((((((#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
///////((((((((((#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
/////////////////((((((((((((((((((((((((((((((((((((((((((((((((# /////////////


            ''')
main()