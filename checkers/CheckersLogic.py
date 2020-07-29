import numpy as np

DEFAULT_WIDTH = 8
DEFAULT_LENGTH = 8
np_pieces = 12


class board():
    """
    Checkers Board.
    """

    def __init__(self):
        # Odd nums are player 1, even nums are player 2
        board = np.array([ 
              [0, 1, 0, 3, 0, 5, 0, 7],
              [9, 0, 11, 0, 13, 0, 15, 0],
              [0, 17, 0, 19, 0, 21, 23],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [2, 0, 4, 0, 6, 0, 8, 0],
              [0, 10, 0, 12, 0, 14, 0, 16],
              [18, 0, 20, 0, 22, 0, 24, 0]])

    def move_stone(self, player, direction, piece):
        "Create copy of board containing moves stone."
        pass

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
