import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
not_availables = list(sys.stdin.readline().split())
result = abs(n - 100)

for num in range(1000001):
  for digit in str(num):
    if digit in not_availables:
      break
  else:
    result = min(result, len(str(num)) + abs(n - num))

print(result)