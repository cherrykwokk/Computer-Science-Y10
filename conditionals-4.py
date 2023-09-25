name1 = input("Enter name of first person")
name2 = input("Enter name second person")

date1day = int(input("Enter the day of the first person's birth"))
date1month = int(input("Enter the month of the first person's birth"))
date1year = int(input("Enter the year of the first person's birth"))

date2day = int(input("Enter the day of the second person's birth"))
date2month = int(input("Enter the month of the second person's birth"))
date2year = int(input("Enter the year of the second person's birth"))

if date1month > 13:
    print("Try again1")
    
elif date2month > 13:
    print("Try again2")
    
elif date1day > 32:
    print("Try again3")
    
elif date2day > 32:
    print("Try again4")


elif date2year < date1year:
    print(name2)
    
elif date2year > date1year:
    print(name1)

elif date2month < date1month:
    print(name2)
    
elif date2month > date1month:
    print(name1)
    
elif date2day < date1day:
    print(name2)
    
elif date2day > date1day:
    print(name1)