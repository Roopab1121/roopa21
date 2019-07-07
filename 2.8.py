a,b=map(int,input().split())
for i in range(a+1,b):
    temp=i
    s=0
    while temp>0:
        r=temp%10
        s=s+r**3
        temp=temp//10
    if i==s:
        print(i,end=" ")

