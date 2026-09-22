import random

# Options
CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice() -> str:
    """generates a random choice for the computer."""
    return random.choice(CHOICES)


def get_user_choice() -> str:
    """tells user for input and ensures it is a valid choice."""
    while True:
        user_input = input("Enter rock, paper, or scissors (or 'quit'): ").strip().lower()
        if user_input in CHOICES or user_input == "quit":
            return user_input
        print("Invalid choice. Please try again.")


def determine_winner(user: str, computer: str) -> str:
    """
    says the winner based on standard game rules.
    Returns: 'tie', 'user', or 'computer'
    """
    if user == computer:
        return "tie"

    # Dictionary mapping winning conditions to keep code DRY
    winning_rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_rules[user] == computer:
        return "user"
    return "computer"


def main():
    """Main game loop managing score and game flow."""
    print("--- Welcome to Rock, Paper, Scissors! ---")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!\n")
        elif result == "user":
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1


if __name__ == "__main__":
    main()