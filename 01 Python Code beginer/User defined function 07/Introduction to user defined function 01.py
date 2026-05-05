def myfunction():
    print('This is a function.')
print(myfunction())




def square(i):
    return i**2

print(square(40))



def square(i):
    return i * 3

print(square("three   "))




def list_square(i):
    return i*3

print(list_square([1,2,3,4,5,8,7,5,4,6]))




def multipale_function(x,y):
    return (x*y)

print(multipale_function(4,5))





# Prime নাম্বার নির্ণয় করার প্রোগ্রাম :

def isprime(x):
    for i in range(2,x):
        if (x%i==0):
            return False
        return True
    
print(isprime(19))
        
























