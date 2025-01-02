x = input("Enter value of x:")
y = input("Enter value of y:")
z = input("Enter value of z:")
temp = x
x = y
y = temp
temp = y
y = z
z = temp
print("value of x after swapping is ",x)
print("value of y after swapping is ",y)
print("value of z after swapping is ",z)