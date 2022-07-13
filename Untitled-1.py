initial_list = [12,12,34,5,1,2,3,0,8]
new_list =[]
while initial_list:
    minimum = initial_list[0]
    for i in initial_list:
        if minimum > i:
            minimum = 1
    #new_list.insert(a, minimum)
    new_list.append(minimum)
    initial_list.remove(minimum)
    #initial_list.remove(minimum)
print(new_list)
    
