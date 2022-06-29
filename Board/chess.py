from Pieces import Pawn, Rook, Knight, Bishop, Queen, King, WhiteSpace
import Board.chess as chess

white_pieces = ["R", "N", "B", "Q", "K", "P"]
black_pieces = ["r", "n", "b", "q", "k", "p"]
ranks = [1, 2, 3, 4, 5, 6, 7, 8]
files = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]

W_ROOK1 = Rook.Rook("white", 8, 1)
W_ROOK2 = Rook.Rook("white", 8, 8)
W_KNIGHT1 = Knight.Knight("white", 8, 2)
W_KNIGHT2 = Knight.Knight("white", 8, 7)
W_BISHOP1 = Bishop.Bishop("white", 8, 3)
W_BISHOP2 = Bishop.Bishop("white", 8, 6)
W_QUEEN = Queen.Queen("white", 8, 4)
W_KING = King.King("white", 8, 5)
W_PAWN1 = Pawn.Pawn("white", 7, 1)
W_PAWN2 = Pawn.Pawn("white", 7, 2)
W_PAWN3 = Pawn.Pawn("white", 7, 3)
W_PAWN4 = Pawn.Pawn("white", 7, 4)
W_PAWN5 = Pawn.Pawn("white", 7, 5)
W_PAWN6 = Pawn.Pawn("white", 7, 6)
W_PAWN7 = Pawn.Pawn("white", 7, 7)
W_PAWN8 = Pawn.Pawn("white", 7, 8)

B_ROOK1 = Rook.Rook("black", 1, 1)
B_ROOK2 = Rook.Rook("black", 1, 8)
B_KNIGHT1 = Knight.Knight("black", 1, 2)
B_KNIGHT2 = Knight.Knight("black", 1, 7)
B_BISHOP1 = Bishop.Bishop("black", 1, 3)
B_BISHOP2 = Bishop.Bishop("black", 1, 6)
B_QUEEN = Queen.Queen("black", 1, 4)
B_KING = King.King("black", 1, 5)
B_PAWN1 = Pawn.Pawn("black", 2, 1)
B_PAWN2 = Pawn.Pawn("black", 2, 2)
B_PAWN3 = Pawn.Pawn("black", 2, 3)
B_PAWN4 = Pawn.Pawn("black", 2, 4)
B_PAWN5 = Pawn.Pawn("black", 2, 5)
B_PAWN6 = Pawn.Pawn("black", 2, 6)
B_PAWN7 = Pawn.Pawn("black", 2, 7)
B_PAWN8 = Pawn.Pawn("black", 2, 8)

board = [
            [B_ROOK1, B_KNIGHT1, B_BISHOP1, B_QUEEN, B_KING, B_BISHOP2, B_KNIGHT2, B_ROOK2],
            [B_PAWN1, B_PAWN2, B_PAWN3, B_PAWN4, B_PAWN5, B_PAWN6, B_PAWN7, B_PAWN8],
            [WhiteSpace.WhiteSpace(3, 1), WhiteSpace.WhiteSpace(3, 2), WhiteSpace.WhiteSpace(3, 3), WhiteSpace.WhiteSpace(3, 4), WhiteSpace.WhiteSpace(3, 5), WhiteSpace.WhiteSpace(3, 6), WhiteSpace.WhiteSpace(3, 7), WhiteSpace.WhiteSpace(3, 8)],
            [WhiteSpace.WhiteSpace(4, 1), WhiteSpace.WhiteSpace(4, 2), WhiteSpace.WhiteSpace(4, 3), WhiteSpace.WhiteSpace(4, 4), WhiteSpace.WhiteSpace(4, 5), WhiteSpace.WhiteSpace(4, 6), WhiteSpace.WhiteSpace(4, 7), WhiteSpace.WhiteSpace(4, 8)],
            [WhiteSpace.WhiteSpace(5, 1), WhiteSpace.WhiteSpace(5, 2), WhiteSpace.WhiteSpace(5, 3), WhiteSpace.WhiteSpace(5, 4), WhiteSpace.WhiteSpace(5, 5), WhiteSpace.WhiteSpace(5, 6), WhiteSpace.WhiteSpace(5, 7), WhiteSpace.WhiteSpace(5, 8)],
            [WhiteSpace.WhiteSpace(6, 1), WhiteSpace.WhiteSpace(6, 2), WhiteSpace.WhiteSpace(6, 3), WhiteSpace.WhiteSpace(6, 4), WhiteSpace.WhiteSpace(6, 5), WhiteSpace.WhiteSpace(6, 6), WhiteSpace.WhiteSpace(6, 7), WhiteSpace.WhiteSpace(6, 8)],
            [W_PAWN1, W_PAWN2, W_PAWN3, W_PAWN4, W_PAWN5, W_PAWN6, W_PAWN7, W_PAWN8],
            [W_ROOK1, W_KNIGHT1, W_BISHOP1, W_QUEEN, W_KING, W_BISHOP2, W_KNIGHT2, W_ROOK2]
        ]

def print_board():
    current_loop_position = 0
        
    # print("\033[2J\033[H")

    print(" ", end="")
    for i in range(53):
        print("_", end="")
    print()
    
    for rank in chess.board:
        print("|  ", f"\033[34;1m{chess.ranks[current_loop_position]}\033[0m", end="  |  ", sep="")
        for piece in rank:
            if piece.get_alpha() == 0:
                print(" ", end="  |  ")
            else:
                if piece.get_color() == "white":
                    print(f"\033[31m{piece.get_alpha()}\033[0m", end="  |  ")
                elif piece.get_color() == "black":
                    print(f"\033[32m{piece.get_alpha()}\033[0m", end="  |  ")

        print(end="\n")
        for i in range(55):
            if i % 6 == 0:
                print("|", end="")
            else:
                print("-", end="")
        print()
            
        current_loop_position += 1
    
    print('|  ', end='')
    for pf in chess.files:
        print(f"\033[33;1m{pf}\033[0m", end='  |  ')
    print()

    for i in range(55):
            if i % 6 == 0:
                print("|", end="")
            else:
                print("_", end="")
    print()