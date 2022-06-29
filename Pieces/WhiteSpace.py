class WhiteSpace:
    def __init__(self, rank, file):
        self.alpha = 0
        self.rank = rank
        self.file = file
    def get_rank(self):
        return self.rank
    def get_file(self):
        return self.file
    def get_color(self):
        return None
    def get_alpha(self):
        return self.alpha
    def set_alpha(self, alpha):
        self.alpha = alpha