#n=int(input())
#oc=0
#ec=0
#while n!=0:
#        d=n%10
#        n=n//10
#        if d%2==0:
#               ec+=1
#        else:
#              oc+=1
#print(oc,ec)




#n=int(input())
#oc=0
#ec=0
#c=0
#while n!=0:
#    c+=1
#    d=n%10
#    n=n//10
#    if d%2==0:
#         ec+=1
#    else:
#         oc+=1
#if ec==c:
#    print("even")
#elif oc==0:
#    print("odd")
#else:
#    print("mixed")



n=int(input())
num=n
while n:
    d=n%10
    n=n//10
    if num%2==0 and d%2==1:
        print("mixed")
        break
    if num%2==1 and d%2==0:
        print("mixed")
        break
else:
    if num%2==0:
        print("even")
    else:
        print("odd")


