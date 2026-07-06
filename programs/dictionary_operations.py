# Cannot Contain Duplicate values
# it is mutable
# it is unordered
# it is indexed


#marks = {}   # This is Empty Dicstionary


marks = {
    "Akash" : 100,
    "Rohan" : 87,
    "Pandu" : 54,
    "list": [1,54,45,566],
    0 : "Mango",
    12 : "DJ"

}

# print(marks["Akash"])
# print(marks["list"])

# print(marks[12])
# print(type(marks))

# print(marks.items())   # Prints all the items in dictionary in tuple form
# print(marks.keys())   # Prints all the items in dictionary in tuple form
# print(marks.values())   # Prints all the items in dictionary in tuple form

# marks.update({"Akash":455})
# print(marks)
# marks.update({"Akash":63, "Mahesh":343})
# print(marks)

print(marks.get("Akash"))
print(marks["Akash"])

# marks.get("Akash") and marks["Akash"] will print the same values then what's the difference
# The difference is :-

print(marks.get("Akash3"))   #  -->  will give "None"
print(marks["Akash3"])       #  -->  will give "Error"

