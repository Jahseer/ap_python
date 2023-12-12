import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guess = 0
    
    print("Welcome to the Guessing Game! Try to guess the secret number between 1 and 100.")
    
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guessing_game()