'''
Created on Nov 4, 2017

@author: Ancuta
'''
from board import getAvailablePositions, getPositionBoard
from board import setBoard, getAvailablePositions, setToken, isBoardFull
from TicTacToe import whoGoesFirst, computerChoice, getWinner
from builtins import dict


def inputPlayerLetter():
    '''
      Lets the player what letter want to be.
      Returns a list that contains the player's token on the first position and the computer's token on the second one .
    '''   
    valid=True
    while valid is True:
        choice = input("Choose your token(X or O): ").upper()
        if choice == 'X':
            tokens=['X','O']
            valid=False
        elif choice == 'O':
            tokens=['O','X']
            valid=False
        else:
            print ("Your token is invalid. \n \n")
    
    return tokens


def isInList(avb, position):
    '''
        Checks if the given positions is or not in available position list.
        Returns true if position is in list, otherwise return false.
    '''
    if position in avb:
        return True
    return False

def displayOptionsPlayer(avb):
    '''
        Displays a special board for player. The board contains all available positions.
        
    '''
    
    print ("\n                            ~AVAIBLABLE OPTIONS~ \n")
    if isInList(avb, [0,0]):
        print ('                                1 | ',end='')
    else:
        print ('                                # | ',end='')
    
    if isInList(avb, [0,1]):
        print (' 2  | ',end='')
    else:
        print (' #  | ',end='')
    
    if isInList(avb, [0,2]):
        print ('3  ')
    else:
        print ('#  ')
    print ("                              ---------------")
        
    if isInList(avb, [1,0]):
        print ('                                4 | ',end='')
    else:
        print ('                                # | ',end='')
    
    if isInList(avb, [1,1]):
        print (' 5  | ',end='')
    else:
        print (' #  | ',end='')
    
    if isInList(avb, [1,2]):
        print ('6  ')
    else:
        print ('#   ')
        
    print ("                              ---------------")
   
    if isInList(avb, [2,0]):
        print ('                                7 | ',end='')
    else:
        print ('                                # | ',end='')
        
    if isInList(avb, [2,1]):
        print (' 8  | ',end='')
    else:
        print (' #  | ',end='')
        
    if isInList(avb, [2,2]):
        print ('9  \n \n')
    else:
        print ('#  \n \n')
        
        
def displayCurrentBoard (board):
    '''
        Display the current board.
    '''  
      
    print ("                               ~CURRENT BOARD~  \n  ")
    
    print ('                               ',board[0][0],' | ',board[0][1], ' | ', board[0][2])
    print ('                               ---------------')
    print ('                               ',board[1][0],' | ',board[1][1], ' | ', board[1][2])
    print ('                               ---------------')
    print ('                               ',board[2][0],' | ',board[2][1], ' | ', board[2][2], '\n')
    
    
def getOption(avb): 
    '''
        The player chooses a valid available option from 1 to 9 ().
    '''
    valid=True
    while valid is True:
        try:
            op=int(input("Choose an available option: "))
        except:
            print("Option has to be an available number from the board.")
            continue
        
        if op>10 or op<1 or getPositionBoard(op-1) not in  avb:
            displayOptionsPlayer(avb)
            print ("Option has to be an available number from the board. ")
            continue
        valid=False
    return op-1


def getAnswer():
    '''
        Returns the player's answer at the end of every game.
    '''    
    valid =True
    while valid is True:
        op=input(" \n Do you want to play again?(yes/no) ").lower()
        if op=='yes' or op=='no':
            valid=False
        else:
            print("Invalid answer. \n")
    return op



def game():
    print ("Welcome to TIC~TAC~TOE! \n")
    board=setBoard()
    tokens=inputPlayerLetter()
    turn= whoGoesFirst()
    valid=True
    
    
    while valid == True:
        if turn=='computer':
            print (" \n \n---It's computer's turn: ")
            position=computerChoice(board,tokens[1])
            board=setToken(board, tokens[1], position)
            print(" Computer's choice was: ",position+1)
            
            
            #displayCurrentBoard(board)
            
            turn ='player'
        else:
            print ("\n \n---It's your turn: ")
            displayCurrentBoard(board)
            displayOptionsPlayer(getAvailablePositions(board))
            op=getOption(getAvailablePositions(board))
            setToken(board, tokens[0], op)
            turn='computer'
        
        
        if getWinner(board) is not None or isBoardFull(board) is True:
            displayCurrentBoard(board)
            if tokens[0]==getWinner(board):
                print ("                            ~CONGRATULATIONS! YOU WON THIS ROUND~")
            elif tokens[1]==getWinner(board):
                print ("                            ~GAME OVER! YOU LOST THOS ROUND~")
            else:
                print ("                            ~THE GAME IS A TIE~")
                
            if getAnswer()=='yes':
                board=setBoard()
                tokens=inputPlayerLetter()
                turn= whoGoesFirst()
            else:
                print("Goodbye")
                valid=False
game()


    