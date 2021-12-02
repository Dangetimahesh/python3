#from math import *
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







#from math import *
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
#    if isprime(num//2):
#        print("safe prime")
#    else:
#         print(" not a safe prime")

#else:
#    print(" not a prime")






from math import *
def isprime(num):
    if num==1:
        return False
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
    return True

num=int(input())
if isprime(num):




