# This program calculates following and displays Grams of fat, Fat calories, Grams of carbs, Carb calories in 2 decimal positions.

#Defines the showCarbs() function & prints input values, calculates & prints calories from fat and carbs.
def showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs):

        #This code block outputs the input values and calculated values.
        print(f'If fat grams consumed entered is {int(gramsFat)}\n')
        print(f'If carbohydrate grams consumed entered is {int(gramsCarbs)} then the output would be:\n')
        print(f'Grams of fat: {gramsFat:.2f}\n')
        print(f'Fat calories: {caloriesFat:.2f}\n')
        print(f'Grams of carbs: {gramsCarbs:.2f}\n')
        print(f'Carb calories: {caloriesCarbs:.2f}\n')

#The main() function prompts user input for grams of fat, fat calories, grams of carbs, & carb calories and passes them as arguments to showCarbs() function.
def main(): 

    #It calculates the calories from fat & carbs using the input values and passes them as additional arguments to the showCarbs() function.
    gramsFat= float(input("Enter Grams of fat: ")) #This accepts user input for gramsFat, & converts them to floating-point numbers.
    user_caloriesFat= float(input("Enter Fat calories: ")) #This accepts user input for user_caloriesFat & converts them to floating-point numbers.
    gramsCarbs= float(input("Enter Grams of carbs: ")) #This accepts user input for gramCarbs & converts them to floating-point numbers.
    user_caloriesCarbs= float(input("Enter Carb calories: ")) #This accepts user input for user_caloriesCarbs & converts them to floating-point numbers.

    Calories_from_fat = gramsFat * 9.125  #Calories_from_fat is equivalent to gramsFat times 9.125.
    caloriesFat = Calories_from_fat       #caloriesFat is equivalent to Calories_from_fat.

    Calories_from_carbs = gramsCarbs * 4.159 #Calories_from_carbs is equivalent to gramsCarbs times 4.159.
    caloriesCarbs = Calories_from_carbs      #caloriesCarbs is equivalent to Calories_from_carbs.

    showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs) #Calls showCarbs() with input and calculated values to display results.
main() #Calls the main() function which will call showCarbs() with the user inputs and calculated values to display the results.