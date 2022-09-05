from collections import deque

def maxRectangle(matriz):
  memo = [[None] * len(matriz[0]) for i in matriz]
  for i, linha in enumerate(matriz):
    memo[i] = linha.copy()
    if i > 0:
      memo[i] = [x if x == 0 else x + y for x, y in zip(memo[i], memo[i - 1])]

  resultado = 0
  for linha in memo:
    resultado = max(calcRectangle(linha), resultado)

  return resultado

def peekStack(stack):
  return stack[len(stack) - 1]

def calcRectangle(linha):
  stack = deque()
  maior = 0

  for i in range(len(linha)):
    while len(stack) != 0 and (i == len(linha) or linha[peekStack(stack)] > linha[i]):
      altura = linha[stack.pop()]
      largura = i - peekStack(stack) - 1 if len(stack) != 0 else i
      maior = max(maior, altura * largura)
    
    stack.append(i)

  return maior


maxRectangle([
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 1, 1, 1],
  [1, 0, 0, 0, 1],
])
