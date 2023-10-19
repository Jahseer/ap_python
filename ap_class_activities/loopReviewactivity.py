# Create a security camera program that uses a while loop to detect if there is an
# object in site. 

while True:
    #object_detected = False
    
    if object_detected:
        print('Object dectected!')




# 2. Create a Printer Loop program that will continue to print copies of a document based on the number
# that the user inputs. 

copies = int(input("Enter the number of copies"))

while copies > 0:
    print('printing copy...')

copies -= 1

print('printing completed!')


# 3. Create a Stop Light Loop that will change the light color based on different time intervals. 
# every 30 seconds the light should change between green and red. 

while True:
    print('Green light')
    time.sleep(30)

    print('Red light')
    Time.sleep(30)



# 3. BONUS: add an additional condition that will change the light to yellow for 5 seconds before the
# next light change. 


