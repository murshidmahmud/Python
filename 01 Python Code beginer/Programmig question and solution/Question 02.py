# তিন বাহুর মান দিয়ে ত্রিভুজের সম্ভাব্যতা যাচাই পূর্বক ক্ষেত্রফল নির্ণয়ের একিট প্রোগ্রাম লিখ অথবা শুধু ত্রিভুজের ক্ষেত্রফল নির্ণয়ের একটি প্রোগ্রাম লিখ?

import math

x = float(input("Enter the 1st line of value:"))
y = float(input("Enter the 2nd line of value:"))
z = float(input("Enter the 3rd line of value:"))

if (x+y)>z and (y+z)>x and (z+x)>y:
    S = (x+y+z)/2
    Area = math.sqrt(S*(S-x)*(S-y)*(S-z))
    print("The Triangle is possible")
    
else:
    print("The Triangle isn't possible")





















