r,b=map(int,input().split())
a=[]
for z in range(r,b+1):
    for p in range(2,z):
        if(z%p==0):
            break
    else:
        a.append(z)
print(len(a))
