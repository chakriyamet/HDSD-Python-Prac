number = int(input("Enter any numbers you want!: "))
reverse = 0 
while number!=0:
    reverse = reverse*10 + number%10
    number = number //10
    
print("Your reverse number is:", reverse)
    