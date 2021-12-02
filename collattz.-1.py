n,r=map(int,input().split())
c=1
while True:
    if c==r:
        print(n)
        break
    if n==1:
        print(-1)
        break
    if n%2==0:
        n=n//2
    else:
        n=n*3+1
    c+=1 
