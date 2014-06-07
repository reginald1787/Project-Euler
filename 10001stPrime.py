
primes = [2,3,5,7]

i=11
isPrime = True
while i<10**10:
  for c in primes:
    if i%c==0:
      isPrime = False
      break
    if 2*c>i:
      break
  if isPrime:
    primes.append(i)
  if len(primes)>100001:
    print primes[100001-1]
    break
  i+=2
  isPrime = True
