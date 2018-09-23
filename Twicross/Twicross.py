################################################################################
## Twicross Demo                                                              ##
## A Twilio Picross Demo using MMS                                            ##
################################################################################

from flask import Flask, render_template, request
import requests
from twicross.game import Game

# initialize the Flask app
app = Flask(__name__)
game = Game()
game.getBoard('boards/owl')


# create the home route
@app.route('/')
def index():
    return render_template('index.html', game=game)


# play a coordinate
@app.route('/coord', methods=['GET', 'POST'])
def play_coord():
    number = request.values.get('From', None)
    number = number[2:]
    body = request.values.get('Body', None)

    try:
        game.playerMove(number, body)
        return render_template('index.html', game=game)
    except ValueError:
        return


if __name__ == '__main__':
    app.run(debug=True)

