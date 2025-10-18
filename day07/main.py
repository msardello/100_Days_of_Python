import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list

print(hangman_art.logo)
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

lives = 6
game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in incorrect_letters:
        print(f"You have already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    print("Word to guess: " + display)

    if guess not in chosen_word and guess not in incorrect_letters:
        lives -= 1
        incorrect_letters.append(guess)
        print(f"You guessed {guess}. That's not in the word.  You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
