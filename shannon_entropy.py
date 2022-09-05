from math import log2

n = int(input())

entropy = 0
average_bits = 0

for i in range(n):
  freq, bits = (float(i) for i in input().split())
  entropy += round(freq * log2(freq), 4)
  average_bits += freq * bits

print("{:.4f}".format(-1 * entropy))
print("{:.4f}".format(average_bits))
