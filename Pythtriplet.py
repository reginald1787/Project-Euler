for c in range(500,333,-1):
  for a in range(c-1,0,-1):
    b = 1000-a-c
    if a**2+b**2!=c**2:
      pass
    else:
      print a,b,c
      break
