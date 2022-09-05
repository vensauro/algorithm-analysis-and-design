def gordao(n, k, total):
  return gordao(n - k, k, total * n) if n > 1 else total

T = int(input())

for i in range(T):
  s = input()
  n = int(''.join(x for x in s if x.isdigit()))
  k = s.count("!")
  print(gordao(n, k, 1))
