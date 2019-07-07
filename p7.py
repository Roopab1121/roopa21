r=list(input())
k=0
while(k<len(r)):
    temp=r[k]
    r[k]=r[k+1]
    r[k+1]=temp
    k+=2
print("".join(r))
