n,k=map(int,input().split())
arr=[]
h=0
for i in range(0,n):
    x=int(input(""))
    arr.append(x)
for i in range(0,k):
    h=h+arr[i]
print(h)
