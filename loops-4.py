num = int(input("Enter a number"))

def fibonacci(n):
    a, b = 0, 1

    while b < n:
        a, b = b, a + b

    return b

result = fibonacci(num)
print(result)