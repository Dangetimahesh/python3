num,r=map(int,input().split())
for i in range(1,r+1):
    if i%num:
        print(num,"X",i,"=",num*i)
