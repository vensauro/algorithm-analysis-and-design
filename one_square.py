def maxSquare(matrix):
    linhas = len(matrix)
    colunas = len(matrix[0])
    resultado = 0

    memo=[[0] * colunas for i in range(linhas)]

    def subproblem(x, y):
        acima = memo[x][y - 1]
        diagonal = memo[x - 1][y - 1]
        abaixo = memo[x - 1][y]
        return 1 + min(acima, diagonal, abaixo)

    for linha in range(linhas):
        for coluna in range(colunas):
            if linha == 0 or coluna == 0:
                memo[linha][coluna] = matrix[linha][coluna]
            else:
                if matrix[linha][coluna] == 0:
                    memo[linha][coluna] = 0
                else:
                    rec = subproblem(linha, coluna)
                    memo[linha][coluna] = rec

                    resultado = max(resultado, rec)

    return resultado

maxSquare([
[1, 1, 0, 1],
[1, 1, 1, 1],
[1, 0, 1, 1],
])
