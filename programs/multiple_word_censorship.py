words = ["donkey", "monkey", "Hippo"]

with open("content2.txt", "r") as f:
    contentt = f.read()
    for word in words:
        newcontent = contentt.replace(word, "#"* len(word))

with open("content2.txt", "w") as f:
    f.write(newcontent)