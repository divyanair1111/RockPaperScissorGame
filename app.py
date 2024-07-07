from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def get_bot_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        return "You win!"
    else:
        return "Bot wins!"

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    user_choice = data.get('user_choice')
    bot_choice = get_bot_choice()
    result = determine_winner(user_choice, bot_choice)
    return jsonify({
        'user_choice': user_choice,
        'bot_choice': bot_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
