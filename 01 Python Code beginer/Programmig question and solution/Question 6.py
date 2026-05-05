#ফাংশন ব্যবহারপূর্বক কোন সংখ্যা মৌলিক কিনা তা নির্ণয় করার প্রোগ্রাম লিখ?

def test_prime(n):
    if(n==1):
        return False;
    elif(n==2):
        return True;
    
    else:
        for x in range(2,n):
            if(n%x==0):
                return False
            return True
print("The prime number is:",test_prime(19))