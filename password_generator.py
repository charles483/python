#2 lowercase 
#2 uppercase
#2 digits from 0-9
#2 special characters such as question marks and exclamation marks
import random
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']
print("Welcome to the PyPassword Generator!")
nr_letters=2
nr_symbols=2
nr_numbers=2
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(password)