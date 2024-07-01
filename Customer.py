# Define a class called 'Person'
class Person:
    
    # Initialize the class with the attributes of Name, Address, and Mobile_Number
    def __init__(self, Name, Address, Mobile_Number):
        self.__Name = Name
        self.__Address = Address
        self.__Mobile_Number = Mobile_Number

    # Define a mutator method for the attribute 'Name'
    def set_Name(self, Name):
        self.__Name = Name

    # Define a mutator method for the attribute 'Address'
    def set_Address(self, Address):
        self.__Address = Address

    # Define a mutator method for the attribute 'Mobile_Number'
    def set_Mobile_Number(self, Mobile_Number):
        self.__Mobile_Number = Mobile_Number

    # Define an accessor method for the attribute 'Name'
    def get_Name(self):
        return self.__Name

    # Define an accessor method for the attribute ‘Address'
    def get_Address(self):
        return self.__Address

    # Define an accessor method for the attribute ‘Mobile_Number'
    def get_Mobile_Number(self):
        return self.__Mobile_Number



# Define a subclass called 'Customer' that inherits from the 'Person' class
class Customer(Person):

    # Initialize the subclass with the superclass' __init__ method and the additional attributes of customer ID and mailing list
    def __init__(self, Name, Address, Mobile_Number, Customer_ID, Mailing_List):
        Person.__init__(self, Name, Address, Mobile_Number)
        self.__Customer_ID = Customer_ID
        self.__Mailing_List = Mailing_List

    # Define a mutator method for the attribute ‘Customer_ID'
    def set_customer_ID(self, Customer_ID):
        self.__Customer_ID = Customer_ID
        
    # Define a mutator method for the attribute ‘Mailing_List'
    def set_Mailing_List(self, Mailing_List):
        self.__Mailing_List = Mailing_List

    # Define an accessor method for the attribute ‘Customer_ID'
    def get_Customer_ID(self):
        return self.__Customer_ID

    # Define an accessor method for the attribute ‘Mailing_List'
    def get_Mailing_List(self):
        return self.__Mailing_List

# Define a function called 'main'
def main():

    # Prompt the user to enter information about a customer
    Name = input("Enter the name: ")
    Address = input("Enter the address: ")
    Mobile_Number = input("Enter the mobile number: ")
    Customer_ID = input("Enter the customer ID: ")
    Mailing_List = input("Does the customer wish to be on the mailing list?(Yes/No) ")

    # Create an object 'customer_One’ of the 'Customer' class with the entered information
    customer_One = Customer(Name, Address, Mobile_Number, Customer_ID, Mailing_List)


    # Prints out the customer information
    print("\nCustomer information:")
    print('Name:', customer_One.get_Name())
    print('ID:', customer_One.get_Address())
    print('Department:', customer_One.get_Mobile_Number())
    print('Title:', customer_One.get_Customer_ID())

    #return Mailing_List with boolean values
    if Mailing_List == 'Yes' or 'yes':
        xyz = True
    elif Mailing_List == 'No' or 'no':
        xyz = False
    print('On Mailing List:', (xyz))


#call function 'main'
main()
