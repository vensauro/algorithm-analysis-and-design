from collections import defaultdict, deque 

def challenge():
  inicial = int(input())
  vertices, arestas = [int(i) for i in input().split()]

  labirinto = defaultdict(set)
  for aresta in range(arestas):
    a, b = [int(i) for i in input().split()]
    labirinto[a].add(b)
    labirinto[b].add(a)

  visitados = set()
  stack = deque([inicial])

  while len(stack) != 0:
    item = stack.pop()

    if item not in visitados:
      visitados.add(item)

    for filho in labirinto[item]:
      if filho not in visitados:
        stack.append(filho)

  print((len(visitados) - 1) * 2)

if __name__ == '__main__':
  for i in range(int(input())):
    challenge()
