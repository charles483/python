# LEAP YEAR CHALLENGE

print("welcome again here we check whether the given year is a leap year or not")

year=int(input("enter your year of choice"))

if year%4==0:
    if year%400==0:
        print("this is a leap year")
    else:
        print("not a leap year")
    print(f"so the year {year} is a leap year")
else:
    print('not a leap year')