# Exercice 1 : Facile
N = int(input("Entrez un nombre entier N : "))
somme = 0
for i in range(1, N + 1):
    somme += i
print("La somme des nombres de 1 à {} est {}".format(N, somme))

# Exercice 2 : Facile (table de multiplication)
N = int(input("Entrez un nombre entier N : "))
for i in range(1, 11):
    print("{} x {} = {}".format(N, i, N * i))

# Exercice 3 : Facile (pair & impair)
for i in range(1, 11):
    if i % 2 == 0:
        print("{} est pair".format(i))
    else:
        print("{} est impair".format(i))

# Exercice 4 : intermédiaire 
N = int(input("Entrez un nombre entier N : "))
factorielle = 1
for i in range(1, N + 1):
    factorielle *= i
print("La factorielle de {} est {}".format(N, factorielle))

# Exercice 5 : intermédiaire 
def is_palindrome(mot):
  return mot == mot[::-1]
mot = input("Entrez un mot : ")
if is_palindrome(mot):
  print("Le mot", mot, "est un palindrome.")
else:
  print("Le mot", mot, "n'est pas un palindrome.")

# Exercice 6 : intermédiaire 
def generate_magic_square(n):
  # Initialisation du tableau
  magic_square = [[0 for _ in range(n)] for _ in range(n)]

  # Placement des nombres
  for i in range(1, n ** 2 + 1):
    # Calculer la position du nombre
    x = i % n
    y = (i // n) % n

    # Placer le nombre
    magic_square[y][x] = i

  return magic_square
def main():
  # Saisie de l'ordre du carré magique
  n = int(input("Entrez l'ordre du carré magique : "))

  # Génération du carré magique
  magic_square = generate_magic_square(n)

  # Affichage du carré magique
  for row in magic_square:
    print(" ".join([str(x) for x in row]))
if __name__ == "__main__":
  main()
