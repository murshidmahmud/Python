name = "Murshid Mahmud"
mylist = [letter for letter in name]
print(mylist)




mylist = []
for number in range(1,11):
    mylist.append(number)
    print(mylist)



mylist = [number]
mylist = [number for number in range(1,110)]
print(mylist)




mylist = [ number for number in range(1,111)]
print(mylist)





mylist = [number]
mylist = [number for number in range(1,11) if number%2==0]        # জোড় সংখ্যা বের করার নিয়ম
print(mylist)




mylist = [number]
mylist = [number for number in range(1,11) if number%2==1]        # বিজোড় সংখ্যা বের করার নিয়ম
print(mylist)





mylist = [number]
mylist = [number for number in range(1,11) if number%2==0 and number>5]        
print(mylist)





mylist = [number]
mylist = [number for number in range(1,11) if number%2==0 or number>5]        # পার্থক্য বের করার নিয়ম
print(mylist)






mylist = [1,15,28,45,99,145]
newlist = ['even' if number%2==0 else "odd" for number in mylist]             # জোড় বিজোড় একসাথে বের করার নিয়ম
print(newlist)









