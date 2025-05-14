# Get three numbers from the user
a = floar(int("enter the number:"))
b = float(int("enter the number:"))
c = float(int("enter the number:"))

# Find the maximum using nested ternary operator
max_num = a if (a > b and a > c) else (b if b > c else c)

# Display the result
print("The maximum of the three numbers is:", max_num)