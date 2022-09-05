memo = {0: 0, 1: 1}

def fibonacci_of(n):
  if n in memo:
    return memo[n]
  memo[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
  return memo[n]

chamadas = [2, 0]
while len(chamadas) < 38:
  chamadas = [chamadas[0] + chamadas[1] + 2] + chamadas

if __name__ == '__main__':
  for i in range(int(input())):
    entrada = int(input())
    print("fib({}) = {} calls = {}".format(entrada, chamadas[-entrada], fibonacci_of(entrada)))


def chamadas(n):
  calls = [2, 0]
  for i in range(2, n):
    calls = [calls[0] + calls[1] + 2] + calls

  return calls[-n]
