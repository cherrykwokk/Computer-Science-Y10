sentence = input(str("Enter a sentence"))

a = sentence.count("a")
e = sentence.count("e")
i = sentence.count("i")
o = sentence.count("o")
u = sentence.count("u")
vowels = (a + e + i + o + u)

print("The number of vowels is", vowels)