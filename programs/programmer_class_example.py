class Programmer:
    name = "Name"
    salary = "salary"
    company =  "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin =  pin
    
akash = Programmer("Salunkhe", 3434343, 43434)
print(akash.name,akash.salary, akash.pin)

sid = Programmer("Nikam", 35435, 434)
print(sid.name,sid.salary, sid.pin)
