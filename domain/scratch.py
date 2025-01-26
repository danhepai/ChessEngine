from board import Board

b = Board()
b.init_pieces()
print(b.white_R_bb.tobytes())
