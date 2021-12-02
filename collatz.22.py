n,r=map(int,input().split())
c=1
while True:
    if n==r:
        print(True)
        break
    if n==1:
        print(False)
        break
    if n%2==0:
        n=n//2
    else:
        n=n*3+1
    c+=1 
