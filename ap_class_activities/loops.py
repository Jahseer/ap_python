# 1. Provided below is some starter code. 
# Fix this code to create a loop that will iterate
# until it gets to the number 10.

# hint: remember there are 3 parts to a loop. 
#while i # insert missing code.
    #print('insert missing value')
    # insert missing code here

# 2. Create a simple while loop that will iterate over a the following condition:
# The loop will ask the user to enter the secret number. The secret number is 3. 
# If the user enters the secret number correctly, the loop will stop and tell the user
# the can win a prize. 
# If the user puts in an incorrect secret number, the loop will ask them to enter the 
# correct secret number. 

secret_number = 3

while True:
    number = int(input("Enter an integer: "))    
    if number == secret_number: 
        break
    print("you can win a prize!")

print("enter the correct number to win a prize .")




# 3. describe the difference between a while loop and a conditional statement. 
# Try be as specific as you can

answer = # a while loop is very similar to an if conditional, except that a while is continually executed until it's no longer true and an if is only executed once.')

# 4. Create a while loop that will iterate over the list of names 
# and print out only the following name: William

names= ['Avery','Paige','William','Ade','Jasmyn','Crystal']

while name()

io<100
while(100)
print("william")


# 5. Create a loop that will ask the user to add a new string value to the list of names above.
# hint you will need use append().

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Enter an integer, try again...")

my_list = ["jasmyn", "avery"]
print(f"{my_list = }")
num_names_to_add = get_int_input("How many names would you like to add? ")
for i in range(1, num_names_to_add + 1):
    my_list.append(input(f"Enter name {i} to add: "))
print(f"{my_list = }")

# BONUS QUESTION
# Describe the differences between a FOR loop and WHILE loop.

answer= ("For loop is used when the number of iterations is already known. While loop is used when the number of iterations is already Unknown")