 অথবা, কী বোর্ড হতে তিনটি সংখ্যা রিড করে বড়ো সংখ্যটি প্রিন্ট করার প্রোগ্রাম লিখ?

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))

if (a>b) and (a>c):
    print("The biggest number is a")

elif (b>a) and (b>c):
    print("The biggest number is b")


else:
    print("The biggest number is c")
