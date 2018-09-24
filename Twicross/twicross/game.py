################################################################################
## Twicross Demo                                                              ##
## Basic Twilio Picross board and classes                                     ##
################################################################################

import requests
import json
import time
import datetime


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

    def updateBoard(self, x_coord, y_coord):
        if x_coord < 0 or x_coord > self.dimensions[1]\
                or y_coord < 0 or y_coord > self.dimensions[0]\
                or self.board[y_coord][x_coord] == 'X':
            return False

        if self.image[y_coord][x_coord] == 'X':
            self.board[y_coord][x_coord] = 'X'
            return True

        return False

    def scanRow(self, y_coord):
        if y_coord < 0 or not self.dimensions or y_coord > self.dimensions[1]:
            raise TypeError('Invalid Row index')

        for count in range(0, self.dimensions[0]):
            if self.image[y_coord][count] is not self.board[y_coord][count]:
                return False
        return True

    def scanCol(self, x_coord):
        if x_coord < 0 or not self.dimensions or x_coord > self.dimensions[0]:
            raise TypeError('Invalid Column Index')

        for count in range(0, self.dimensions[1]):
            if self.image[count][x_coord] is not self.board[count][x_coord]:
                return False
        return True

    def checkWin(self):
        return self.board == self.image


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
        return score


class Game:
    def __init__(self):
        self.players = {}
        self.board = None
        self.session_id = ''
        self.log = []

    def getBoard(self, filename, session=''):
        self.board = Board(filename)

        if not self.board:
            return False

        self.session_id = session
        self.log.append('Uploaded the board: '.format(filename))

    def playerMove(self, phone, body):
        number = phone

        if number not in self.players.keys():
            self.players[number] = Player(name='', phone=number, game=self.session_id)

        message = body.strip().lstrip()
        message = message.split(',')
        coords = []

        for value in message:
            try:
                coords.append(int(value))
            except TypeError:
                raise ValueError('Player Message invalid')

        if self.board.updateBoard(coords[1], coords[0]):
            score = self.players[number].updateScore(1)
            self.log.append('{} earned a point!'.format(self.players[number].name))
        else:
            score = self.players[number].updateScore(-1)
            self.log.append('{} has guess poorly and lost a point'.format(self.players[number].name))

        if self.board.scanRow(coords[1]):
            score = self.players[number].updateScore(3)
            self.log.append('{} completed the row and gains 3 points!'.format(self.players[number].name))
        if self.board.scanCol(coords[0]):
            score = self.players[number].updateScore(3)
            self.log.append('{} completed the column and gains 3 points!'.format(self.players[number].name))
        if self.board.checkWin():
            score = self.players[number].updateScore(5)
            self.log.append('{} finished the puzzel and gains 5 points!!!'.format(self.players[number].name))
            self.log.append('Congratulations!')

        return score
