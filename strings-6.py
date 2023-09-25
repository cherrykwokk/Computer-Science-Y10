year = int(input("Enter year"))
month = int(input("Enter month"))
day = int(input("Enter day"))

result1 = (year, month, day)
a = 2000+year
result2 = (a, month, day)

if year > 999:
    print(result1)

if year < 1000:
    print(result2)

