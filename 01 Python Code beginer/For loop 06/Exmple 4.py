# Prime number or মেীলিক সংখ্যা বের করার প্রোগ্রাম:

# পদ্ধতি নাম্বার ০১:

print("Enter a number:")

x = int(input())
n = 1

for i in range(2,x):
    if(x%i==0):
        print("Not a prime.")
        n = 0
        break;
    
if (n==1):
    print('Prime.')
    
    
    
    
    
# পদ্ধতি নাম্বার ০২:

# function use করে মেীলিক সংখ্যা নির্ণয় এর পদ্ধতি:

a = int(input("Enter the number:"))

def test_prime(n):
    
    if(n==1):
        return False;
    elif(n==2):
        return True;
    
    
    else:     
        for x in range(2,n):
            if (n%x==0):
                return False
            return True
        
print("The prime number is:",test_prime(a))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    