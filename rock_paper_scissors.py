import random

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

def main():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue
        
        bot_choice = get_bot_choice()
        print(f"Bot chose: {bot_choice}")
        
        result = determine_winner(user_choice, bot_choice)
        print(result)

if __name__ == "__main__":
    main()
