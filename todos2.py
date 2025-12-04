solde=100


def compte(solde):
    choix=input("choisir: solde, déposer, retirer, quitter : ")
    while True:
        if choix == "solde":
            print(f"votre solde est de : {solde}")
            return compte(solde)
        elif choix == "déposer":
            print(f"votre solde actuel : {solde}")
            depot=int(input("combien voulez vous déposer : "))
            solde += depot 
            print(f"votre solde aprés dépot : {solde}")
            return compte(solde)
        elif choix == "retirer":
            print(f"votre solde actuel : {solde}")
            retrait=int(input("combien voulez vous retirer : "))
            if retrait > solde:
                print("vous n'avez pas assez de solde pour retirer")
                return compte(solde)
            else:
                solde -= retrait
                print(f"votre solde aprés retrait : {solde}")
                return compte(solde)
        elif choix == "quitter":
            print("Merci Aurevoir!!!")
            return False

compte(solde)
        