# Python | Ways to check if element exists in list

chai_types = ["Masala Chai","Lemon Tea","Ginger Tea","Black Tea","Simple Chai"]

element = input("Enter any Element you find in this list : ")

if chai_types.count(element) == 0:
    print(f"No. {element} is not in this List")

else:
    print(f"Yes. {element} is in this List")

