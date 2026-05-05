x = int(input("Enter the number:"))
y = int(input("Enter the number:"))
z = int(input("Enter the number:"))

if (x<y) and (x<z):
    print("x is the smallest number.")
    
elif (y<x) and (y<z):
    print("y is the smallest number")
    
else:
    print("z is the smallest nuumber.")