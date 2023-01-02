import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().rstrip().split()))

acc = 0
accs = [0]
for v in l:
  acc += v
  accs.append(acc)

for _ in range(m):
  i, j = map(int, sys.stdin.readline().rstrip().split())
  print(accs[j] - accs[i -1])
  