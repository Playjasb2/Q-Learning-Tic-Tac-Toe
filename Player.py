class Player:

    def __init__(self, id):
        self.id = id

    def getAction(self, board):
        raise NotImplementedError
