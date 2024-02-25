# Python program to swap two elements in a list
my_list = [1,2,3,5,6,7]

i = 0

while i < len(my_list):
    if i == 2:
        n = my_list[i]
        my_list[i] = my_list[len(my_list) - 3]
        my_list[len(my_list) - 3] = n
    
    i +=1

print(my_list)
    
