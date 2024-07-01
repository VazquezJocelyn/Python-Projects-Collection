# This code converts regular numbers to Roman numerals
User_number = int(input("Enter a number between 1 and 10: "))  # This code lets a user input a number between 1 and 10.

if (User_number < 1) or (User_number > 10):                    # The code checks if the number entered is between 1 and 10
    print("Error: Invalid Number")                             # The program will print an error message saying "Error: Invalid Number."
else:                                                       
    print("Number", "Roman Number", sep='\t\t')    # If the number entered is valid, the program will print the text 

    if User_number == 1:     # The code uses a series of "if" statements to check what the number is and then print the corresponding Roman numeral.
        print("1", "I",sep="\t\t" )
    elif User_number == 2:
        print("2", "II",sep="\t\t" )
    elif User_number == 3: 
        print("3", "III",sep="\t\t" )
    elif User_number == 4:
        print("4", "IV",sep="\t\t" )
    elif User_number == 5:
        print("5", "V",sep="\t\t" )
    elif User_number == 6:
        print("6", "VI",sep="\t\t" )
    elif User_number == 7:
        print("7", "VII",sep="\t\t" )
    elif User_number == 8:
        print("8", "VIII",sep="\t\t" )
    elif User_number == 9:
        print("9", "IX",sep="\t\t" )
    elif User_number == 10:
        print("10", "X",sep="\t\t",end="\n\n" )

