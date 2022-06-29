import Board.chess as chess
from Pieces import King, Queen, Rook, Bishop, Knight, Pawn, WhiteSpace

class ChessBoard:
    def __init__(self):
        self.board = chess.board
        self.show_board()
        print(self.board)

    def show_board(self):
        chess.print_board()

    def get_board(self):
        return self.board

    def get_piece(self, pos):
        return self.board[int(pos[0]) - 1][int(pos[1]) - 1]

    def make_move(self, cur_pos, to_pos):

        # IMPORTANT : Representation of board indices is in the following manner: (file, rank)
        # Example: (1, 1) is the first square on the board, (2, 1) is the second square on the board, etc.

        if isinstance(self.board[cur_pos[0]][cur_pos[1]], WhiteSpace.WhiteSpace):
            print("There is no piece at this position.")
            return False
        else:
            print(self.get_piece(cur_pos))
            print(self.get_piece(to_pos))
            print((self.board[to_pos[0]][to_pos[1]].get_rank(), self.board[to_pos[0]][to_pos[1]].get_file()))
            print(self.board[cur_pos[0]][cur_pos[1]].legal_moves())
            
            # if self.board[to_pos[0]][to_pos[1]].get_color() == self.board[cur_pos[0]][cur_pos[1]].get_color():
            #     print("Invalid move. You cannot move a piece onto your own piece.")
            #     return False
            if (self.board[to_pos[0]][to_pos[1]].get_rank(), self.board[to_pos[0]][to_pos[1]].get_file()) in self.board[cur_pos[0]][cur_pos[1]].legal_moves():
                self.board[cur_pos[0]][cur_pos[1]].move(to_pos[0], to_pos[1])
                self.board[to_pos[0]][to_pos[1]] = self.board[cur_pos[0]][cur_pos[1]]
                self.board[cur_pos[0]][cur_pos[1]] = WhiteSpace.WhiteSpace(cur_pos[0], cur_pos[1])
                return True
            else:
                print("Invalid move.")
                return False
