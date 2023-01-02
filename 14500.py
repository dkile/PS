import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
ans = 0
visited = [[0] * m for _ in range(n)]

def dfs(x, y, s, cnt):
  global ans
  s += board[x][y]
  cnt += 1
  if cnt == 4:
    ans = max(ans, s)
    return
  visited[x][y] = 1
  for (next_x, next_y) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
    if next_x < n and next_x >= 0 and next_y < m and next_y >= 0 and visited[next_x][next_y] == 0:
      dfs(next_x, next_y, s, cnt)
  visited[x][y] = 0

def T(x, y):
  global ans
  t_points = [[(0, 1), (0, -1), (1, 0)], [(0, 1), (0, -1), (-1, 0)], [(1, 0), (-1, 0), (0, 1)], [(1, 0), (-1, 0), (0, -1)]]
  for t_point in t_points:
    s = board[x][y]
    for (x_diff, y_diff) in t_point:
      next_x = x + x_diff
      next_y = y + y_diff
      if next_x >= n or next_x < 0 or next_y >= m or next_y < 0:
        break
      s += board[next_x][next_y]
    else:
      ans = max(ans, s)
      
for i in range(n):
  for j in range(m):
    dfs(i, j, 0, 0)  
    T(i, j)

print(ans)