name = "Murshid"
mylist = []

for letter in name:
    mylist.append(letter)
print(mylist)


name = "Mahmud"
mylist = [letter for letter in name]
print(mylist)






mylist = []

for number in range(1,11):
    mylist.append(number)
print(mylist)


mylist = [number for number in range(1,11)]
print(mylist)






mylist = [number for number in range(1,11) if number%2==0]                   # জোড় সংখ্যা বের করা প্রোগ্রাম
print(mylist)



mylist = [number for number in range (1,11) if number%2==1]                  # বিজোড় সংখ্যা বের করার প্রোগ্রাম
print(mylist)



mylist = [number for number in range(1,11) if number%2==0 and number>5]      # ৫ এর থেকে বড় জোড় সংখ্যা বের করার প্রোগ্রাম 
print(mylist)


mylist = [number for number in range(1,11) if number%2==1 or number>5]       # ৫ এর থেকে ছোট বিজোড় সংখ্যা বের করার প্রোগ্রাম
print(mylist)




mylist = [1,2,3,4,5,6,7,8,9]

newlist = ['even' if number%2==0 else 'odd' for number in mylist]            # জোড় বিজোড় সংখ্যা একসাথে বের করার প্রোগ্রাম
print(newlist)
