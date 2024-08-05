#multiple if conditions
print("welcome agin to our rolllercoster")
height=int(input("enter your height in cm: "))
bill=0
if height>120:
    print("you can ride the roller coster")
    
    age=int(input("enter your age"))
    if age>18:
        bill=20
        print("adult ticket: $20")
    elif age<12:
        bill=5
        print("children ticket: $5")
    elif age>=12 and age<=18:
        bill=7
        print("youth tickets: $7")
    
    wantphoto=input("do ypu want a photo taken ?:  Y or N: ")
    if wantphoto.lower()=="y":
        bill+=3
        
    if wantphoto.lower()=='n':
        bill+=0
        print("thank you and enjoy your ride")
    print(f"your total bill is {bill}")
       
else:
    print("you will have to grow taller to ride")
    