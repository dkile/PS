import sys
import re

def getResult(cmds, arr, n):
  start = 0
  end = n
  isReverse = False
  for cmd in cmds:
    if cmd == "R":
      isReverse = not isReverse
    elif cmd == "D":
      if isReverse == False:
        start += 1
      else:
        end -= 1
    if start > end:
      return "error"
  result = list(reversed(arr[start:end])) if isReverse else arr[start:end]
  return "[" + ",".join(result) + "]"
    
t = int(sys.stdin.readline())
for _ in range(t):
  cmds = list(sys.stdin.readline().rstrip())
  n = int(sys.stdin.readline())
  arr = re.compile("\d+").findall(sys.stdin.readline().rstrip())
  print(getResult(cmds, arr, n))