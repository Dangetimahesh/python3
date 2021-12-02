a,b=map(int,input().split())
t=2
while True:
    if a%t==0 and b%t==0:
        a=a//t
        b=b//t
        print(t,a,b)
    else:
        t+=1
    if a<t or b<t:
        break
