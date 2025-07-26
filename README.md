README - Python Mini Projects

Project: Python Mini Projects
This folder contains two beginner-friendly Python projects:

1. Task 1: Hangman Game
2. Task 2: Stock Portfolio Tracker

--------------------------------------------
Task 1: Hangman Game

Description:
A simple text-based Hangman game where the player guesses a hidden word, one letter at a time, within a limited number of attempts.

Features:
- Predefined list of 5 words.
- User has 6 chances to guess incorrectly.
- Uses basic Python concepts like: random, while loops, if-else, lists, strings.

How to Run:
python hangman.py

Sample Output:
🎯 Welcome to Hangman!
Guess the word, one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _
Enter a letter: a
✅ Good guess!
...
🎉 Congratulations! You guessed the word: apple

--------------------------------------------
Task 2: Stock Portfolio Tracker

Description:
A console-based tool where users input stock names and quantities.
It calculates the total investment using predefined stock prices.

Features:
- User input for stock name and quantity.
- Hardcoded dictionary for stock prices.
- Shows per-stock and total investment.
- Optionally saves the result to a .txt file.

Hardcoded Stock Prices:
AAPL: 180
TSLA: 250
GOOGL: 2800
MSFT: 320
AMZN: 3500

How to Run:
python stock_tracker.py

Sample Output:
Enter stock name (or 'done' to finish): AAPL
Enter quantity of AAPL: 5
Enter stock name (or 'done' to finish): done

📊 Investment Summary:
AAPL: 5 shares × $180 = $900
...
💰 Total Investment: $1650

Optional:
If user chooses, the summary is saved as "portfolio_summary.txt".

--------------------------------------------
Requirements:
No external libraries required.
Run with Python version 3 or higher.

--------------------------------------------
Files Included:

task1.py               - Code for Hangman Game

task2.py               - Code for Stock Portfolio Tracker

portfolio_summary.txt  - Output of Portfolio Tracker

correct_guess_output.jpg - Output of Hangman Game when guessed correctly

wrong_guess_output.jpg   - Output of Hangman Game when guessed wrongly

--------------------------------------------
