bazar_list = ['Onion','Ginger','Mouse','Keyboard','Mouse',5,'Mouse',3,8,'Mouse',3.4] # creating a list(লিস্টে [third braket use] হয়)

print(bazar_list)

print(bazar_list[3])                              # positive accessing করার জন্য এই element use করা হয়। 

print(bazar_list[-7])                             # negative accessing করার জন্য এই element use করা হয়।

print(len(bazar_list))                            # লিস্টে কতগুলো আইটেম আছে তা গণণার জন্য এই element use করা হয়

print(bazar_list.count('Mouse'))                  # লিস্টের উপাদান সংখ্যা গণনা করার জন্য এই element use করা হয়। 

print(bazar_list.append(9))                       # লিস্টের শেষে কোন আইটেমকে যুক্ত করতে এই element use করা হয়। 

print(bazar_list.insert(3,"Mobile Phone"))        # লিস্টে কোন নিদিষ্ট পজিশনে কোন আইটেমকে যুক্ত করার জন্য এই element use করা হয়

print(bazar_list.remove('Keyboard'))              # লিস্টের কোন নিদিষ্ট কোন আইটেমকে বিয়োজন করার জন্য এই element use করা হয়।

bazar_list.pop()      
print(bazar_list)                                 # লিস্টের একবারে শেষ আইটেমকে রিমুভ করার জন্য এই element use করা হয়। 

del bazar_list[3]                                                     
print(bazar_list)                                 # একটি লিস্ট থেকে নির্ধারিত element delete করার জন্য এই element use করা হয়।



bazar_list = ['Onion','Ginger','Mouse','Keyboard','Mouse',5,'Mouse',3,8,'Mouse',3.4]
seceond_list = ["Pant",'Shirt','Shoes','belt','watch,etc']

third_list = bazar_list + seceond_list            # এলিমেন্ট সমূহকে join করার জন্য joining element ব্যবহার করা হয় । 
print(third_list)

if 'Shirt' in third_list:
    x = third_list.index('Shirt')                 # index এর ক্ষেত্রে (একটি এলিমেন্ট একটি লিস্টের মধ্যে কত নাম্বারে আছে তা প্রিন্ট করে।)
    print(x)



mylist = [1,2,3,4,5,6,7,8,9,10]
mylist[3] = "Mouse"                               # change elemant এর জন্য 
print(mylist)



mylist = [1,2,3,4,5,6,7,8,9]
mylist.reverse()                                   # reverse element (উল্টা পাশ থেকে এলিমেন্ট সমূহকে সাজানো)
print(mylist)



mylist = [4,6,-9,2,44,66,-15,-4,22,-39,17,22]
mylist.sort()                                      # sort করার ক্ষেত্রে (ছোট থেকে বড়)
print(mylist)

mylist = [4,6,-9,2,44,66,-15,-4,22,-39,17,22]       
mylist.sort(reverse = True)                        # sort করার ক্ষেত্রে (বড়ো থেকে ছোট)
print(mylist)




mylist2 = ['Shirt',"Pant",'Shoes','belt','watch etc']
mylist2.sort()                                     # sort করার ক্ষেত্রে 
print(mylist2)




mylist3 = [1,2,3,4,5,6,7,8,9]                      # ‍slicing করার জন্য 
print(mylist3[2:7])
print(mylist3[:6])
print(mylist3[-4:])

print(mylist3[0:9:2])
print(mylist3[0:9:3])
print(mylist3[::2])
print(mylist3[1::2])






mylist3 = [1,2,3,4,5,6,7,8,9]                      # multiplication করার জন্য (লিস্টের আইটেম সমূহ একই সাথে ৩ বার প্রিস্ট হবে।)
print(mylist3 * 3)

























