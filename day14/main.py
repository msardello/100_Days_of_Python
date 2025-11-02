import random
from game_data import data
from art import logo, vs

def calculate_answer(list_of_items):
    a = list_of_items[0]["follower_count"]
    b = list_of_items[1]["follower_count"]
    answer = max(a, b)
    return answer

def format_items(list_of_items):
    items_name = list_of_items["name"]
    items_descr = list_of_items["description"]
    items_country = list_of_items["country"]
    return f"{items_name}, a {items_descr}, from {items_country}"

def calculate_user_guess(u_input, list_of_items):
    if u_input == "a":
        return list_of_items[0]["follower_count"]
    else:
        return list_of_items[1]["follower_count"]

def calculate_score(user_guess, correct_answer, current_score):
    if user_guess != correct_answer:
        print(f"Sorry, that's wrong.  Final score: {current_score}")
    else:
        current_score += 1
        print(f"You're right! Current score:  {current_score}.")
        return current_score

def create_new_items(list_of_items):
    list_of_items[0] = list_of_items[1]
    list_of_items.remove(list_of_items[1])
    list_of_items.append(random.choice(data))
    return list_of_items

def game():

    print(logo)
    items = []
    for item in range(2):
        items.append(random.choice(data))

    guess = 0
    score = 0
    answer = 0
    while guess == answer:
        answer = calculate_answer(items)
        print(f"Compare A: {format_items(items[0])}")
        print(vs)
        print(f"Against B: {format_items(items[1])}")
        user_input = input("Who has more followers? Type 'A' or 'B':  ").lower()
        print("\n" * 25)
        print(logo)
        guess = calculate_user_guess(user_input, items)
        score = calculate_score(guess, answer, score)
        items = create_new_items(items)


game()










