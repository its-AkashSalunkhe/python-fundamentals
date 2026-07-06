# Sets are Mutable
# Order doesn't matter
# Repeatation is not allowed
# Cannot contains duplicate values
# There is no way to change items in set


# Empty set 

# a = set()    --> This is an empty set

a = {23, 43, 5, 343, 5, 5, 34, 5}
print(a)


a = {23, 43, 5, 343, 5, 5, 34, 5, "Akash", "Harry"}
print(type(a))

a.add("Prabhu")
print(a)

a.remove(5)
print(a)

b = {43, 543, 43, 5635, 5, "Akash" }

print(a.intersection(b))
print(a.union(b))