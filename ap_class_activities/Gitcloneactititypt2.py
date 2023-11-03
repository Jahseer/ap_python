def function():

 food =  ("mac and cheese")
guess = input("So I'm thinking of a food's name. Try to guess it: ")


while guess != food and < len(food):
    print("Nope, that's not it! Hint: letter ", end='')
    print( "is", food)
    guess = input("Guess again: ")
   

if 'mac and cheese' == len(food) and food != guess:
    print("Too bad, you couldn't get it.  The food was", 'mac and cheese' + ".")
else:
    print("\nGreat, you got it in",  "guesses!")