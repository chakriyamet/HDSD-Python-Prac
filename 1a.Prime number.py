# 1a.Prime number 
amount = 0
for num in range(100, 201):
    for i in range(2, num):
        if(num%i ==0):
            break
    else:
        print(num)
        amount = amount + 1 