rb=input()
rb=rb.split()
vs=rb[0]
y=rb[1]
count=0
o=0
while(o<len(vs) and count<2):
    if(vs[o]!=y[o]):
        count+=1
    o+=1
if(count==1 or count==0):
    print("yes")
else:
    print("no")
