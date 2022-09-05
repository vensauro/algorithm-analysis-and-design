n = int(input())
for a in range(n):
  x1, y1 = (int(i) for i in input().split())

  while x1 > 1:
    if x1 > y1:
      x1 = x1 % y1
    else:
      x1, y1 = y1, x1

  print(y1)
