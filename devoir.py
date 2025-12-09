def menu():
    print("Menu général :")
    print("(1) Ajouter les produits")
    print("(2) Calculer le prix total à payer par le client")
    print("(3) Afficher la facture totale du client")
    print("(4) Modifier les informations d'un produit")
    print("(5) Supprimer un produit")
    print("(6) Quitter le programme")
    ch = int(input("Entrer votre choix : "))
    return ch


def ajouter_produit():
    code = input("Code : ")
    nom = input("Nom : ")
    prix = float(input("Prix Unitaire : "))
    qte = int(input("Quantité : "))

    produit = {
        "code": code,
        "nom": nom,
        "prix": prix,
        "quantite": qte
    }
    return produit


def calculer_prix(panier):
    total = 0
    for produit in panier:
        total += produit["prix"] * produit["quantite"]
    return total


def rechercher_produit(panier, code):
    for i, produit in enumerate(panier):
        if produit["code"] == code:
            return i
    return -1


# Programme principal
Panier = []
choix = 0

while choix != 6:
    choix = menu()

    # --- AJOUT PRODUITS ---
    if choix == 1:
        nbr = int(input("Entrer le nombre de produits : "))
        for i in range(nbr):
            print(f"\nProduit N°{i + 1}")
            Panier.append(ajouter_produit())
        print("\nPanier actuel :", Panier)

    # --- CALCUL TOTAL ---
    elif choix == 2:
        if not Panier:
            print("Aucun produit ajouté au panier")
        else:
            print("Total à payer :", calculer_prix(Panier))

    # --- FACTURE ---
    elif choix == 3:
        if not Panier:
            print("Aucun produit acheté")
        else:
            print("\nFacture détaillée : ")
            print("Code\tNom\tPrix U.\tQuantité")
            for p in Panier:
                print(f"{p['code']}\t{p['nom']}\t{p['prix']}\t{p['quantite']}")
            print("\nPrix total :", calculer_prix(Panier))

    # --- MODIFIER PRODUIT ---
    elif choix == 4:
        code = input("Entrer le code du produit à modifier : ")
        index = rechercher_produit(Panier, code)

        if index == -1:
            print("Produit introuvable")
        else:
            produit = Panier[index]
            choix2 = 0
            while choix2 != 5:
                print("\n1. Modifier le code")
                print("2. Modifier le nom")
                print("3. Modifier le prix")
                print("4. Modifier la quantité")
                print("5. Retour au menu principal")
                choix2 = int(input("Votre choix : "))

                if choix2 == 1:
                    produit["code"] = input("Nouveau code : ")
                elif choix2 == 2:
                    produit["nom"] = input("Nouveau nom : ")
                elif choix2 == 3:
                    produit["prix"] = float(input("Nouveau prix : "))
                elif choix2 == 4:
                    produit["quantite"] = int(input("Nouvelle quantité : "))
                elif choix2 == 5:
                    print("Retour au menu principal")
                else:
                    print("Choix invalide")

    # --- SUPPRIMER PRODUIT ---
    elif choix == 5:
        code = input("Entrer le code du produit à supprimer : ")
        index = rechercher_produit(Panier, code)

        if index == -1:
            print("Produit introuvable")
        else:
            del Panier[index]
            print("Produit supprimé avec succès")

    # --- QUITTER ---
    elif choix == 6:
        print("Merci, au revoir !")

    else:
        print("Choix invalide, veuillez entrer une valeur entre 1 et 6.")
