def probabilidade(vampiro1, vampiro2, ataque):
  if ataque == 3:
    return vampiro1 / (vampiro1 + vampiro2)
  else:
    dado = 1 - (6 - ataque) / 6
    dado = (1 - dado) / dado
    return (1 - (dado ** vampiro1)) / (1 - (dado ** (vampiro1 + vampiro2)))

def challenge_compute(vampiro1, vampiro2, ataque, dano):
  aux = vampiro1
  vampiro1 = 0
  while aux > 0:
    aux -= dano
    vampiro1 += 1

  aux = vampiro2
  vampiro2 = 0
  while aux > 0:
    aux -= dano
    vampiro2 += 1
  
  return probabilidade(vampiro1, vampiro2, ataque) * 100

if __name__ == '__main__':
  while True:
    vampiro1, vampiro2, at, d = (int(x) for x in input().split())
    if all(el == 0 for el in [vampiro1, vampiro2, at, d]):
      break

    p  = (challenge_compute(vampiro1, vampiro2, at, d))
    print("{:.1f}".format(p))
