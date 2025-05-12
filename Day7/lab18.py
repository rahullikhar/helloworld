x = [1, 2, 3]
y = [1, 2, 3]
z = x


# Case 1: Identity comparison (is)
if x is y:
    print("True")
else:
    print("False")

# Case 2: Comparing references (is)
if x is z:
    print("True")
else:
    print("False")