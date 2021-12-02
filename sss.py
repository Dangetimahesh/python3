n,r=map(int,input().split())
c=1
while True:
    print(n,end=" ")
    if n==1:
        break
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
        c+=1

