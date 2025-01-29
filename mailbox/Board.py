from Piece import Piece

class Board:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        board = [[Piece.OUTSIDE] * 12 for _ in range(12)]

        for i in range(2, 10):
            for j in range(2, 10):
                board[i][j] = Piece.EMPTY

        for i in range(2, 10):
            board[8][i] = Piece.wP
            board[3][i] = Piece.bP

        board[9] = [Piece.OUTSIDE, Piece.OUTSIDE, Piece.wR, Piece.wN, Piece.wB, Piece.wQ, Piece.wK, Piece.wB, Piece.wN, Piece.wR, Piece.OUTSIDE, Piece.OUTSIDE]
        board[2] = [Piece.OUTSIDE, Piece.OUTSIDE, Piece.bR, Piece.bN, Piece.bB, Piece.bQ, Piece.bK, Piece.bB, Piece.bN, Piece.bR, Piece.OUTSIDE, Piece.OUTSIDE]

        return board

    def pretty_print_board(self):
        for i in range(2, 10):
            for j in range(2, 10):
                print(Piece.pretty_pieces[self.board[i][j]], end=' ')
            print()



