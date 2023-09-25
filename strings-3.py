sentence = str(input("Enter a sentence"))

space = sentence.find(" ")

a = sentence[space:]
b = a.split(" ")
c = b[1]
d = c.title()

print(d)