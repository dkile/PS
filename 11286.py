import sys
from heapq import heappush, heappop

t = int(sys.stdin.readline())
heap = []
for _ in range(t):
  n = int(sys.stdin.readline())
  if n == 0:
    print(heappop(heap)[1] if len(heap) else 0)
  else:
    heappush(heap, (abs(n), n))
