height = int(input("Enter a number"))

def pyramid(height):
    for i in range(1, height + 1):
        print('*' * i)
        
pyramid(height)

        