################################################################################
## Twicross Demo                                                              ##
## A Twilio Picross Demo using MMS                                            ##
################################################################################

from flask import Flask, render_template, request
from twilio import twiml

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
@app.route('/coord', methods=['POST'])
def play_coord():
    number = request.form['From']
    body = request.form['Body']

    try:
        score = game.playerMove(number, body)
        resp = twiml.Response()

        if score > 0:
            message = "You found a piece. Score is now {}".format(score)
        else:
            message = "You didn't find a piece. Score is now {}".format(score)

        resp.message(message)
        return str(resp)
    except ValueError:
        return


if __name__ == '__main__':
    app.run(debug=True)

