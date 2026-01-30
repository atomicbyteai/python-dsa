# Python number guessing game
import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
running = True
print("Welcome to number guessing game!!")
print(f"Select a number between {low} to {high}")

while running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("Out of range! Try again..")
            print(f"Please select a number between {low} to {high}")
        elif guess < answer:
            print("Too low..Try again!!")
        elif guess > answer:
            print("Too high..Try again!!")
        else:
            print(f"Your answer is correct: {answer}")
            print(f"Number of guesses: {guesses}")
            running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {low} to {high}")
