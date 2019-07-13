rb  =input()
vs = list(map(int,input().split()))
for i in range(len(vs)):
    if (i%2 == 0 and vs[i]%2 !=0) or (i%2!= 0 and vs[i]%2 == 0):
        print(vs[i],end = " ")
