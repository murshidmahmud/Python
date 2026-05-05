#while loop statement ব্যবহার করে কতিপয় সংখ্যার যোগফল বের করার প্রোগ্রাম লেখ?/ ১ হতে ১০০ পর্যন্ত সংখ্যার যোগফল বের করার প্রোগ্রাম লিখ?


n = int(input("Enter the value of n:"))

sum = 0
i = 1
while i<=n:
    
    sum = sum + i
    
    i = i + 1
    
print("The sum is",sum)