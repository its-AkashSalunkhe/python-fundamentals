class Employee:
    language = "Marathi"    # This is called class Attribute
    salary = 50000000

    def getInfo(self):
        print(f"The language is: {self.language} and salary is: {self.salary}")


    @staticmethod
    def greet():
        print("Good Morning")

    
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age          # Dunder method, automatically get called without requiring function to be called
        print("Dunder method called")       # only executes when object is created

        
    
Akash = Employee("Salunkhe",434333, 43)
# print(Akash.language)
# print(Akash.salary)                  
    
print(Akash.name, Akash.salary, Akash.age)

# Akash.salary = 545645454 # This is called method (Instance) Attribute

Akash.getInfo()
Akash.greet()
# Employee.getInfo(Akash)

# rahul = Employee()     this object is created to called the dunder function again 