import numpy as np
from bitboard_helpers import make_uint64, set_bit, clear_bit

class Board:
    """
    PIECES: R - ROOK, N - KNIGHT, B - BISHOP, Q - QUEEN, K - KING, P - PAW
    """

    def __init__(self):
        # White pieces group
        self.white_R_bb = make_uint64()
        self.white_N_bb = make_uint64()
        self.white_B_bb = make_uint64()
        self.white_Q_bb = make_uint64()
        self.white_K_bb = make_uint64()
        self.white_P_bb = make_uint64()

        # Black pieces group
        self.black_R_bb = make_uint64()
        self.black_N_bb = make_uint64()
        self.black_B_bb = make_uint64()
        self.black_Q_bb = make_uint64()
        self.black_K_bb = make_uint64()
        self.black_P_bb = make_uint64()

        self.init_pieces()

    # ----------------------------------
    # BOARD INTIALIZATION
    # --------------------------------

    def init_pieces(self):
        self._init_white_pieces()
        self._init_black_pieces()

    def _init_white_pieces(self):
        self.white_R_bb |= set_bit(self.white_R_bb, 0)
        self.white_N_bb |= set_bit(self.white_N_bb, 1)
        self.white_B_bb |= set_bit(self.white_B_bb, 2)
        self.white_Q_bb |= set_bit(self.white_Q_bb, 3)
        self.white_K_bb |= set_bit(self.white_K_bb, 4)
        self.white_B_bb |= set_bit(self.white_B_bb, 5)
        self.white_N_bb |= set_bit(self.white_N_bb, 6)
        self.white_R_bb |= set_bit(self.white_R_bb, 7)
        for i in range(8, 16):
            self.white_P_bb |= set_bit(self.white_P_bb, i)

    def _init_black_pieces(self):
        self.black_R_bb |= set_bit(self.black_R_bb, 56)
        self.black_N_bb |= set_bit(self.black_N_bb, 57)
        self.black_B_bb |= set_bit(self.black_B_bb, 58)
        self.black_Q_bb |= set_bit(self.black_Q_bb, 59)
        self.black_K_bb |= set_bit(self.black_K_bb, 60)
        self.black_B_bb |= set_bit(self.black_B_bb, 61)
        self.black_N_bb |= set_bit(self.black_N_bb, 62)
        self.black_R_bb |= set_bit(self.black_R_bb, 63)
        for i in range(48, 56):
            self.black_P_bb |= set_bit(self.black_P_bb, i)

