import sys

liste = []

menu = """Que voulez vous faire?  :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉🏾 Votre choix : """

menu_choix = ["1", "2", "3", "4", "5"]

while  True:
    user_choice = ""
    while user_choice not in menu_choix:
        user_choice = input(menu)
        if user_choice not in menu_choix:
            print("Veuillez choisir une des options")

    if user_choice == "1":
        item = input("Entrez le nom d'un élement à ajouter à la liste de courses : ")
        liste.append(item)
        print(f"L'élement {item} a bien été ajouté à la liste.")
    elif user_choice =="2":
        item = input("Entrez le nom de élement à retirer à la liste de courses : ")
        if item in liste:
            liste.remove(item)
            print(f"L'élement {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élement {item} n'est pas dans la liste.")
    elif user_choice == "3":
        if liste:
            print("Voici le contenu de la liste: ")
            for i, item in enumerate(liste, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élement")
    elif user_choice == "4":
        liste.clear()
        print("La liste a bien été vidée !")
    elif user_choice =="5":
        print("Aurevoir...")
        sys.exit()

    print("_" *50)