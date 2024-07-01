# This program prompts the user to enter 5 test scores. 
# Which will display a letter grade for each score and the average and total test scores.

def main(): #The main() function is defined & prompts the user to enter 5 test scores.
    n1 = int(input('Enter test score 1: '))
    n2 = int(input('Enter test score 2: '))
    n3 = int(input('Enter test score 3: '))
    n4 = int(input('Enter test score 4: '))
    n5 = int(input('Enter test score 5: '))
    
    print('\nScore\t NumericGrade\t LetterGrade')   #Prints one new line for Score & tabs in outside of NumericGrade & LetterGrade.
    print('----------------------------------------------------')   #Prints a long line border.
    
    #Lines 15-19 will print 5 scores & calls the determine_grade() & specify the score as a letter grade.
    print('Score1:','\t', n1, "\t\t", determine_grade(n1))  
    print('Score2:','\t', n2, "\t\t", determine_grade(n2))
    print('Score3:','\t', n3, "\t\t", determine_grade(n3))
    print('Score4:','\t', n4, "\t\t", determine_grade(n4))
    print('Score5:','\t', n5, "\t\t", determine_grade(n5))
    print('----------------------------------------------------')   #Prints a long line border.
    
    avg = calc_average(n1,n2,n3,n4,n5)   #avg is equivalent to calc_average() function & it calls for the function.
    print('\nAverage score:',avg, '\t\t', determine_grade(avg)) 
    
    total_score = calc_total(n1,n2,n3,n4,n5)    #Total_score is equivalent to calc_total() function & it calls for the function.
    print('\nTotal score: ',float(total_score)) 

def calc_average(n1,n2,n3,n4,n5): #Defines the cal_average() function takes 5 test scores as inputs.
    return (n1+n2+n3+n4+n5)/5   #Which will return the average by the sum of 5 tests dividing by 5.

def calc_total(n1,n2,n3,n4,n5): #Defines calc_total() function takes 5 test scores as inputs.
    return (n1+n2+n3+n4+n5) #Which will returns the sum of all 5 test scores.

def determine_grade(score): #Define determine_grade() function.
    if score < 60:    #If score is less than 60 then the letter is an "F"
        grade = 'F'
    elif score < 70:  #If score is less than 70 then the letter is an "D"
        grade ='D'
    elif score < 80:  #If score is less than 80 then the letter is an "C"
        grade ='C'
    elif score < 90:  #If score is less than 90 then the letter is an "B"
        grade ='B'
    else:
        grade = 'A'  #Or else if the scores are not like the top then it's considered an "A"
    return grade    #Returns the corresponding letter grade based on the input numeric score's range.

main()  #The main() function calls the determine_grade(), calc_average(), and calc_total() functions to calculate the grades and scores.