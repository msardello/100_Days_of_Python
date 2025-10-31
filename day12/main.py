import random
import art

EASY_ATTEMPTS_REMAINING = 10
HARD_ATTEMPTS_REMAINING = 5

# Evaluate the player's guess
def check_guess(player_guess, num_to_guess, attempts_remaining):
    if player_guess > num_to_guess:
        print("Too high")
        return attempts_remaining - 1
    elif player_guess < num_to_guess:
        print("Too low")
        return attempts_remaining - 1
    else:
        print(f"You got it! The answer was {num_to_guess}")


# Manage number of attempts based on easy vs. hard
def set_difficulty_level():
    difficulty_level = input("Choose a difficulty.  Type 'easy' or 'hard':  ").lower()
    if difficulty_level == 'easy':
        return EASY_ATTEMPTS_REMAINING
    else:
        return HARD_ATTEMPTS_REMAINING

# play the game
def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    num_to_guess = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100")

    attempts_remaining = set_difficulty_level()

    player_guess = 0
    while player_guess != num_to_guess:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess:  "))
        attempts_remaining = check_guess(player_guess, num_to_guess, attempts_remaining)
        if attempts_remaining == 0:
            print("You've run out of guesses.  Refresh the page to run again.")
            return
        elif player_guess != num_to_guess:
            print("Guess again.")

play_game()














