import pygame

class Piece: #parent class, all pieces inherit from it
  def get_captured(self):
    self.position = (-1,-1) #so that the piece won't get printed after getting captured
    
  def get_position(self):
    return self.position #for printing position on board

  def get_colour(self):
    return self.colour #so that white player can't move black pieces and vice versa

  def get_image(self):
    return self.image #for printing image on board

  def get_piece_type(self):
    return self.pieceType #for more complex code such as castling
  
  def get_en_passant(self):
    return self.enPassant #for en passant calculations

class Pawn(Piece):
  val = 1
  
  def __init__(self, position, image, colour):
    self.position = position
    self.colour = colour
    self.image = pygame.transform.scale(image,(80, 80)) #so image can be printed on the gui
    self.hasMoved = False
    self.pieceType = "pawn"
    self.enPassant = False

  @classmethod #decorator to show this is class method and not instance
  def get_value(cls):
    return cls.val #for displaying material difference in chess, haven't implemented it yet

  def movement(self, position, lastMoveEnPassant):
    #check moving twice on first turn
    if position[0] - self.position[0] == 0 and not self.hasMoved and (self.position[1] - position[1] == -2 and self.get_colour() == "black"):
      for pos in ((position[0], position[1]),(position[0],position[1]-1)):
        for piece in pieceList:
          if piece.get_position() == pos:
            raise ValueError() #checking that no piece is blocking the square
      self.position = position
      self.hasMoved = True #makes sure it can't move two squares again
      self.enPassant = True #showing it to be eligible to en passant
    #same thing but for white pawns
    elif position[0] - self.position[0] == 0 and not self.hasMoved and (self.position[1] - position[1] == 2 and self.get_colour() == "white"):
      for pos in ((position[0], position[1]), (position[0],position[1]+1)):
        for piece in pieceList:
          if piece.get_position() == pos:
            raise ValueError()
      self.position = position
      self.hasMoved = True
      self.enPassant = True
    #moving one square forwards
    elif position[0] - self.position[0] == 0 and ((self.position[1] - position[1] == -1 and self.get_colour() == "black") or (self.position[1] - position[1] == 1 and self.get_colour() == "white")):
      for piece in pieceList:
        if piece.get_position() == position:
          raise ValueError("c")
      self.position = position
      self.hasMoved = True
      self.enPassant = False
    elif self.capture(position, lastMoveEnPassant) == True:
      self.position = position
      self.hasMoved = True
      self.enPassant = False
    else:
      raise ValueError() #means pawn can't move to chosen square

  def capture(self, position, lastMoveEnPassant):
    if self.en_passant(position, lastMoveEnPassant) == True:
      return True
    elif (self.get_colour() == "black" and abs(self.position[0] - position[0]) == 1 and self.position[1] - position[1] == -1) or (self.get_colour() == "white" and abs(self.position[0] - position[0]) == 1 and self.position[1] - position[1] == 1):
      for piece in pieceList:
        if piece.get_colour() != self.get_colour() and piece.get_position() == position:
          return True
      return False
    else:
      return False
        
    
  def en_passant(self, position, lastMoveEnPassant):
    if not lastMoveEnPassant:
      return False
    elif self.get_colour() == "black" and abs(self.position[0] - position[0]) == 1 and self.position[1] - position[1] == -1:
      for i in range(len(pieceList)):
        if pieceList[i].get_colour() != self.get_colour() and pieceList[i].get_position() == (position[0],position[1]-1) and pieceList[i].get_en_passant() == True:
          pieceList[i].get_captured()
          return True
    elif self.get_colour() == "white" and abs(self.position[0] - position[0]) == 1 and self.position[1] - position[1] == 1:
      for i in range(len(pieceList)):
        if pieceList[i].get_colour() != self.get_colour() and pieceList[i].get_position() == (position[0], position[1]+1) and pieceList[i].get_en_passant() == True:
          pieceList[i].get_captured()
          return True
    return False
class Knight(Piece):
  val = 3
  
  def __init__(self, position, image, colour):
    self.colour = colour
    self.position = position 
    self.image = pygame.transform.scale(image, (80, 80))
    self.hasMoved = None
    self.pieceType = "knight"
    self.enPassant = None

  @classmethod
  def get_value(cls):
    return cls.val

  def movement(self, position):
    if abs(position[0] - self.position[0]) == 2 and abs(position[1] - self.position[1]) == 1 or abs(position[1] - self.position[1]) == 2 and abs(position[0] - self.position[0]) == 1:
      self.position = position
    else:
      raise ValueError()
    
