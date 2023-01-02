import sys

n = int(sys.stdin.readline().rstrip())
data = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def checkAllSame(n, x, y):
  result = ""
  base = data[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if not data[i][j] == base:
        result += checkAllSame(n // 2, x, y)
        result += checkAllSame(n // 2, x, y + n // 2)
        result += checkAllSame(n // 2, x + n // 2, y)
        result += checkAllSame(n // 2, x + n // 2, y + n // 2)
        return "(" + result + ")"
  return data[x][y]

print(checkAllSame(n, 0, 0))