year=int(input(""))
if year%4==0 or year%400==0:
    if year%100==0:
        print("no")
    else:
        print("yes")
else:
    print("no")
