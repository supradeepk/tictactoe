class Tictactoe:
    def __init__(self):
        self.board = [" " for i in range(9)]

    def myfunc(self, x):
        return "|{}|{}|{}|".format(self.board[x-1], self.board[x], self.board[x+1])
    
    def isVictory(self, icon):
        if (self.board[0] == icon and self.board[1] == icon and self.board[2] == icon ) or \
            (self.board[3] == icon and self.board[4] == icon and self.board[5] == icon ) or \
                (self.board[6] == icon and self.board[7] == icon and self.board[8] == icon ) or \
                    (self.board[0] == icon and self.board[3] == icon and self.board[6] == icon ) or \
                        (self.board[1] == icon and self.board[4] == icon and self.board[7] == icon ) or \
                            (self.board[2] == icon and self.board[5] == icon and self.board[8] == icon ) or \
                                (self.board[0] == icon and self.board[4] == icon and self.board[8] == icon ) or \
                                    (self.board[2] == icon and self.board[4] == icon and self.board[6] == icon ):
                                        return True
        else:
            return False
            

