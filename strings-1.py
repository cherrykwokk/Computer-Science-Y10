name = input("Enter your first and last name")

position_of_space = name.find(" ")

space = ( )

if name.count(" ") != 1:
    print("Try again")
    
elif name.count(" ") == 1:
    a = name[:position_of_space]
    b = name[position_of_space:]
    print((a.upper()) + (",") + (b.title()))
    

    

    