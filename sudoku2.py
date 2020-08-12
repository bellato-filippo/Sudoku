import numpy as np

grid = [[0,0,8,0,0,0,0,0,0], #inizializza la griglia del sudoku
        [3,7,0,0,0,0,0,8,9],
        [2,5,0,4,0,0,0,7,0],
        [5,0,0,1,0,0,0,2,0],
        [0,0,0,0,4,0,7,1,0],
        [0,0,0,0,8,0,0,9,0],
        [9,0,3,0,0,5,0,0,0],
        [0,0,0,7,2,0,0,0,6],
        [7,6,0,0,0,0,0,0,0]]


#funzione per vedere se è possibile inserire il numero n nella riga x e colonna y
def possible(y, x, n):
    global grid
    for i in range(0, 9): #controlla lungo tutta la colonna
        if grid[y][i] == n:
            return False

    for i in range(0, 9): #controlla lungo tutta la riga
        if grid[i][x] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0, 3): #controlla all'interno del riquadro 3x3
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

#funzione per la risoluzione
def solve():
    global grid
    for y in range(9):
        for x in range(9):          #doppio for per accedere a tutte le caselle una ad una
            if grid[y][x] == 0:         #se incontra uno zero si mette a risolvere altrimenti passa al prossimo spazio vuoto
                for n in range(1, 10):      #prova tutti i numeri da 1-9 in quella casella
                    if possible(y, x, n):       #verifica se un certo numero è valido
                        grid[y][x] = n              #se è valido inserisce quel valore nella griglia
                        solve()                     #chiamata ricorsiva dato che la griglia ha uno zero in meno
                        grid[y][x] = 0              #se la chiamata fallisce rimette a 0 il valore e torna al ramo precedente
                return                      #se non trova nessun numero da 1-9 torna indietro al ramo precedente
    print(np.matrix(grid))
    input()


#la questione sta alla riga 44. Idealmente quando finisce tutto il sudoku quella riga viene eseguita comunque(?)
#visto che finisce il ramo ricorsivo della riga sopra e viene eseguita la riga dopo. Quindi mi immagino che
#ritorni tutta la griglia a zero??
solve()
