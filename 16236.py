import sys
from collections import deque

n = int(sys.stdin.readline())
board = []
baby_x, baby_y = 0, 0
baby_size = 2


for i in range(n):
  row = list(map(int, sys.stdin.readline().rstrip().split()))
  board.append(row)
  if 9 in row:
    baby_x, baby_y = i, row.index(9)
    board[baby_x][baby_y] = 0

def bfs():
  visited = [[-1]*n for _ in range(n)]
  visited[baby_x][baby_y] = 0
  q = deque([(baby_x, baby_y)])

  while q:
    x, y = q.popleft()
    
    for (nx, ny) in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
      if 0 > nx or n <= nx or 0 > ny or n <= ny or baby_size < board[nx][ny] or not visited[nx][ny] == -1: continue
      visited[nx][ny] = visited[x][y] + 1
      q.append((nx, ny))

  min_dist = 1e9
  temp_x, temp_y = 0, 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == -1 or board[i][j] >= baby_size or board[i][j] < 1: continue
      if visited[i][j] < min_dist:
        min_dist = visited[i][j]
        temp_x, temp_y = i, j

  if min_dist == 1e9:
    return False
  else:
    return temp_x, temp_y, min_dist

size_cnt = 0
move_cnt = 0

while True:
  result = bfs()
  if not result:
    print(move_cnt)
    break
  else:
    baby_x, baby_y = result[0], result[1]
    move_cnt += result[2]
    board[baby_x][baby_y] = 0
    size_cnt += 1
  if size_cnt >= baby_size:
    baby_size += 1
    size_cnt = 0