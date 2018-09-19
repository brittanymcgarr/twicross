################################################################################
## Twicross Game Class Testing                                                ##
## Basic Twilio Picross board and classes                                     ##
################################################################################


from twicross.game import Board


class TestGameBoard:
    def __init__(self):
        self.dimensions = [10, 10]
        self.image = [
            ['-', '-', 'X', 'X', 'X', 'X', 'X', 'X', '-', '-'],
            ['-', 'X', '-', '-', '-', '-', '-', '-', 'X', '-'],
            ['X', '-', 'X', 'X', '-', '-', 'X', 'X', '-', 'X'],
            ['X', '-', 'X', 'X', '-', '-', 'X', 'X', '-', 'X'],
            ['X', '-', '-', '-', '-', '-', '-', '-', '-', 'X'],
            ['X', '-', '-', '-', '-', '-', '-', '-', '-', 'X'],
            ['X', '-', 'X', 'X', '-', '-', 'X', 'X', '-', 'X'],
            ['X', '-', 'X', 'X', '-', '-', 'X', 'X', '-', 'X'],
            ['-', 'X', '-', '-', '-', '-', '-', '-', 'X', '-'],
            ['-', '-', 'X', 'X', 'X', 'X', 'X', 'X', '-', '-']
        ]
        self.hints = [
            [[6], [1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1], [1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1], [6]],
            [[6], [1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1], [1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1], [6]]
        ]
        self.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

    def test_import_board(self):
        board = Board('boards/twilio')
        assert(board.dimensions == self.dimensions)
        assert(board.image == self.image)
        assert(board.hints == self.hints)
        assert(board.board == self.board)


if __name__ == '__main__':
    test_board = TestGameBoard()

    try:
        print("Testing the Game Board ... ")
        print("Importing game board ...")
        test_board.test_import_board()
        print("SUCCESS")
    except:
        print("TESTS FAILED")
