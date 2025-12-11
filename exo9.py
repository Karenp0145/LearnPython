# Exercice 9 :  Suite de Fibonacci
# Génère les N premiers nombres de la suite de Fibonacci (chaque nombre est la somme des deux précédents : 0, 1, 1, 2, 3, 5, 8...).

liste = [0,1]

a = int(input("nb"))

for i in range(a-2):

    n = liste[0+i] + liste[1+i]
    liste.append(n)
    print(liste)