# Hangman Game

This is a simple Hangman game where you have to guess a word. You need to guess the letters one by one to uncover the word. You have only 5 chances, and each time you guess a wrong letter, you lose one chance.

# How to Run

1. First, clone the code from GitHub:

   ```bash
   git clone https://github.com/faridg79/Hangman.git


1. Navigate to the project directory:

   ```bash
   cd Hangman

1.Run the game:

   python game.py

# How to Play

1. The game will start, and a blank line will be displayed, representing the hidden word. Each letter of the word is initially shown as an underscore (_).

   ```bash
   _ _ _ _

2. Guess a letter by entering it when prompted:

   ```bash
   Guess a letter: a

3.If the letter is in the word and you guessed it correctly, the letter will be revealed in the corresponding blank space:

    ```bash
    _ a _ _

4. If the letter is in the word but you have already guessed it before, you will receive the message "You've already guessed that letter!"

5. If the letter is not in the word, you will receive the message "Wrong guess! Chances left: X", and one chance will be deducted.

6. The game continues until you guess all the letters of the word correctly or run out of chances.

7. If you correctly guess all the letters of the word, you will receive the message "Good job! You guessed the word: [word]", and the game ends.

8. If you run out of chances and haven't guessed the word yet, you will receive the message "Game over! The word was: [word]", and the game ends.
