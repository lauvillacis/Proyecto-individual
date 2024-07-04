#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import random
import time
from colorama import Fore

class Sudoku:
    def __init__(self,sudoku,solucion,solucion_original,contador):
        self.__sudoku = []
        self.__solucion = []
        self.__solucion_original = []
        self.__contador = 0
        
    def sudoku(self):
        '''
        Es el metodo get, para devolver el valor del atributo 'sudoku'
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        No devuelve nada
        '''
        return self.__sudoku
    
    def solucion(self):
        '''
        Es el metodo get, para devolver el valor del atributo 'sudoku'
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        No devuelve nada
        '''
        return self.__solucion
    
    def solucion_original(self):
        '''
        Es el metodo get, para devolver el valor del atributo 'sudoku'
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        No devuelve nada
        '''
        return self.__solucion_original
    
    def contador(self):
        '''
        Es el metodo get, para devolver el valor del atributo 'sudoku'
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        No devuelve nada
        '''
        return self.__contador

    def validar_casilla(self, valor, sudoku_evaluado, i, j):
        #Se encuentra el bloque en el que se encuentra
        bloque_i = i // 3
        bloque_j = j // 3

        #Se revisa que no esté el número en el bloque
        for b_i in range(bloque_i * 3, bloque_i * 3 + 3):
            for b_j in range(bloque_j * 3, bloque_j * 3 + 3):
                if sudoku_evaluado[b_i][b_j] == valor:
                    return False
        #Se revisa que no esté el número en la fila
        for columna in range(0, 9):
            if sudoku_evaluado[i][columna] == valor:
                return False

        #Se revisa que no esté el número en la columna
        for fila in range(0, 9):
            if sudoku_evaluado[fila][j] == valor:
                return False

        return True

    def backtracking(self):
        #Se itera sobre todas las casillas
        for row in range(9):
            for col in range(9):
                #Si la casilla es cero(está vacía), intento llenarla
                if self.__solucion[row][col] == 0:
                    #Se itera sobre todos los posibles valores para cada casilla
                    for valor in range(1, 10):
                        #Si el número es válido
                        if self.validar_casilla(valor, self.__solucion, row, col):
                            #Rellena la casilla con el número 
                            self.__solucion[row][col] = valor
                            #Llama a la función backtracking de nuevo, si esta devuelve True es porque se encontró solución
                            if self.backtracking(): #(self.__solucion):
                                return True
                            #Si no se encontró una solución, se resetea la casilla
                            self.__solucion[row][col] = 0
                    #Si ningún número funcionó devuelve Falso y se devuelve         
                    return False
        #Ya no hay más casillas vacías y resolvió el sudoku  
        return True


    def contador_soluciones(self, sudoku_evaluado, i, j): #Es mejor hacer un atributo copia o meter como parámetro otra vez la matriz?
        #Itera sobre todas las casillas
        if j > 8:
            j = 0
            i += 1
            if i > 8:
                #Si ya se llegó a la última casilla, significa que se encontró una solución
                self.__contador += 1
                return
        #Si la casilla es distinta de cero    
        if sudoku_evaluado[i][j] != 0:
            #Llama recursivamente a la función en la siguiente casilla
            self.contador_soluciones(sudoku_evaluado,i, (j + 1))
        else:
            #Se prueban todos los valores para la casilla vacía
            for valor in range(1, 10):
                #Si el número es válido en la casilla
                if self.validar_casilla(valor, sudoku_evaluado, i, j):
                    #Se cambia el valor de la casilla
                    sudoku_evaluado[i][j] = valor
                    #Se llama recursivamente al contador de soluciones en la siguiente casilla
                    self.contador_soluciones(sudoku_evaluado,i, (j + 1))
                    #Si no es una solución válida, devuelve el valor de la casilla
                    sudoku_evaluado[i][j] = 0
                    #Si el contador es mayor a uno, queire decir que la solución no es única
                    if self.__contador > 1:
                        #Se sale de la función
                        return


    def generador(self, grid, i, j):
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #Itera sobre los posibles valores para cada casilla
        if j > 8:
            j = 0
            i += 1
            if i > 8:
                return True
        #Si la casilla es distinta de cero
        if grid[i][j] != 0:
            #Lama recursivamente a la función en la siguiente casilla
            if self.generador(grid, i, (j + 1)):
                return True
        else:
            # Desordena de manera aleatorio a los números
            random.shuffle(numeros)
            #Itera sobre todos los valores de números
            for valor in numeros:
                # revisa si se puede poner en la casilla
                if self.validar_casilla( valor,grid, i, j):
                    #Se llena la casilla 
                    grid[i][j] = valor
                    #Sigue a la siguiente casilla
                    if self.generador(grid, i, (j + 1)):
                        return True
                    #Si el valor con el que se está probando no funciona, resetea la casilla
                    grid[i][j] = 0
        return False


    def generador_sudoku_resuelto(self):
        # se inicializa el sudoku
        sudoku_resuelto= []
        for i in range(9):
            sudoku_resuelto.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        # se genera el sudoku usando backtracking y se guarda en el sudoku nuevo
        self.generador(sudoku_resuelto, 0, 0)
        return sudoku_resuelto

    def generador_sudoku(self, level=2):
        # se genera un sudoku resuelto
        sudoku_resuelto = self.generador_sudoku_resuelto()
        #se guarda el sudoku resuelto 
        self.__solucion_original = copy.deepcopy(sudoku_resuelto)
        #Se establecen los niveles de dificultad, quita más números entre mayor sea el nivel
        if level == 1:
            casilla_a_remover = random.randint(32, 38)
        if level == 2:
            casilla_a_remover = random.randint(40, 46)
        if level == 3:
            casilla_a_remover = random.randint(48, 52)
        if level == 4:
            casilla_a_remover = random.randint(54, 56)
        if level == 5:
            casilla_a_remover = random.randint(59, 61)

        # se hace una lista con todas las posibles casillas
        indice = []
        for i in range(81):
            indice.append(i)

        #Se hace un while para eliminar números de casillas aleatorias    
        while casilla_a_remover > 0:
            casilla_id = random.sample(indice, 1)[0]
            row = casilla_id // 9
            col = casilla_id % 9

            indice.remove(casilla_id)

            
            #Se guarda el valor eliminado en caso de que se decida no eliminarlo
            valor_eliminado = sudoku_resuelto[row][col]
            
            #Se pone la casilla en cero
            sudoku_resuelto[row][col] = 0
            
            self.contador_soluciones(sudoku_resuelto,0, 0)
            #Si eliminar ese número genera más de una solución, entonces lo devuelve
            if self.__contador > 1:
                sudoku_resuelto[row][col] = valor_eliminado
            else:
                casilla_a_remover -= 1
            #Devuelve el contador de soluciones a cero
            self.__contador = 0
        #self.visualizar(sudoku_resuelto)
        self.__sudoku = copy.deepcopy(sudoku_resuelto)
        self.__solucion = sudoku_resuelto

    
    def visualizar(self):
        print('El sudoku original es:\n')
        for i in range(9):
            print(self.__sudoku[i])
        print("\n")
        print('El sudoku resuelto con backtracking es:\n')
        for i in range(9):
            print(self.__solucion[i])
        print("\n")
        print('La solución original es:\n')
        for i in range(9):
            print(self.__solucion_original[i])
        print("\n")
        
        
        
    def posibles_valores(self, fila, columna):
        if self.__solucion_manual[fila][columna] != 0:
            return
        #Se encuentra el bloque en el que se encuentra

        bloque_i = (fila // 3) * 3
        bloque_j = (columna // 3) * 3        
        candidatos = set(range(1, 10))

        #Se revisa que no esté el número en el bloque
        for b_i in range(bloque_i, bloque_i + 3):
            for b_j in range(bloque_j, bloque_j + 3):
                if self.__solucion_manual[b_i][b_j] in candidatos:
                    candidatos.remove(self.__solucion_manual[b_i][b_j])

        #Se revisa que no esté el número en la fila
        for columnas in range(0, 9):
            if self.__solucion_manual[fila][columnas] in candidatos:
                candidatos.remove(self.__solucion_manual[fila][columnas])


        #Se revisa que no esté el número en la columna
        for filas in range(0, 9):
            if self.__solucion_manual[filas][columna] in candidatos:
                candidatos.remove(self.__solucion_manual[filas][columna])
                    
        self.__solucion_manual[fila][columna] = list(candidatos)
        for i in range(9):
            print(self.__solucion_manual[i])
        print("\n")
        return
    
    
    #Str
    def __str__(self):
        
        return f'El SUDOKU es: {self.__sudoku}, SU SOLUCION ES:{self.__solucion},\n SU SOLUCION ORIGINAL ES: {self.__solucion_original} '
    
    
    

class Juego(Sudoku):
    def __init__(self,sudoku,solucion,solucion_original,contador, proceso): 
        Sudoku.__init__(self,sudoku,solucion,solucion_original,contador) 
        self.__proceso = []
    
    def mostrar_sudoku(self, tablero, fila = -1, columna = -1):
        for i in range(9):
            for j in range(9):
                #Imprime en rojo la casilla seleccionada
                if i == fila and j == columna:
                    print(Fore.RED + f'{tablero[i][j]}', end=' ')
                else:
                    print(Fore.BLACK + f'{tablero[i][j]}', end=' ')
            print()
            
   
    def mostrar_sudoku_lineas(self, tablero, fila=-1, columna=-1):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print(Fore.BLACK + "------+-------+------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(Fore.BLACK + '|', end=' ')
                if i == fila and j == columna:
                    print(Fore.RED + f'{tablero[i][j]}', end=' ')
                else:
                    print(Fore.BLACK + f'{tablero[i][j]}', end=' ')
            print()

    def jugar(self):
        self.mostrar_sudoku_lineas(self.sudoku())
        vidas = 3
        while True:
            entrada = input('Selecciona la casilla (fila, columna): ')
            if entrada.lower() == 'solucion':
                self.backtracking()
                self.mostrar_sudoku_lineas(self.solucion())
                break

            try:
                fila, columna = [int(valor) for valor in entrada.split(',')]
            except ValueError:
                print('Entrada inválida. Intente de nuevo.')
                continue

            if not (0 <= fila < 9 and 0 <= columna < 9):
                print('Posición inválida. Intente de nuevo.')
                continue

            if self.sudoku()[fila][columna] != 0:
                print('La casilla ya cuenta con un número. Intente de nuevo.')
                continue

            valor = int(input('Ingrese el número: '))
            self.backtracking()
            if self.solucion()[fila][columna] == valor:
                self.sudoku()[fila][columna] = valor
                self.mostrar_sudoku_lineas(self.sudoku())
            else:
                tablero_incorrecto = copy.deepcopy(self.sudoku())
                tablero_incorrecto[fila][columna] = valor
                self.mostrar_sudoku_lineas(tablero_incorrecto,fila,columna)
                print('Valor incorrecto. Intente de nuevo.')
                vidas -= 1
                if vidas == 0:
                    print('Te has quedado sin vidas. Fin del juego.')
                    break

            if not any(0 in fila for fila in self.sudoku()):
                print('¡Felicidades! Has completado el Sudoku.')
                break
        