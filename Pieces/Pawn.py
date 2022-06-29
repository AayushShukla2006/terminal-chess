import Pieces.piece as piece

class Pawn(piece.Piece):
    def __init__(self, color, rank, file):
        super().__init__(color, rank, file)
        self.alpha = "p"
    
    def legal_moves(self):
        self.legal_moves_list = []
        if self.color == "black":
            if self.get_moved() == False:
                self.legal_moves_list.append((self.get_rank() + 1, self.get_file())) if self.get_rank() + 1 <= 8 else None
                self.legal_moves_list.append((self.get_rank() + 2, self.get_file())) if self.get_rank() + 2 <= 8 else None
                return self.legal_moves_list
            else:
                self.legal_moves_list.append((self.get_rank() + 1, self.get_file())) if self.get_rank() + 1 <= 8 else None
                return self.legal_moves_list
        else:
            if self.get_moved() == False:
                self.legal_moves_list.append((self.get_rank() - 1, self.get_file())) if self.get_rank() - 1 >= 1 else None
                self.legal_moves_list.append((self.get_rank() - 2, self.get_file())) if self.get_rank() - 2 >= 1 else None
                return self.legal_moves_list
            else:
                self.legal_moves_list.append((self.get_rank() - 1, self.get_file())) if self.get_rank() - 1 >= 1 else None
                return self.legal_moves_list