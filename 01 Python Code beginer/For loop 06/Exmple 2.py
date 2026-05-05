mylist = []

for i in range(5):
    print('Enter the', i+1, 'th number:',end="")
    x = input()
    mylist.append(int(x))
print(mylist)



# উক্ত লিস্ট থেকে বড় এবং ছোট সংখ্যা বের করার নিয়ম:

bigger = mylist[0]
smallest = mylist[0]

for number in mylist:
    if number>bigger:
        bigger = number
    if number<smallest:
        smallest = number
print("The bigger number is",bigger)
print("The smallest number is",smallest)




# উক্ত লিস্ট থেকে এলিমেন্টগুলোকে যোগ করার নিয়ম:

sum = 0
for num in mylist:
    sum = sum + num
print('The summation is:',sum)



# উক্ত লিস্ট থেকে এলিমেন্টগুলোর গড় বের করার নিয়ম:

sum = 0
for num in mylist:
    sum = sum+num
    
avg = sum/ len(mylist)
print('The avarege is:',avg)




# একই লিস্ট থেকে বড়ো সংখ্যা এবং ছোট সংখ্যা এবং গড় বের করার নিয়ম:


x = int(input("Enter the 1 th number:"))

bigger = x
smaller = x

sum = x

for i in range(2,11):
    print('Enter the', i ,'th number:', end="")
    x = int(input())
    if x>bigger:
        bigger = x
    if x<smaller:
        smaller = x
        
    sum = sum + x
    
print('The bigger number:',bigger)
print('The smaller number:',smaller)
print('The avarege number:', sum / 10)



















































