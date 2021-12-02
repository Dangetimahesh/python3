num,r=map(int,input().split())
for i in range(1,r+1):
    if  num*i<r:
         print(num,"X",i,"=",num*i)
    else:
        break
    
