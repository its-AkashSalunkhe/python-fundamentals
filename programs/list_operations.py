# List are Mutable ( it can be changed after creating ) Conversely Strings are Immutable (Can't be changed after creating)

friends = ["Akash", "Aditya", "Siddhesh", "Mahesh", 545.454, 144, "Apple"]

print(friends[3])
print(friends)

friends[3] = "Rushikesh"
print(friends)                 # here the list has been changed