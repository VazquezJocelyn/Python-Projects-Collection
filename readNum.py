def main():                                              #Defines the variable for line & counter.
    line = ''
    counter = 1
    user_input = (input("Enter the name of the file: ")) #Prompts user for file name input
        
    try:                                                   
        infile = open('user_input', 'r')                 #When the user attempts to open file.
    
    except FileNotFoundError:                            #It will print an 'Error Message' if file is not found.
        print('File Not Found Error')
        return

    while counter < 16:                                  #Read & print first 15 lines from file.
        line = infile.readline()                         #During each iteration, the line is read & printed to the console. 
        print(line.rstrip)                               #Calls the line to remove any trailing white space.
        
        counter += 1
    infile.close()                                       #The file is closed using the close() method.

main()              #Calls the 'main' function to execute the code.