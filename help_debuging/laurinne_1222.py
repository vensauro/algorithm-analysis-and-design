def MDC(m,n):
  aux = 0
  while m > 0:
    aux += 1 
    m -= n
    if(m <= 0):
      break

  if(aux == 0):
    aux = 1

  return aux

while(True):
  try:
    n, l, c = [int(x) for x in input().split()]
    text = input()
    qntC = len(text)
    linhas = MDC(qntC,c)
    paginas = MDC(linhas,l)
    print(paginas)
  except EOFError:
    break
