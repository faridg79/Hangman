import random


def select_word():
    words = ['supra', 'mclaren', 'pride', 'bmw', 'benz']
    word = random.choice(words)
    return word


def start_game():
    word = select_word()
    user_letters = []
    chances = 5

    print("The game is running")
    print("_ " * len(word))

    while chances > 0:
        guess = input("Guess a letter: ")
        if guess in user_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            user_letters.append(guess)
            if set(word) == set(user_letters):
                print("GoodJob! You guessed the word:", word)
                break
        else:
            chances -= 1
            print("Wrong guess! chances left:", chances)

        guessed_word = ""
        for letter in word:
            if letter in user_letters:
                guessed_word += letter + " "
            else:
                guessed_word += "_ "

        print(guessed_word)

    if chances == 0:
        print("Game over! The word was:", word)


start_game()
