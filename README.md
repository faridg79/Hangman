# Hangman

# Word Guessing Game
This is a simple word guessing game where you have to guess a word. You need to guess the letters one by one to uncover the word. You have only 5 chances, and each time you guess a wrong letter, you lose one chance.

# How to Run
- First, clone the code from GitHub.
<pre> git clone https://github.com/your-username/word-guessing-game.git </pre>
- Navigate to the project directory.
<pre>cd word-guessing-game</pre>
- Run the program.
<pre>python game.py</pre>
# How to Play
By running the program, the game starts, and a blank line is displayed, where each line represents a letter of the word. The letters that have not been guessed yet are shown with underscores (_).
Copy code
_ _ _ _
You need to guess a letter that you think exists in the word and enter it.
less
Copy code
Guess a letter: a
If the letter is in the word and you guessed it correctly, the letter is shown in the blank line.
css
Copy code
_ a _ _
If the letter is in the word but you have already guessed it before, the message "You've already guessed that letter!" is displayed.

If the letter is not in the word, the message "Wrong guess! Chances left: X" is displayed, and one of your chances is deducted.

The game continues until you guess all the letters of the word correctly or you run out of chances.

If you correctly guess all the letters of the word, the message "Good job! You guessed the word: [word]" is displayed, and the game ends.

If you run out of chances and you haven't guessed the word yet, the message "Game over! The word was: [word]" is displayed, and the game ends.

You can customize this README according to your needs and add more descriptions to it.
