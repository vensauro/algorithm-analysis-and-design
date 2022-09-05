'''
Abordagem Gulosa com sistema canônico
'''

def num_min_moedas_troco(troco_valor, moedas, troco_moedas):

  r = 0
  moedas.sort(reverse=True)

  for i in range(len(moedas)):
    x = troco_valor//moedas[i]
    r += x #mesmo se for 0
    troco_moedas[i] = x
    troco_valor -= x * moedas[i]

  return r


#------------------------------------------------------------------------------

def main():

  moedas = [1, 5, 10, 25, 50]
  troco_valor = 49
  troco_moedas = [0] * len(moedas)

  print("Troco possui", num_min_moedas_troco(troco_valor, moedas, troco_moedas), "moedas:")
  for i in range(len(moedas)):
    if troco_moedas[i] > 0:
      print(str(moedas[i]) + ": " + str(troco_moedas[i]) + " moeda(s)")


#=============================================================================#
#=============================================================================#
    
if __name__ == "__main__":
  main()
