#BMI CALCULATOR

print("welcome to our bmi calculator")

height=float(input('enter your height in cm: '))
weight= float(input("enter your  weight in kg: "))

bmi= round(weight/(height/100)**2)

print(bmi)
if bmi<18.5:
    print("you are under weight")
elif bmi>=18.8 and bmi <25:
    print("you have  a normal weight")
elif bmi >=25 and bmi<30:
    print("you are over weight")
elif bmi>=30 and bmi<35:
    print("you are obese")
else:
    print("you are clinically obese")