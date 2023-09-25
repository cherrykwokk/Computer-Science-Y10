num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

def divide(num1, num2):
    a = num1 / num2
    b = "{:.3f}".format(a)
    return b[:5]

result = divide(num1, num2)
print(result)