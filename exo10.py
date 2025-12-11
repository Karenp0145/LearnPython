# Exercice 10 : Tri personnalisé
# Crée une fonction qui trie une liste de tuples par le deuxième élément.
# Ex : [(1, 5), (3, 2), (2, 8)] → [(3, 2), (1, 5), (2, 8)]

liste = [(1, 5), (3, 2), (2, 8)]

print(sorted(liste, key=lambda x: x[1]))