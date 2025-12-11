# Exercice 6 : Palindrome
# Écris une fonction qui vérifie si un mot ou une phrase est un palindrome (se lit pareil dans les deux sens). Ignore les espaces et la casse.
# Exemples : "kayak" → True, "Elu par cette crapule" → True 

mot = input("Choisir un mot: ")

def is_palindrome(text):
    processed_text = ''.join(text.lower().split())
    return processed_text == processed_text[::-1]

if is_palindrome(mot):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")