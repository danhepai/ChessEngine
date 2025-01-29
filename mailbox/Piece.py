class Piece:
    EMPTY = 0
    OUTSIDE = 99

    wP = 1
    wR = 2
    wN = 3
    wB = 4
    wQ = 5
    wK = 6

    bP = 7
    bR = 8
    bN = 9
    bB = 10
    bQ = 11
    bK = 12

    white_pieces = {wP, wR, wN, wB, wQ, wK}
    black_pieces = {bP, bR, bN, bB, bQ, bK}

    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"

    pretty_pieces = {
        OUTSIDE: "X",
        EMPTY: "_",
        wP: "♙",
        bP: "♟︎",
        wR: "♖",
        bR: "♜",
        wN: "♘",
        bN: "♞",
        wB: "♗",
        bB: "♝",
        wQ: "♕",
        bQ: "♛",
        wK: "♔",
        bK: "♚",
    }
