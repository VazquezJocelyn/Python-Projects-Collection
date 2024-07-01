year = int(input("Enter a year: ")) # Asks user to input a year and converts it to an integer using the int() function.
def leapYear(year):                 # It defines a function called leapYear that takes a year as input.
    leapYear = False                # The function sets a boolean variable called leapYear to False by default.
    if (year % 4) == 0:             # It checks if the year is divisible by 4.
        leapYear = True;            # If so, it sets leapYear to True.
        if (year % 100) == 0:       # If the year is also divisible by 100.
            if (year % 400) == 0:   # It checks if it's also divisible by 400.
                leapYear = True;    # If it is, it sets leapYear to True.
            else:
                leapYear = False;   # Otherwise it sets it to False.
    else:
        leapYear = False            # If the year is not divisible by 4, leapYear remains False.
    return leapYear                 # The function returns the value of leapYear.
if(leapYear(year)):                 # The main code calls the leapYear function with the user-inputted year as input & checks if the result is True./n
    print("That is a leap year. February has 29 days.") # If it is a leap year, it prints a message saying so.
    
else:
    print("That is not a leap year. February has 28 days.") # If it's not, it prints a message saying so.
