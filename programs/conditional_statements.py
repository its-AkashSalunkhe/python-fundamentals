age = int(input("Enter your age:"))

if(age%2==0):
    print("your age is even")
else:
    print("Your age is Odd")

if(age>=18):
    print("You are eligible for driving")
elif(age==0):
    print("age cannot be \"0\" ")
elif(age<0):
    print("Please Enter a valid age")
else:
    print("You are not eligible, underage")