print("welcome agin to our rolllercoster")
height=int(input("enter your height in cm: "))

if height>120:
    print("you can ride the roller coster")
    
    age=int(input("enter your age"))
    if age>18:
        print("you will have to pay adult price $20")
    elif age<12:
        print("please pay $5")
    elif age>=12 and age<=18:
        print("please pay $7")
else:
    print("you will have to grow taller to ride")
    