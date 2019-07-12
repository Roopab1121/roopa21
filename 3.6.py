rb=int(input(""))
lst1=list(map(int,input().split()))
lst1.sort()
for i in range(0,len(lst1)):
    print(lst1[i],end=" ")
