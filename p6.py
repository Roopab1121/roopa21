def ar(q,s):
  if(len(q)==len(s)):
    return("yes")
  else:
   return("no")
q,s=map(str,input().split())
print(ar(q,s))
