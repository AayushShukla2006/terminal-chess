import Pieces.piece as piece

class Bishop(piece.Piece):
    def __init__(self, color, rank, file):
        super().__init__(color, rank, file)
        self.alpha = "b"