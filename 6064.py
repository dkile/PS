import sys
# from math import lcm

def gcd(x, y):
  while (y):
    x, y = y , x%y
  return x

def lcm(x, y):
  return (x * y) // gcd(x, y)

def getResult(m, n, x, y):
  limit = lcm(m, n)
  i = 0
  j = 0
  ms = 0
  ns = 1
  while ms <= limit or ns <= limit:
    ms = m * i + x
    ns = n * j + y
    if ms > ns:
      j+=1
    elif ms < ns:
      i+=1
    else:
      return ms
  return -1
  
t = int(sys.stdin.readline())
for _ in range(t):
  m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
  print(getResult(m, n, x, y))