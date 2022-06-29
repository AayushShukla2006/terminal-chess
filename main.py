from Board.board import *

if __name__ == "__main__":
    chess_board = ChessBoard()
    while True:
        print(chess_board.get_board())
        print("Enter the current position: ", end="")
        cur_pos = input().split(",")
        print("Enter the destination position: ", end="")
        to_pos = input().split(",")
        print()

        chess_board.make_move((int(cur_pos[0]) - 1, int(cur_pos[1]) - 1), (int(to_pos[0]) - 1, int(to_pos[1]) - 1))
        chess_board.show_board()