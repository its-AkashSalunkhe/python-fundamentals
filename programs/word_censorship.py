
with open("content.txt", "r") as f:
    contentt = f.read()
    newcontent = contentt.replace("Donkey", "######")

with open("content.txt", "w") as f:
    f.write(newcontent)