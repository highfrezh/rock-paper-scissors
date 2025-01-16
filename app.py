from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Mapping choices to emojis
choices = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

# Rules of the game
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🎉"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.json
    player_choice = data.get("choice")
    computer_choice = random.choice(list(choices.keys()))
    result = determine_winner(player_choice, computer_choice)

    return jsonify({
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "player_emoji": choices[player_choice],
        "computer_emoji": choices[computer_choice],
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
