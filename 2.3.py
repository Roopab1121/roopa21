g=int(input(""))
if g>1:
    for i in range(2,g//2):
        if(g%i)==0:
            print("no")
            break
        else:
            print("yes")
else:
    print("no")
    
