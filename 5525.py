import sys

n = int(sys.stdin.readline())
s_len = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
i = 0
matchingChar = 0
result = 0

while i < s_len - 2:
  if s[i] == "I" and s[i + 1] == "O" and s[i + 2] == "I":
    matchingChar += 1
    if matchingChar == n:
      result += 1
      matchingChar -= 1
    i += 1
  else:
    matchingChar = 0
  i += 1

print(result)