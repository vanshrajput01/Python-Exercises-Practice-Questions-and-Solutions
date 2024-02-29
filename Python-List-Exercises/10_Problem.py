# Python | Count occurrences of an element in a list

# solution One

chai_type = ["Masala Chai","Green Chai","Lemon Chai"]

print(chai_type.count("Green Chai")) 

print(chai_type.count("Green chai")) # This methrod is Case sensitive

print(chai_type.count("Black chai")) # not Give an Error

# Solution Two

chai_type = ["Masala Chai","Green Chai","Lemon Chai"]

find_element = "Masala Chai"

counter = 0

for element in range(0,len(chai_type)+1):
    if element == "Masala Chai":
        counter = counter + 1
    
print("Your",counter)
    




