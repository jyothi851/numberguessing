import random

print("=== Number Guessing Game ===")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < number:
        print("Too Low!")

    elif guess > number:
        print("Too High!")

    else:
        print("\nCongratulations!")
        print("You guessed the correct number.")
        print("Attempts:", attempts)
        break