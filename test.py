import Pieces.Knight as Knight
import Pieces.Pawn as Pawn

pawn = Pawn.Pawn("black", 1, 1)
print(pawn.legal_moves())
pawn.move(2,1)
print(pawn.legal_moves())

knight = Knight.Knight("black", 1, 1)
print(knight.legal_moves())
knight.move(3,4)
print(knight.legal_moves())