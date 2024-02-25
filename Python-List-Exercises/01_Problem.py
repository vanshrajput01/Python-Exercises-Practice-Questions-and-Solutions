my_list = [1,2,3,4,5]
i = 0
while i < len(my_list):
    if i == 0:
        n = my_list[i] 
        my_list[i] = my_list[len(my_list)-1]
        my_list[len(my_list)-1] = n
    
    i +=1

print(my_list)







