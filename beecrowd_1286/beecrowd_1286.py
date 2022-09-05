class Pedido:
    def __init__(self, listen_input=False) -> None:
        if listen_input:
            self.tempo, self.pizzas = (int(i) for i in input().split())
        else:
            self.tempo = 0
            self.pizzas = 0

    def __repr__(self) -> str:
        return "{}(tempo={!r}, pizzas={!r})".format(
            self.__class__.__name__, self.tempo, self.pizzas
        )


while True:

    n = int(input())
    if n == 0:
        break
    p = int(input())

    pedidos = [Pedido(listen_input=True) for j in range(n)]
    pedidos = [Pedido()] + pedidos + [Pedido()] * 20

    mochila = [[None] * 31 for i in range(21)]

    for i in range(n + 1):
        for j in range(p + 1):
            if i == 0 or j == 0:
                mochila[i][j] = 0
            else:
                mochila[i][j] = (
                    mochila[i - 1][j]
                    if pedidos[i].pizzas > j
                    else max(
                        mochila[i - 1][j - pedidos[i].pizzas] + pedidos[i].tempo,
                        mochila[i - 1][j],
                    )
                )

    print("{} min.".format(mochila[n][p]))
