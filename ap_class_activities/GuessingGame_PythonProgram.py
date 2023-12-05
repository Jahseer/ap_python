# My name is Jahseer Griffin and  my program is a guessing game that gives the user hints on what the number is for 1 to 100 . 
# my game will give out hints the user will have x amount of attempts and if you don't get it you can try again
#breifly describe what your program is about?
#My program is called def function and its about guessing what the number is 

#What probblem is your program trying to solve?
#there are several problems my program aims to solve by gueesing the number i inputed

#How will your program solve this problem?
#def function will solve the problems listed above in several ways by printing the  number that i put it in it and some other ways that you can do it is use other data types

#Are there any apps/programs that similar to your program? (be descriptive)
#There are several programs that inspired my program  they are different def functions that i know and that i used the inspiried me

#Who is this program designed for? Please describe the user who will be useing the program by describing three(3) things about them and how it relates to them using the program.
#The general user for this program are students who...(be descriptive)

#This program and designed for students who like guessing games all you have to do is guess the number between 1,100


import random


print("Welcome to my guessing game, Guess my number between 1 and 100")
secret_number = random.randint(1,100)
num_guesses = 0

while num_guesses < 5:
    guess = input(" Guess a number:")
    num_guesses += 1

    if guess == secret_number:
        print("congrulations, you guessed the secret number")
        break
    elif guess:
        print("Too low, try again.")
    else:
        print("Too high, try again>")

if num_guesses == 5:
    print("Sorry , you've run out of guesses, The secret number was",secret_number)


