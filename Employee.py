# Defines a class named 'Employee' with attributes: Name, ID, Department, and Title.
class Employee:

    # Initializes the class with four attributes: Name, ID, Department, & Title.
    def __init__(self, Name, ID, Department, Title):
        self.__Name = Name
        self.__ID = ID
        self.__Department = Department
        self.__Title = Title

    # Defines mutator methods for each attribute.
    def set_name(self, Name):
        self.__Name = Name

    def set_ID(self, ID):
        self.__ID = ID

    def set_department(self, Department):
        self.__Department = Department


    # Defines accessor methods for each attribute.
    def set_title(self, Title):
        self.__Title = Title

    def get_name(self):
        return self.__Name

    def get_id(self):
        return self.__ID

    def get_department(self):
        return self.__Department

    def get_title(self):
        return self.__Title

# Defines a function named 'main'.
def main():

    # Creates three objects of class 'Employee' and set the given values.
    Employee_One = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    Employee_Two = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    Employee_Three = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    # Prints the output in which it displays information about each Employee object.
    print("\nEmployee 1:")
    print('Name:', Employee_One.get_name())
    print('ID:', Employee_One.get_id())
    print('Department:', Employee_One.get_department())
    print('Title:', Employee_One.get_title())

    print("\nEmployee 2:")
    print('Name:', Employee_Two.get_name())
    print('ID:', Employee_Two.get_id())
    print('Department:', Employee_Two.get_department())
    print('Title:', Employee_Two.get_title())

    print("\nEmployee 3:")
    print('Name:', Employee_Three.get_name())
    print('ID:', Employee_Three.get_id())
    print('Department:', Employee_Three.get_department())
    print('Title:', Employee_Three.get_title())

# Calls the function 'main'
main()
