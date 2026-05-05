import math

a = int(input('Enter the number:'))
b = int(input('Enter the number:'))
lcm = int((a*b)/math.gcd(a,b))
print(lcm)



import numpy as np

print(np.lcm(40,50))