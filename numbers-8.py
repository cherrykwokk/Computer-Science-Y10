import math

adjacent = float(input("Enter adjacent side"))
angle = float(input("Enter the adjacent angle"))

def sides(adjacent, angle):
    angle = math.radians(angle)

    hypotenuse = adjacent / math.cos(angle)

    opposite = math.sin(angle) * hypotenuse

    return hypotenuse, opposite

hypotenuse, opposite = sides(adjacent, angle)

print(hypotenuse)
print(opposite)