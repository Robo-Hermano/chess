import pygame

def create_chess_position_board():
  chessBoard = []
  for i in range(8, 0):
    for j in range(1, 9):
      chessBoard.append((j, i))
  return chessBoard

chessBoard = create_chess_position_board()
letterToNumber = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
numberToLetter = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}

class Piece:
  def get_captured(self):
    self.position = (-1,-1)

class Pawn(Piece):
  def __init__(self, position):
    self.val = 1
    self.position = position

  def movement(self, position):
    pass #slightly more complicated

  def capture(self, position):
    pass
    
  def en_passant(self, position):
    pass
    
class Knight(Piece):
  def __init__(self, position):
    self.val = 3
    self.position = position 

  def movement(self, position):
    if abs(position[0] - self.position[0]) == 2 and abs(position[1] - self.position[1]) == 1 or abs(position[1] - self.position[1]) == 2 and abs(position[0] - self.position[0]) == 1:
      self.position = position
    
class Bishop(Piece):
  def __init__(self, position):
    self.val = 3
    self.position = position

  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]):
      self.position = position

class Rook(Piece):
  def __init__(self, position):
    self.val = 5
    self.position = position

  def movement(self, position):
    if position[0] == self.position[0] or position[1] == self.position[1]:
      self.position = position

class Queen(Piece):
  def __init__(self, position):
    self.val = 9
    self.position = position

  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]) or position[0] == self.position[0] or position[1] == self.position[1]:
      self.position = position
      
class King(Piece):
  def __init__(self, position):
    self.val = 0
    self.position = position

  def movement(self, position):
    if abs(self.position[0] - position[0]) <= 1 and abs(self.position[1] - position[1]) <= 1 and self.check_for_checks(position) == True:
      self.position = position
  
  def check_for_checks(self, position):
    pass

  def castling(self, position):
    pass

def game_loop():
  pygame.init()
  pygame.display.set_caption("2 player chess, stockfish coming soon")
  screen = pygame.display.set_mode((640, 640))
  BLACK = (0,0,0)
  WHITE = (255, 255, 255)
  loop = True
  while loop:
    squareIsWhite = 1 #if 1, paint square white; if -1, paint square black
    pygame.time.Clock.tick(10)
    for i in range(0, 641, 80):
      for j in range(0, 641, 80):
        if squareIsWhite == 1:
          pygame.draw.rect(screen, WHITE, (j, i, 80, 80))
        else:
          pygame.draw.rect(screen, BLACK, (j, i, 80, 80))
        squareIsWhite /= -1 #so value switches every time between white square and black square
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        loop = False
    pygame.display.update()
  pygame.quit()
game_loop()
