mytuple = ('mango','banana','jackfruit','painapple','lichi')  # creating a tuple an iteam (tuple এর ক্ষেত্রে (first braket) ব্যবহার করা হয়।)
print(mytuple)
type(mytuple)


print(mytuple[0])      # positive accessing an iteam
print(mytuple[1])
print(mytuple[2])
print(mytuple[3])
print(mytuple[4])



print(mytuple[-1])      # negative accessing an iteam
print(mytuple[-2])
print(mytuple[-3])
print(mytuple[-4])



print(len(mytuple))     # Tuple of length



mytuple = ('mango','banana','jackfruit','painapple','lichi')   # টাপেল করার ক্ষেত্রে append object টি সরাসরি ব্যবহার করা যাবে না
mytuple = list(mytuple)                                        # তাই list obejcet এ convert করে append object টি ব্যবহার করতে হবে                                           
mytuple.append('guava')                                        # এরপর tuple  এ convert করে print করতে হবে। 
print(mytuple)
mytuple = tuple(mytuple)
print(mytuple)




mytuple = ('mango','banana','jackfruit','painapple','lichi')   # টাপেল করার ক্ষেত্রে insert object টি সরাসরি ব্যবহার করা যাবে না
mytuple = list(mytuple)                                        # তাই list obejcet এ convert করে insert object টি ব্যবহার করতে হবে                                           
mytuple.insert(2,'guava')                                      # এরপর tuple  এ convert করে print করতে হবে। 
print(mytuple)
mytuple = tuple(mytuple)
print(mytuple)





mytuple = ('mango','banana','jackfruit','painapple','lichi')   # টাপেল করার ক্ষেত্রে remove object টি সরাসরি ব্যবহার করা যাবে না
mytuple = list(mytuple)                                        # তাই list obejcet এ convert করে remove object টি ব্যবহার করতে হবে                                           
mytuple.remove('banana')                                       # এরপর tuple  এ convert করে print করতে হবে। 
print(mytuple)
mytuple = tuple(mytuple)
print(mytuple)




mytuple = ('mango','banana','jackfruit','painapple','lichi')   # টাপেল করার ক্ষেত্রে pop object টি সরাসরি ব্যবহার করা যাবে না
mytuple = list(mytuple)                                        # তাই list obejcet এ convert করে pop object টি ব্যবহার করতে হবে                                           
mytuple.pop()                                                  # এরপর tuple  এ convert করে print করতে হবে। 
print(mytuple)
mytuple = tuple(mytuple)
print(mytuple)





mytuple = ('mango','banana','jackfruit','painapple','lichi')   # টাপেল করার ক্ষেত্রে del object টি সরাসরি ব্যবহার করা যাবে না
mytuple = list(mytuple)                                        # তাই list obejcet এ convert করে del object টি ব্যবহার করতে হবে                                           
del mytuple[3]                                                 # এরপর tuple  এ convert করে print করতে হবে। 
print(mytuple)
mytuple = tuple(mytuple)
print(mytuple)





mytuple1 = ('mango','banana','jackfruit','painapple','lichi','guava')     # joining tuple এর জন্য
mytuple2 = ('orange','mango','banana','jackfruit','painapple','lichi')

mytuple3 = mytuple1 + mytuple2
print(mytuple3)




if 'banana' in mytuple2:
    x = mytuple2.index('banana')                 # index এর ক্ষেত্রে (একটি এলিমেন্ট একটি লিস্টের মধ্যে কত নাম্বারে আছে তা প্রিন্ট করে।)
    print(x)
    




mytuple = [1,2,3,4,5,6,7,8,9,10]
mytuple = list(mytuple)                          # change elemant এর জন্য 
mytuple[2] = 'Mango'
print(mytuple)
mytuple = tuple(mytuple)
print(mytuple)




mytuple4 = ('mango','banana','jackfruit','painapple','lichi','guava',1,2,3,6,5,4,88)
print(mytuple4[:5])
print(mytuple4[3:5])
print(mytuple4[:-5])                              # slicing এর ক্ষেত্রে ব্যবহার হয়ে থাকে। 
print(mytuple4[-4:])

print(mytuple4[::5])
print(mytuple4[2:3:11])
print(mytuple4[3::5])





mytuple4 = ('mango','banana','jackfruit','painapple')
print(mytuple4 * 3)                                #  multiplication করার জন্য (লিস্টের আইটেম সমূহ একই সাথে ৩ বার প্রিস্ট হবে।)





























