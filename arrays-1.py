num = int(input("Enter size of array"))

heights = []
for i in range(num):
    height = float(input("Enter height"))
    heights.append(height)

total = 0.0
for height in heights:
    total += height
    average = total/ num

a = sorted(heights)
b = a[-1] - a[0]

print(round(average, 1))
print(round(b, 1))