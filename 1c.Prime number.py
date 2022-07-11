# 1c.Prime number between 2 numbers 
firstnum = 1
secondnum = 100
amount = 0
prime = True

for betnum in range (firstnum, secondnum+1):
    if betnum > 1:
        for primenum in range(2, betnum):
            if betnum % primenum ==0:
                prime = False
                break
        if(prime):
            print(betnum)
            ammount = amount + 1
            
        prime = True
print(" The amount of prime number is:", amount)