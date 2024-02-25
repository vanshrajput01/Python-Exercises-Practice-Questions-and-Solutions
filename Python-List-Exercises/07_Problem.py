# Different ways to clear a list in Python

# Solution One

temp_list = [1,2,3,4,5,6,7,8]

print(temp_list)

temp_list.clear()

print(temp_list)

# Solution Two

temp_list = [1,2,3,4,5,6,7,8]

i = 0


for element in range(0,len(temp_list)):
    if element == 8:
        break
    else:
        temp_list.pop()


print(temp_list)








