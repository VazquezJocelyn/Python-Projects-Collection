def main():
   num_list = []                                                #Creates an empty list called 'num_list'.
   for i in range(8):                                           #This is a for loop that runs 8 times.
      num_list.append(int(input('Enter a number from 1-8: ')))  #Prompts the user to enter a number between 1 - 8 and appends(known as including) user's numbers into 'num_list' as an integer. 
   low = min(num_list)                                          #Finds the lowest value in the 'num-list' & store it in the variable 'low'.
   high = max(num_list)                                         #Find the highest value in the 'num_list' and store it in the variable 'high'.
   total = sum(num_list)                                        #Calculates the sum of all numbers in the 'num_list' & stores it in the variable 'total'.
   average = total/len(num_list)                                #Calculates the average of all numbers in the 'num_list' & stores it in the variable 'average'.
   
   tup = tuple(num_list)                                        #Converts the 'num_list' to a tuple and store it in the variable 'tup'.

   print(f'List:', num_list)                                    #Prints the 'num_list', 'low', 'high', 'total', 'average', and 'tup' variables using f-string format
   print(f'Low:', low)
   print(f'High:', high)
   print(f'Total:', total)
   print(f'Average:', average)
   print(f'Tuple:' , tup)
   print(f'Tuple contents printed in reverse order:')           #Prints the contents of the 'num_list' in reverse order.
   for i in num_list[::-1]:
      print(int(i))
main()                                                          #Calls the 'main' function to execute the code.
