n,r=map(int,input().split())
for i in range(1,r):
    if n==1:
        print(-1)
        break
    if n%2==0:
        n=n//2
    else:
        n=n*3+1
else:
    print(n)
