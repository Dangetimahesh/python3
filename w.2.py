num,r1,r2=map(int,input().split())
if r2<r1:
    start=r1
    stop=r2
else:
    start=r2
    stop=r1
for i in range(r1,r2+1):
    print(num,"X",i,"=",num*i)
