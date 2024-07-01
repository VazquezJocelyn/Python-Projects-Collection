def main():                                                       # Defines a function called main that serves as the main code for this program.              
    user_month= int(input("Enter a month: "))                     # Prompts user to enter a month.
    if user_month<1 or user_month>12:                             # Checks if month is outside the range 1-12.
        print("Error: Month should be between 1 and 12.")         # If so, it prints out an error message.
    else:                                      
        user_day = int(input("Enter a day: ")) # If month is within range, function promots user to enter a day.
        if user_day<1 or user_day>31:          # It checks if the entered day is outside the range 1-31.
            print("Error: Day should be between 1 and 31.")     # If so, it prints out an error message.
        else:
            user_year = int(input("Enter a two digit year: "))    # If the date is valid the function prints the entered date in month/day/year format
            if user_year<0 or user_year>99:                       # It checks if the entered day is outside the range 0-99.
                print("Error: Year should be between 0 and 99.")  # If so, it prints out an error message.
            print(user_month,"/",user_day,"/",user_year)
            if user_month * user_day == user_year:   # It then checks if the product of the entered month and day is equal to the entered year
                print(f"The date is {user_month}/{user_day}/{user_year}")
                print("This is a magic date.")      
            else:
                print(f"The date is {user_month}/{user_day}/{user_year}")
                print("The date is not magic. ")     # If the production of the month & day is not equal to the year, the function prints out an error message.
main()                                               #the function calls the main() function to run the code.
