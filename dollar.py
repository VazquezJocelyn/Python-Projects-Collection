# Get the user's income amount.
User_amount = float(input("Enter your income amount: "))  # Assign the value of User_amount to a variable amount
amount = User_amount
User_amount *= 100                                        # The amount is multiplied by 100 to convert the dollars into cents.

#Dollars are worth 100 pennies
Dollars = int(User_amount //100)                          # The amount of dollars is subtracted from the total amount and then the quarters are counted.
User_amount %= 100

#Quarters are worth 25 cents
Quarters  = int(User_amount //25)                         # The amount of quarters is subtracted from the total amount and then the dimes are counted.
User_amount %= 25

#Dimes are worth 10 cents
Dimes  = int(User_amount //10)                            # The amount of dimes is subtracted from the total amount and then the nickels are counted.
User_amount %= 10

#Nickels are worth 5 cents 
Nickels  = int(User_amount //5)                           # The amount of nickels is subtracted from the total amount and then the pennies are counted.
User_amount %= 5

#Pennies are worth 1 cent
Pennies  = int(User_amount //1)                           # The program will print out the amount of dollars, quarters, dimes, nickels, and pennies in the inputted amount.
User_amount %= 1

print(f"Your amount {amount} consists of")                # Print results
print(f"Dollars {Dollars}\nQuarters {Quarters}\nDimes {Dimes}\nNickels {Nickels}\nPennies {Pennies}")
