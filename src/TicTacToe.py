'''
Created on Nov 4, 2017

@author: Ancuta
'''

import random
import copy
from board import getAvailablePositions, getPositionBoard, setToken,\
    getPositionPlayer
   

def whoGoesFirst():
    '''
        We use randon fugenction to choose who goes first.
    '''
    if random.randint(0,1)==0:
        return 'computer' 
    else:
        return 'player'
    
    
def getCopy(board) :
    '''
        Creates and returns a copy to current board.
    '''
    cop=[]
    cop=copy.deepcopy(board)
    return cop 


def isFreeSpace(board, position):
    '''
        Returns True if the element at given  postion is void . Oherwise False
        
    '''
    position =getPositionBoard(position)
    if board[position[0]][position[1]]==' ':
        return True
    else:
        return False
  
def getPossibleWinner ( board, token):
    '''
        Returns the possible position for winning the game.
          | o | o
        ---------
        x |   |  
        ---------
          | x |  
        
        The player with token 'o''s turn:
            -he can win the game if he makes the wise choice. (He chooses the 1 position)
        The player with token 'x''s turn:
            - he still has a change to win if he blocks the other's win.  (He chooses the 1 position)
              
    '''
    for index in range(9):
        copy=getCopy(board)
        if isFreeSpace(board,index) :
            setToken(copy, token, index)
            if getWinner(copy)==token:
                return index
    
    
    
    
def computerChoice(board, computerToken):
    '''
        We use an AI algorithm from computer's choice.
        1. Checks out if computer can make a choice to win the game. Otherwise, step 2:
        2. Verifies if player can make a move to win the game, if there is, computer will block player's win . Otherwise we jump to 3 step.
        3. Checks if any corner is free (1,3,7,9), otherwise step 4
        4. Checks if the center is available (5).
        5. Return randomly an available position.
        
        Return a player's position like 1,2,3,4,...
    '''
    
    
    
    #step 1  (we use a backtracking algorithm)
    if getPossibleWinner(board, computerToken):
        return getPossibleWinner(board, computerToken)
     
    #step 2 
    if computerToken=='X':
        playerToken='O'
    else:
        playerToken='X'
    if getPossibleWinner(board, playerToken):
        return getPossibleWinner(board, playerToken)
    
    #step 3:
    
    l=[]
    for index in [0,2,6,8]:
        if isFreeSpace(board, index):
            l.append(index)
    if len(l)>0:
        return random.choice(l)
        
    #step 4
    
    if isFreeSpace(board, 4):
        return 4
    
    avb=getAvailablePositions(board)
    return getPositionPlayer(random.choice(avb))
    
           
    
    
    

def getWinner(board):
    '''
        Checks out if we have a winner.
        If the winner exists return his token.
    '''
    for index in range(3):
        if board[index][0]== board[index][1] and board[index][1]==board[index][2] and board[index][1]!=' ':
            return board[index][1]
        if board[0][index]==board[1][index] and board[1][index]==board[2][index] and board[1][index]!=' ':
            return board[0][index]
    
    if board[0][2]== board[1][1] and board[1][1]==board[2][0] and board[1][1]!=' ':
        return board[0][2]
       
    if board[0][0]== board[1][1] and board[1][1]==board[2][2] and board[1][1]!=' ':
        return board[0][0]

             
                
  