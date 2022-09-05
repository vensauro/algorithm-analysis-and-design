def min3(a, b, c):
    return min(a, min(b, c))

def maxSquare(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = 0

    def subproblema(x, y):
        if x < 0 or y < 0 or x >= linhas or y >= colunas or matriz[x][y]==0:
            return 0
        return 1 + min3(subproblema(x + 1, y + 1), subproblema(x + 1, y),subproblema(x, y + 1))

    for i in range(linhas):
        for j in range(colunas):
            resultado = max(resultado, subproblema(i,j))#for each cell in the matrix calculate the largest square submatrix with all ones with it as the top-left corner
    return resultado

print(maxSquare([
    [1, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0],
]))
