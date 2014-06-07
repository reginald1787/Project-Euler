
def isPalin(n):
  s = str(n)
  i = 0
  j = len(s)-1
  while i<j:
    if s[i]!=s[j]:
      return False
    i+=1
    j-=1
  return True


for i in range(999,836,-1):
  for j in range(999,836,-1):
    if isPalin(i*j):
      print i,j,i*j
      break


  
