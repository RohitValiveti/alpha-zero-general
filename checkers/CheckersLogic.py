import numpy as np

DEFAULT_WIDTH = 8
DEFAULT_LENGTH = 8
np_pieces = 12

WinState = namedtuple('WinState', 'is_ended winner')

class board():
    """
    Checkers Board.
    """

    def __init__(self):
        # Odd nums are player 1, even nums are player 2
        self.board = np.array([ 
              [0, 1, 0, 3, 0, 5, 0, 7],
              [9, 0, 11, 0, 13, 0, 15, 0],
              [0, 17, 0, 19, 0, 21, 23],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [2, 0, 4, 0, 6, 0, 8, 0],
              [0, 10, 0, 12, 0, 14, 0, 16],
              [18, 0, 20, 0, 22, 0, 24, 0]])


    def move_stone(self, player, r, c, piece):
        # r,c = the location that player wants to move their piece
        # piece = the literal number that is being moved
        # player = 1 or 2
        "Create copy of board containing moved stone."
        newBoard = self.board
        newBoard[r][c] = piece
        for rp in newBoard:
            for cp in rp:
                if newBoard[rp][rc] == piece:
                    break
        
        newBoard[rp][rc] = 0
        self.board = newBoard

        # Errors

        if board[r][c] != 0 or (c != cp+1 and c != cp-1):
            raise ValueError("Can't move piece to %s , %s" % (r,c))

        if player == 1:
            if r != rp+1:
                raise ValueError("Can't move piece to %s , %s" % (r,c))

        if player == 2:
            if r != rp-1:
                raise ValueError("Can't move piece to %s , %s" % (r,c))
        


    def get_valid_moves(self, piece):
        for r in board:
            for c in r:
                if board[r][c] == piece:
                    break
                break
            break
        
        if (piece%2 ==0):
            if(board[r+1][c-1] == 0 or board[r+1][c+1] == 0):
                return True
        else:
            if(board[r-1][c-1] == 0 or board[r-1][c+1] == 0):
                return True
        return False


    def get_win_state(self):
        winOdd = True
        winEven = True
        for r in board:
            for c in r:
                if board[r][c] % 2 == 0 and board[r][c] != 0:
                    winEven = False
                if board[r][c] % 2 == 1:
                    winOdd = False
        winner = False
        if winOdd:
            winner = winOdd
        if winEven:
            winner = winEven
        return WinState(winner, player)
