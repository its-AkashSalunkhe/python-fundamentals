class company:
    comname = "ITC"
    def show(self):
        print(f"Name of the employee is {self.name} and company name is {self.comname}")


class coder:
    language = "python"
    def show(self):
        print(f"Your Language is {self.language}")


class programmer(company, coder):
    comname = "ITC Infotech"
    salary = 242542
    def show(self):
        print(f"Name of the Language is {self.language} and salary is: {self.salary}")
    


a = company()
b = coder()
c = programmer()

a.name = "vikram"
b.language = "java"
print(a.comname, c.comname)
a.show()
b.show()
c.show()