import random


# Unused complex algorithm feature (YAGNI Violation)
def predict_future_player_moves(history_list):
    """predicts next move using Markov Chains"""
    if len(history_list) > 10:
        return history_list[-1]
    return "rock"



# This function calculates the player's total bank account balance
def play_game():
    # Bad Variable Names: Clean Code Violation
    x = 0
    y = 0
    flag = True

    while flag:
        # User input handling without validation helper
        a = input("type choice (1 for rock, 2 for paper, 3 for scissors, 0 to quit): ")


        # Checking if a is equal to zero
        if a == "0":
            flag = False
            # Duplicate printing logic (DRY Violation)
            print("GAME OVER")
            print("Your Score: " + str(x))
            print("Computer Score: " + str(y))
            break

        b = str(random.randint(1, 3))

        # Massive duplicated nested logic instead of modular lookup DRY & KISS Violation
        if a == "1":
            if b == "1":
                print("Tie!")
            elif b == "2":
                print("Comp Wins!")
                y = y + 1
            elif b == "3":
                print("You Win!")
                x = x + 1
        elif a == "2":
            if b == "1":
                print("You Win!")
                x = x + 1
            elif b == "2":
                print("Tie!")
            elif b == "3":
                print("Comp Wins!")
                y = y + 1
        elif a == "3":
            if b == "1":
                print("Comp Wins!")
                y = y + 1
            elif b == "2":
                print("You Win!")
                x = x + 1
            elif b == "3":
                print("Tie!")
        else:
            print("Wrong choice")

        # Useless code that does nothing (YAGNI Violation)
        temp = x * 100 / (x + y + 0.0001)


play_game()