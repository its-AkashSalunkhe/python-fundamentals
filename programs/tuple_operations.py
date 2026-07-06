#Tuple is also Immutable, so whenever you performed operations and changed the tuple, it will return the copy of it, acutal tuple remains unchanged

a = (1,24,455,"akash","rohit", 34.53)
print(a)


t1 = (1, 2, 3, 2, 2, 4)
print(t1.count(2))   # Output: 3


t2 = (10, 20, 30, 20)
print(t2.index(20))  # Output: 1


t3 = (5, 2, 9, 1)
print(len(t3))      # 4
print(max(t3))      # 9
print(sorted(t3))   # [1, 2, 5, 9]


# Concatenation (+)
(1, 2) + (3, 4)   # (1, 2, 3, 4)


# Repetition (*)
(1, 2) * 3   # (1, 2, 1, 2, 1, 2)

# Membership (in)

3 in (1, 2, 3)   # True