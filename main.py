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
    
  def print_on_board(self):
    pass
    
  def get_position(self):
    return self.position

class Pawn(Piece):
  def __init__(self, position, image):
    self.val = 1
    self.position = position
    self.image = image

  def movement(self, position):
    pass #slightly more complicated

  def capture(self, position):
    pass
    
  def en_passant(self, position):
    pass
    
class Knight(Piece):
  def __init__(self, position, image):
    self.val = 3
    self.position = position 
    self.image = image

  def movement(self, position):
    if abs(position[0] - self.position[0]) == 2 and abs(position[1] - self.position[1]) == 1 or abs(position[1] - self.position[1]) == 2 and abs(position[0] - self.position[0]) == 1:
      self.position = position
    
class Bishop(Piece):
  def __init__(self, position, image):
    self.val = 3
    self.position = position
    self.image = image

  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]):
      self.position = position

class Rook(Piece):
  def __init__(self, position, image):
    self.val = 5
    self.position = position
    self.image = image

  def movement(self, position):
    if position[0] == self.position[0] or position[1] == self.position[1]:
      self.position = position

class Queen(Piece):
  def __init__(self, position, image):
    self.val = 9
    self.position = position
    self.image = image

  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]) or position[0] == self.position[0] or position[1] == self.position[1]:
      self.position = position
      
class King(Piece):
  def __init__(self, position, image):
    self.val = 0
    self.position = position
    self.image = image

  def movement(self, position):
    if abs(self.position[0] - position[0]) <= 1 and abs(self.position[1] - position[1]) <= 1 and self.check_for_checks(position) == True:
      self.position = position
  
  def check_for_checks(self, position):
    pass

  def castling(self, position):
    pass

pawnImgWhite = pygame.image.load("white_pawn.png")
pawnImgBlack = pygame.image.load("black_pawn.png")
rookImgWhite = pygame.image.load("white_rook.png")
rookImgBlack = pygame.image.load("black_rook.png")
knightImgWhite = pygame.image.load("white_knight.png")
knightImgBlack = pygame.image.load("black_knight.png")
bishopImgWhite = pygame.image.load("white_bishop.png")
bishopImgBlack = pygame.image.load("black_bishop.png")
queenImgWhite = pygame.image.load("white_queen.png")
queenImgBlack = pygame.image.load("black_queen.png")
kingImgWhite = pygame.image.load("white_king.png")
kingImgBlack = pygame.image.load("black_king.png")

WhitePawnOne = Pawn((1,7),"white_pawn.png")
WhitePawnTwo = Pawn((2,7),"white_pawn.png")
WhitePawnThree = Pawn((3,7),"white_pawn.png")
WhitePawnFour = Pawn((4,7),"white_pawn.png")
WhitePawnFive = Pawn((5,7),"white_pawn.png")
WhitePawnSix = Pawn((6,7),"white_pawn.png")
WhitePawnSeven = Pawn((7,7),"white_pawn.png")
WhitePawnEight = Pawn((8,7),"white_pawn.png")
WhiteRookOne = Rook((1,8), "white_rook.png")
WhiteRookTwo = Rook((8,8), "white_rook.png")
WhiteKnightOne = Knight((2,8), "white_knight.png")
WhiteKnightTwo = Knight((7,8), "white_knight.png")
WhiteBishopOne = Bishop((3,8), "white_bishop.png")
WhiteBishopTwo = Bishop((6,8), "white_bishop.png")
WhiteQueen = Queen((4,8), "white_queen.png")
WhiteKing = King((5,8), "white_king.png")

BlackPawnOne = Pawn((1,2),"black_pawn.png")
BlackPawnTwo = Pawn((2,2),"black_pawn.png")
BlackPawnThree = Pawn((3,2),"black_pawn.png")
BlackPawnFour = Pawn((4,2),"black_pawn.png")
BlackPawnFive = Pawn((5,2),"black_pawn.png")
BlackPawnSix = Pawn((6,2),"black_pawn.png")
BlackPawnSeven = Pawn((7,2),"black_pawn.png")
BlackPawnEight = Pawn((8,2),"black_pawn.png")
BlackRookOne = Rook((1,1), "black_rook.png")
BlackRookTwo = Rook((8,1), "black_rook.png")
BlackKnightOne = Knight((2,1), "black_knight.png")
BlackKnightTwo = Knight((7,1), "black_knight.png")
BlackBishopOne = Bishop((3,1), "black_bishop.png")
BlackBishopTwo = Bishop((6,1), "black_bishop.png")
BlackQueen = Queen((4,1), "black_queen.png")
BlackKing = King((5,1), "black_king.png")



def game_loop():
  pygame.init()
  pygame.display.set_caption("2 player chess, stockfish coming soon")
  screen = pygame.display.set_mode((640, 640))
  BLACK = (0,0,0)
  WHITE = (255, 255, 255)
  loop = True
  while loop:
    squareIsWhite = 1 #if 1, paint square white; if -1, paint square black
    pygame.time.Clock().tick(10)
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
