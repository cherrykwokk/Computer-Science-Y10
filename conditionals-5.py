todayday = int(input("Enter today's day"))
todaymonth = int(input("Enter today's month"))
todayyear = int(input("Enter today's year"))

birthday = int(input("Enter your birthday's day"))
birthmonth = int(input("Enter your bithday's month"))
birthyear = int(input("Enter your birthday's year"))

year = todayyear - birthyear
month = todaymonth - birthmonth
day = todayday - birthday

if todayday > 32:
    print("Try again1")

elif birthday > 32:
    print("Try again2")
    
elif todaymonth > 13:
    print("Try again3")
    
elif birthmonth > 13:
    print("Try again4")

elif todaymonth < birthmonth:
    print(year - 1)
        
elif todaymonth == birthmonth and todayday < birthday:
    print(year - 1)
        
else:
    print(year)