# Python | Cloning or Copying a list

# Solution One

temp_list = ["Mango","Banana","Apple","Green Apple"]

temp_list_Copy = temp_list.copy()

print(temp_list_Copy)

# Solution Two

temp_list = ["Mango","Banana","Apple","Green Apple"]

temp_list_Clone = []

for element in temp_list:

    temp_list_Clone.append(element)

print(temp_list_Clone)






