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
    
  def get_position(self):
    return self.position

class Pawn(Piece):
  def __init__(self, position, image):
    self.val = 1
    self.position = position
    self.image = pygame.transform.scale(image,(80, 80))

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
    self.image = pygame.transform.scale(image, (80, 80))

  def movement(self, position):
    if abs(position[0] - self.position[0]) == 2 and abs(position[1] - self.position[1]) == 1 or abs(position[1] - self.position[1]) == 2 and abs(position[0] - self.position[0]) == 1:
      self.position = position
    
class Bishop(Piece):
  def __init__(self, position, image):
    self.val = 3
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))
    
  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]):
      self.position = position

class Rook(Piece):
  def __init__(self, position, image):
    self.val = 5
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))

  def movement(self, position):
    if position[0] == self.position[0] or position[1] == self.position[1]:
      self.position = position

class Queen(Piece):
  def __init__(self, position, image):
    self.val = 9
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))

  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]) or position[0] == self.position[0] or position[1] == self.position[1]:
      self.position = position
      
class King(Piece):
  def __init__(self, position, image):
    self.val = 0
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))

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

WhitePawnOne = Pawn((1,7),pawnImgWhite)
WhitePawnTwo = Pawn((2,7),pawnImgWhite)
WhitePawnThree = Pawn((3,7),pawnImgWhite)
WhitePawnFour = Pawn((4,7),pawnImgWhite)
WhitePawnFive = Pawn((5,7),pawnImgWhite)
WhitePawnSix = Pawn((6,7),pawnImgWhite)
WhitePawnSeven = Pawn((7,7),pawnImgWhite)
WhitePawnEight = Pawn((8,7),pawnImgWhite)
WhiteRookOne = Rook((1,8), rookImgWhite)
WhiteRookTwo = Rook((8,8), rookImgWhite)
WhiteKnightOne = Knight((2,8),knightImgWhite)
WhiteKnightTwo = Knight((7,8),knightImgWhite)
WhiteBishopOne = Bishop((3,8), bishopImgWhite)
WhiteBishopTwo = Bishop((6,8), bishopImgWhite)
WhiteQueen = Queen((4,8), queenImgWhite)
WhiteKing = King((5,8), kingImgWhite)

BlackPawnOne = Pawn((1,2),pawnImgBlack)
BlackPawnTwo = Pawn((2,2),pawnImgBlack)
BlackPawnThree = Pawn((3,2),pawnImgBlack)
BlackPawnFour = Pawn((4,2),pawnImgBlack)
BlackPawnFive = Pawn((5,2),pawnImgBlack)
BlackPawnSix = Pawn((6,2),pawnImgBlack)
BlackPawnSeven = Pawn((7,2),pawnImgBlack)
BlackPawnEight = Pawn((8,2),pawnImgBlack)
BlackRookOne = Rook((1,1),rookImgBlack)
BlackRookTwo = Rook((8,1),rookImgBlack)
BlackKnightOne = Knight((2,1),knightImgBlack)
BlackKnightTwo = Knight((7,1),knightImgBlack)
BlackBishopOne = Bishop((3,1),bishopImgBlack)
BlackBishopTwo = Bishop((6,1),bishopImgBlack)
BlackQueen = Queen((4,1),queenImgBlack)
BlackKing = King((5,1),kingImgBlack)

WhitePromotionOne = None
WhitePromotionTwo = None
BlackPromotionOne = None
BlackPromotionTwo = None

pieceList = [WhitePawnOne, WhitePawnTwo, WhitePawnThree, WhitePawnFour, WhitePawnFive, WhitePawnSix, WhitePawnSeven, WhitePawnEight, 
             WhiteRookOne, WhiteRookTwo, WhiteKnightOne, WhiteKnightTwo, WhiteBishopOne, WhiteBishopTwo, WhiteQueen, WhiteKing,
             BlackPawnOne, BlackPawnTwo, BlackPawnThree, BlackPawnFour, BlackPawnFive, BlackPawnSix, BlackPawnSeven, BlackPawnEight,
             BlackRookOne, BlackRookTwo, BlackKnightOne, BlackKnightTwo, BlackBishopOne, BlackBishopTwo, BlackQueen, BlackKing
            ]

def print_positions(pieceList, screen):
  for piece in pieceList:
    position = piece.get_position()
    screen.blit(piece.image, ((position[0]-1)*80, (position[1]-1)*80))

def game_loop(pieceList):
  pygame.init()
  pygame.display.set_caption("2 player chess, stockfish coming soon")
  screen = pygame.display.set_mode((640, 640))
  BROWN = (137, 81, 41)
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
          pygame.draw.rect(screen, BROWN, (j, i, 80, 80))
        squareIsWhite /= -1 #so value switches every time between white square and black square
    print_positions(pieceList, screen)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        loop = False
    pygame.display.update()
  pygame.quit()
game_loop(pieceList)
