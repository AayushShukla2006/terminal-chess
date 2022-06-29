import Board.chess as chess
class Piece:
    def __init__(self, color, rank, file):
        self.moved = False
        self.color = color
        self.rank = rank
        self.file = file
    
    def get_color(self):
        return self.color
    
    def get_rank(self):
        return self.rank
    
    def get_file(self):
        return self.file
    
    def get_moved(self):
        return self.moved
    
    def set_moved(self, moved):
        self.moved = moved
    
    def get_alpha(self):
        if self.color == "white":
            return self.alpha.upper()
        else:
            return self.alpha.lower()
    
    def set_alpha(self, alpha):
        self.alpha = alpha
    
    def move(self, rank, file):
        self.board = chess.board
        if self.board[rank][file].get_color() == self.color:
            print("Invalid move. You cannot move a piece onto your own piece.")
            return False
        else:
            self.rank = rank
            self.file = file
            self.moved = True