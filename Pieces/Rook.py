import Pieces.piece as piece

class Rook(piece.Piece):
    def __init__(self, color, rank, file):
        super().__init__(color, rank, file)
        self.alpha = "r"