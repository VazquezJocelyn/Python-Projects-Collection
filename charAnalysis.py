                                            # Defines the main function
def main():                                 # Initializes 4 variables with 0 counting spaces, lowercase letters, digits, and uppercase letters in a text file.
    space = 0
    lowerCase = 0
    digits = 0
    upperCase = 0
                                            
    with open('text.txt', 'r') as file:     # The 'with' statement reads the content of the 'text.txt' file and assigns it to the 'file' variable.
        file = file.read()

        for i in file:                      # A 'for' loop is used to iterate through every character in the 'file' variable.
            if (i.isspace()):               # If the character is a space, the 'space' variable is incremented by 1.
                space = space+1
            elif (i.islower()):             # If the character is a lowercase letter, the 'lowercase' variable is incremented by 1.
                lowerCase = lowerCase+1
            elif (i.isdigit()):             # If the character is a digit, the 'digits' variable is incremented by 1.
                digits = digits+1
            elif (i.isupper()):             # If the character is an uppercase letter, the 'uppercase' variable is incremented by 1.
                upperCase = upperCase+1
                                            # The number of spaces, lowercase letters, digits, and uppercase letters are printed using the 'print' function.
    print('Spaces: ', space)
    print('Lowercase letter: ', lowerCase)
    print('Digits: ', digits)
    print('Uppercase letters: ', upperCase)
    
main()                                      # Calls the main function
