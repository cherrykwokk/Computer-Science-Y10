num = int(input("Enter the size of the array: "))

heights = []
for i in range(num):
    height = float(input("Enter the height"))
    heights.append(height)

a = sorted(heights)

if num % 2 == 0:
    mid = num // 2
    median = (a[mid - 1] + a[mid]) / 2
    
else:
    mid = (num - 1) // 2
    median = a[mid]

print(median)