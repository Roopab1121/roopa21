def cm(m):
    
  if not m: return ''
  s1 = min(m)
  s2 = max(m)
  for i, c in enumerate(s1):
    if c != s2[i]:
      return s1[:i]
  return s1
def main():
  a=int(input())
  asd=[]
  for i in range(0,a):
    ele=input()
    asd.append(ele)
  str1=cm(asd) 
  print(str1)
  
if __name__== "__main__":
  main()
