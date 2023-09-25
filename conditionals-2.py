a = int(input("Enter a year"))

if a%400 == 0:
    print("Leap year")
    
if a%100 == 0:
    print("Non leap year")
    
if a%4 == 0:
    print("Leap year")

else:
    print("Non leap year")