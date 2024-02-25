# Minimum of two numbers in Python

# Solution one

number_one = int(input("Enter one Number : "))
number_two = int(input("Enter another Number : "))

if number_one > number_two:
    print(f"{number_two}")

else:
    print(f"{number_one}")

# Solution two
    
print(min(number_one,number_two))
