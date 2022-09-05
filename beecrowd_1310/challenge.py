def challenge():
  days_qty = int(input())
  cost = int(input())

  days = [int(input()) - cost for i in range(days_qty)]

  smaller = greater = days[0]
  for i in days[1:]:
      smaller = max(i, smaller + i)
      greater = max(greater, smaller)

  if greater < 0:
    greater = 0

  return greater

while True:
  try:
    print(challenge())
  except EOFError:
    break
