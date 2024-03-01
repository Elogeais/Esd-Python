  # Exercice 1
def main():
  # Création de la liste
  numbers = [10, 5, 15, 2, 8]

  # Tri de la liste
  sorted_numbers = sorted(numbers)

  # Affichage de la liste triée
  print(sorted_numbers)
if __name__ == "__main__":
  main()



def main():
  # Initialisation du dictionnaire
  contacts = {}

  # Boucle de menu
  while True:
    print("Que souhaitez-vous faire ?")
    print("1. Ajouter un contact")
    print("2. Supprimer un contact")
    print("3. Rechercher un contact")
    print("4. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
      # Ajouter un contact
      nom = input("Nom du contact : ")
      numero = input("Numéro de téléphone : ")
      contacts[nom] = numero

    elif choix == "2":
      # Supprimer un contact
      nom = input("Nom du contact à supprimer : ")
      if nom in contacts:
        del contacts[nom]
      else:
        print("Le contact n'existe pas.")

    elif choix == "3":
      # Rechercher un contact
      nom = input("Nom du contact à rechercher : ")
      if nom in contacts:
        numero = contacts[nom]
        print("Le numéro de téléphone du contact est", numero)
      else:
        print("Le contact n'existe pas.")

    elif choix == "4":
      # Quitter
      break


if __name__ == "__main__":
  main()
