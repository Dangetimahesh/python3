num,r1,r2=map(int,input().split())
if r1>r2:
    for i in range(r1,r2+1):
        print(num,"X",i,"=",num*i)
else:   
    for i in range(r1,r2+1):
        print(num,"X",i,"=",num*i)