class Bishop(Piece):
  val = 3
  
  def __init__(self, position, image, colour):
    self.colour = colour
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))
    self.hasMoved = None
    self.enPassant = None
    self.pieceType = "bishop"

  @classmethod
  def get_value(cls):
    return cls.val

  def check_validity(self, position):
    if self.position[0] - position[0] == self.position[1] - position[1]:
      C = (position[0]-self.position[0])/abs(position[0]-self.position[0])
      for j in range(int(C), position[0]-self.position[0], int(C)):
        for piece in pieceList:
          if piece.get_position() == (self.position[0]+j,self.position[1]+j):
            raise ValueError()
    elif self.position[0] - position[0] < 0:
      for j in range(-1, position[1]-self.position[1], -1):
        for piece in pieceList:
          if piece.get_position() == (self.position[0]-j,self.position[1]+j):
            raise ValueError()
    else:
      for j in range(-1, position[0]-self.position[0], -1):
        for piece in pieceList:
          if piece.get_position() == (self.position[0]+j, self.position[1]-j):
            raise ValueError()
  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]):
      self.check_validity(position)
      self.position = position
    else:
      raise ValueError()

class Rook(Piece):
  val = 5
  
  def __init__(self, position, image, colour):
    self.colour = colour
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))
    self.hasMoved = False
    self.enPassant = None
    self.pieceType = "rook"

  @classmethod
  def get_value(cls):
    return cls.val

  def check_validity(self, originalPos, NewPos, index):
    C = (NewPos[index]-originalPos[index])/abs(NewPos[index]-originalPos[index])
    for i in range(int(C), NewPos[index]-originalPos[index], int(C)):
      if index == 0:
        pos = (originalPos[0] + i, originalPos[1])
      else:
        pos = (originalPos[0], originalPos[1] + i)
      for piece in pieceList:
        if piece.get_position() == pos:
          raise ValueError()

  def movement(self, position):
    if position[0] == self.position[0] or position[1] == self.position[1]:
      if position[0] != self.position[0]:
        self.check_validity(self.position, position, 0)
      else:
        self.check_validity(self.position, position, 1)
      self.position = position
      self.hasMoved = True
    else:
      raise ValueError()

class Queen(Piece):
  val = 9
  
  def __init__(self, position, image, colour):
    self.colour = colour
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))
    self.hasMoved = None
    self.pieceType = "queen"
    self.enPassant = None

  @classmethod
  def get_value(cls):
    return cls.val
  
  def check_validity_diagonal(self, position):
    if self.position[0] - position[0] == self.position[1] - position[1]:
      C = (position[0]-self.position[0])/abs(position[0]-self.position[0])
      for j in range(int(C), position[0]-self.position[0], int(C)):
        for piece in pieceList:
          if piece.get_position() == (self.position[0]+j,self.position[1]+j):
            raise ValueError()
    elif self.position[0] - position[0] < 0:
      for j in range(-1, position[1]-self.position[1], -1):
        for piece in pieceList:
          if piece.get_position() == (self.position[0]-j,self.position[1]+j):
            raise ValueError()
    else:
      for j in range(-1, position[0]-self.position[0], -1):
        for piece in pieceList:
          if piece.get_position() == (self.position[0]+j, self.position[1]-j):
            raise ValueError()
  
  def check_validity_lateral(self, originalPos, NewPos, index):
    C = (NewPos[index]-originalPos[index])/abs(NewPos[index]-originalPos[index])
    for i in range(int(C), NewPos[index]-originalPos[index], int(C)):
      if index == 0:
        pos = (originalPos[0] + i, originalPos[1])
      else:
        pos = (originalPos[0], originalPos[1] + i)
      for piece in pieceList:
        if piece.get_position() == pos:
          raise ValueError()

  def movement(self, position):
    if abs(position[0] - self.position[0]) == abs(position[1] - self.position[1]) or position[0] == self.position[0] or position[1] == self.position[1]:
      if abs(position[0]-self.position[0]) == abs(position[1]-self.position[1]):
        self.check_validity_diagonal(position)
      elif position[0] != self.position[0]:
        self.check_validity_lateral(self.position, position, 0)
      else:
        self.check_validity_lateral(self.position, position, 1)
      self.position = position
    else:
      raise ValueError()
      
