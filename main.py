def create_chess_position_board():
  chessBoard = []
  for i in range(8, 0):
    for j in range(1, 9):
      chessBoard.append((j, i))
  return chessBoard

chessBoard = create_chess_position_board()

class Piece:
  def __init__(self):
    pass

class Pawn(Piece):
  def __init__(self):
    self.val = 1
    
class Knight(Piece):

class Bishop(Piece):
  
