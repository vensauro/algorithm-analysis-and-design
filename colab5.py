import itertools

n, C = (int(i) for i in input().split())

result = []
for i in itertools.permutations(range(C), n):
  if sum(i) == 7 and 0 not in i:
    result.append(i)
# [i for i in itertools.permutations(range(C), n) if sum(i) == 7 and 0 not in i]
