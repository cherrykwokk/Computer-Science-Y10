num= int(input("Enter size of array"))

numbers = []
for i in range(num):
    number = float(input("Enter a number"))
    numbers.append(number)

sum = 0.0
for number in numbers:
    if number % 2 == 0:
        sum += number

print(sum)