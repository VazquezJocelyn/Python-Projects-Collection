def main():                                             # Defines the main function
    variable = ''                                       # Initializes a string variable named 'variable' with an empty value.
    print('These are the unique words in the text: ')   # Prints a message to the console.

    with open('text2.txt', 'r') as file:                # The 'with' statement is used to open a file named 'text2.txt' in read-only mode and assign its contents to the 'file' variable.
        lines = file.readlines()                        # The 'readlines' method is used to read the file's contents and store them in a list named 'lines'.

        variable = variable +(''.join(lines))           # The 'join' method is used to concatenate all the elements in the 'lines' list to the 'variable' string variable.       
        st = set(variable.split(' '))                   # The 'split' method is used to split the 'variable' string variable into a set of unique words based on space.
        for words in st:                                # A 'for' loop is used to iterate over the set of unique words.
            print(words.strip())                        # Prints each word to the console after stripping any leading or trailing whitespaces using the 'strip' method.
        file.close()                                    # The 'close' method is called to close the 'file' object.

main()                                                  # Calls the main function to execute the code.

    
