#This program writes the range of numbers 
#from 11 to 111 to the numList file.

def main():
   
    outfile = open('numList.txt', 'w')   #Opens a file named numList
    
    for i in range(11,112):              #Writes the range of numbers into the file.
        
        outfile.write(str(i)  +'\n')   
                  
    outfile.close()                     #Close the file.

main()                                  #Calls the 'main' function to execute the code.
