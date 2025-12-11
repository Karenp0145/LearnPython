# Exercice 8 : Compteur de mots
# Crée un programme qui analyse un texte et retourne un dictionnaire avec la fréquence de chaque mot.
# Exemple : "le chat et le chien" → {"le": 2, "chat": 1, "et": 1, "chien": 1}


message = 'it was the best of times it was the worst of times '

liste_mots = message.split()

frequences_mots = [liste_mots.count(mot) for mot in liste_mots]

print("Paires (mot, fréquence)\n" + str(dict(zip(liste_mots, frequences_mots))))
result_dict = dict(zip(liste_mots, frequences_mots))


# result_dict = {}
# for i in range(len(liste_mots)):

#     result_dict.setdefault(frequences_mots[i], [])
#     result_dict[frequences_mots[i]].append(liste_mots[i])

# print(result_dict)