import os

directory_path = '/users'

contents = os.listdir(directory_path)

# print(contents)

for item in contents:
    print(item)