class employee:
    a = 1 

class manager(employee):
    b = 2

class ceo(manager):
    c = 3


x = employee()
y = manager()
z = ceo()


print(x.a)
print(y.a, y.b)
print(z.a,z.b,z.c)