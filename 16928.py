import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

move_dic = {}
for _ in range(n + m):
  s, e = map(int, sys.stdin.readline().rstrip().split())
  move_dic[s] = e

q = []
q.append(1)
visited=[False]*101
cnts = [100]*101
cnts[1] = 0
visited[1] = True
while q:
  v = q.pop(0)
  for i in range(1, 7):
    dest = v + i
    if dest > 100: continue
    if dest in move_dic:
      dest = move_dic[dest]
    if visited[dest]: continue
    q.append(dest)
    visited[dest] = True
    cnts[dest] = cnts[v] + 1

print(cnts[100])