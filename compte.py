solde=100
trait= "--------------------------"


def compte(solde):
    choix=input("choisir: solde, déposer, retirer, quitter : ")
    while True:
        if choix == "solde":
            print(trait)
            print(f"votre solde est de : {solde}")
            print(trait)
            return compte(solde)
        elif choix == "déposer":
            print(trait)
            print(f"votre solde actuel : {solde}")
            print(trait)
            depot=int(input("combien voulez vous déposer : "))
            print(trait)
            solde += depot 
            print(f"votre solde aprés dépot : {solde}")
            print(trait)
            return compte(solde)
        elif choix == "retirer":
            print(trait)
            print(f"votre solde actuel : {solde}")
            print(trait)
            retrait=int(input("combien voulez vous retirer : "))
            print(trait)
            if retrait > solde:
                print("vous n'avez pas assez de solde pour retirer")
                print(trait)
                return compte(solde)
            else:
                solde -= retrait
                print(f"votre solde aprés retrait : {solde}")
                print(trait)
                return compte(solde)
        elif choix == "quitter":
            print(trait)
            print("Merci Aurevoir!!!")
            print(trait)
            return False
        else:
            print(trait)
            print("choix invalid")
            print(trait)
            return compte(solde)

compte(solde)



