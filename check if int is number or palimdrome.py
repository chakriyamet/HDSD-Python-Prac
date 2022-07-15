number = int(input("Enter number as you wish: " ))
a = number
reverse = 0 
while number!=0:
    reverse = reverse*10 + number%10
    number = number //10
    print("Reverse number:", reverse)   
     
if (a==reverse):
    print('True')
else:
    print('False')

    
    
