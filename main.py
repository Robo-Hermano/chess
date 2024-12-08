import pygame

class Piece:
  def get_captured(self):
    self.position = (-1,-1) #so that the piece won't get printed after getting captured
    
  def get_position(self):
    return self.position #for printing position on board

  def get_colour(self):
    return self.colour #so that white player can't move black pieces and vice versa

class Pawn(Piece):
  def __init__(self, position, image, colour):
    self.val = 1
    self.position = position
    self.colour = colour
    self.image = pygame.transform.scale(image,(80, 80)) #so image can be printed on the gui

  def movement(self, position):
    pass #slightly more complicated

  def capture(self, position):
    pass
    
  def en_passant(self, position):
    pass
    
class Knight(Piece):
  def __init__(self, position, image, colour):
    self.val = 3
    self.colour = colour
    self.position = position 
    self.image = pygame.transform.scale(image, (80, 80))

  def movement(self, position):
    if abs(position[0] - self.position[0]) == 2 and abs(position[1] - self.position[1]) == 1 or abs(position[1] - self.position[1]) == 2 and abs(position[0] - self.position[0]) == 1:
      self.position = position
    else:
      raise ValueError()
    
class Bishop(Piece):
  def __init__(self, position, image, colour):
    self.val = 3
    self.colour = colour
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))
    
  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]):
      self.position = position
    else:
      raise ValueError()

class Rook(Piece):
  def __init__(self, position, image, colour):
    self.val = 5
    self.colour = colour
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))

  def movement(self, position):
    if position[0] == self.position[0] or position[1] == self.position[1]:
      self.position = position
    else:
      raise ValueError()

class Queen(Piece):
  def __init__(self, position, image, colour):
    self.val = 9
    self.colour = colour
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))

  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]) or position[0] == self.position[0] or position[1] == self.position[1]:
      self.position = position
    else:
      raise ValueError()
      
class King(Piece):
  def __init__(self, position, image, colour):
    self.val = 0
    self.colour =  colour
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))

  def movement(self, position):
    if abs(self.position[0] - position[0]) <= 1 and abs(self.position[1] - position[1]) <= 1 and self.check_for_checks(position) == True:
      self.position = position
    else:
      raise ValueError()
  
  def check_for_checks(self, position):
    pass

  def castling(self, position):
    pass

#adjusting images so that they can be loaded into pygame
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

#initialising every piece
WhitePawnOne = Pawn((1,7),pawnImgWhite, "white")
WhitePawnTwo = Pawn((2,7),pawnImgWhite, "white")
WhitePawnThree = Pawn((3,7),pawnImgWhite, "white")
WhitePawnFour = Pawn((4,7),pawnImgWhite, "white")
WhitePawnFive = Pawn((5,7),pawnImgWhite, "white")
WhitePawnSix = Pawn((6,7),pawnImgWhite, "white")
WhitePawnSeven = Pawn((7,7),pawnImgWhite, "white")
WhitePawnEight = Pawn((8,7),pawnImgWhite, "white")
WhiteRookOne = Rook((1,8), rookImgWhite, "white")
WhiteRookTwo = Rook((8,8), rookImgWhite, "white")
WhiteKnightOne = Knight((2,8),knightImgWhite, "white")
WhiteKnightTwo = Knight((7,8),knightImgWhite, "white")
WhiteBishopOne = Bishop((3,8), bishopImgWhite, "white")
WhiteBishopTwo = Bishop((6,8), bishopImgWhite, "white")
WhiteQueen = Queen((4,8), queenImgWhite, "white")
WhiteKing = King((5,8), kingImgWhite, "white")

BlackPawnOne = Pawn((1,2),pawnImgBlack, "black")
BlackPawnTwo = Pawn((2,2),pawnImgBlack, "black")
BlackPawnThree = Pawn((3,2),pawnImgBlack, "black")
BlackPawnFour = Pawn((4,2),pawnImgBlack, "black")
BlackPawnFive = Pawn((5,2),pawnImgBlack, "black")
BlackPawnSix = Pawn((6,2),pawnImgBlack, "black")
BlackPawnSeven = Pawn((7,2),pawnImgBlack, "black")
BlackPawnEight = Pawn((8,2),pawnImgBlack, "black")
BlackRookOne = Rook((1,1),rookImgBlack, "black")
BlackRookTwo = Rook((8,1),rookImgBlack, "black")
BlackKnightOne = Knight((2,1),knightImgBlack, "black")
BlackKnightTwo = Knight((7,1),knightImgBlack, "black")
BlackBishopOne = Bishop((3,1),bishopImgBlack, "black")
BlackBishopTwo = Bishop((6,1),bishopImgBlack, "black")
BlackQueen = Queen((4,1),queenImgBlack, "black")
BlackKing = King((5,1),kingImgBlack, "black")

#incase pawns promote
WhitePromotionOne = None
WhitePromotionTwo = None
BlackPromotionOne = None
BlackPromotionTwo = None

pieceList =[ WhitePawnOne, WhitePawnTwo, WhitePawnThree, WhitePawnFour, WhitePawnFive, WhitePawnSix, WhitePawnSeven, WhitePawnEight, 
             WhiteRookOne, WhiteRookTwo, WhiteKnightOne, WhiteKnightTwo, WhiteBishopOne, WhiteBishopTwo, WhiteQueen, WhiteKing,
             BlackPawnOne, BlackPawnTwo, BlackPawnThree, BlackPawnFour, BlackPawnFive, BlackPawnSix, BlackPawnSeven, BlackPawnEight,
             BlackRookOne, BlackRookTwo, BlackKnightOne, BlackKnightTwo, BlackBishopOne, BlackBishopTwo, BlackQueen, BlackKing
            ]

def print_positions(pieceList, screen):
  for piece in pieceList:
    position = piece.get_position()
    if position != (-1, -1):
      screen.blit(piece.image, ((position[0]-1)*80, (position[1]-1)*80))

def take_turn(turnColour, mousePosition, pieceChosen, pieceList):
  if turnColour == 1:
    turnColour = "white"
  else:
    turnColour = "black"
  chosenSquare = (mousePosition[0]//80*80, mousePosition[1]//80*80)
  for piece in pieceList:
    if piece.get_position() == chosenSquare and piece.get_colour() == turnColour:
      pieceChosen = piece
      return pieceChosen, pieceList
  try:    
    pieceChosen.movement(chosenSquare)
    for piece in pieceList:
      if piece.get_position() == chosenSquare and piece.get_colour() != turnColour:
        piece.get_captured()
    return None, pieceList
  except:
    return None, pieceList
  #debugging
  #bonus movement for pawns and kings

def game_loop(pieceList):
  pygame.init()
  pygame.display.set_caption("2 player chess, stockfish coming soon")
  screen = pygame.display.set_mode((640, 640))
  BROWN = (137, 81, 41)
  WHITE = (255, 255, 255)
  loop = True
  turnColour = 1
  pieceChosen = None
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
      elif event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        pieceChosen, pieceList = take_turn(turnColour, pos, pieceChosen, pieceList)
    pygame.display.update()
    turnColour /= -1
  pygame.quit()
game_loop(pieceList)
