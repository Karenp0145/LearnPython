# Demande un nombre à l’utilisateur et affiche sa table de multiplication de 1 à 10.

# number = int(input("Nombre : "))

# for i in range(1, 11) :
#     print(number, "x", i, "=", number * i)56



# Calcule la somme de tous les nombres d’une liste [5, 10, 15, 20, 25].

# numbers = [5, 10, 15, 20, 25]
# total = 0

# for n in numbers :
#     total += n 
#     print(total)



#Demande un mot à l’utilisateur et affiche-le à l’envers.

# word = input("Ecris un mot : ")

# # reverseWord = ''.join(reversed(word))
# # print(reverseWord)

# # La fonction reversed retourne un itérable inversé.
# # La méthode join permet de fusionner les éléments pour obtenir la chaîne inversée.

# OU DEUXIEME METHODE
# reverseWord = word[::-1]
# print("Le mot inversé est :", reverseWord)


# ///////////////////////////////////////////////////////////////////////////


# Exercice 7 : Pair ou impair
# Demande un nombre à l'utilisateur et indique s'il est pair ou impair.

# number = int(input("Choisis un nombre"))

# if number % 2 == 0 :
#     print("c'est un nombre pair !")
# else :
#     print("c'est un nombre impair !")


# ///////////////////////////////////////////////////////////////////////////


# # Exercice 8 : Somme des nombres
# # Calcule la somme de tous les nombres de 1 à 100.

# somme = 0

# for i in range(101):
#     somme += i
#     print(somme)


# ///////////////////////////////////////////////////////////////////////////


# Exercice 9 : Palindrome
# Écris une fonction qui vérifie si un mot ou une phrase est un palindrome (se lit pareil dans les deux sens). Ignore les espaces et la casse.
# Exemples : "kayak" → True, "Elu par cette crapule" → True 

# mot = input("Choisir un mot")

# def is_palindrome(text):
#     processed_text = ''.join(text.lower().split())
#     return processed_text == processed_text[::-1]

# if is_palindrome(mot):
#     print("C'est un palindrome.")
# else:
#     print("Ce n'est pas un palindrome.")


# ///////////////////////////////////////////////////////////////////////////


# Exercice 10
# Affiche les nombres de 1 à 100, mais :

# Si le nombre est divisible par 3, affiche "Fizz"
# Si divisible par 5, affiche "Buzz"
# Si divisible par 3 ET 5, affiche "FizzBuzz"
# Sinon, affiche le nombre


# def Fizzbuzz():
    
#     for n in range(1,101):
    
#         if n % 3 == 0 and n % 5 == 0:
#             print("FizzBuzz")
#         elif n % 5 == 0:
#             print("Buzz")
#         elif n % 3 == 0:
#             print("Fizz")
#         else:
#             print(n)

# Fizzbuzz()


# ///////////////////////////////////////////////////////////////////////////


# Exercice 11 : Compteur de mots
# Crée un programme qui analyse un texte et retourne un dictionnaire avec la fréquence de chaque mot.
# Exemple : "le chat et le chien" → {"le": 2, "chat": 1, "et": 1, "chien": 1}


# message = 'it was the best of times it was the worst of times '

# liste_mots = message.split()

# frequences_mots = [liste_mots.count(mot) for mot in liste_mots]

# print("Paires (mot, fréquence)\n" + str(dict(zip(liste_mots, frequences_mots))))
# mon_dico = dict(zip(liste_mots, frequences_mots))


# mon_dico = {}
# for i in range(len(liste_mots)):

#     mon_dico.setdefault(frequences_mots[i], [])
#     mon_dico[frequences_mots[i]].append(liste_mots[i])

# print(mon_dico)


# ///////////////////////////////////////////////////////////////////////////


# Exercice 12 :  Suite de Fibonacci
# Génère les N premiers nombres de la suite de Fibonacci (chaque nombre est la somme des deux précédents : 0, 1, 1, 2, 3, 5, 8...).

# liste = [0,1]

# a = int(input("nb"))

# for i in range(a-2):

#     n = liste[0+i] + liste[1+i]
#     liste.append(n)
#     print(liste)


# ///////////////////////////////////////////////////////////////////////////


# Exercice 13 : Tri personnalisé
# Crée une fonction qui trie une liste de tuples par le deuxième élément.
# Ex : [(1, 5), (3, 2), (2, 8)] → [(3, 2), (1, 5), (2, 8)]

# liste = [(1, 5), (3, 2), (2, 8)]

# print(sorted(liste, key=lambda x: x[1]))


# ///////////////////////////////////////////////////////////////////////////


# Exercice : Gestionnaire de contacts
# Crée un mini-programme avec un menu pour :

# Ajouter un contact (nom, téléphone)
# Rechercher un contact (nom)
# Afficher tous les contacts
# Supprimer un contact



    
# contacts = []

# def addcontact():
#     name = input("Nom : ")
#     tel = input("Téléphone : ")

#     contacts.append({"name": name, "tel": tel})
#     print("Contact ajouté :", contacts[-1])

# def findcontact():
#     search_name = input("Entrez un nom pour débuter la recherche : ").lower()

#     for contact in contacts:
#         if contact["name"].lower() == search_name:
#             print("Contact trouvé :", contact)
#             return

#     print("Aucun contact trouvé.")

# def showcontacts():
#     print(contacts)


# def delcontact():
#     del_name = input("Entrez un nom pour supprimer le contact : ").strip().lower()

#     for contact in contacts:
#         if contact["name"].lower() == del_name:
#             verif = input(f"Êtes vous sûr de vouloir supprimer : {del_name} ? OUI NON : ")
#             if verif == "OUI" or start == "1":
#                 contacts.remove(contact)
#                 print("Contact", del_name, "supprimé.")
#                 return

#             else:
#                 print("Demande annulée")
#                 return
                
#     print("Aucun contact trouvé.")

# exit_app = False

# while exit_app == False:
#     start = input("Que souhaitez vous faire ? \n 1. Ajouter un contact \n 2. Rechercher un contact \n 3. Afficher tous les contacts \n 4. Supprimer un contact \n 5. Quitter \n").strip().lower()

#     if start in ("Quitter","5"):
#         exit_app = True
    
#     elif start in ("Ajouter un contact", "1"):
#         addcontact()
    
#     elif start in ("Rechercher un contact", "2"):
#         findcontact()

#     elif start in ("Afficher tous les contacts","3"):
#         showcontacts()

#     elif start in ("Supprimer un contact","4"):
#         delcontact()

#     else :
#         print("Choix invalide")


# ///////////////////////////////////////////////////////////////////////////

