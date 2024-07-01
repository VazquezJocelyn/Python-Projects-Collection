# This program generates a random number in the range of 1 through 15.
# Which will ask the user to guess what the number is.

def main(): #This line defines a main() function.
    user_guess = 99   #user_guess equivalent to 99.

    Number = randomNum()    #Number is equivalent to randomNum() function in which it calls for it.

    while user_guess!= 0: #The loop runs while the user inputs a non-zero number from 1 to 15.
        user_guess = int(input('Enter a number between 1 and 15, or 0 to quit: '))
        #Depending on the user's input, the program either...

        if user_guess > Number: print('Too high, try again') 
        #prints "Too high, try again" if the user's guess is greater than Number.

        elif user_guess < Number: print('Too low, try again') 
        #prints "Too low, try again" if the user's guess is less than Number.
    
        elif user_guess == Number: print('Congratulations! You guessed the right number!') 
        #prints "Congratulations! You guessed the right number!" if the user's guess is equal to Number.
        
        if user_guess == 0: print('Thanks for playing!')
        #If the user inputs 0, the program prints "Thanks for playing!" and ends the game.

def randomNum():    #Calls the randomNum() function where it generates random integers.
    import random   #Imports the random function.
    random=random.randint(1,15) #randomNum() creates a random integer between 1 and 15 using random.randint() from the random module.
    return (random) #The random integer is then returned to the main() function.

main()  #Calls the main() function first.