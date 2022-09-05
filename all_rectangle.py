def maxRectangle(matriz):
  linhas = len(matriz)
  colunas = len(matriz[0])
  resultado = 0

  def subproblema(c1, c2, r1, r2):
    # m = [row[c1:c2] for row in matriz[r1:r2]]
    allOne = all(all(i == 1 for i in row[c1:c2]) for row in matriz[r1:r2])
    if allOne:
      return abs(r2 - r1) * abs(c2 - c1)
    return 0

  for r1 in range(linhas + 1):
    for r2 in range(r1 + 1, linhas + 1):
      for c1 in range(colunas + 1):
        for c2 in range(c1 + 1, colunas + 1):
          resultado = max(resultado, subproblema(c1, c2, r1, r2))

  return resultado


print(
  maxRectangle([
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
  ])
)
