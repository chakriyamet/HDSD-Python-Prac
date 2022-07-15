num = int(input("Please enter any numbers: "))
reverse = 0
while ( num >0):
    reminder = num % 10 # find somnol
    reverse = ( reverse *10)+ reminder 
    num = num //10
    
print("\n Reverse of entered number is = %d" %reverse)

#reverse just make the list of numbers turn back, not list from biiger to smaller. 
#by that, we need to multiply by 10.
#ex.num = 6371  ---> 1736
# num //10 = 637
# num % 10 = 1, reminder = somnol
# devide by 10 is like a loop. Use loop while cuz we devide many times. 
# 6371 / 10 = 637, 1 ----  1 * 10 + 7 = 17 
# 637 / 10= 63, 7 ------17 * 10 + 3 = 173 
# 63 / 10 =6, 3 -----173 * 10 + 6 = 1736 