# 1.Prime number between 2 numbers 
amount = 0
for num in range (100, 201):
    if all(num%i !=0 for i in range(2, num)):
        #prime (num)
        amount = amount + 1
print(amount)