##from math import *
#def isprime(num):
#    if num==1:
#        return False
#    sq=int(sqrt(num))
#    for i in range(2,sq+1):
#        if num%i==0:
#            return False
#   return True

#num=int(input())
#print(isprime(num))







##from math import *
#def isprime(num):
#    if num==1:
#        return False
#    sq=int(sqrt(num))
#    for i in range(2,sq+1):
#        if num%i==0:
#            return False
#    return True

#a,b=map(int,input().split())
#c=0
#while a<=b:
#    if a%2 and isprime(a) and isprime(a+2):
#        c+=1
#        a+=2
#    else:
#        a+=1
#print(c)







##from math import *
#def isprime(num):
#    if num==1:
#        return False
#    sq=int(sqrt(num))
#    for i in range(2,sq+1):
#        if num%i==0:
#            return False
#    return True

#num=int(input())
#if isprime(num):
#    print("prime")
#    if isprime(num//2):
#        print("safe prime")
#    else:
#         print(" not a safe prime")

#else:
#    print(" not a prime")






#from math import *
#def isprime(num):
#    if num==1:
#        return False
#    sq=int(sqrt(num))
#    for i in range(2,sq+1):
#        if num%i==0:
#            return False
#    return True

#num=int(input())
#if isprime(num):
#    print("prime")
#    np=num+2
#    while True:
#        if isprime(np):
#            break
#        else:
#            np+=2
#    pp=num-2
#    while True:
#        if isprime(pp):
#            break
#        else:
#            pp-=2
#    if np*pp<=num*num:
#        print("good prime")
#    else:
#        print("bad prime")

#else:
#    print("not a prime")




##from math import *
#def isprime(num):
#    if num==1:
#        return False
#    sq=int(sqrt(num))
#    for i in range(2,sq+1):
#        if num%i==0:
#            return False
#    return True

#num=int(input())
#if isprime(num):
#    print("prime")
#    np=num+2
#    while True:
#        if isprime(np):
#            break
#           np+=2
#    pp=num-2
#    while True:
#        if isprime(pp):
#            break
#        else:
#            pp-=2
#    if np-num==num-pp:
#        print("balanced prime")
#    else:
#        print("bad prime")

#else:
#    print("not a balanced prime")




def gcd(a,b):
    while b:
        if a>b:
            a,b=b,a
        b=b%a
        if b==0:
            return a
    
a,b=map(int,input().split())
if (a%2 or b%2) and gcd(a,b)==1:
    print("coprime")
else:
    print("not a coprime")    
        
        
        
            
            
            
        




