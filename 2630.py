import sys

n = int(sys.stdin.readline().rstrip())
papers = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

result = [0, 0];


def checkSameColor(n, x, y):
  color = papers[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if not papers[i][j] == color:
        checkSameColor(n // 2, x, y)
        checkSameColor(n // 2, x, y + n // 2)
        checkSameColor(n // 2, x + n // 2, y)
        checkSameColor(n // 2, x + n // 2, y + n // 2)
        return
  result[color] += 1
  return

checkSameColor(n, 0, 0)
print(result[0])
print(result[1])