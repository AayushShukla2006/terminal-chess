import Pieces.piece as piece
from Pieces import WhiteSpace, King, Queen, Rook, Bishop, Knight, Pawn

class Knight(piece.Piece):
    def __init__(self, color, rank, file):
        super().__init__(color, rank, file)
        self.alpha = "n"
    
    def legal_moves(self):
        self.legal_moves_list = []
        if self.color == "black":
            self.legal_moves_list.append((self.get_rank() + 1, self.get_file() + 2)) if self.get_rank() + 1 <= 8 and self.get_file() + 2 <= 8 else None
            self.legal_moves_list.append((self.get_rank() + 1, self.get_file() - 2)) if self.get_rank() + 1 <= 8 and self.get_file() - 2 >= 1 else None
            self.legal_moves_list.append((self.get_rank() - 1, self.get_file() + 2)) if self.get_rank() - 1 >= 1 and self.get_file() + 2 <= 8 else None
            self.legal_moves_list.append((self.get_rank() - 1, self.get_file() - 2)) if self.get_rank() - 1 >= 1 and self.get_file() - 2 >= 1 else None
            self.legal_moves_list.append((self.get_rank() + 2, self.get_file() + 1)) if self.get_rank() + 2 <= 8 and self.get_file() + 1 <= 8 else None
            self.legal_moves_list.append((self.get_rank() + 2, self.get_file() - 1)) if self.get_rank() + 2 <= 8 and self.get_file() - 1 >= 1 else None
            self.legal_moves_list.append((self.get_rank() - 2, self.get_file() + 1)) if self.get_rank() - 2 >= 1 and self.get_file() + 1 <= 8 else None
            self.legal_moves_list.append((self.get_rank() - 2, self.get_file() - 1)) if self.get_rank() - 2 >= 1 and self.get_file() - 1 >= 1 else None
            return self.legal_moves_list
        else:
            self.legal_moves_list.append((self.get_rank() + 1, self.get_file() + 2)) if self.get_rank() + 1 <= 8 and self.get_file() + 2 <= 8 else None
            self.legal_moves_list.append((self.get_rank() + 1, self.get_file() - 2)) if self.get_rank() + 1 <= 8 and self.get_file() - 2 >= 1 else None
            self.legal_moves_list.append((self.get_rank() - 1, self.get_file() + 2)) if self.get_rank() - 1 >= 1 and self.get_file() + 2 <= 8 else None
            self.legal_moves_list.append((self.get_rank() - 1, self.get_file() - 2)) if self.get_rank() - 1 >= 1 and self.get_file() - 2 >= 1 else None
            self.legal_moves_list.append((self.get_rank() + 2, self.get_file() + 1)) if self.get_rank() + 2 <= 8 and self.get_file() + 1 <= 8 else None
            self.legal_moves_list.append((self.get_rank() + 2, self.get_file() - 1)) if self.get_rank() + 2 <= 8 and self.get_file() - 1 >= 1 else None
            self.legal_moves_list.append((self.get_rank() - 2, self.get_file() + 1)) if self.get_rank() - 2 >= 1 and self.get_file() + 1 <= 8 else None
            self.legal_moves_list.append((self.get_rank() - 2, self.get_file() - 1)) if self.get_rank() - 2 >= 1 and self.get_file() - 1 >= 1 else None
            return self.legal_moves_list