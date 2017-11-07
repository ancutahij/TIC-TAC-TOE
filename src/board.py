'''
Created on Nov 4, 2017

@author: Ancuta
'''
def setBoard():
    """
        We return a start board which is empty (it contains only elements egual with ' ' ).
    """   
    board=[]
    board.append([' ',' ',' '])
    board.append([' ',' ',' '])
    board.append([' ',' ',' '])
    return board


def getAvailablePositions(board):
    '''
        Create a list with all available positions in the board. 
        If an element is equal to ' ' that means we have an available position. Otherwise the position is taken.
        e.g
        board=[['x',' ','o'], [' ','x','x'], ['o','o','o']]
        
        We should have :
        
        avb=[[0,1],[1,0]]
    '''
    
    avb=[]
    for index1,list in enumerate(board):
        for index2,item in enumerate(list):
            if item ==' ' :
                avb.append([index1,index2])
    return avb


def isBoardFull(board):
    '''
        Return true if the board is full, otherwise return false if there are still available positions.
    
    '''
    if  getAvailablePositions(board)==[]:
        return True
    else:
        return False
    
    
def getPositionBoard(position):
    '''
        From an user's position (e.g 1, 2 ,3 ,4), we get the real position on the board (0==[0,0], 1==[0,1]....)
        
    '''
    if position is 0:
        return [0,0]
    elif position is 1:
        return [0,1]
    elif position is 2:
        return [0,2]
    elif position is 3:
        return [1,0]
    elif position is 4:
        return [1,1]
    elif position is 5:
        return [1,2]
    elif position is 6:
        return [2,0]
    elif position is 7:
        return [2,1]
    else:
        return [2,2]
 

def getPositionPlayer(position):
    '''
        This time position is a list that contains an available position in board (for exemple [0,2])
        Returns the positions for the player ([0,2]==3)
        DE STERS!!!!
    '''   
    if position == [0,0]:
        return 1
    elif position == [0,1]:
        return 2
    elif position == [0,2]:
        return 3
    elif position == [1,0]:
        return 4
    elif position == [1,1]:
        return 5
    elif position == [1,2]:
        return 6
    elif position == [2,0]:
        return 7
    elif position == [2,1]:
        return 8
    else:
        return 9
    
    
    
def setToken(board, token, position):
    '''
        Sets a token in an available position.
        Positions on the board:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
        
        Elements on the current board:
        
        
        x | o | 
        ---------
        x |   |  
        ---------
        o | x | 
        
        It's the player's with the token o turn.
        We want to append  an 'o' in position 3.
        Now the current board is:
        
        x | o | o
        ---------
        x |   |  
        ---------
        o | x |  
        
         
          ''' 
    if type(position) == int: 
        
        pos=getPositionBoard(position)
    else:
        pos=position 
        
    board[pos[0]][pos[1]]=token
    return board


def test_setToken():
    board=[['x',' ',' '], [' ','x','x'], ['o','o','o']]
    token='x'
    position=2
    assert setToken(board, token, position)==[['x',' ','x'], [' ','x','x'], ['o','o','o']]
    
def test_getAvailablePositions():
    '''
        test for getAvailablePositions.
    '''
    board=[['x',' ','o'], [' ','x','x'], ['o','o','o']]
    assert getAvailablePositions(board)==[[0,1],[1,0]]
 

test_setToken() 
test_getAvailablePositions()
                