from math import remainder

number = int(input("Enter decimal number:"))

while number!=0:
    remainder = number %10
    if(remainder!=0 and remainder!=1):
        print("This is not binary number representation")
        break
    number = number //10
    if (number==0):
        print("This is binary number representation")
    
