import random, math

def RandomGuess():
    right_number = random.randint(0, 100)
    numberOfGuesses = 5

    print("A random number between 0 and 100 has been chosen, can you guess which number it is? ")

#Give Hints as to the value of the hidden number

#By Multiples
    print(" ***********   HINTS  ************ \n")
    if (right_number % 2 == 0):
        print ("It is a multiple of 2 \n ")
    elif(right_number % 3 == 0):
        print ("It is a multiple of 3 \n")
    elif(right_number % 5 == 0):
        print ("It is a multiple of 5 \n")
    elif(right_number % 7 == 0):
        print ("It is a multiple of 7 \n")
    elif(right_number % 11 == 0):
        print ("It is a multiple of 11 \n")
    else:
        print("It is not a multiple of 2, 3, 5, 7 and 11")

#By Magnitude
    if (right_number <= 25):
        print("The number belongs below 25 \n")
    elif(right_number >25 and right_number <= 50):
        print("The number is between 25 and 50 \n")
    elif(right_number >50 and right_number <= 75):
        print("The number is between 50 and 75 \n")
    elif(right_number >75 and right_number <= 100):
        print("The number belongs above 75 \n")


#Check the Number of Guesses Left 
    while(numberOfGuesses >= 1):
        try:
            guess = int(input(" You have {} guesses left: \n".format(numberOfGuesses)))
        except:
            print("That is not a valid Number")
            break

        if guess == right_number:
            print(" That's Correct. {} was the hidden number \n".format(right_number))
            break
        elif numberOfGuesses == 1:
            print("Oops, That's Incorrect... \n The right answer was {}".format(right_number))
            break
        elif guess > right_number:
            print("That's over the Top, Take another Swipe at it")
        else:
            print("That's a little low, Guess again")
        
        numberOfGuesses -= 1

        if numberOfGuesses == 1:
            print("Last Chance")

RandomGuess()