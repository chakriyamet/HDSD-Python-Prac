a = [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,12,13,14,15]
new_list=[]
while a:
    minimum = a[0]
    for i in a:
        if minimum > i:
            minimum =i
    #new list.insert(0, minimum)
    new_list.append(minimum)
    a.remove(minimum)
print(new_list)
    

            