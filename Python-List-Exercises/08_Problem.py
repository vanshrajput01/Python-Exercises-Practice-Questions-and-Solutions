# Python | Reversing a List

# Solution one

temp_list = [1,2,3,4,5,6,7,8]

temp_list.reverse()

print(temp_list)

# Solution two

temp_list = [1,2,3,4,5,6,7,8]

reverse_list = []
i  = 0

for element in range(1,len(temp_list)+1):
    if element == 9:
        break
    else:
        reverse_list.append(temp_list[-element])
print(reverse_list)





