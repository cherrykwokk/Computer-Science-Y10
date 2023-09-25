import math

num = int(input("Enter num"))
flag = True

for Q in range(2, math.ceil(math.sqrt(num)) + 1):
    if num % Q == 0:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")