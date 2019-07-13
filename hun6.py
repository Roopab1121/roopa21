rb = input()
r1 = list(map(int,input().split()))
b1 = False
for i in r1:
    if r1.count(i) > 1:
        b1 = True
        break
if b1:
    print(i)
else:
    print("unique")
