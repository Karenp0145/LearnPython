# Exercice 7
# Affiche les nombres de 1 à 100, mais :

# Si le nombre est divisible par 3, affiche "Fizz"
# Si divisible par 5, affiche "Buzz"
# Si divisible par 3 ET 5, affiche "FizzBuzz"
# Sinon, affiche le nombre


def Fizzbuzz():
    
    for n in range(1,101):
    
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 3 == 0:
            print("Fizz")
        else:
            print(n)

Fizzbuzz()