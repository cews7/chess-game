class chessBoard:
    def __init__(self,name):
        self.name=name
        self.board = [[x for x in range(8)] for y in range(8)]

        for x in range(8):
            for y in range(8):
                if (x==0 and (y==0 or y==7)):
                    self.board[x][y]=piece('rook','white',(x,y))
                elif (x==7 and (y==0 or y==7)):
                    self.board[x][y]=piece('rook','black',(x,y))
                elif x==1:
                    self.board[x][y]=piece('pawn','white',(x,y))
                elif x==6:
                    self.board[x][y]=piece('pawn','black',(x,y))
                elif (x==0 and (y==1 or y==6)):
                    self.board[x][y]=piece('knight','white',(x,y))
                elif (x==7 and (y==1 or y==6)):
                    self.board[x][y]=piece('knight','black',(x,y))
                elif (x==0 and (y==2 or y==5)):
                    self.board[x][y]=piece('bishop','white',(x,y))
                elif (x==7 and (y==2 or y==5)):
                    self.board[x][y]=piece('bishop','black',(x,y))
                elif (x==0 and y==3):
                    self.board[x][y]=piece('queen','white',(x,y))
                elif(x==7 and y==3):
                    self.board[x][y]=piece('queen','black',(x,y))
                elif (x==0 and y==4):
                    self.board[x][y]=piece('king','white',(x,y))
                elif (x==7 and y==4):
                    self.board[x][y]=piece('king','black',(x,y))
                else:
                    self.board[x][y]=piece(' ','green',(x,y))

    def printBoard(self):
        for x in range(8):
            row=''
            for y in range(8):
                row=row +'| '+ self.board[x][y].name[0] + ' |'
            print(row)

    def movePiece(self,p,position):
        x,y=position[0],position[1]
        piece_x,piece_y=p.position[0],p.position[1]
        if p.canMove(position,self.board):
            self.board[x][y]=p
            self.board[piece_x][piece_y]=piece(' ','green',(piece_x,piece_y))
            p.position=(x,y)
        else:
            return False


class piece:
    def __init__(self,name,color,position):
        self.name=name
        self.color=color
        self.position=position

    def getOtherColor(self):
        if self.color=='white':
            return 'black'
        else:
            return 'white'
    def canMove(self,position,board):
        x,y=position[0], position[1]
        piece_x,piece_y=self.position[0],self.position[1]
        if self.name=='pawn':
            if self.color=='white':
                if board[x][y].name==' ':
                    if self.position[0]==1:
                        if y==self.position[1] and (x==3 or x==2):
                            if board[2][y].name==' ':
                                return True
                    else:
                        if y==self.position[1] and (x==1+self.position[0]):
                            return True
                else:
                    if self.position[0]+1==x and (self.position[1]==y+1 or self.position[1]==y-1) and board[x][y].color=='black':
                        return board[x][y]
            if self.color=='black':
                if board[x][y].name==' ':
                    if self.position[0]==6:
                        if y==self.position[1] and (x==4 or x==5):
                            if board[5][y].name==' ':
                                return True
                    else:
                        if y==self.position[1] and (x==-1+self.position[0]):
                            return True
                else:
                    if self.position[0]-1==x and (self.position[1]==y+1 or piece.position[1]==y-1) and board[x][y].color=='white':
                        return board[x][y]
            return False
        if self.name=='rook':
            if piece_x==x:
                for i in range(min(piece_y,y),max(piece_y,y))[1:]:
                    if board[x][i].name!=' ':
                        return False
                if board[x][y].color==self.getOtherColor():
                    return board[x][y]
                elif board[x][y].color==self.color:
                    return False
                else:
                    return True

            if piece_y==y:
                for i in range(min(piece_x,x),max(piece_x,x))[1:]:
                    if board[i][y].name!=' ':
                        return False
                if board[x][y].color==self.getOtherColor():
                    return board[x][y]
                elif board[x][y].color==self.color:
                    return False
                else:
                    return True



chess=chessBoard('tim')
rook=chess.board[0][0]
pawn = chess.board[1][3]
