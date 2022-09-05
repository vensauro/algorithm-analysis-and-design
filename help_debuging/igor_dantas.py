def challenge_compute():
    # N = número de palavras
    # L = linhas por página
    # C = caracteres por linha
    texto = []

    n, l, c = input().split()
    n = int(n)
    l = int(l)
    c = int(c)

    #input
    while(1):
        texto.extend(input().split())
        if(len(texto)>=n):
            break
    new = texto[0:n]

    #pegar ultimo caractere
    new2 = ' '.join(new)
    tamanho=0 # número de caracteres
    for i in new2:
        tamanho+=1

    resto = 0
    linhas = tamanho/c
    if (linhas%l)!=0:
        print(int(linhas/l) + 1)
    else:
        print(linhas/l)


if __name__ == '__main__':
    while True:
        try:
            challenge_compute()
        except EOFError:
            break
