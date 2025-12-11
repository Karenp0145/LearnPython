# Exercice 13 : Validation d'email
# Crée une fonction qui vérifie si une adresse email est valide (contient @, un domaine, etc.).


""" Input : str(email_input)
Output : str(result1) """
def check_at(email_input):

    if email_input.count("@") == 1 :
        result1 = True

    else:
        result1 = False

    return result1


""" Input : str(email_input)
Output : str(result2) """
def check_domain(email_input):
    domain = email_input.split("@")[1]

    if domain in ("gmail.com", "hotmail.fr" ) :
        result2 = True
    else:
        result2 = False
    
    return result2

""" Input : str(email_input)
Output : str(final_result) """
def final_verification(email_input):
    if check_at(email_input) == True and check_domain(email_input) == True :
        final_result = True
    else:
        final_result = False

    return final_result


def main():
    email_input = input("Veuillez indiquer votre email")

    if final_verification(email_input) == True :
        print("Email valide !")

    else:
        print("Email invalide")

main()