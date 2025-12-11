# Exercice 11 : Gestionnaire de contacts
# Crée un mini-programme avec un menu pour :

# Ajouter un contact (nom, téléphone)
# Rechercher un contact (nom)
# Afficher tous les contacts
# Supprimer un contact



    
contacts = []

def addcontact():
    name = input("Nom : ")
    tel = input("Téléphone : ")

    contacts.append({"name": name, "tel": tel})
    print("Contact ajouté :", contacts[-1])

def findcontact():
    search_name = input("Entrez un nom pour débuter la recherche : ").lower()

    for contact in contacts:
        if contact["name"].lower() == search_name:
            print("Contact trouvé :", contact)
            return

    print("Aucun contact trouvé.")

def showcontacts():
    print(contacts)


def delcontact():
    del_name = input("Entrez un nom pour supprimer le contact : ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == del_name:
            verif = input(f"Êtes vous sûr de vouloir supprimer : {del_name} ? OUI NON : ")
            if verif == "OUI" or start == "1":
                contacts.remove(contact)
                print("Contact", del_name, "supprimé.")
                return

            else:
                print("Demande annulée")
                return
                
    print("Aucun contact trouvé.")

exit_app = False

while exit_app == False:
    start = input("Que souhaitez vous faire ? \n 1. Ajouter un contact \n 2. Rechercher un contact \n 3. Afficher tous les contacts \n 4. Supprimer un contact \n 5. Quitter \n").strip().lower()

    if start in ("quitter", "5"):
        exit_app = True
    
    elif start in ("ajouter un contact", "1"):
        addcontact()
    
    elif start in ("rechercher un contact", "2"):
        findcontact()

    elif start in ("afficher tous les contacts","3"):
        showcontacts()

    elif start in ("supprimer un contact","4"):
        delcontact()

    else :
        print("Choix invalide")