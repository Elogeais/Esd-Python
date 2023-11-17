def multiplie(a, b):
  resultat = 0
  for i in range(b):
    resultat += a
  return resultat
print(multiplie(15, 30))


def puissance5(n):
  if n == 0:
    return 1
  else:
    return 5 * puissance5(n - 1)
print(puissance5(5))