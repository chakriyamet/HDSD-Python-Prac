initial_list = [12,12,34,5,1,2,3,0,8]
new_list =[]
while initial_list:
    mininum = initial_list[0]
    for i in initial_list:
        if mininum > i:
            mininum = 1
    #new_list.insert(a, mininum)
    new_list.append(mininum)
    #initial_list.remove(mininum)
print(new_list)
    
