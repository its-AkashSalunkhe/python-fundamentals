class employee:
    def __init__(self):
        print("This is employee constructor")
    a = 1 

class manager(employee):
    def __init__(self):
        print("This is manager constructor")
    b = 2

class ceo(manager):
    def __init__(self):
        super().__init__
        print("This is CEO constructor")
    c = 3


x = employee()
y = manager()
z = ceo()


print(x.a)
print(y.a, y.b)
print(z.a,z.b,z.c)