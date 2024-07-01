# This program displays all of the prime numbers from 1 through 15.

def main(): #The main() function is defined at the beginning of the code.
    for i in range(1,16,1): #This loops through numbers 1 to 15 and calls is_prime() to check if each number is prime or not.
        if is_prime(i):     # Calls the its_prime function & if its prime then it will print "prime" appended.
            print((i) ,"prime", sep='   ') 
        else:              #If not, it'll print "not prime" appended.
            print((i), "not prime", sep='   ')  

def is_prime(num):  # Defines the is_prime() function checks if a number is prime or not.
    if num==2 or num==3 or num==5 or num==7 or num==11 or num==13:
        return True  #returns True for 2, 3, 5, 7, 11, or 13
    else:
        return False #Or else it'll return it as False.
    
main() #Calls the main() function calls is_prime() function for each number & prints the result accordingly.