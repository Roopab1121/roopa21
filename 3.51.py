r=int(input(""))
lst=list(map(int,input().split()))
lst.sort()
median=(r+1)//2
print(lst[median-1])
