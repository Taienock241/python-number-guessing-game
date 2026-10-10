#number guessing game day 1 project
#random module is used to generate random numbers
import random

secret_number = random.randint(1, 10)
print("\n==================================")
print("        NUMBER GUESSING GAME")
print("==================================\n")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
guess = int(input("Take a guess: "))
number_of_attempts = 1
while guess != secret_number:

    number_of_attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Take a guess: "))
    
print(f"Congratulations! You guessed the number {secret_number} correctly! after {number_of_attempts} attempts.")
print("Thanks for playing the Number Guessing Game!")
