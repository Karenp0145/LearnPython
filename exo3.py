#Exercice 3 : Demande un mot à l’utilisateur et affiche-le à l’envers.

word = input("Ecris un mot : ")

reverseWord = ''.join(reversed(word))
print(reverseWord)

# # La fonction reversed retourne un itérable inversé.
# # La méthode join permet de fusionner les éléments pour obtenir la chaîne inversée.

# OU DEUXIEME METHODE
# reverseWord = word[::-1]
# print("Le mot inversé est :", reverseWord)