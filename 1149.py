import sys

n = int(sys.stdin.readline())
rgbs = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

min_rgb = [rgbs[0][0], rgbs[0][1], rgbs[0][2]]
for i in range(1, n):
  red = rgbs[i][0] + min(min_rgb[1], min_rgb[2])
  green = rgbs[i][1] + min(min_rgb[0], min_rgb[2])
  blue = rgbs[i][2] + min(min_rgb[0], min_rgb[1])
  min_rgb = [red, green, blue]
print(min(min_rgb))