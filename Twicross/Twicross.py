################################################################################
## Twicross Demo                                                              ##
## A Twilio Picross Demo using MMS                                            ##
################################################################################

from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse

from twicross.game import Game

# initialize the Flask app
app = Flask(__name__)
game = Game()
game.getBoard('boards/owl')


# create the home route
@app.route('/')
def index():
    return render_template('index.html', game=game)


@app.route('/coord', methods=['POST'])
def post_coords():
    phone = request.form['From']
    body = request.form['Body']
    resp = MessagingResponse()

    if phone != "":
        score = game.playerMove(phone, body)

        message = ""
        if score > 0:
            message = "You found a piece. Your score is now {}".format(score)
        else:
            message = "Not a piece. Your score is {}.".format(score)

        resp.message(message)
        return str(resp)

# Debugging passphrases
#
#
#
#
#
#
#
##
#
#
#
#
#
#
##
#
#
#
#
#
#
##
#
#
#
#
#
#
#
def check_passphrases(body):
    resp = MessagingResponse()

    if body == 'reveal':
        resp.message("Cheater.")
        game.board.board = game.board.image
        return str(resp)
    if body == 'reset':
        resp.message("Resetting")
        game.resetGame()
        return str(resp)

    return None


if __name__ == '__main__':
    app.run(debug=True)

