def main():                                  # Defines a main function.
    string = input('Enter your full name: ') # Prompts the user to enter their full name & stores it in the 'string' variable.
    full_name= string.split(" ")             # Splits a string into pieces based on the space character & stores each piece in a list.
    for i in full_name:                      # The 'for' loop goes through each name in the 'full_name' list, & then converts the first character of each name to uppercase using the 'upper' method.
        print(i[0].upper(), end= '.')        # The modified substring is printed to the console.

main()                                       # Calls the main function to execute the code.
