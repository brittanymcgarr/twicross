################################################################################
## Twicross Demo                                                              ##
## Basic Twilio Picross board and classes                                     ##
################################################################################


class Board:
    def __init__(self, filename):
        self.board = []
        self.hints = [[], []]
        self.image = []
        self.dimensions = [0, 0]
        self.loadBoard(filename)

    def loadBoard(self, filename):
        try:
            file = open(filename, 'r')
        except FileNotFoundError:
            return

        dimensions = file.readline()
        dimensions = dimensions.split(',')
        if len(dimensions) != 2:
            return

        self.dimensions[0] = int(dimensions[0])
        self.dimensions[1] = int(dimensions[1])

        self.image = []
        for line in file:
            hold_line = line.strip()
            hold_line = list(hold_line)
            self.image.append(hold_line)

        for line in self.image:
            hold_line = line
            hint_count = 0
            hint_row = []
            new_row = []

            for symbol in hold_line:
                if symbol == 'X':
                    hint_count += 1
                elif symbol != 'X' and hint_count > 0:
                    hint_row.append(hint_count)
                    hint_count = 0
                new_row.append(' ')

            if hint_count > 0:
                hint_row.append(hint_count)
            self.hints[0].append(hint_row)
            self.board.append(new_row)

        for col in range(0, self.dimensions[1]):
            hint_count = 0
            hint_col = []

            for row in range(0, self.dimensions[0]):
                if self.image[row][col] == 'X':
                    hint_count += 1
                elif self.image[row][col] != 'X' and hint_count > 0:
                    hint_col.append(hint_count)
                    hint_count = 0

            if hint_count > 0:
                hint_col.append(hint_count)
            self.hints[1].append(hint_col)

    def updateBoard(self, x_coord, y_coord, symbol):
        self.board[x_coord][y_coord] = symbol

    def scanRow(self, y_coord):
        pass

    def scanCol(self, x_coord):
        pass

    def checkWin(self):
        pass


class Player:
    def __init__(self,
                 name='anon',
                 phone='(555)123-4567',
                 score=0,
                 game=None):
        self.name = name
        self.phone = phone
        self.score = score
        self.game = game

    def setGame(self, game):
        self.game = game

    def updateScore(self, score):
        self.score += score