class King(Piece):
  val = 0
  
  def __init__(self, position, image, colour):
    self.colour =  colour
    self.position = position
    self.image = pygame.transform.scale(image, (80, 80))
    self.hasMoved = False
    self.pieceType = "king"
    self.enPassant = None

  @classmethod
  def get_value(cls):
    return cls.val

  def movement(self, position):
    if abs(self.position[0] - position[0]) <= 1 and abs(self.position[1] - position[1]) <= 1 and self.check_for_checks(position) == True:
      self.position = position
      self.hasMoved = True
    elif self.castling(position) != False and self.check_for_checks(self.position) == True:
      self.position = position
      self.hasMoved = True
      for piece in pieceList:
        if piece.get_piece_type() == "rook" and position == (3,8) and piece.get_position() == (1,8):
          piece.position = (4,8)
        elif piece.get_piece_type() == "rook" and position == (7,8) and piece.get_position() == (8,8):
          piece.position = (6,8)
        elif piece.get_piece_type() == "rook" and position == (3,1) and piece.get_position() == (1,1):
          piece.position = (4,1)
        elif piece.get_piece_type() == "rook" and position == (7,1) and piece.get_position() == (8,1):
          piece.position = (6,1)
    else:
      raise ValueError()
  
  def check_for_checks(self, position): #for preventing illegal moves
    oldPos = self.position
    self.position = position
    #loop to check if any piece of other colour can reach king's current square
    for piece in pieceList:
      check = False
      if piece.get_colour() != self.get_colour() and piece.get_position() != (-1, -1):
        oldPosition = piece.get_position()
        kingPosition = position
        try:
          piece.movement(kingPosition)
          check = True
          raise KeyError()
        except:
          if check:
            piece.position = oldPosition
            self.position = oldPos
            return False
    self.position = oldPos
    return True

  def castling(self, position):
    if self.hasMoved:
      return False
    rookNotMoved = False
    if self.get_colour() == "white" and position == (7,8):
      if self.check_for_checks((7,8)) == False or self.check_for_checks((6,8)) == False:
        return False
      for i in ((7,8),(6,8)):
        for piece in pieceList:
          if piece.get_position() == i:
            return False
          elif piece.get_piece_type() == "rook" and piece.get_position() == (8,8) and piece.get_colour() == "white" and piece.hasMoved == False:
            rookNotMoved = True
    elif self.get_colour() == "white" and position == (3,8):
      if self.check_for_checks((3,8)) == False or self.check_for_checks((4,8)) == False:
        return False
      for i in ((4,8),(3,8),(2,8)):
        for piece in pieceList:
          if piece.get_position() == i:
            print(i, piece)
            return False
          elif piece.get_piece_type() == "rook" and piece.get_position() == (1,8) and piece.get_colour() == "white" and piece.hasMoved == False:
            rookNotMoved = True
    elif self.get_colour() == "black" and position == (7,1):
      if self.check_for_checks((7,1)) == False or self.check_for_checks((6,1)) == False:
        return False
      for i in ((7,1),(6,1)):
        for piece in pieceList:
          if piece.get_position() == i:
            return False
          elif piece.get_piece_type() == "rook" and piece.get_position() == (8,1) and piece.get_colour() == "black" and piece.hasMoved == False:
            rookNotMoved = True
    elif self.get_colour() == "black" and position == (3,1):
      if self.check_for_checks((3,1)) == False or self.check_for_checks((4,1)) == False:
        return False
      for i in ((4,1),(3,1), (2,1)):
        for piece in pieceList:
          if piece.get_position() == i:
            return False
          elif piece.get_piece_type() == "rook" and piece.get_position() == (1,1) and piece.get_colour() == "black" and piece.hasMoved == False:
            rookNotMoved = True
    else:
      return False
    if not rookNotMoved:
      return False
    return True
    
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

#for usage in promotions
images = [rookImgWhite, rookImgBlack, knightImgWhite, knightImgBlack, bishopImgWhite, bishopImgBlack, queenImgWhite, queenImgBlack]

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

#will loop through this list as it makes adjusting the pieces much easier
pieceList =[ WhitePawnOne, WhitePawnTwo, WhitePawnThree, WhitePawnFour, WhitePawnFive, WhitePawnSix, WhitePawnSeven, WhitePawnEight, 
             WhiteRookOne, WhiteRookTwo, WhiteKnightOne, WhiteKnightTwo, WhiteBishopOne, WhiteBishopTwo, WhiteQueen, WhiteKing,
             BlackPawnOne, BlackPawnTwo, BlackPawnThree, BlackPawnFour, BlackPawnFive, BlackPawnSix, BlackPawnSeven, BlackPawnEight,
             BlackRookOne, BlackRookTwo, BlackKnightOne, BlackKnightTwo, BlackBishopOne, BlackBishopTwo, BlackQueen, BlackKing
            ]

