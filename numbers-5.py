import math

timeofday = int(input("Enter the time of day in seconds"))

hours = math.trunc(timeofday/60/60)

minutes = math.trunc((timeofday%3600)/3600*60)

print(hours)
print("Hours")
print("And")
print(minutes)
print("Minutes")