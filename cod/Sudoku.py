import copy
import random
from colorama import Fore

class Sudoku:
    def __init__(self,sudoku,solucion_backtracking,solucion_manual,solucion_original,contador):
        '''
        Es el metodo constructor de los objetos de la clase
        
        Parametros
        -------
        sudoku: lista
            Guarda el sudoku a resolver
        solucion_backtracking: lista
            Contiene la solución que devuelve el método backtracking
        solucion_manual: lista
            Contiene la solución que devuelve el método heurístico
        solucion_original: lista
            Contiene la solución original
        contador: int
            Cuenta la cantidad de soluciones del sudoku
            
        Returns
        -------
        No devuelve nada
        '''
        self.__sudoku = sudoku #[]
        self.__solucion_backtracking = solucion_backtracking #[]
        self.__solucion_manual = solucion_manual #[]
        self.__solucion_original = solucion_original #[]
        self.__contador = contador #0
        
    @property
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
    
    @property
    def solucion_backtracking(self):
        '''
        Es el metodo get, para devolver la solución por medio de backtracking
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        No devuelve nada
        '''
        return self.__solucion_backtracking
    
    @property
    def solucion_manual(self):
        '''
        Es el metodo get, para devolver la solución con el método heurístico
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        No devuelve nada
        '''
        return self.__solucion_manual
    
    @property
    def solucion_original(self):
        '''
        Es el metodo get, para devolver la solución original
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        No devuelve nada
        '''
        return self.__solucion_original
    
    @property
    def contador(self):
        '''
        Es el metodo get, para devolver el contador, que cuenta la cantidad de soluciones
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        No devuelve nada
        '''
        return self.__contador
    
    
    
        #Str
    def __str__(self):
        '''
        Devuelve lo que contenga el objeto
        
        Parametros
        -------
        No lleva parametros explicitos pero se usa el objeto de la clase
        
        Returns
        -------
        Devuelve una cadena de texto
            En la cadena de texto se pone prosa y se imprime el valor de todos los 
            atributos

        '''
        return f'El sudoku es: {self.__sudoku}, Su solución es: {self.__solucion_original}\n Su solución con backtracking es: {self.__solucion_backtracking} \
        \n Su solución con el método heurístico es: {self.__solucion_manual} \n \
        el contador que se utiliza temporalmente en algunos métodos es: {self.__contador}'
    
    

    
    
    
    
    def validar_casilla(self, valor, sudoku_evaluado, fila, columna):
        '''
        Dada una casilla, valida si el valor propuesto puede ir o no en la casilla
        
        Parametros
        -------
        valor: int
            valor que se está intentando poner en la casilla
        sudoku_evaluado: lista
            corresponde al sudoku que se quiere verificar
        fila: int
            corresponde a la fila de la casilla
        columna:int
            corresponde a la columna de la casilla

        Returns
        -------
        Boolean: indica si el valor puede o no puede ir en la casilla
        '''
        #Se encuentra el bloque en el que se encuentra
        bloque_i = fila // 3
        bloque_j = columna // 3

        #Se revisa que no esté el número en el bloque
        for b_i in range(bloque_i * 3, bloque_i * 3 + 3):
            for b_j in range(bloque_j * 3, bloque_j * 3 + 3):
                if sudoku_evaluado[b_i][b_j] == valor:
                    return False
        #Se revisa que no esté el número en la fila
        for j in range(0, 9):
            if sudoku_evaluado[fila][j] == valor:
                return False

        #Se revisa que no esté el número en la columna
        for i in range(0, 9):
            if sudoku_evaluado[i][columna] == valor:
                return False

        return True

    def backtracking(self):
        '''
        Dado un tablero de sudoku, se resuelve el sudoku con el método bactracking
        
        Parametros
        -------
        no recibe nada, ya que modifica el atributo de la clase: solucion_backtracking

        Returns
        -------
        no devuelve nada, solo modifica el atribuo solucion_backtracking
        '''
        #Se itera sobre todas las casillas
        for row in range(9):
            for col in range(9):
                #Si la casilla es cero(está vacía), intento llenarla
                if self.__solucion_backtracking[row][col] == 0:
                    #Se itera sobre todos los posibles valores para cada casilla
                    for valor in range(1, 10):
                        #Si el número es válido
                        if self.validar_casilla(valor, self.__solucion_backtracking, row, col):
                            #Rellena la casilla con el número 
                            self.__solucion_backtracking[row][col] = valor
                            #Llama a la función backtracking de nuevo, si esta devuelve True es porque se encontró solución
                            if self.backtracking(): #(self.__solucion):
                                return True
                            #Si no se encontró una solución, se resetea la casilla
                            self.__solucion_backtracking[row][col] = 0
                    #Si ningún número funcionó devuelve Falso y se devuelve         
                    return False
        #Ya no hay más casillas vacías y resolvió el sudoku  
        return True


    def contador_soluciones(self, sudoku_evaluado, fila, columna): 
        '''
        Cuenta la cantidad de soluciones que tiene un sudoku dado
        
        Parametros
        -------
        sudoku_evaluado: lista
            Recibe el sudoku a evaluar 
        fila: int
            El número de fila
        columna: int
            El número de columna

        Returns
        -------
        no devuelve nada, solo modifica el atribuo contador
        '''
        #Itera sobre todas las casillas
        if columna > 8:
            columna = 0
            fila += 1
            if fila > 8:
                #Si ya se llegó a la última casilla, significa que se encontró una solución
                self.__contador += 1
                return
        #Si la casilla es distinta de cero    
        if sudoku_evaluado[fila][columna] != 0:
            #Llama recursivamente a la función en la siguiente casilla
            self.contador_soluciones(sudoku_evaluado,fila, (columna + 1))
        else:
            #Se prueban todos los valores para la casilla vacía
            for valor in range(1, 10):
                #Si el número es válido en la casilla
                if self.validar_casilla(valor, sudoku_evaluado, fila, columna):
                    #Se cambia el valor de la casilla
                    sudoku_evaluado[fila][columna] = valor
                    #Se llama recursivamente al contador de soluciones en la siguiente casilla
                    self.contador_soluciones(sudoku_evaluado, fila, (columna + 1))
                    #Si no es una solución válida, devuelve el valor de la casilla
                    sudoku_evaluado[fila][columna] = 0
                    #Si el contador es mayor a uno, queire decir que la solución no es única
                    if self.__contador > 1:
                        #Se sale de la función
                        return


    def generador(self, tablero, fila, columna):
        '''
        Genera un sudoku desde cero, con el método backtracking
        
        Parametros
        -------
        sudoku_evaluado: lista
            Recibe el sudoku a evaluar 
        fila: int
            El número de fila
        columna: int
            El número de columna

        Returns
        -------
        no devuelve nada, solo modifica el parámetro tablero
        '''
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #Itera sobre los posibles valores para cada casilla
        if columna > 8:
            columna = 0
            fila += 1
            if fila > 8:
                return True
        #Si la casilla es distinta de cero
        if tablero[fila][columna] != 0:
            #Lama recursivamente a la función en la siguiente casilla
            if self.generador(tablero, fila, (columna + 1)):
                return True
        else:
            # Desordena de manera aleatorio a los números
            random.shuffle(numeros)
            #Itera sobre todos los valores de números
            for valor in numeros:
                # revisa si se puede poner en la casilla
                if self.validar_casilla( valor,tablero, fila, columna):
                    #Se llena la casilla 
                    tablero[fila][columna] = valor
                    #Sigue a la siguiente casilla
                    if self.generador(tablero, fila, (columna + 1)):
                        return True
                    #Si el valor con el que se está probando no funciona, resetea la casilla
                    tablero[fila][columna] = 0
        return False


    def generador_sudoku_resuelto(self):
        '''
        Genera un sudoku resuelto
        
        Parametros
        -------
        no lleva parámetros

        Returns
        -------
        sudoku_resuelto: lista
            Devuelve el sudoku resuelto
        '''
        # se inicializa el sudoku
        sudoku_resuelto= []
        for i in range(9):
            sudoku_resuelto.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        # se genera el sudoku usando backtracking y se guarda en el sudoku nuevo
        self.generador(sudoku_resuelto, 0, 0)
        return sudoku_resuelto

    def generador_sudoku(self, nivel=2):
        '''
        Genera un tablero de sudoku según la dificultad establecida
        
        Parametros
        -------
        nivel: int
            Es la dificultad del sudko que varía desde 1 a 5, donde 1 es el más fácil y 5 el más difícil
        Returns
        -------
        no devuelve nada, solo modifica los atributos sudoku, solucion_backtracking y solución_manual
        '''
        # se genera un sudoku resuelto
        sudoku_resuelto = self.generador_sudoku_resuelto()
        #se guarda el sudoku resuelto 
        self.__solucion_original = copy.deepcopy(sudoku_resuelto)
        #Se establecen los niveles de dificultad, quita más números entre mayor sea el nivel
        if nivel == 1:
            casilla_a_remover = random.randint(32, 38)
        if nivel == 2:
            casilla_a_remover = random.randint(40, 46)
        if nivel == 3:
            casilla_a_remover = random.randint(48, 52)
        if nivel == 4:
            casilla_a_remover = random.randint(54, 56)
        if nivel == 5:
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
        #Se guarda el sudoku obtenido para resolverlo posteriormente
        self.__sudoku = copy.deepcopy(sudoku_resuelto)
        self.__solucion_backtracking = copy.deepcopy(sudoku_resuelto)
        self.__solucion_manual = copy.deepcopy(sudoku_resuelto)
    
    def visualizar(self):
        print('El tablero del sudoku es:\n')
        self.imprimir_sudoku(self.__sudoku)
        print('La solución original es:\n')
        self.imprimir_sudoku(self.__solucion_original)
        print('El sudoku resuelto con backtracking es:\n')
        self.imprimir_sudoku(self.__solucion_backtracking)
        print('El sudoku resuelto con el método heurístico es:\n')
        self.imprimir_sudoku(self.__solucion_manual)
        
        
    def posibles_valores(self, fila, columna):
        '''
        Evalúa según la fila, columna y bloque de la casilla en cuestión, todos los
        posibles valores que pueden ir en la casilla
        
        Parametros
        -------
        fila: int
            El número de fila
        columna: int
            El número de columna

        Returns
        -------
        no devuelve nada, solo modifica el la solución sudoku
        '''
        #Si la casilla es distinta de cero no evalúa nada
        if self.__solucion_manual[fila][columna] != 0:
            return
        #Se consiguen los valores del bloque
        bloque_i = (fila // 3) * 3
        bloque_j = (columna // 3) * 3  
        #Se guardan los posibles candidatos como un conjunto
        candidatos = set(range(1, 10))
        
        #Se revisa que no esté el número en el bloque
        for b_i in range(bloque_i, bloque_i + 3):
            for b_j in range(bloque_j, bloque_j + 3):
                if isinstance(self.__solucion_manual[b_i][b_j], int) and self.__solucion_manual[b_i][b_j] in candidatos:
                    candidatos.remove(self.__solucion_manual[b_i][b_j])

        #Se revisa que no esté el número en la fila
        for columnas in range(0, 9):
            if isinstance(self.__solucion_manual[fila][columnas], int) and self.__solucion_manual[fila][columnas] in candidatos:
                candidatos.remove(self.__solucion_manual[fila][columnas])


        #Se revisa que no esté el número en la columna
        for filas in range(0, 9):
            if isinstance(self.__solucion_manual[filas][columna], int) and self.__solucion_manual[filas][columna] in candidatos:
                candidatos.remove(self.__solucion_manual[filas][columna])
        #Se guarda en la casilla dada una lista con los posibles valores            
        self.__solucion_manual[fila][columna] = list(candidatos)
        return 
    

        
    def valores_basic_filler(self):
        '''
        Calcula la intersección para cada casilla y hay un único valor entonces lo agrega en la solución
        
        Parametros
        -------
        No lleva parámetros

        Returns
        -------
        no devuelve nada, solo modifica el la solución manual de la clase
        '''
        #Se mide el error cómo la cantidad de datos que son diferentes al de la solución
        faltantes = self.medir_error(self.__solucion_manual)
        faltantes_anteriores = 0
        contador = 0
        #Se genera un while que mientras la cantidad de números diferentes cambie, entonces que siga ejecutandose
        while faltantes_anteriores != faltantes:
            contador +=1
            if contador != 1:
                #Las listas se convierten a ceros para volver a calcular los posibles valores
                for i in range(0,9):
                    for j in range(0,9):
                        if type(self.__solucion_manual[i][j]) == list:
                            self.__solucion_manual[i][j] = 0
            for i in range(0,9):
                for j in range(0,9):
                    self.posibles_valores(i,j)
                    if type(self.__solucion_manual[i][j]) == list and len(self.__solucion_manual[i][j]) == 1:
                        self.__solucion_manual[i][j] = self.__solucion_manual[i][j][0]
            faltantes_anteriores = faltantes
            faltantes = self.medir_error(self.__solucion_manual)
        self.imprimir_sudoku(self.__solucion_manual)
        #Si sale TRUE se resolvió el sudoku con éxito, si no, no se ha llegado a la solución
        print(self.__solucion_manual == self.__solucion_original)
        return 
        
        
    def imprimir_sudoku(self, sudoku_a_imprimir):
        '''
        Imprime el sudoku que se desee
        
        Parametros
        -------
        sudoku_a_imprimir: lista
            El sudoku que se quiere imprimir

        Returns
        -------
        no devuelve nada, solo imprime el sudoku
        '''
        for fila in sudoku_a_imprimir:
            print(" ".join(str(num) if num != 0 else '.' for num in fila))
        print("\n")
        
    def medir_error(self, sudoku_evaluado):
        '''
        Cuenta la cantidad de valores diferentes a la solucion original que tiene el sudoku evaluado 
        
        Parametros
        -------
        sudoku_evaluado: lista
            El sudoku que se quiere revisar

        Returns
        -------
        errores: int
            Es la cantidad de valores diferentes que tiene el sudoku que se está evaluando
        '''
        errores = 0
        for i in range(0,9):
                for j in range(0,9):
                    #Si el valor es una lista o es diferente al correcto, suma 1 a la cantidad de errores
                    if type(sudoku_evaluado[i][j]) == list or sudoku_evaluado[i][j] != self.__solucion_original[i][j] :
                        errores += 1
        return errores
    

  
    

class Juego(Sudoku):
    def __init__(self,sudoku,solucion_backtracking,solucion_manual,solucion_original,contador): 
        '''
        Es el metodo constructor de los objetos de la clase, hereda todos los atributos
        de la clase sudoku
        
        Parametros
        -------
        sudoku: lista
            Guarda el sudoku a resolver
        solucion_backtracking: lista
            Contiene la solución que devuelve el método backtracking
        solucion_manual: lista
            Contiene la solución que devuelve el método heurístico
        solucion_original: lista
            Contiene la solución original
        contador: int
            Cuenta la cantidad de soluciones del sudoku
        Returns
        -------
        No devuelve nada
        '''
        Sudoku.__init__(self,sudoku,solucion_backtracking,solucion_manual,solucion_original,contador) 
    
     
   
    def mostrar_sudoku_lineas(self, tablero, fila=-1, columna=-1):
        '''
        Imprime el sudoku con lineas para que se facilite la visualización
        
        Parametros
        -------
        tablero: lista
            El sudoku que se quiere imprimir
        fila: int
            Es la fila de la casilla
        columna: lista
            Es la fila

        Returns
        -------
        no devuelve nada, solo imprime
        '''
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

    def jugar_con_vidas(self):
        '''
        Es la función de juego con vidas, le muestra al usuario cun tablero de sudoku sin resolver
        y conforme va obteniendo los valores que le ingrese el usuraio evalua el input.
        Si el usuario se equivoca más de tres veces termina el juego.
        A la hora de ingresar la casilla tiene que ser en el formato: fila,columna
        Los números tienen que ser del 1 al 9
        Parametros
        -------
        no recibe parámetros

        Returns
        -------
        no devuelve nada
        '''
        self.mostrar_sudoku_lineas(self.sudoku())
        vidas = 3
        while True:
            #Si se pide la solucion se resuelve con bactracking y se muestra, se termina el juego
            entrada = input('Selecciona la casilla (fila, columna): ')
            if entrada.lower() == 'solucion':
                self.backtracking()
                self.mostrar_sudoku_lineas(self.solucion())
                break
            #si no se ingresan valores validos vuelve a pedir una entrada
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
            #Se revisa el valor ingresado y se guarda si este es correcto
            self.backtracking()
            if self.solucion()[fila][columna] == valor:
                self.sudoku()[fila][columna] = valor
                self.mostrar_sudoku_lineas(self.sudoku())
            else:
                tablero_incorrecto = copy.deepcopy(self.sudoku())
                tablero_incorrecto[fila][columna] = valor
                self.mostrar_sudoku_lineas(tablero_incorrecto,fila,columna)
                print('Valor incorrecto. Intente de nuevo.')
                #se elimina una vida si se equivoca
                vidas -= 1
                if vidas == 0:
                    print('Te has quedado sin vidas. Fin del juego.')
                    break
            #Si se rellenaron todas las casillas, se ganó
            if not any(0 in fila for fila in self.sudoku()):
                print('¡Felicidades! Has completado el Sudoku.')
                break
        