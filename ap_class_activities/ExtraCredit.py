import random

def choose_movie():
    movies = ["Good burger 2", "Spy kids", "elemental", "A Madea homecoming", "men and black", "The batman"]
    return random.choice(movies)

def display_hint(movie, guessed_letters):
    hint = ""
    for letter in movie:
        if letter.lower() in guessed_letters or letter == " ":
            hint += letter
        else:
            hint += "_"
    return hint

def movie_guessing_game():
    print("Welcome to the Movie Guessing Game!")
    selected_movie = choose_movie()
    guessed_letters = []
    attempts = 5

    while attempts > 0:
        hint = display_hint(selected_movie, guessed_letters)
        print("Movie: " + hint)
        guess = input("Guess a letter: ").lower()

        if guess.lower() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in selected_movie.lower():
                guessed_letters.append(guess)
                if set(guessed_letters) == set(letter.lower() for letter in selected_movie if letter.lower()):
                    print("Congratulations! You guessed the movie: " + selected_movie)
                    break
                else:
                    print("Good guess!")
            else:
                attempts -= 1
                print(f"Wrong letter! {attempts} attempts remaining.")
        else:
            print("Invalid input. Please enter a single letter.")

    if attempts == 0:
        print("\nSorry, you're out of attempts. The correct movie was: " + selected_movie)

# Run the game
movie_guessing_game()