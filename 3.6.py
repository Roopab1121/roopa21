r=int(input(""))
lst=list(map(int,input().split()))
lst.sort()
for i in range(0,len(lst)):
    print(lst[i],end=" ")
