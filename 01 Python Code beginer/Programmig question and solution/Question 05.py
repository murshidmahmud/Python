# ধনাত্নক পূর্ণসংখ্যার Factorial(গুণণ) এর মান নির্ণয় করার প্রোগ্রাম লেখ?

import math

n = int(input("Enter the number:"))

i = 1
sum = 1
while(i<=n):
    sum = sum * i
    i = i + 1
print("The factorial is:",sum)