# Exercice 1 : Demande un nombre à l’utilisateur et affiche sa table de multiplication de 1 à 10.

number = int(input("Nombre : "))

for i in range(1, 11) :
    print(number, "x", i, "=", number * i)