#def fun(n):
#    if n<=0:
#        return 1
#   return fun(n-1)+fun(n-2)






#def fun(n):
#    if n<=0:
#        return
#    fun(n-1)
#    print(n,end=" ")
#    fun(n-2)

#fun(5)


def fun(n):
    if n<=0:
        print("*")
        return
    fun(n-1)
    fun(n-2)

fun(5)    
    
    
    

