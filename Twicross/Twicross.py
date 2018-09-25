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


# play a coordinate
@app.route('/coord', methods=['POST'])
def play_coord():
    number = request.form['From']
    body = request.form['Body'].lower()

    resp = MessagingResponse()

    try:
        if body == 'reveal':
            resp.message("Cheater.")
            game.board.board = game.board.image
            return str(resp)
        if body == 'reset':
            resp.message("Resetting")
            game.resetGame()
            return str(resp)

        score = game.playerMove(number, body)

        if number != "":
            if score > 0:
                message = "You found a piece. Score is now {}".format(score)
            elif score == 0:
                message = "You didn't find a piece. Score is still {}".format(score)
            else:
                message = "You didn't find a piece. Score is now {}".format(score)

            resp.message(message)
            return str(resp)

    except ValueError:
        return


if __name__ == '__main__':
    app.run(debug=True)

