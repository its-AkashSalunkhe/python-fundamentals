class company:
    comname = "ITC"
    def show(self):
        print(f"Name of the employee is {self.name} and company name is {self.comname}")


class programmer(company):
    comname = "ITC Infotech"
    def show(self):
        print(f"Name of the Language is {self.language}")
    


a = company()
b = programmer()
a.name = "vikram"
b.language = "java"
print(a.comname, b.comname)
a.show()
b.show()