x = float(input("Enter the number is:"))
y = float(input("Enter the number is:"))
z = float(input("Enter the number is:"))

if (x+y)>z and (y+z)>x and (z+x)>y:
    S = (x+y+z)/2
    Area = (S*(S-x)*(S-y)*(S-z))
    print("Triangle is possible.")
    
else:
    print("Triangle isn't possible.")