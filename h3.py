r=int(input())
flag=0

l=[]
lst=list(map(int,input().split()))
for i in range(0,len(lst)):
   if(lst[i]==i):
      temp=lst[i]
      flag=1
      l.append(temp)
      l=sorted(l)
print(*l)
if(flag==0):
   print("-1")
