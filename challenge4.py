# this is a pizza ordering program

print("welcome to python pizza deliveries")

size = input("what size do you want? S,M, or L: ")
add_pepperoni=input("do you want pepperoni? Y or N: ")
extra_cheese=input("do you want extra cheese? Y or N: ")
price=0
if size.lower()=="S":
    price=15
    if add_pepperoni.lower()=='y':
      price+=2
    if extra_cheese.lower()=='y':
        price+=1
elif size.lower=='m':
    price=20
    if add_pepperoni.lower()=='y':
      price+=3
    if extra_cheese.lower()=='y':
        price+=1
elif size.lower()=='l':
    price=25
    if add_pepperoni.lower()=='y':
        price+=3
    if extra_cheese.lower()=='y':
        price+=1
else:
    print("you")
print(f"your total price is {price}")