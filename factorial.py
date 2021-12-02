#n=int(input())
#c=1
##for i in range(1,n+1):
#for i in range(n,0,-1):    
#  c*=i
#print(c)




#def fun(n):
#    c=1
#    for i in range(1,n+1):
#        c*=i
#    print(c)

#n=int(input())
#fun(n)




def fun(n):
    if n==1:
        return n
    else:
        return n*fun(n-1)

n=int(input())    
print(fun(n))    



    









