


# f = open("info.txt")
# data = f.read()
# print(data)
# f.close()

# We can see above we have to close the file explicitely everytime



with open("info.text")as f:
    print(f.read())


# However by using "With" Statement we don't have to mention to close the file
# everytime, it will automatically closes it