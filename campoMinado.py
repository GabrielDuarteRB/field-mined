from random import randrange
import os

class Game():

    def start(self):
        self.perdeu = False
        self.createBoard()
        while self.finishGame():
            self.printBoard(board=self.board)
            self.chooseCoords()
            self.checkCoords() 
        if self.perdeu == True:
            os.system('cls')
            print('='* self.dimensions * 5)
            self.printBoard(board=self.board)
            print('')
            print('Você Perdeu!')
            print('='* self.dimensions * 5)
        else:
            os.system('cls')
            print('='* self.dimensions * 5)
            self.printBoard(board=self.fakeBoard)
            print('')
            print('Você ganhou!')
            print('='* self.dimensions * 5)

    
    def createBoard(self):
        
        self.scorePositions = 0
        getRight = False
        
        while getRight == False:
            getRight = False
            try:
                self.dimensions = int(input('What size of board (min:4/max:10)? '))
                getRight = True
                if self.dimensions < 4 or self.dimensions > 10:
                    getRight = False
            except ValueError as error:
                print('Only numbers in range 4 - 10!')
        
        getRight = False
        while getRight == False:
            try:
                self.bombs = int(input('How many bombs? '))
                if self.bombs > self.dimensions:
                    print(f'The number of bombs cant be higher than the area({self.dimensions})')
                elif self.bombs <= 0:
                    print('The number of bombs cant be zero or below it')
                else:
                    getRight = True
            except ValueError as error:
                print('Only numbers!')

        
    

        self.fakeBoard = []
        self.board = []
        getRight = False

        #Real Board
        for i in range(self.dimensions):
            self.board.append(["_"]*self.dimensions)  
        
        #Fake Board
        #Space
        for i in range(self.dimensions):
            self.fakeBoard.append(["N"]*self.dimensions)
        #Bombs
        for i in range(self.bombs):
            positionX = randrange(self.dimensions)
            positionY = randrange(self.dimensions)
            
                
            self.fakeBoard[positionX][positionY] = "B"
        

    def chooseCoords(self):
        
        getRight = False
        while getRight == False:      
            try:
                self.coordX = int(input('Where do you want to play in horizontal?'))
                self.coordY = int(input('Where do you want to play in vertical?'))
                if self.coordX >= 0 or self.coordY >= 0:
                    if self.board[self.coordX][self.coordY] == '_':
                        getRight = True
                    else:
                        print('This positions has already been played')
                else:
                    print(f'Only positives numbers in range 0 - {self.dimensions - 1}')
            except:
                print(f'Only positives numbers in range 0 - {self.dimensions - 1}')


    def checkCoords(self):
        contBomb = 0
        
        if self.fakeBoard[self.coordX][self.coordY] == 'B' and self.board[self.coordX][self.coordY] == '_':

            self.board[self.coordX][self.coordY] = 'B'
            self.perdeu = True

        elif self.fakeBoard[self.coordX][self.coordY] == 'N' and self.board[self.coordX][self.coordY] == '_':

            for x in range(self.coordX-1, self.coordX+2):
                if x >= 0 and x <= self.dimensions - 1:
                    for y in range(self.coordY-1, self.coordY+2):
                        if y >= 0 and y <= self.dimensions - 1:
                            if self.fakeBoard[x][y] == 'B':
                                contBomb += 1

            self.board[self.coordX][self.coordY] = contBomb
            self.scorePositions += 1
            
    def printBoard(self, board):
        linha = 0
        print('     ', end='')
        for item in range(self.dimensions):
            if item == self.dimensions-1:
                print(f'{item}')
            else:
                print(f'{item}  ', end='')
        print('=' * (self.dimensions * 4))
            
        for item in board:
            print(f'{linha}|   ', end='')
            print ('  '.join(map(str, item)))
            linha += 1

    def finishGame(self):
        if self.perdeu == True:
            return False
        elif self.scorePositions == self.dimensions ** 2 - self.bombs:
            return False
        return True


fieldMined = Game()
fieldMined.start()