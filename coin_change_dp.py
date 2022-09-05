import sys

def coin_change(n):
  moedas = [1, 5, 10, 20, 25, 50]
  qty_moedas = len(moedas)

  # amount = n = coluna = j
  # coin = linha = i

  solutions = {(i, j): 1 if j == 0 else 0 for i in range(qty_moedas + 1) for j in range(n + 1)}

  for row in range(1, qty_moedas + 1):
    for col in range(1, n + 1):

      # valor da linha anterior, o resultado do calculo anterior
      resultado_anterior = solutions[row - 1, col]

      # a moeda que estamos verificando se chega no valor de col
      moeda_atual = moedas[row - 1]
      # coluna do valor menos o valor da moeda
      coluna_anterior = col - moeda_atual
      # o valor antes do tamanho da moeda, caso seja possível utilizar
      usar_a_moeda = 0 if coluna_anterior < 0 else solutions[row, coluna_anterior]

      # a soma do resultado anterior com se podemos usar o valor atual
      solutions[row, col] = resultado_anterior + usar_a_moeda

  return solutions[qty_moedas, n]


if __name__ == '__main__':
  n = int(sys.argv[1])
  print(coin_change(n))
