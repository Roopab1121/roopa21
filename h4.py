h=int(input())
lst=list(map(int,input().split()))[:n]
rb=[]
for i in range(0,n):
  if(lst.count(lst[i])==1):
    c=lst[i]
    rb.append(c)
    
  sorted(rb)
  
rb = list(dict.fromkeys(asd))
print(*rb)
