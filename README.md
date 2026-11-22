# Number Guessing Game

A simple number guessing game written in Python.

The computer picks a random number between 1 and 100, and the player tries to guess it. After each guess, the program tells the player if the number is too high or too low. The game ends when the player guesses the number or runs out of attempts.

## How to run

python guess_num.py

## Features

- Three difficulty levels: easy (10 attempts), medium (7 attempts), hard (5 attempts)
- Input validation: rejects letters and numbers outside the allowed range
- Rejects numbers that were already ruled out, without using an attempt
- Option to play again after each game