def promotion(piece, pieceList, pieceChosen, images):
  position = pieceChosen.get_position()
  for i in range(len(pieceList)):
    if pieceList[i] == pieceChosen:
      if piece == "queen" and pieceChosen.get_colour() == "white":
        pieceList[i] = Queen(colour = "white", position = position, image = images[6])
        return pieceList
      elif piece == "queen" and pieceChosen.get_colour() == "black":
        pieceList[i] = Queen(colour = "black", position = position, image = images[7])
        return pieceList
      elif piece == "rook" and pieceChosen.get_colour() == "white":
        pieceList[i] = Rook(colour = "white", position = position, image = images[0])
        return pieceList
      elif piece == "rook" and pieceChosen.get_colour() == "black":
        pieceList[i] = Rook(colour = "black", position = position, image = images[1])
        return pieceList
      elif piece == "bishop" and pieceChosen.get_colour() == "white":
        pieceList[i] = Bishop(colour = "white", position = position, image = images[4])
        return pieceList
      elif piece == "bishop" and pieceChosen.get_colour() == "black":
        pieceList[i] = Bishop(colour = "black", position = position, image = images[5])
        return pieceList
      elif piece == "knight" and pieceChosen.get_colour() == "white":
        pieceList[i] = Knight(colour = "white", position = position, image = images[2])
        return pieceList
      else:
        pieceList[i] = Knight(colour = "black", position = position, image = images[3])
        return pieceList

def print_positions(pieceList, screen):
  for piece in pieceList:
    position = piece.get_position()
    if position != (-1, -1):
      screen.blit(piece.get_image(), ((position[0]-1)*80, (position[1]-1)*80))

def take_turn(turnColour, mousePosition, pieceChosen, pieceList, images, lastMoveEnPassant):
  if turnColour == 1:
    turnColour = "white"
  else:
    turnColour = "black"
  colourToNumber = {"white":1, "black": -1}
  chosenSquare = (mousePosition[0]//80+1, mousePosition[1]//80+1)
  for piece in pieceList:
    if piece.get_position() == chosenSquare and piece.get_colour() == turnColour:
      pieceChosen = piece
      return pieceChosen, pieceList, colourToNumber[turnColour], lastMoveEnPassant
  try:
    oldPos = pieceChosen.get_position()
    if pieceChosen.get_piece_type() != "pawn":
      pieceChosen.movement(chosenSquare)
      lastMoveEnPassant = False
    else:
      pieceChosen.movement(chosenSquare, lastMoveEnPassant)
      if abs(chosenSquare[1] - oldPos[1]) == 2:
        lastMoveEnPassant = True
      else:
        lastMoveEnPassant = False 
    if pieceChosen.get_colour() == "white" and pieceChosen.get_piece_type() != "king" and pieceList[15].check_for_checks(pieceList[15].get_position()) == False:
      pieceChosen.position = oldPos
      raise KeyError()
    elif pieceChosen.get_colour() == "black" and pieceChosen.get_piece_type() != "king" and pieceList[31].check_for_checks(pieceList[31].get_position()) == False:
      pieceChosen.position = oldPos
      raise KeyError()
    for piece in pieceList:
      if piece.get_position() == chosenSquare and piece.get_colour() != turnColour:
        piece.get_captured()   
    if pieceChosen.get_piece_type() == "pawn" and ((turnColour == "white" and chosenSquare[1] == 1) or (turnColour == "black" and chosenSquare[1] == 8)):
      promotedPiece = input("input your promoted piece: ")
      promotedPiece = promotedPiece.lower()
      while promotedPiece not in ["pawn", "knight","bishop","queen"]:
        promotedPiece = input("input your promoted piece: ")
        promotedPiece = promotedPiece.lower()
      else:
        pieceList = promotion(promotedPiece, pieceList, pieceChosen, images)
    turnColour = colourToNumber[turnColour]
    turnColour /= -1
    return None, pieceList, turnColour, lastMoveEnPassant
  except:
    return None, pieceList, colourToNumber[turnColour], lastMoveEnPassant

def game_loop(pieceList, images, lastMoveEnPassant):
  #set up the screen
  pygame.init()
  pygame.display.set_caption("2 player chess, stockfish coming soon")
  screen = pygame.display.set_mode((640, 640))
  BROWN = (137, 81, 41)
  WHITE = (255, 255, 255)
  #set up variables for loop
  loop = True
  turnColour = 1 #so turn switches between white and black
  pieceChosen = None
  while loop:
    screen.fill(WHITE)
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
        pieceChosen, pieceList, turnColour, lastMoveEnPassant = take_turn(turnColour, pos, pieceChosen, pieceList, images, lastMoveEnPassant)
    pygame.display.update()
  pygame.quit()
game_loop(pieceList, images, False)
