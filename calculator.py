#************************************* HOW TO BUILD A CALCULATOR APP ***************************************************************
#this takes a case of two numbers ie num 1 and num2 which performs the following operations as listed below
#the user is to select an operation to perform
#the user is to enter the first number
#the user is to enter the second number
#the result is then printed out

#ADD
#SUBTRACT
#MULTIPLY
#DIVIDE
#MODULUS
#POWER
#ROOT
print('select an operation to perform:')
print('1. ADD')
print('2. SUBTRACT')
print('3. MULTIPLY')
print('4. DIVIDE')
print('5. MODULUS')
print('6. POWER')


operation = int(input("enter the operation you want to perform: "))

if operation == 1:
    num1 =int( input("enter first nmber"))
    num2= int(input("enter secon1d number"))
    result = num1 + num2
    print(result)
elif operation ==2:
    num1 =int( input("enter first nmber"))
    num2= int(input("enter secon1d number"))
    result = num1 - num2
    print(result)

elif operation ==3:
     num1 =int( input("enter first nmber"))
     num2= int(input("enter secon1d number"))
     result = num1 * num2
     print(result)

elif operation==4:
     num1 =int( input("enter first nmber"))
     num2= int(input("enter secon1d number"))
     result = num1 / num2
     print(f"the result is {result}")

elif operation==5:
     num1 =int( input("enter first nmber"))
     num2= int(input("enter secon1d number"))
     result = num1 % num2
     print(result)

elif operation==6:
     num1 =int( input("enter first nmber"))
     num2= int(input("enter secon1d number"))
     result = num1 ** num2
     print(result)
elif operation>=7:
    print("invalid operation selected")
else:
    print("not supported operation")
print("thank you for using the calculator, welcome bank again")
